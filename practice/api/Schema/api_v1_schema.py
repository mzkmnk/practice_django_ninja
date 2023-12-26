from ninja import Schema
from datetime import date

class HelloSchema(Schema):
    name : str = "test"
    
class UserSchema(Schema):
    username : str
    is_authenticated : bool
    email : str = None
    first_name : str = None
    last_name : str = None

class ErrorSchema(Schema):
    message : str

class DepartmentIn(Schema):
    title : str
    
class DepartmentOut(DepartmentIn):
    id : int

class EmployeeIn(Schema):
    first_name : str
    last_name : str
    department_id : int = None
    birthdate : date = None
    
class EmployeeOut(EmployeeIn):
    id : int