from sqlalchemy import (
    Column,
    DateTime,
    func
)


class TimeMixin:
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
