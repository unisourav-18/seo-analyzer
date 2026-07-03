# ==========================================
# SEO Scoring Configuration
# ==========================================

# Maximum Scores
TECHNICAL_MAX = 30
ONPAGE_MAX = 30
CONTENT_MAX = 20
PERFORMANCE_MAX = 20
OVERALL_MAX = 100

# Technical SEO Weights
HTTPS_POINTS = 5
ROBOTS_POINTS = 5
SITEMAP_POINTS = 4
CANONICAL_POINTS = 4
MOBILE_POINTS = 4
INDEXABLE_POINTS = 4
STRUCTURED_DATA_POINTS = 4

# On-Page SEO Weights
TITLE_POINTS = 8
DESCRIPTION_POINTS = 8
H1_POINTS = 6
IMAGE_ALT_POINTS = 4
INTERNAL_LINK_POINTS = 2
EXTERNAL_LINK_POINTS = 2

# Content Weights
CONTENT_LENGTH_POINTS = 8
READABILITY_POINTS = 6
HEADING_POINTS = 6

# Performance
PERFORMANCE_PLACEHOLDER = 15


# ==========================================
# Technical SEO Score
# ==========================================

def technical_score(report):

    score = 0

    passed = []
    failed = []

    tech = report["technical"]

    if tech["https"]:
        score += HTTPS_POINTS
        passed.append("HTTPS enabled")
    else:
        failed.append("HTTPS missing")

    if tech["robots_txt"]:
        score += ROBOTS_POINTS
        passed.append("robots.txt found")
    else:
        failed.append("robots.txt missing")

    if tech["sitemap_xml"]:
        score += SITEMAP_POINTS
        passed.append("Sitemap found")
    else:
        failed.append("Sitemap missing")

    if tech["canonical"]:
        score += CANONICAL_POINTS
        passed.append("Canonical tag present")
    else:
        failed.append("Canonical tag missing")

    if report["mobile"]["mobile_friendly"]:
        score += MOBILE_POINTS
        passed.append("Mobile friendly")
    else:
        failed.append("Viewport meta tag missing")

    if report["indexability"]["indexable"]:
        score += INDEXABLE_POINTS
        passed.append("Page is indexable")
    else:
        failed.append("Page marked as noindex")

    if report["structured_data"]["structured_data_present"]:
        score += STRUCTURED_DATA_POINTS
        passed.append("Structured data detected")
    else:
        failed.append("Structured data missing")

    return {
        "score": score,
        "max_score": TECHNICAL_MAX,
        "passed": passed,
        "failed": failed
    }


# ==========================================
# On-Page SEO Score
# ==========================================

def onpage_score(report):

    score = 0

    passed = []
    failed = []

    meta = report["meta"]

    if 30 <= meta["title_length"] <= 60:
        score += TITLE_POINTS
        passed.append("Good title length")
    else:
        failed.append("Title length should be between 30 and 60 characters")

    if 120 <= meta["description_length"] <= 160:
        score += DESCRIPTION_POINTS
        passed.append("Good meta description length")
    else:
        failed.append("Meta description should be between 120 and 160 characters")

    if report["heading_validation"]["has_h1"]:
        score += H1_POINTS
        passed.append("H1 tag found")
    else:
        failed.append("Missing H1 tag")

    images = report["images"]

    if images["total_images"] == 0:
        score += IMAGE_ALT_POINTS
        passed.append("No images requiring alt text")
    elif images["missing_alt"] == 0:
        score += IMAGE_ALT_POINTS
        passed.append("All images contain alt text")
    else:
        failed.append(
            f'{images["missing_alt"]} image(s) missing alt text'
        )

    if report["links"]["internal_links"] > 0:
        score += INTERNAL_LINK_POINTS
        passed.append("Internal links found")
    else:
        failed.append("No internal links found")

    if report["links"]["external_links"] > 0:
        score += EXTERNAL_LINK_POINTS
        passed.append("External links found")
    else:
        failed.append("No external links found")

    return {
        "score": score,
        "max_score": ONPAGE_MAX,
        "passed": passed,
        "failed": failed
    }


# ==========================================
# Content Score
# ==========================================

def content_score(report):

    score = 0

    passed = []
    failed = []

    content = report["content"]

    if content["content_length"] >= 300:
        score += CONTENT_LENGTH_POINTS
        passed.append("Good content length")
    else:
        failed.append("Content is too short")

    readability = content["readability"]

    if readability >= 50:
        score += READABILITY_POINTS
        passed.append("Readable content")
    else:
        failed.append("Content readability is low")

    heading = report["heading_validation"]

    if (
        heading["has_h1"]
        and not heading["skipped_heading_level"]
    ):
        score += HEADING_POINTS
        passed.append("Heading hierarchy is valid")
    else:
        failed.append("Heading hierarchy needs improvement")

    return {
        "score": score,
        "max_score": CONTENT_MAX,
        "passed": passed,
        "failed": failed
    }


# ==========================================
# Performance Score (Placeholder)
# ==========================================

def performance_score():

    return {

        "score": PERFORMANCE_PLACEHOLDER,

        "max_score": PERFORMANCE_MAX,

        "passed": [
            "Performance analysis placeholder"
        ],

        "failed": []
    }


# ==========================================
# Final Score Calculator
# ==========================================

def calculate_scores(report):

    technical = technical_score(report)

    onpage = onpage_score(report)

    content = content_score(report)

    performance = performance_score()

    total = (
        technical["score"]
        + onpage["score"]
        + content["score"]
        + performance["score"]
    )

    return {

        "technical": technical,

        "onpage": onpage,

        "content": content,

        "performance": performance,

        "overall": {

            "score": total,

            "max_score": OVERALL_MAX
        }
    }