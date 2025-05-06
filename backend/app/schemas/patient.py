from datetime import datetime
from pydantic import BaseModel
from schemas.user import UserCreate

class PatientUser(UserCreate):
    user_id: int
    
class AdminUpdatePatient(BaseModel):
    id: int   #patient_id
    status_expiry : datetime | None = None