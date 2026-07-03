import json

from sqlalchemy.orm import Session

from .models import AnalysisJob


def create_job(db: Session, url: str):

    job = AnalysisJob(
        url=url,
        status="processing"
    )

    db.add(job)

    db.commit()

    db.refresh(job)

    return job


def get_job(db: Session, job_id: int):

    return db.query(AnalysisJob).filter(
        AnalysisJob.id == job_id
    ).first()


def update_job(db: Session, job, result):

    job.status = "completed"

    job.result = json.dumps(result)

    db.commit()