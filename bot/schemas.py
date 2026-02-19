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

    def __str__(self):
        message = "#cctv\n"
        match self.status:
            case 0:
                message += "<b>НАРУШЕНИЙ НЕТ</b>\n"
            case 2:
                message += "<b>ИНЦИДЕНТ</b>\n"
            case 3:
                message += "<b>КОНТРОЛЬ</b>\n"
        message += "\n"
        message += f"<i>{self.time_created.strftime('%d.%m.%Y %T')}</i>"
        
        return message
    

    # 0 всё хор, 1 не см (системный), 2 инц, 3 контр 