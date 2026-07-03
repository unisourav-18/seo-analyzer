from app.database import SessionLocal
from app.crud import get_job, update_job
from app.analyzer import analyze_website


def process_analysis(job_id: int):
    db = SessionLocal()

    try:
        job = get_job(db, job_id)

        if not job:
            return

        result = analyze_website(job.url)

        update_job(db, job, result)

    finally:
        db.close()