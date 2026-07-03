# Backend Architecture

## Overview

The backend is built using **FastAPI** and follows a modular architecture. Each component has a single responsibility, making the project easier to understand, maintain, and extend.

The system performs website SEO analysis asynchronously, stores the generated report in the database, and exposes REST APIs for retrieving the results.

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Backend Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | SQLite (Development), PostgreSQL (Production) |
| HTML Parsing | BeautifulSoup |
| HTTP Requests | Requests |
| Background Processing | FastAPI BackgroundTasks |
| Deployment | Render |

---

# Project Structure

```
backend/
│
├── app/
│   ├── analyzer.py
│   ├── scoring.py
│   ├── crud.py
│   ├── database.py
│   ├── jobs.py
│   ├── models.py
│   ├── schemas.py
│   ├── main.py
│   └── routers/
│       └── analyze.py
│
├── requirements.txt
└── results.db
```

---

# Architecture Overview

```
                React Frontend
                       │
                       │
         POST /api/analyze
                       │
                       ▼
                FastAPI Router
                       │
                       ▼
              Create Analysis Job
                       │
                       ▼
          FastAPI Background Task
                       │
                       ▼
              Website Analyzer
                       │
      ┌────────────────┼────────────────┐
      │                │                │
      ▼                ▼                ▼
 Meta Analysis   Technical SEO   Content Analysis
      │                │                │
      └────────────────┼────────────────┘
                       ▼
               SEO Scoring Engine
                       │
                       ▼
             Store Report in Database
                       │
                       ▼
          GET /api/results/{job_id}
                       │
                       ▼
               React Frontend
```

---

# Request Flow

## Step 1

The user enters a website URL in the React frontend.

Example:

```
https://github.com
```

---

## Step 2

The frontend sends a request to:

```
POST /api/analyze
```

---

## Step 3

FastAPI creates a new analysis job in the database with the status:

```
pending
```

---

## Step 4

A FastAPI Background Task starts processing the website asynchronously.

This allows the API to respond immediately without blocking the client.

---

## Step 5

The analyzer downloads the webpage and performs multiple SEO checks including:

- Meta tag analysis
- Heading analysis
- Image analysis
- Link analysis
- Technical SEO checks
- Structured data detection
- Social metadata detection
- Content analysis
- Keyword extraction
- URL structure analysis

---

## Step 6

The scoring engine calculates:

- Technical SEO Score
- On-Page SEO Score
- Content Quality Score
- Performance Score
- Overall SEO Score

---

## Step 7

The complete report is stored in the database and the job status becomes:

```
completed
```

---

## Step 8

The frontend periodically requests:

```
GET /api/results/{job_id}
```

Once the analysis is complete, the backend returns the full SEO report.

---

# Database Design

Each analysis job stores:

| Field | Description |
|--------|-------------|
| id | Job identifier |
| url | Website URL |
| status | pending / completed |
| result | JSON SEO report |

The generated report is stored as JSON, making it flexible and easy to extend with additional SEO metrics.

---

# Design Decisions

The backend was designed with the following principles:

- Modular architecture
- Separation of concerns
- Asynchronous processing
- RESTful API design
- Extensible scoring system
- Database-backed job tracking

Each module has a dedicated responsibility, reducing coupling and improving maintainability.

---

# Scalability

The current architecture can be extended with:

- Multiple worker processes
- Redis task queue
- Celery background workers
- Scheduled website monitoring
- Authentication and user accounts
- Report history
- PDF report generation
- Lighthouse integration
- Core Web Vitals analysis

---

# Summary

The backend architecture separates API routing, SEO analysis, scoring, and data persistence into independent modules.

This modular design keeps the project easy to maintain while allowing future enhancements without major architectural changes.