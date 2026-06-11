from pydantic import BaseModel

class Employee(BaseModel):
    emp_id: int
    emp_name: str
    department: str
    salary: float

class SalaryUpdate(BaseModel):
    salary: float
    
