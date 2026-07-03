from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from .database import Base


class AnalysisJob(Base):

    __tablename__ = "analysis_jobs"

    id = Column(Integer, primary_key=True, index=True)

    url = Column(String, nullable=False)

    status = Column(String, default="processing")

    result = Column(Text, nullable=True)