from ninja import NinjaAPI

from django.shortcuts import get_object_or_404

from api.Schema.api_v1_schema import HelloSchema
from api.Schema.api_v1_schema import UserSchema
from api.Schema.api_v1_schema import ErrorSchema
from api.Schema.api_v1_schema import DepartmentIn
from api.Schema.api_v1_schema import DepartmentOut
from api.Schema.api_v1_schema import EmployeeIn
from api.Schema.api_v1_schema import EmployeeOut

from api.models import Employee
from api.models import Department
app : NinjaAPI = NinjaAPI(
    title = "django-ninjaの練習",
    version = "0.1.0",
)

@app.get('/hello')
def add(request):
    return {"Hello":"World"}


@app.get('/hello_for_you')
def add(request,name:str="your_name",age:int=0):
    return f"hello {name},{age}"

@app.get('/math')
def get_result(request,a:int=0,b:int=0):
    return {"add":a+b,"multi":a*b}

@app.post("hello_post")
def hello(request,data:HelloSchema):
    return f"hello {data.name}"

@app.get("/me",response = {200:UserSchema, 403:ErrorSchema})
def get_me(request):
    if not request.user.is_authenticated:
        return 403, {"message":"not authenticated"}
    return request.user

@app.post("/department")
def create_department(request,payload: DepartmentIn):
    department = Department.objects.create(**payload.dict())
    return {"id":department.id}

@app.get("/departments/{department_id}",response = DepartmentOut)
def get_department(request,department_id:int):
    department = get_object_or_404(Department,id=department_id)
    return department

@app.post("/employee")
def create_employee(request,payload: EmployeeIn):
    employee = Employee.objects.create(**payload.dict())
    return {"id":employee.id}

@app.get("/employees/{employee_id}",response = EmployeeOut)
def get_employee(request,employee_id:int):
    employee = get_object_or_404(Employee,id=employee_id)
    return employee