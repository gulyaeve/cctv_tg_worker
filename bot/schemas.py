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
        if self.comment:
            message += f"<i>{self.comment}</i>\n"
        message += "\n"
        message += f"Кабинет: <i>{self.current_classroom}</i>\n"
        message += f"Занятие: <i>{self.current_schedule}</i>\n"
        message += f"Преподаватель: <i>{self.current_teacher}</i>\n"
        message += f"Группа: <i>{self.current_group}</i>\n"
        
        return message
    

    # 0 всё хор, 1 не см (системный), 2 инц, 3 контр 
