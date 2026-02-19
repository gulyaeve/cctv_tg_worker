from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class IncidentFullInfo(BaseModel):
    id: int
    comment: str
    event: int
    time_created: datetime
    visor_id: int
    status: int
    cameras_ids: Optional[list[int]] = None
    cameras_screenshots: Optional[list[str]] = None
    current_teacher: str
    current_group: str
    current_schedule: str
    current_classroom: str
    current_visor: str
