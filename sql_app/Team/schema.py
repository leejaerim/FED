from pydantic import BaseModel

class TeamCreate(BaseModel):
    team_name : str
    emp_fk : int