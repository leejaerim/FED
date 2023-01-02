from pydantic import BaseModel

class TeamCreate(BaseModel):
    team_name : str
    emp_fk : int

class TeamSelect(BaseModel):
    team_id : int
    team_name : str
    emp_fk : int