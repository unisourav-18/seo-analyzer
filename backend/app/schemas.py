from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    url: str


class AnalyzeResponse(BaseModel):
    job_id: int
    status: str