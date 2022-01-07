from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLResolver

from hrms import croviews, shoutoutViews
from . import goalscheckinviews
from . import attendanceCheckinViews
from . import eventsRemindersViews
from . import views
from . import ERClaimViews
from . import PeopleAnalyticsViews
from . import pmsviews
from hrms import IntranetEssView
from hrms import HrRelatedViews
from hrms import organisationChartViews


urlpatterns = [
    path('', views.index, name='index'),
    path('Users',croviews.get_users_view),
    path('Userss',croviews.autocomplete_user_view),
    path('get_goals_listing', goalscheckinviews.get_goals_listing, name='get_goals_listing'),
    path('get_goal_details', goalscheckinviews.get_goal_details, name='get_goal_details'),
    path('get_goal_task_details', goalscheckinviews.get_goal_task_details, name='get_goal_task_details'),
    path('set_goal_details', goalscheckinviews.set_goal_details, name='set_goal_details'),
    path('submit_goals_checkin', goalscheckinviews.submit_goals_checkin, name='submit_goals_checkin'),
    path('is_a_manager', goalscheckinviews.is_a_manager, name='is_a_manager'),
    path('emp_listing_for_rm', goalscheckinviews.emp_listing_for_rm, name='emp_listing_for_rm'),
    path('set_goal_details_from_rm', goalscheckinviews.set_goal_details_from_rm, name='set_goal_details_from_rm'),
    path('submit_goals_checkin_by_rm', goalscheckinviews.submit_goals_checkin_by_rm, name='submit_goals_checkin_by_rm'),
    path('get_comment_listing', goalscheckinviews.get_comment_listing, name='get_comment_listing'),
    path('set_comments_for_rm', goalscheckinviews.set_comments_for_rm, name='set_comments_for_rm'),
    path('get_goals_check_in_history', goalscheckinviews.get_goals_check_in_history, name='get_goals_check_in_history'),

    path('set_attendance_in_details', attendanceCheckinViews.set_attendance_in_details, name='set_attendance_in_details'),
    path('get_attendance_in_out_details', attendanceCheckinViews.get_attendance_in_out_details, name='get_attendance_in_details'),
    path('set_attendance_out_details', attendanceCheckinViews.set_attendance_out_details, name='set_attendance_in_details '),
    # path('edit_attendance_in_out_details', attendanceCheckinViews.edit_attendance_in_out_details, name='edit_attendance_in_out_details'),
    path('get_attendance_read_only_details', attendanceCheckinViews.get_attendance_read_only_details, name='get_attendance_read_only_details'),
    path('get_attendance_read_only_for_other_emp', attendanceCheckinViews.get_attendance_read_only_for_other_emp, name='get_attendance_read_only_for_other_emp'),

    path('set_attendance_in_details_mobile', attendanceCheckinViews.set_attendance_in_details_mobile, name='set_attendance_in_details'),
    path('get_attendance_in_out_details_mobile', attendanceCheckinViews.get_attendance_in_out_details_mobile, name='get_attendance_in_details'),
    path('set_attendance_out_details_mobile', attendanceCheckinViews.set_attendance_out_details_mobile, name='set_attendance_in_details '),
    # path('edit_attendance_in_out_details', attendanceCheckinViews.edit_attendance_in_out_details, name='edit_attendance_in_out_details'),
    path('get_attendance_read_only_details_mobile', attendanceCheckinViews.get_attendance_read_only_details_mobile, name='get_attendance_read_only_details'),
    path('get_attendance_read_only_for_other_emp_mobile', attendanceCheckinViews.get_attendance_read_only_for_other_emp_mobile, name='get_attendance_read_only_for_other_emp'),
    
    path('get_reminder_summary', eventsRemindersViews.get_reminder_summary_for_employee ),
    path('get_reminder_listing', eventsRemindersViews.get_reminder_listing_for_employee ),
    path('get_email_addresses', ERClaimViews.get_email_addresses, name='get_email_addresses'),
    path('set_email_address', ERClaimViews.set_email_address, name='set_email_address'),
    path('delete_email_address', ERClaimViews.delete_email_address, name='delete_email_address'),

    # URLs For People Analytics:
    path('get_emp_config_details', PeopleAnalyticsViews.get_emp_config_details, name="get_emp_additional_details"),
    path('get_fy_pick_list', PeopleAnalyticsViews.get_fy_pick_list, name="get_fy_pick_list"),
    path('get_month_pick_list', PeopleAnalyticsViews.get_month_pick_list, name="get_month_pick_list"),
    path('get_quarter_pick_list', PeopleAnalyticsViews.get_quarter_pick_list, name="get_quarter_pick_list"),
    path('get_function_dept_pick_list', PeopleAnalyticsViews.get_function_dept_pick_list, name="get_function_dept_pick_list"),
    path('get_sub_department_pick_list', PeopleAnalyticsViews.get_sub_department_pick_list, name="get_sub_department_pick_list"),
    path('get_managers_pick_list', PeopleAnalyticsViews.get_managers_pick_list, name="get_managers_pick_list"),
    path('get_drill_down_emp_details', PeopleAnalyticsViews.get_drill_down_emp_details, name="get_drill_down_emp_details"),

    path('get_hiring_ratio_summary', PeopleAnalyticsViews.get_hiring_ratio_summary, name="get_hiring_ratio_summary"),
    path('get_hiring_ratio_details', PeopleAnalyticsViews.get_hiring_ratio_details, name="get_hiring_ratio_details"),

    path('get_head_count_summary', PeopleAnalyticsViews.get_head_count_summary, name="get_head_count_summary"),
    path('get_head_count_details', PeopleAnalyticsViews.get_head_count_details, name="get_head_count_details"),

    path('get_performance_summary', PeopleAnalyticsViews.get_performance_summary, name="get_performance_summary"),
    path('get_performance_details', PeopleAnalyticsViews.get_performance_details, name="get_performance_details"),

    path('get_process_completion_summary', PeopleAnalyticsViews.get_process_completion_summary, name="get_process_completion_summary"),
    path('get_process_completion_details', PeopleAnalyticsViews.get_process_completion_details, name="get_process_completion_details"),

    path('get_thi_summary', PeopleAnalyticsViews.get_thi_summary, name="get_thi_summary"),
    path('get_thi_details', PeopleAnalyticsViews.get_thi_details, name="get_thi_details"),

    path('get_attrition_summary', PeopleAnalyticsViews.get_attrition_summary, name="get_attrition_summary"),
    path('get_attrition_details', PeopleAnalyticsViews.get_attrition_details, name="get_attrition_details"),

    path('get_idp_summary', PeopleAnalyticsViews.get_idp_summary, name="get_idp_summary"),
    path('get_idp_details', PeopleAnalyticsViews.get_idp_details, name="get_idp_details"),

    path('get_hierarchy_count', PeopleAnalyticsViews.get_hierarchy_count, name="get_hierarchy_count"),

    # URLs for PMS System (Emp Goal Submission):
    path('get_pms_half_year_pick_list', pmsviews.get_pms_half_year_pick_list, name="get_pms_half_year_pick_list"),
    path('get_direct_pick_list', pmsviews.get_direct_pick_list, name="get_direct_pick_list"),
    path('get_indirect_pick_list', pmsviews.get_indirect_pick_list, name="get_indirect_pick_list"),
    path('get_function_head_function_pick_list', pmsviews.get_function_head_function_pick_list, name="get_function_head_function_pick_list"),
    path('get_cascade_project_emp_pick_list', pmsviews.get_cascade_project_emp_pick_list, name="get_cascade_project_emp_pick_list"),
    path('get_pms_config_details', pmsviews.get_pms_config_details, name="get_pms_config_details"),
    path('get_pms_goal_listing', pmsviews.get_pms_goal_listing, name="get_pms_goal_listing"),
    path('get_pms_goal_details', pmsviews.get_pms_goal_details, name="get_pms_goal_details"),
    path('get_idp_tech_need_pick_list', pmsviews.get_idp_tech_need_pick_list, name="get_idp_tech_need_pick_list"),
    path('get_idp_behaviour_need_pick_list', pmsviews.get_idp_behaviour_need_pick_list, name="get_idp_behaviour_need_pick_list"),
    path('get_pms_idp_details', pmsviews.get_pms_idp_details, name="get_pms_idp_details"),
    path('set_pms_goals', pmsviews.set_pms_goals, name="set_pms_goals"),
    path('set_pms_auto_save_task_details', pmsviews.set_pms_auto_save_task_details, name="set_pms_auto_save_task_details"),
    path('set_pms_bulk_save_task_details', pmsviews.set_pms_bulk_save_task_details, name="set_pms_bulk_save_task_details"),
    path('set_pms_idp_details', pmsviews.set_pms_idp_details, name="set_pms_idp_details"),
    path('submit_pms_idp_question_from_rm', pmsviews.submit_pms_idp_question_from_rm, name="submit_pms_idp_question_from_rm"),
    path('submit_pms_goals_to_rm', pmsviews.submit_pms_goals_to_rm, name="submit_pms_goals_to_rm"),
    path('get_idp_prev_discussion_history', pmsviews.get_idp_prev_discussion_history, name="get_idp_prev_discussion_history"),
    path('get_pms_goal_summary', pmsviews.get_pms_goal_summary, name="get_pms_goal_summary"),
    path('set_pms_rollback_goals_pending_for_approval', pmsviews.set_pms_rollback_goals_pending_for_approval, name="set_pms_rollback_goals_pending_for_approval"),
    path('get_idp_competency_master_pick_list', pmsviews.get_idp_competency_master_pick_list, name="get_idp_competency_master_pick_list"),
    path('save_competency_hr',pmsviews.save_competency_hr, name="save_competency_hr"),
    path('get_pms_employee_goals_export',pmsviews.get_pms_employee_goals_export, name="get_pms_employee_goals_export"),
    path('get_pms_idp_competency_search_pick_list',pmsviews.get_pms_idp_competency_search_pick_list, name="get_pms_idp_competency_search_pick_list"),

    # URLs for PMS System (RM Goal Approval):
    path('get_emp_goal_status_summary', pmsviews.get_emp_goal_status_summary, name="get_emp_goal_status_summary"),
    path('get_emp_signed_image', pmsviews.get_emp_signed_image, name="get_emp_signed_image"),
    path('set_accept_reject_goals', pmsviews.set_accept_reject_goals, name="set_accept_reject_goals"),
    path('set_idp_discussion_from_rm', pmsviews.set_idp_discussion_from_rm, name="set_idp_discussion_from_rm"),

    # URLs for PMS Project Management
    path('set_pms_update_project', pmsviews.set_pms_update_project, name="set_pms_update_project"),
    path('get_pms_emp_pick_list', pmsviews.get_pms_emp_pick_list, name="get_pms_emp_pick_list"),
    path('get_pms_emp_except_managers_pick_list', pmsviews.get_pms_emp_except_managers_pick_list, name="get_pms_emp_except_managers_pick_list"),
    path('get_project_function_pick_list', pmsviews.get_project_function_pick_list, name="get_project_function_pick_list"),
    path('get_project_department_pick_list', pmsviews.get_project_department_pick_list, name="get_project_department_pick_list"),
    path('get_fh_pick_list', pmsviews.get_fh_pick_list, name="get_fh_pick_list"),
    path('get_pms_project_table_details', pmsviews.get_pms_project_table_details, name="get_project_table_details"),
    path('get_pms_project_details', pmsviews.get_pms_project_details, name="get_pms_project_details"),
    path('get_pms_project_op_details', pmsviews.get_pms_project_op_details, name="get_pms_project_op_details"),
    path('get_pms_goal_weightage_listing', pmsviews.get_pms_goal_weightage_listing, name="get_pms_goal_weightage_listing"),
    path('set_pms_goal_weightage', pmsviews.set_pms_goal_weightage, name="set_pms_goal_weightage"),

    # HR Operations:
    path('get_pms_hr_operations_emp_listing', pmsviews.get_pms_hr_operations_emp_listing, name="get_pms_hr_operations_emp_listing"),
    path('get_pms_function_picklist', pmsviews.get_pms_function_picklist, name="get_pms_function_picklist"),
    path('get_pms_department_picklist', pmsviews.get_pms_department_picklist, name="get_pms_department_picklist"),
    path('get_pms_function_goals_listing', pmsviews.get_pms_function_goals_listing, name="get_pms_function_goals_listing"),
    path('get_pms_hr_ops_goals_listing', pmsviews.get_pms_hr_ops_goals_listing, name="get_pms_hr_ops_goals_listing"),
    path('set_pms_hr_ops_goals_setting', pmsviews.set_pms_hr_ops_goals_setting, name="set_pms_hr_ops_goals_setting"),
    path('set_pms_hr_ops_change_rm', pmsviews.set_pms_hr_ops_change_rm, name="set_pms_hr_ops_change_rm"),
    path('set_pms_hr_ops_mark_not_applicable', pmsviews.set_pms_hr_ops_mark_not_applicable, name="set_pms_hr_ops_mark_not_applicable"),
    path('set_pms_hr_ops_review_mark_not_applicable', pmsviews.set_pms_hr_ops_review_mark_not_applicable, name="set_pms_hr_ops_qr_review_mark_not_applicable"),
    path('set_pms_extend_goal_setting_deadlines', pmsviews.set_pms_extend_goal_setting_deadlines, name="set_pms_extend_goal_setting_deadlines"),
    path('get_pms_goal_setting_deadlines', pmsviews.get_pms_goal_setting_deadlines, name="get_pms_goal_setting_deadlines"),
    path('set_pms_update_org_goal_file', pmsviews.set_pms_update_org_goal_file, name="set_pms_update_org_file"),
    path('get_pms_op_logs', pmsviews.get_pms_op_logs, name="get_pms_op_logs"),
    path('get_pms_employee_end_dates', pmsviews.get_pms_employee_end_dates, name="get_pms_employee_end_dates"),
    path('get_pms_idp_export', pmsviews.get_pms_idp_export, name="get_pms_idp_export"),
    path('get_pms_carry_function_goals_employee', pmsviews.get_pms_carry_function_goals_employee, name="get_pms_carry_function_goals_employee"),
    path('set_pms_carry_function_goals_employee', pmsviews.set_pms_carry_function_goals_employee, name="set_pms_carry_function_goals_employee"),
    path('set_pms_hr_ops_review_details_move_to_employee_draft', pmsviews.set_pms_hr_ops_review_details_move_to_employee_draft, name="set_pms_hr_ops_review_details_move_to_employee_draft"),
    path('set_pms_hr_ops_review_details_move_to_rm_draft', pmsviews.set_pms_hr_ops_review_details_move_to_rm_draft, name="set_pms_hr_ops_review_details_move_to_rm_draft"),
    path('set_pms_hr_ops_review_details_move_to_slm_draft', pmsviews.set_pms_hr_ops_review_details_move_to_slm_draft, name="set_pms_hr_ops_review_details_move_to_slm_draft"),
    path('set_pms_hr_ops_review_details_extend_deadline', pmsviews.set_pms_hr_ops_review_details_extend_deadline, name="set_pms_hr_ops_review_details_extend_deadline"),
    path('set_pms_hr_ops_review_details_complete', pmsviews.set_pms_hr_ops_review_details_complete, name="set_pms_hr_ops_review_details_complete"),
    path('set_pms_check_in_suggestions', pmsviews.set_pms_check_in_suggestions, name="set_pms_check_in_suggestions"),
    path('set_pms_hr_ops_move_from_slm_to_pm_draft', pmsviews.set_pms_hr_ops_move_from_slm_to_pm_draft, name="set_pms_hr_ops_move_from_slm_to_pm_draft"),

    # Goal Check-In
    path('get_pms_check_in_goal_wise_comment_listing', pmsviews.get_pms_check_in_goal_wise_comment_listing, name='get_pms_check_in_goal_wise_comment_listing'),
    path('get_pms_check_in_goal_picklist', pmsviews.get_pms_check_in_goal_picklist, name='get_pms_check_in_goal_picklist'),
    path('set_pms_goals_check_in', pmsviews.set_pms_goals_check_in, name="set_pms_check_in"),
    path('set_pms_idp_check_in', pmsviews.set_pms_idp_check_in, name="set_pms_idp_check_in"),
    path('get_pms_check_in_suggestions', pmsviews.get_pms_check_in_suggestions, name="get_pms_check_in_suggestions"),

    # Initiate New PMS Cycle:
    path('get_pms_next_two_period_cycle', pmsviews.get_pms_next_two_period_cycle, name="get_pms_next_two_period_cycle"),
    path('get_pms_functional_goal_period', pmsviews.get_pms_functional_goal_period, name="get_pms_functional_goal_period"),
    path('set_pms_initiate_new_goal_cycle', pmsviews.set_pms_initiate_new_goal_cycle, name="set_pms_initiate_new_goal_cycle"),
    path('set_pms_functional_goals', pmsviews.set_pms_functional_goals, name="set_pms_functional_goals"),
    path('get_pms_functional_goals', pmsviews.get_pms_functional_goals, name="get_pms_functional_goals"),
    path('get_pms_initiate_review_picklist', pmsviews.get_pms_initiate_review_picklist,name="get_pms_initiate_review_picklist"),
    path('set_pms_initiate_review', pmsviews.set_pms_initiate_review, name="set_pms_initiate_review"),
    path('set_pms_add_project_creator', pmsviews.set_pms_add_project_creator, name="set_pms_add_project_creator"),

    # Quarterly and performance review services
    path('get_pms_goal_review_rating_listing', pmsviews.get_pms_goal_review_rating_listing, name='get_pms_goal_review_rating_listing'),
    path('set_pms_goal_wise_quarter_hy_review_details', pmsviews.set_pms_goal_wise_quarter_hy_review_details, name="set_pms_goal_wise_quarter_hy_review_details"),
    path('set_pms_task_quarter_hy_review_details', pmsviews.set_pms_task_quarter_hy_review_details, name="set_pms_task_quarter_hy_review_details"),
    path('submit_pms_overall_quarter_hy_review_to_rm', pmsviews.submit_pms_overall_quarter_hy_review_to_rm, name="submit_pms_overall_quarter_hy_review"),
    path('submit_pms_project_review', pmsviews.submit_pms_project_review, name="submit_pms_project_review"),
    path('submit_pms_overall_review_from_rm_to_slm', pmsviews.submit_pms_overall_review_from_rm_to_slm, name="submit_pms_overall_quarter_hy_review_to_slm"),
    path('submit_pms_overall_review_from_slm', pmsviews.submit_pms_overall_review_from_slm, name="submit_pms_overall_review_from_slm"),
    path('set_pms_overall_quarter_hy_auto_save', pmsviews.set_pms_overall_quarter_hy_auto_save, name="set_pms_overall_quarter_hy_auto_save"),
    path('get_pms_overall_quarter_hy_review_details', pmsviews.get_pms_overall_quarter_hy_review_details, name="get_pms_overall_quarter_hy_review_details"),
    path('get_pms_rating_master_details', pmsviews.get_pms_rating_master_details, name='get_pms_rating_master_details'),
    path('get_pms_managers_input_questions', pmsviews.get_pms_managers_input_questions, name='get_pms_managers_input_questions'),
    path('set_pms_auto_save_managers_input', pmsviews.set_pms_auto_save_managers_input, name='set_pms_auto_save_managers_input'),
    path('get_pms_goal_status_pick_list', pmsviews.get_pms_goal_status_pick_list, name='get_pms_goal_status_pick_list'),
    path('set_pms_move_review_back_to_draft', pmsviews.set_pms_move_review_back_to_draft, name="set_pms_move_review_back_to_draft"),
    path('set_pms_move_review_back_to_draft_from_rm_slm', pmsviews.set_pms_move_review_back_to_draft_from_rm_slm, name="set_pms_move_review_back_to_draft_from_rm_slm"),
    path('get_pms_idp_review_details', pmsviews.get_pms_idp_review_details, name="get_pms_idp_review_details"),
    path('set_pms_idp_review', pmsviews.set_pms_idp_review, name="set_pms_idp_review"),
    path('submit_pms_project_review_from_emp', pmsviews.submit_pms_project_review_from_emp, name="submit_pms_project_review_from_emp"),
    path('set_pms_emp_comments_on_review', pmsviews.set_pms_emp_comments_on_review, name="set_pms_emp_comments_on_review"),
    path('set_pms_idp_progress_made', pmsviews.set_pms_idp_progress_made, name="set_pms_idp_progress_made"),
    path('set_pms_project_overall_rating', pmsviews.set_pms_project_overall_rating, name="set_pms_project_overall_rating"),

    # URLs for calibration screen:
    path('get_pms_calibration_config_details', pmsviews.get_pms_calibration_config_details, name='get_pms_calibration_config_details'),
    path('get_pms_calibration_details', pmsviews.get_pms_calibration_details, name='get_pms_calibration_details'),
    path('get_pms_career_level_picklist', pmsviews.get_pms_career_level_picklist, name='get_pms_career_level_picklist'),
    path('get_pms_rm_pick_list', pmsviews.get_pms_rm_pick_list, name='get_pms_rm_pick_list'),
    path('submit_pms_calibration_rating', pmsviews.submit_pms_calibration_rating, name='submit_pms_calibration_rating'),
    path('set_pms_calibration_fh_sign_off', pmsviews.set_pms_calibration_fh_sign_off, name='set_pms_calibration_fh_sign_off'),
    path('set_pms_calibration_rating', pmsviews.set_pms_calibration_rating, name='set_pms_calibration_rating'),
    path('get_pms_calibration_review_pending_details', pmsviews.get_pms_calibration_review_pending_details, name='set_pms_calibration_rating'),


    # URLs for PMS Goals Review and Rating Listings and all.
    path('get_pms_goal_review_rating_listing', pmsviews.get_pms_goal_review_rating_listing, name='get_pms_goal_review_rating_listing'),

    # URL for HR where they will get and insert Rating in TBL_HRMS_PMS_REVIEW_RATING_MASTER table for current Period.
    path('get_pms_hr_ops_rating_name_setting', pmsviews.get_pms_hr_ops_rating_name_setting, name="get_pms_hr_ops_rating_name_setting"),
    path('set_pms_hr_ops_rating_name_setting', pmsviews.set_pms_hr_ops_rating_name_setting, name="set_pms_hr_ops_rating_name_setting"),

    # shout out
    path('add_post', shoutoutViews.add_post, name='create a shout out'),
    path('shoutouts', shoutoutViews.get_so_types, name='get types of shout outs'),
    path('delete_post', shoutoutViews.delete_post, name='delete a shout out'),
    path('edit_post', shoutoutViews.edit_post, name='edit a shout out'),
    path('get_post', shoutoutViews.get_post, name='get a single detailed shout out'),
    path('get_all_posts', shoutoutViews.get_all_posts, name='get an array of shout outs based on filters'),
    path('get_img_url', shoutoutViews.get_image, name='get s3 url to display image'),

    # URL for HR competency edit
    path('get_competency_list', pmsviews.get_competency_list, name='GetCompetencyListHR'),

    # ESS (Intranet Revamp Phase 1)
    path('NewTallyWalaSummary', IntranetEssView.new_tally_wala_summary, name='NewTallyWalaSummary'),
    path('MyApplications', IntranetEssView.my_applications, name='MyApplications'),
    path('Utility', IntranetEssView.utility, name='Utility'),
    path('MyPMS', IntranetEssView.my_pms, name='MyPMS'),
    path('MyAttendance', IntranetEssView.my_attendance, name='MyAttendance'),
    path('FilterData', IntranetEssView.filter_data, name='FilterData'),
    path('NewTallyWalaDetails', IntranetEssView.new_tally_wala_details, name='NewTallyWalaDetails'),  # Drilldown
    path('NewJoineeInfo', IntranetEssView.new_joinee_info, name='NewJoineeInfo'),                     # HR interface
    path('AddNewJoineeInfo', IntranetEssView.add_new_joinee_info, name='AddNewJoineeInfo'),           # HR interface
    path('InductionCalendar', IntranetEssView.induction_calendar, name='InductionCalendar'),
    path('AddInductionPlan', IntranetEssView.add_induction_plan, name='AddInductionPlan'),            # HR interface
    path('EditInductionPlan', IntranetEssView.edit_induction_plan, name='EditInductionPlan'),         # HR interface
    path('DeleteInductionPlan', IntranetEssView.delete_induction_plan, name='DeleteInductionPlan'),   # HR interface

    path('Birthday', IntranetEssView.birthday, name='Birthday'),
    path('UpcomingBirthday', IntranetEssView.upcoming_birthday, name='UpcomingBirthday'),
    path('Experience', IntranetEssView.experience, name='Experience'),
    path('EmpSearchAutoComplete', IntranetEssView.emp_search_auto_complete, name='EmpSearchAutoComplete'),
    path('EmpSearch', IntranetEssView.emp_search, name='EmpSearch'),
    path('SendEmail', IntranetEssView.send_email, name='SendEmail'),
    path('OrganisationGoals', IntranetEssView.organisation_goals, name='OrganisationGoals'),

    path('Introduction', IntranetEssView.introduction, name='Introduction'),
    path('TallyNetIntroduction', IntranetEssView.tallynetintroduction, name='TallyNetIntroduction'),
    path('MyProfile', IntranetEssView.my_profile, name='MyProfile'),
    path('EditProfilePic', IntranetEssView.edit_profile_pic, name='EditProfilePic'),

    path('ListBasicDetails', IntranetEssView.list_basic_details, name='ListBasicDetails'),
    path('EditBasicDetails', IntranetEssView.edit_basic_details, name='EditBasicDetails'),

    path('ListPresentAddress', IntranetEssView.list_present_address, name='ListPresentAddress'),
    path('ListPermanentAddress', IntranetEssView.list_permanent_address, name='ListPermanentAddress'),
    path('EditPresentAddress', IntranetEssView.edit_present_address, name='EditPresentAddress'),
    path('EditPermanentAddress', IntranetEssView.edit_permanent_address, name='EditPermanentAddress'),

    path('ListEducationQualification', IntranetEssView.list_education_qualification, name='ListEducationQualification'),  # multiple records
    path('DelEducationQualification', IntranetEssView.del_education_qualification, name='DelEducationQualification'),
    path('EditEducationQualification', IntranetEssView.edit_education_qualification, name='EditEducationQualification'),

    path('ListExtraCurricular', IntranetEssView.list_extra_curricular, name='ListExtraCurricular'),  # multiple comma separated values
    path('EditExtraCurricular', IntranetEssView.edit_extra_curricular, name='EditExtraCurricular'),

    path('ListOfficialComm', IntranetEssView.list_official_comm, name='ListOfficialComm'),
    path('EditOfficialComm', IntranetEssView.edit_official_comm, name='EditOfficialComm'),

    path('ListSkill', IntranetEssView.list_skill, name='ListSkill'),  # multiple records
    path('ListTraining', IntranetEssView.list_training, name='ListTraining'),
    path('DelSkill', IntranetEssView.del_skill, name='DelSkill'),
    path('DelTraining', IntranetEssView.del_training, name='DelTraining'),
    path('EditSkill', IntranetEssView.edit_skill, name='EditSkill'),
    path('EditTraining', IntranetEssView.edit_training, name='EditTraining'),

    path('ListDependents', IntranetEssView.list_dependents, name='ListDependents'),
    path('ListMedicalCondition', IntranetEssView.list_medical_condition, name='ListMedicalCondition'),  # multiple records
    path('DelMedicalCondition', IntranetEssView.del_medical_condition, name='DelMedicalCondition'),  # when applicable == No
    path('EditMedicalCondition', IntranetEssView.edit_medical_condition, name='EditMedicalCondition'),  # when applicable == Yes

    path('ListRelationDetails', IntranetEssView.list_relation_details, name='ListRelationDetails'),  # multiple records
    path('DelRelationDetails', IntranetEssView.del_relation_details, name='DelRelationDetails'),
    path('EditRelationDetails', IntranetEssView.edit_relation_details, name='EditRelationDetails'),

    path('ListPassport', IntranetEssView.list_passport, name='ListPassport'),
    path('EditPassport', IntranetEssView.edit_passport, name='EditPassport'),
    path('ListVisa', IntranetEssView.list_visa, name='ListVisa'),  # multiple records
    path('DelVisa', IntranetEssView.del_visa, name='DelVisa'),
    path('EditVisa', IntranetEssView.edit_visa, name='EditVisa'),

    path('ListPriorExperience', IntranetEssView.list_prior_experience, name='ListPriorExperience'),  # multiple records
    path('DelPriorExperience', IntranetEssView.del_prior_experience, name='DelPriorExperience'),
    path('EditPriorExperience', IntranetEssView.edit_prior_experience, name='EditPriorExperience'),

    path('PrefillProfileDetails', IntranetEssView.prefill_profile_details, name='PrefillProfileDetails'),  # multiple records

    path('Mapper', IntranetEssView.mapper, name='Mapper'),

    path('AwardsFilter', IntranetEssView.awards_filter, name='AwardsFilter'),
    path('Awards', IntranetEssView.awards, name='Awards'),

    path('CustomerBase', IntranetEssView.customer_base, name='CustomerBase'),
    # path('FavouriteLink', IntranetEssView.favourite_link, name='FavouriteLink'),
    path('MyTasks', IntranetEssView.my_tasks, name='MyTasks'),
    path('AllFavouriteLinks', IntranetEssView.all_favourite_links, name='AllFavouriteLinks'),
    path('UpdateFavouriteLink', IntranetEssView.update_favourite_link, name='UpdateFavouriteLink'),

    path('TallyNetAccounts', IntranetEssView.tally_net_accounts, name='TallyNetAccounts'),
    path('ChangeAccountStatus', IntranetEssView.change_account_status, name='ChangeAccountStatus'),
    path('CheckIfSSO', IntranetEssView.check_if_sso, name='CheckIfSSO'),
    path('ValidateExistingPwd', IntranetEssView.validate_existing_pwd, name='ValidateExistingPwd'),
    path('ChangePassword', IntranetEssView.change_password, name='ChangePassword'),

    path('ListAllAwards', IntranetEssView.list_all_awards, name='ListAllAwards'),                        # HR interface
    path('AddNewAwardsPicklist', IntranetEssView.add_new_awards_picklist, name='AddNewAwardsPicklist'),  # HR interface
    path('DeptPicklist', IntranetEssView.dept_picklist, name='DeptPicklist'),                            # HR interface
    path('AddNewAwards', IntranetEssView.add_new_awards, name='AddNewAwards'),                           # HR interface

    path('AwardPeriodPicklist', IntranetEssView.award_period_picklist, name='AwardPeriodPicklist'),      # HR interface
    path('EmpIdImgAutoSearch', IntranetEssView.emp_id_img_auto_search, name='EmpIdImgAutoSearch'),       # HR interface
    path('PrefillAwardee', IntranetEssView.prefill_awardee, name='PrefillAwardee'),                      # HR interface
    path('EditAwardee', IntranetEssView.edit_awardee, name='EditAwardee'),                               # HR interface

    path('Leap', IntranetEssView.leap, name='Leap'),

    path('AccessToTallyhub', IntranetEssView.access_to_tallyhub, name='AccessToTallyhub'),
    path('GetByoIjpDetails', IntranetEssView.get_byo_ijp_openings_details, name='ByoIjp'),
    path('JobOpenings', IntranetEssView.job_openings, name='JobOpenings'),
    path('BYOAdminOperations', IntranetEssView.byoAdminOperations, name='BYOAdminOperations'),
    path('GetDynamicMessagingDetails', IntranetEssView.get_dynamic_messaging_details, name='GetDynamicMessagingDetails'),
    path('create_service_desk_referral_request', IntranetEssView.create_service_desk_referral_request, name='create_service_desk_referral_request'),

    # URLs for HR Related screen:
    path('get_hr_policies_details', HrRelatedViews.get_hr_policies_details, name='get_hr_policies_details'),
    path('get_hr_policies_list', HrRelatedViews.get_hr_policies_list, name='get_hr_policies_list'),
    path('hr_policy_operations', HrRelatedViews.hr_policy_operations, name='hr_policy_operations'),
    path('get_admin_details', HrRelatedViews.get_admin_details, name='get_admin_details'),
    path('get_hr_forms_details', HrRelatedViews.get_hr_forms_details, name='get_hr_forms_details'),
    path('get_group_medical_details', HrRelatedViews.get_group_medical_details, name='get_group_medical_details'),
    path('get_popover_data', HrRelatedViews.get_popover_data, name='get_popover_data'),
    path('get_city_picklist', HrRelatedViews.get_city_list, name='get_city_list'),
    path('set_popover_image_seen', HrRelatedViews.set_image_seen, name='set_image_seen'),
    path('get_career_level_picklist', HrRelatedViews.get_career_level, name='plotly_test'),
    path('get_function_picklist', HrRelatedViews.get_function, name='plotly_test'),
    path('get_office_picklist', HrRelatedViews.get_office, name='plotly_test'),
    path('get_employee_type_picklist', HrRelatedViews.get_employee_type, name='plotly_test'),
    path('get_vaccination_drive_table', HrRelatedViews.get_vaccination_drive_table, name='plotly_test'),
    path('get_vaccine_list', HrRelatedViews.get_vaccine_list, name='plotly_test'),
    path('get_vaccine_status_list', HrRelatedViews.get_vaccine_status_list, name='plotly_test'),
    path('save_vaccine_details', HrRelatedViews.save_vaccine_details, name='plotly_test'),
    path('get_emp_pick_list', HrRelatedViews.get_emp_pick_list, name='plotly_test'),
    path('get_vaccination_details_by_id', HrRelatedViews.get_vaccination_details_by_id, name='plotly_test'),
    path('check_HR_Rights', HrRelatedViews.check_HR_Rights, name='plotly_test'),
    path('check_Rights', HrRelatedViews.check_Rights, name='check_Rights'),

    # Holiday Config screen -- Attendace Global System
    path('get_financial_years_for_holiday_config', HrRelatedViews.get_financial_years_for_holiday_config, name='get_financial_years_for_holiday_config'),
    path('get_all_company_branches', HrRelatedViews.get_all_company_branches, name='get_all_company_branches'),
    path('get_available_branches_to_mark_mandatory', HrRelatedViews.get_available_branches_to_mark_mandatory, name='get_available_branches_to_mark_mandatory'),
    path('get_holidays_for_hr_config_screen', HrRelatedViews.get_holidays_for_hr_config_screen, name='get_holidays_for_hr_config_screen'),
    path('holiday_config_operations', HrRelatedViews.holiday_config_operations, name='holiday_config_operations'),
    path('delete_holiday_from_hr_config', HrRelatedViews.delete_holiday_from_hr_config, name='delete_holiday_from_hr_config'),
    path('import_holidays_from_excel', HrRelatedViews.import_holidays_from_excel, name='import_holidays_from_excel'),
    # Leave Config screen -- Attendace Global System
    path('get_all_leaves_for_leave_config_screen', HrRelatedViews.get_all_leaves_for_leave_config_screen, name='get_all_leaves_for_leave_config_screen'),
    path('leave_config_operations', HrRelatedViews.leave_config_operations, name='leave_config_operations'),
    path('get_prefixed_picklists_for_add_edit_leaves_config', HrRelatedViews.get_prefixed_picklists_for_add_edit_leaves_config, name='get_prefixed_picklists_for_add_edit_leaves_config'),
    path('update_leave_emp_summary', HrRelatedViews.update_leave_emp_summary, name='update_leave_emp_summary'),


    #Organisational Chart URLS
    path('organisation_chart', organisationChartViews.get_all_employees),
    path('get_employee', organisationChartViews.get_employee_by_career_level_id),
    path('get_sub_employee', organisationChartViews.get_sub_employee_by_appraiser_id)

]
