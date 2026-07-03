import json

from fastapi import APIRouter
from fastapi import BackgroundTasks
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas import AnalyzeRequest

from app.crud import create_job
from app.crud import get_job

from app.jobs import process_analysis

router = APIRouter()


@router.post("/analyze")
def analyze(
    request: AnalyzeRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):

    job = create_job(db, request.url)

    background_tasks.add_task(
        process_analysis,
        job.id
    )

    return {
        "job_id": job.id,
        "status": job.status
    }


@router.get("/results/{job_id}")
def results(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = get_job(db, job_id)

    if not job:
        raise HTTPException(404)

    return {
        "status": job.status,
        "result": json.loads(job.result) if job.result else None
    }