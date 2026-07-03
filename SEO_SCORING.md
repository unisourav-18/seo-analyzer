# SEO Scoring System

## Overview

This project uses a custom SEO scoring system inspired by modern SEO auditing tools such as Woorank.

The scoring logic is entirely custom-built and does not use any third-party SEO scoring services.

The overall SEO score is calculated out of **100 points**.

---

# Score Distribution

| Category | Maximum Score |
|------------|--------------:|
| Technical SEO | 30 |
| On-Page SEO | 30 |
| Content Quality | 20 |
| Performance | 20 |
| **Overall** | **100** |

---

# 1. Technical SEO (30 Points)

Technical SEO evaluates whether a website follows essential technical best practices.

## Checks Performed

| Check | Points |
|--------|--------:|
| HTTPS Enabled | 5 |
| robots.txt Present | 5 |
| sitemap.xml Present | 4 |
| Canonical Tag Present | 4 |
| Mobile Friendly | 4 |
| Indexable Page | 4 |
| Structured Data Present | 4 |

Maximum Score

```
30
```

---

# 2. On-Page SEO (30 Points)

On-page SEO evaluates HTML elements that directly affect search engine optimization.

## Checks Performed

| Check | Points |
|--------|--------:|
| Title Length (30–60 chars) | 8 |
| Meta Description (120–160 chars) | 8 |
| H1 Tag Present | 6 |
| All Images Have Alt Text | 4 |
| Internal Links Present | 2 |
| External Links Present | 2 |

Maximum Score

```
30
```

---

# 3. Content Quality (20 Points)

Content quality measures how informative and readable the webpage content is.

## Checks Performed

| Check | Points |
|--------|--------:|
| Content Length ≥ 300 Characters | 8 |
| Readability Score ≥ 50 | 6 |
| Valid Heading Hierarchy | 6 |

Maximum Score

```
20
```

---

# 4. Performance Score (20 Points)

Currently, a placeholder score is returned.

The architecture has been designed so that this module can later be extended using tools such as:

- Google Lighthouse
- Core Web Vitals
- PageSpeed Insights

Current Score

```
15 / 20
```

---

# Overall Score Formula

```
Overall Score =
Technical SEO
+ On-Page SEO
+ Content Quality
+ Performance
```

Maximum Score

```
100
```

---

# Example

Suppose a website receives:

| Category | Score |
|------------|-------:|
| Technical SEO | 24 |
| On-Page SEO | 26 |
| Content Quality | 17 |
| Performance | 15 |

Overall Score

```
24 + 26 + 17 + 15 = 82 / 100
```

---

# Design Considerations

The scoring system was designed to:

- Reward websites following SEO best practices.
- Penalize missing or incorrect SEO elements.
- Keep the scoring simple and transparent.
- Make the logic easy to understand and extend.
- Allow future integration of additional SEO metrics without changing the overall architecture.

---

# Future Improvements

Future versions of the scoring system can include:

- Lighthouse Performance Metrics
- Core Web Vitals
- Accessibility Score
- Best Practices Score
- Multi-page Website Analysis
- Broken Link Detection
- Page Speed Metrics
- Crawl Depth Analysis
- Duplicate Content Detection

---

# Summary

The scoring system is modular, transparent, and easy to extend. Each category is calculated independently and combined to produce a final SEO score out of **100**, giving users a clear understanding of their website's SEO health.