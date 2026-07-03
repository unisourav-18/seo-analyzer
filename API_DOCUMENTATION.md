# API Documentation

## Base URL

### Local Development

```
http://127.0.0.1:8000
```

### Production

```
https://seo-analyzer-icm6.onrender.com
```

---

# Authentication

No authentication is required.

---

# Endpoints

## 1. Analyze Website

**Endpoint**

```
POST /api/analyze
```

### Description

Creates a new SEO analysis job and starts processing it asynchronously using FastAPI BackgroundTasks.

---

### Request Body

```json
{
  "url": "https://github.com"
}
```

---

### Successful Response

```json
{
  "job_id": 1,
  "status": "pending"
}
```

---

### Response Fields

| Field | Type | Description |
|--------|------|-------------|
| job_id | Integer | Unique analysis job identifier |
| status | String | Current job status |

Possible Status Values

- pending
- completed

---

## 2. Get Analysis Result

**Endpoint**

```
GET /api/results/{job_id}
```

Example

```
GET /api/results/1
```

---

### Description

Returns the analysis status. Once processing is complete, the SEO report is returned.

---

### Successful Response

```json
{
  "status": "completed",
  "result": {
    "url": "https://github.com",
    "meta": {
      "title": "...",
      "description": "..."
    },
    "technical": {
      "https": true,
      "robots_txt": true,
      "canonical": "https://github.com"
    },
    "scores": {
      "overall": {
        "score": 61,
        "max_score": 100
      }
    }
  }
}
```

---

### Response Fields

| Field | Type | Description |
|--------|------|-------------|
| status | String | Analysis status |
| result | Object | Complete SEO report |

---

# SEO Report Structure

The generated SEO report contains the following sections.

- URL Information
- Meta Information
- Heading Analysis
- Heading Validation
- Image Analysis
- Internal & External Links
- Technical SEO
- Structured Data
- Social Metadata
- Content Analysis
- Keyword Analysis
- Mobile Friendliness
- Indexability
- URL Structure
- SEO Scores

---

# Error Responses

## Invalid URL

```json
{
  "detail": "Invalid URL"
}
```

---

## Job Not Found

```json
{
  "detail": "Not Found"
}
```

Status Code

```
404
```

---

# API Workflow

```
Client
   │
   ▼
POST /api/analyze
   │
   ▼
Background Task Started
   │
   ▼
SEO Analysis Engine
   │
   ▼
Database
   │
   ▼
GET /api/results/{job_id}
   │
   ▼
SEO Report Returned
```