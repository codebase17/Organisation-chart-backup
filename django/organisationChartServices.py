from django.db import connections
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def convertListToJSON(rows,keys):
    dictionary = {}
    listOfDictionary = [{}]
    count=0
    for i in rows:
        for j in i:
            dictionary[keys[count%len(keys)]]=j
            count=count+1
            if(count%len(keys)==0):
                listOfDictionary.append(dictionary.copy())
                dictionary.clear()
    del listOfDictionary[0]
    return listOfDictionary

@csrf_exempt
def getEmployeeBYCareerLevelId(data,careerLevelId):
    tempResult=[[]]
    length=len(data)
    for i in range(length):
        check=data[i].get("FLD_CAREER_LEVEL_ID")
        if(check==careerLevelId):
            temp=[data[i].get("FLD_EMP_ID"), data[i].get("FLD_FULL_NAME")]
            tempResult.append(tuple(temp))
    del tempResult[0]
    rows=tuple(tempResult)
    keys=["FLD_EMP_ID","FLD_FULL_NAME"] 
    result = convertListToJSON(rows,keys)
    return result

def getEmployeeBYAppraiserId(data, appraiserId):
    tempResult=[[]]
    length=len(data)
    for i in range(length):
        check=data[i].get("FLD_CONTINUOUS_APPRAISER_ID")
        if(check==appraiserId):
            temp=[data[i].get("FLD_EMP_ID"), data[i].get("FLD_FULL_NAME")]
            tempResult.append(tuple(temp))
    del tempResult[0]
    rows=tuple(tempResult)
    keys=["FLD_EMP_ID","FLD_FULL_NAME"] 
    result = convertListToJSON(rows,keys)
    return result

# # Get the total count of reporting employees
# def getCountCommonFun(data, all_employees, appraiserId):
#     res= getEmployeeBYAppraiserId(all_employees, appraiserId)
#     check=data[i].get("FLD_CAREER_LEVEL_ID")
    
#     sum=0
#     sum+=len(res)
#     check=res[i].get("FLD_EMP_PID")
#     getCountCommonFun(all_employees, check)
    
    
    
#     career_level_id =3 (means they dont have any reportee, they MS, manage-self)