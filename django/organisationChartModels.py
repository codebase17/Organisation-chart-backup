from django.db import connections
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from hrms.organisationChartServices import convertListToJSON



@csrf_exempt
def getAllEmployees():
    connection = connections['bssrpt_tallydb']
    select_query = """
                    SELECT 
            THEM.FLD_EMP_ID AS FLD_EMP_ID,
            THEM.FLD_EMP_PID AS FLD_EMP_PID,
            THEM.FLD_FULL_NAME,
            THEM.FLD_JOINING_DATE,
            IF(
                THEM.FLD_EMP_PID = 63001,
                14,
                IF (
                THEM.FLD_FULL_NAME = 'Pugazhendhi T (Pugal)',
                16,
                THEM.FLD_TENURE_YRS
                )
            ) AS FLD_TENURE_YRS,
            THEM.FLD_TRAINEE_FLAG,
            CASE
                THEM.FLD_TEMP_FLAG 
                WHEN 0 
                THEN 'Permanent' 
                WHEN 1 
                THEN 'Temporary' 
                WHEN 2 
                THEN 'Intern' 
                WHEN 3 
                THEN 'External' 
                ELSE '' 
            END AS FLD_EMP_TYPE_NAME,
            CASE
                THEM.FLD_GENDER 
                WHEN 1 
                THEN 'Male' 
                WHEN 2 
                THEN 'Female' 
                ELSE '' 
            END AS FLD_GENDER,
            TAOM_COMP.FLD_NAME AS FLD_COMP_NAME,
            THEPD.FLD_CADRE_ID,
            THEPD.FLD_GRADE_ID,
            THDM.FLD_DEPT_NAME,
            THDM.FLD_DEPT_ID,
            THEM_HOF.FLD_FULL_NAME AS HOF_NAME,
            THERD.FLD_SPONSOR_ID,
            THESDM.FLD_SUB_DEPT_ID,
            THESDM.FLD_NAME AS FLD_SUB_DEPT_NAME,
            THESDM.FLD_SHORT_NAME AS FLD_SUB_DEPT_SHORT_NAME,
            TAOM.FLD_HRMS_PRINT_NAME AS FLD_BRANCH_NAME,
            THEPCM_CADRE.FLD_NAME AS FLD_CADRE_NAME,
            THEPCM_GRADE.FLD_NAME AS FLD_GRADE_NAME,
            THECLM.FLD_CAREER_LEVEL_ID,
            THECLM.FLD_SHORT_NAME AS FLD_CAREER_SHORT_NAME,
            THECLM.FLD_CAREER_LEVEL_NAME AS FLD_CAREER_LEVEL_NAME,
            DESIG_MASTER.FLD_DESIGNATION_NAME AS FLD_DESIGNATION_NAME,
            THEPCM_TITLE.FLD_NAME AS FLD_TITLE_NAME,
            THEM_POTENTIAL_APP.FLD_EMP_ID AS FLD_FUNC_REP_ID,
            THEM_SPONSOR.FLD_EMP_ID AS FLD_FUNC_ADMIN_ID,
            THEM_CONTINUOUS_APPRAISER.FLD_EMP_ID AS FLD_CONTINUOUS_APPRAISER_ID,
            THEM_HALF_YEARLY_APPRAISER.FLD_EMP_ID AS FLD_HALF_YEARLY_APPRAISER_ID,
            THEM_POTENTIAL_APP.FLD_FULL_NAME AS FLD_POTENTIAL_NAME,
            THEM_SPONSOR.FLD_FULL_NAME AS FLD_SPONSOR_NAME,
            THEM_CONTINUOUS_APPRAISER.FLD_EMP_ID AS FLD_CONTINUOUS_APPRAISER_ID,
            THEM_CONTINUOUS_APPRAISER.FLD_FULL_NAME AS FLD_CONTINUOUS_APPRAISER_NAME,
            THEM_HALF_YEARLY_APPRAISER.FLD_FULL_NAME AS FLD_HALF_YEARLY_APPRAISER_NAME,
            THEM.FLD_OFFICE_EMAIL,
            CASE
                THEM.FLD_BLOOD_GROUP 
                WHEN 1 
                THEN 'A +ve ' 
                WHEN 2 
                THEN 'B +ve ' 
                WHEN 3 
                THEN 'O +ve ' 
                WHEN 4 
                THEN 'AB +ve ' 
                WHEN 9 
                THEN 'A1 +ve ' 
                WHEN 11 
                THEN 'A1B +ve ' 
                WHEN 13 
                THEN 'A2 +ve ' 
                WHEN 15 
                THEN 'A2B +ve ' 
                WHEN 5 
                THEN 'A -ve ' 
                WHEN 6 
                THEN 'B -ve ' 
                WHEN 7 
                THEN 'O -ve ' 
                WHEN 8 
                THEN 'AB -ve ' 
                WHEN 10 
                THEN 'A1 -ve ' 
                WHEN 12 
                THEN 'A1B -ve ' 
                WHEN 14 
                THEN 'A2 -ve ' 
                WHEN 16 
                THEN 'A2B -ve ' 
                ELSE '' 
            END AS FLD_BLOOD_GROUP,
            THDM.FLD_FQ_DEPT_SHORT_NAME,
            TCCM_CITY.FLD_CITY_NAME,
            TAOM.FLD_PHONE,
            THEM.FLD_EXTN_NUM,
            THEM.FLD_OFFICE_DIRECT_PHONE,
            THEM.FLD_OFFICE_MOBILE,
            THEM.FLD_ORG_CHART_VISIBILITY_FLAG AS ORG_CHART_VISIBILITY,
            IF (
                THEM.FLD_FULL_NAME = 'Pugazhendhi T (Pugal)',
                3,
                THEPD.FLD_CADRE_ID
            ) AS FLD_MODIFIED_CADRE_ID,
            IF (
                THEM.FLD_FULL_NAME = 'Pugazhendhi T (Pugal)',
                'T2',
                THEPCM_GRADE.FLD_NAME
            ) AS FLD_MODIFIED_GRADE_NAME 
            FROM
            TBL_HRMS_EMP_MASTER THEM 
            LEFT JOIN TBL_HRMS_EMP_POS_DETAILS THEPD 
                ON THEM.FLD_EMP_ID = THEPD.FLD_EMP_ID 
                AND THEPD.FLD_CURR_FLAG = 1 
            LEFT JOIN TBL_HRMS_EMP_REPORTING_DETAILS THERD 
                ON THEM.FLD_EMP_ID = THERD.FLD_EMP_ID 
                AND THERD.FLD_CURR_FLAG = 1 
            LEFT JOIN TBL_HRMS_EMP_MASTER THEM_POTENTIAL_APP 
                ON THEM_POTENTIAL_APP.FLD_EMP_ID = THERD.FLD_POTENTIAL_APPRAISER 
            LEFT JOIN TBL_HRMS_EMP_MASTER THEM_SPONSOR 
                ON THEM_SPONSOR.FLD_EMP_ID = THERD.FLD_SPONSOR_ID 
            LEFT JOIN TBL_HRMS_EMP_MASTER THEM_CONTINUOUS_APPRAISER 
                ON THEM_CONTINUOUS_APPRAISER.FLD_EMP_ID = THERD.FLD_CONTINUOUS_APPRAISER 
            LEFT JOIN TBL_HRMS_EMP_MASTER THEM_HALF_YEARLY_APPRAISER 
                ON THEM_HALF_YEARLY_APPRAISER.FLD_EMP_ID = THERD.FLD_HALF_YEARLY_APPRAISER 
            LEFT JOIN TBL_HRMS_EMP_POS_COMMON_MASTER THEPCM_CADRE 
                ON THEPCM_CADRE.FLD_COMMON_MASTER_ID = THEPD.FLD_CADRE_ID 
            LEFT JOIN TBL_HRMS_EMP_POS_COMMON_MASTER THEPCM_GRADE 
                ON THEPCM_GRADE.FLD_COMMON_MASTER_ID = THEPD.FLD_GRADE_ID 
            LEFT JOIN TBL_HRMS_EMP_POS_COMMON_MASTER THEPCM_TITLE 
                ON THEPCM_TITLE.FLD_COMMON_MASTER_ID = THEPD.FLD_TITLE_ID 
            LEFT JOIN TBL_HRMS_EMP_DEPT_MASTER THDM 
                ON THEPD.FLD_DEPT_ID = THDM.FLD_DEPT_ID 
                AND THDM.FLD_STATUS = 1 
            LEFT JOIN TBL_HRMS_EMP_MASTER THEM_HOF 
                ON THDM.FLD_HOD_ID = THEM_HOF.FLD_EMP_ID 
            LEFT JOIN TBL_HRMS_EMP_SUB_DEPT_MASTER THESDM 
                ON THEPD.FLD_SUB_DEPT_ID = THESDM.FLD_SUB_DEPT_ID 
            LEFT JOIN TBL_HRMS_EMP_CAREER_LEVEL_MASTER AS THECLM 
                ON (
                THECLM.FLD_CAREER_LEVEL_ID = THEPD.FLD_CAREER_LEVEL_ID
                ) 
            LEFT JOIN TBL_HRMS_EMP_DESIGNATION_MASTER AS DESIG_MASTER 
                ON (
                DESIG_MASTER.FLD_DESIGNATION_ID = THEPD.FLD_DESIGNATION_ID
                ) 
            LEFT JOIN TBL_ADMIN_OFFICE_MASTER TAOM 
                ON TAOM.FLD_OFFICE_ID = THEPD.FLD_BRANCH_ID 
            LEFT JOIN TBL_CONTACT_CITY_MASTER TCCM_CITY 
                ON TCCM_CITY.FLD_CITY_ID = TAOM.FLD_CITY_ID 
            LEFT JOIN TBL_ADMIN_OFFICE_MASTER TAOM_COMP 
                ON TAOM_COMP.FLD_OFFICE_ID = THEM.FLD_COMPANY_ID 
            WHERE THEM.FLD_ORG_CHART_VISIBILITY_FLAG = 1 
            AND THEM.FLD_TEMP_FLAG IN (0, 1, 3) 
            AND THEM.FLD_STATUS = 1 
            AND THEM.FLD_PROFILE_CONFIGURED_FLAG = 1 
            ORDER BY FLD_TENURE_YRS DESC,
            FLD_FULL_NAME;
  
    """
    cursor = connection.cursor()
    cursor.execute(select_query)
    rows = cursor.fetchall()
    keys = ["FLD_EMP_ID",
            "FLD_EMP_PID",
            "FLD_FULL_NAME",
            "FLD_JOINING_DATE",
            "FLD_TENURE_YRS",
            "FLD_TRAINEE_FLAG",
            "FLD_EMP_TYPE_NAME",
            "FLD_GENDER",
            "FLD_COMP_NAME",
            "FLD_CADRE_ID",
            "FLD_GRADE_ID",
            "FLD_DEPT_NAME",
            "FLD_DEPT_ID",
            "HOF_NAME",
            "FLD_SPONSOR_ID",
            "FLD_SUB_DEPT_ID",
            "FLD_SUB_DEPT_NAME",
            "FLD_SUB_DEPT_SHORT_NAME",
            "FLD_BRANCH_NAME",
            "FLD_CADRE_NAME",
            "FLD_GRADE_NAME",
            "FLD_CAREER_LEVEL_ID",
            "FLD_CAREER_SHORT_NAME",
            "FLD_CAREER_LEVEL_NAME",
            "FLD_DESIGNATION_NAME",
            "FLD_TITLE_NAME",
            "FLD_FUNC_REP_ID",
            "FLD_FUNC_ADMIN_ID",
            "FLD_CONTINUOUS_APPRAISER_ID",
            "FLD_HALF_YEARLY_APPRAISER_ID",
            "FLD_POTENTIAL_NAME",
            "FLD_SPONSOR_NAME",
            "FLD_CONTINUOUS_APPRAISER_ID",
            "FLD_CONTINUOUS_APPRAISER_NAME",
            "FLD_HALF_YEARLY_APPRAISER_NAME",
            "FLD_OFFICE_EMAIL",
            "FLD_BLOOD_GROUP",
            "FLD_FQ_DEPT_SHORT_NAME",
            "FLD_CITY_NAME",
            "FLD_PHONE",
            "FLD_EXTN_NUM",
            "FLD_OFFICE_DIRECT_PHONE",
            "FLD_OFFICE_MOBILE",
            "ORG_CHART_VISIBILITY",
            "FLD_MODIFIED_CADRE_ID",
            "FLD_MODIFIED_GRADE_NAME"
    ]
    result = convertListToJSON(rows,keys)
    return result



