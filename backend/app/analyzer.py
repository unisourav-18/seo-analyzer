import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin
import requests
import textstat
from collections import Counter
from app.scoring import calculate_scores


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 SEO Analyzer Assignment"
    )
}

def analyze_website(url):

    response = fetch_page(url)

    soup = get_soup(response.text)

    headings = analyze_headings(soup)

    report = {

        "url": url,

        "meta": analyze_meta(soup),

        "headings": headings,

        "heading_validation":
            validate_headings(headings),

        "images": analyze_images(soup),

        "links": analyze_links(soup, url),

        "technical":
            analyze_technical(
                response,
                soup,
                url
            ),

        "structured_data":
            analyze_structured_data(soup),

        "social":
            analyze_social_metadata(soup),

        "content":
            analyze_content(soup),

        "keywords":
            analyze_keywords(soup),

        "mobile":
            analyze_mobile(soup),

        "indexability":
            analyze_indexability(soup),

        "url_structure":
            analyze_url_structure(url)
    }

    report["scores"] = calculate_scores(report)

    return report

def fetch_page(url: str):

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=15,
        allow_redirects=True
    )

    response.raise_for_status()

    return response

def get_soup(html):

    return BeautifulSoup(html, "lxml")

def analyze_meta(soup):

    title = soup.title.string.strip() if soup.title and soup.title.string else ""

    description = ""

    meta = soup.find("meta", attrs={"name": "description"})

    if meta:
        description = meta.get("content", "").strip()

    return {
        "title": title,
        "title_length": len(title),

        "description": description,
        "description_length": len(description),
    }

def analyze_headings(soup):

    headings = {}

    for level in range(1, 7):

        tag = f"h{level}"

        headings[tag] = [
            h.get_text(strip=True)
            for h in soup.find_all(tag)
        ]

    return headings

def analyze_images(soup):

    images = soup.find_all("img")

    total = len(images)

    missing_alt = 0

    for img in images:

        alt = img.get("alt")

        if not alt or not alt.strip():

            missing_alt += 1

    return {

        "total_images": total,

        "missing_alt": missing_alt,

        "with_alt": total - missing_alt
    }


def analyze_links(soup, base_url):

    base_domain = urlparse(base_url).netloc

    internal = 0
    external = 0

    for link in soup.find_all("a", href=True):

        href = link["href"]

        if href.startswith("#"):
            continue

        if href.startswith("/"):

            internal += 1

            continue

        parsed = urlparse(href)

        if parsed.netloc == "":

            internal += 1

        elif parsed.netloc == base_domain:

            internal += 1

        else:

            external += 1

    return {

        "internal_links": internal,

        "external_links": external
    }


def analyze_technical(response, soup, url):

    technical = {}

    # HTTPS
    technical["https"] = url.startswith("https://")

    # Redirect
    technical["redirected"] = len(response.history) > 0

    # Canonical
    canonical = soup.find("link", rel="canonical")

    technical["canonical"] = (
        canonical.get("href")
        if canonical
        else None
    )

    # robots.txt
    robots_url = urljoin(url, "/robots.txt")

    try:
        robots = requests.get(
            robots_url,
            timeout=10
        )

        technical["robots_txt"] = robots.status_code == 200

    except:

        technical["robots_txt"] = False

    # sitemap.xml
    sitemap_url = urljoin(url, "/sitemap.xml")

    try:

        sitemap = requests.get(
            sitemap_url,
            timeout=10
        )

        technical["sitemap_xml"] = sitemap.status_code == 200

    except:

        technical["sitemap_xml"] = False

    return technical


def analyze_structured_data(soup):

    json_ld = soup.find_all(
        "script",
        type="application/ld+json"
    )

    microdata = soup.find_all(attrs={"itemscope": True})

    return {

        "json_ld": len(json_ld),

        "microdata": len(microdata),

        "structured_data_present":
            len(json_ld) > 0 or len(microdata) > 0
    }

def analyze_social_metadata(soup):

    og_tags = {}

    twitter_tags = {}

    for meta in soup.find_all("meta"):

        prop = meta.get("property", "")

        name = meta.get("name", "")

        content = meta.get("content", "")

        if prop.startswith("og:"):

            og_tags[prop] = content

        if name.startswith("twitter:"):

            twitter_tags[name] = content

    return {

        "open_graph": og_tags,

        "twitter": twitter_tags,

        "has_open_graph": len(og_tags) > 0,

        "has_twitter_cards": len(twitter_tags) > 0
    }

def analyze_content(soup):

    text = soup.get_text(
        separator=" ",
        strip=True
    )

    words = text.split()

    return {

        "content_length": len(words),

        "readability":
            textstat.flesch_reading_ease(text),

        "estimated_reading_time":
            round(len(words) / 200, 2)
    }


def analyze_mobile(soup):

    viewport = soup.find(
        "meta",
        attrs={"name": "viewport"}
    )

    return {

        "mobile_friendly":
            viewport is not None
    }

def analyze_indexability(soup):

    robots = soup.find(
        "meta",
        attrs={"name": "robots"}
    )

    if not robots:

        return {

            "indexable": True,

            "robots_meta": None
        }

    content = robots.get(
        "content",
        ""
    ).lower()

    return {

        "indexable": "noindex" not in content,

        "robots_meta": content
    }

def analyze_url_structure(url):

    parsed = urlparse(url)

    return {
        "url_length": len(url),
        "has_https": parsed.scheme == "https",
        "has_query_params": bool(parsed.query),
        "has_fragment": bool(parsed.fragment),
        "is_clean_url": (
            not parsed.query
            and not parsed.fragment
        )
    }


def analyze_keywords(soup):

    text = soup.get_text(
        separator=" ",
        strip=True
    ).lower()

    words = text.split()

    stop_words = {
        "the","a","an","and","or","to","of",
        "in","for","on","with","is","are",
        "this","that","by","from","at","as"
    }

    filtered = []

    for word in words:

        word = word.strip(".,!?()[]{}:;\"'")

        if len(word) < 3:
            continue

        if word in stop_words:
            continue

        filtered.append(word)

    top_keywords = Counter(
        filtered
    ).most_common(10)

    return {
        "top_keywords": top_keywords
    }


def validate_headings(headings):

    h1_count = len(headings["h1"])

    levels_present = []

    for i in range(1, 7):

        if headings[f"h{i}"]:

            levels_present.append(i)

    skipped = False

    for i in range(len(levels_present)-1):

        if levels_present[i+1] - levels_present[i] > 1:

            skipped = True

            break

    return {

        "has_h1": h1_count > 0,

        "multiple_h1": h1_count > 1,

        "skipped_heading_level": skipped
    }