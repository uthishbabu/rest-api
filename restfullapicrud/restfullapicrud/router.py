from employeeapi.views import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register("employee",EmployeeViewset)

#local host: p/ api/
#GET POST UPDATE DELETE

#list