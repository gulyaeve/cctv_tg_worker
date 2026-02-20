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
        message = f"#cctv <i>{self.time_created.strftime('%d.%m.%Y %T')}</i>\n"
        match self.status:
            case 0:
                message += "<b>НАРУШЕНИЙ НЕТ</b>\n"
            case 2:
                message += "<b>ИНЦИДЕНТ</b>\n"
            case 3:
                message += "<b>КОНТРОЛЬ</b>\n"
        message += "\n"
        if self.comment:
            message += f"<i>{self.comment}</i>\n"
        message += f"Занятие: {self.current_schedule}"

        
        return message
    

    # 0 всё хор, 1 не см (системный), 2 инц, 3 контр 
