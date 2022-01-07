from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from hrms import organisationChartModels
from hrms import organisationChartServices

#for fetching all employees
def get_all_employees(request):
    if request.method=='GET':
        try:
            query_data = organisationChartModels.getAllEmployees()
            get_employee_by_career_level_id(request, query_data)
            #request.session['AllEmployeesData'] = query_data
            print("employees data",request.session['AllEmployeesData'])
            #print("using get",request.session.get('AllEmployeesData'))
            result = {"Status": "success", "Data":query_data }
            return JsonResponse(result, safe=False)
        except Exception as e:
            status = 0
            a = {"Status":status, "Data": str(e)}
            return JsonResponse(a, safe=False)
        
#fetching employees by Career level ID
def get_employee_by_career_level_id(request, all_employees):
    if request.method=='GET':
        careerLevelId = int(request.GET.get('q', None))
        try:
           #all_employees = organisationChartModels.getAllEmployees()
            query_data = organisationChartServices.getEmployeeBYCareerLevelId(all_employees,careerLevelId)     
            result = {"Status": "success", "Data":query_data }
            return JsonResponse(result, safe=False)
        except Exception as e:
            status = 0
            a = {"Status":status, "Data": str(e)}
            return JsonResponse(a, safe=False)

#fetching employees by Continuous Appraiser Id          
def get_sub_employee_by_appraiser_id(request, all_employees):
    if request.method=='GET':
        appraiserId= int(request.GET.get('q', None))
        try:
            #all_employees = organisationChartModels.getAllEmployees()
            query_data = organisationChartServices.getEmployeeBYAppraiserId(all_employees,appraiserId)     
            result = {"Status": "success", "Data":query_data, "count":len(query_data) }
            return JsonResponse(result, safe=False)
        except Exception as e:
            status = 0
            a = {"Status":status, "Data": str(e)}
            return JsonResponse(a, safe=False) 
        
# def get_count_of_sub_reportees(request):
#     if request.method=='GET':
#         appraiserId= int(request.GET.get('q', None))
#         try:
#             all_employees = organisationChartModels.getAllEmployees()
#             reportees=organisationChartServices.get_count_common_fun(all_employees, appraiserId)
#             result = {"Status": "success", "Data":reportees}
#             return JsonResponse(result, safe=False)
#         except Exception as e:
#             status = 0
#             a = {"Status":status, "Data": str(e)}
#             return JsonResponse(a, safe=False) 


    