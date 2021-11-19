# col of employee
COL_EMPLOYEE = ['id', 'birthdate', 'location', 'updated_by', 'name', 'created_at', 'updated_at', 'marital_status',
                'email',
                'department_id',
                'user_code', 'active', 'email_company', 'phone_number']

# col of allocation
COL_ALLOCATION = ['id', 'employee_id', 'joining_date', 'work_load', 'status', 'updated_at', 'updated_by', 'sent_to',
                  'created_at', 'is_delete', 'requirement_project_skill_id']

# col of employee certificate
COL_EMPLOYEE_CERTIFICATE = ['id', 'employee_id', 'cert_type', 'status', 'updated_at', 'updated_by', 'created_at',
                            'is_delete',
                            'cert_value']

# col of employee expected skill
COL_EMPLOYEE_EXPECTED_SKILL = ['id', 'employee_id', 'skill_id_expected', 'level_id_expected', 'created_at',
                               'updated_at', 'is_delete']

# col of employee hobby
COL_EMPLOYEE_HOBBY = ['id', 'employee_id', 'hobby_id', 'status', 'created_at', 'updated_at', 'updated_by', 'sent_to',
                      'is_delete']

# col of employee language
COL_EMPLOYEE_LANGUAGE = ['id', 'employee_id', 'language_name_id', 'language_level_id', 'status', 'send_to',
                         'updated_at', 'updated_by',
                         'created_at', 'created_by', 'is_delete']

# col of employee role
COL_EMPLOYEE_ROLE = ['id', 'role_id', 'employee_id', 'level_id', 'status', 'updated_at', 'updated_by', 'sent_to',
                     'created_at', 'is_delete']

# col of employee skill
COL_EMPLOYEE_SKILL = ['id', 'employee_id', 'skill_id', 'interest', 'certificate', 'core_competence', 'level_id',
                      'status', 'updated_at',
                      'updated_by', 'sent_to', 'created_at', 'is_delete']
# col of employee soft skill
COL_EMPLOYEE_SOFT_SKILL = ['id', 'employee_id', 'softskill_id', 'score', 'is_delete', 'created_at', 'updated_at']

# col of project
COL_PROJECT = ['id', 'name', 'customer_id', 'started_at', 'ended_at', 'effort', 'status', 'created_at', 'updated_at',
               'is_delete']

# col of requirement project
COL_REQUIREMENT_PROJECT = ['id', 'project_id', 'role_id', 'level_id', 'status', 'updated_at', 'updated_by',
                           'created_at', 'sent_to',
                           'is_delete']

# col of requirement project skill
COL_REQUIREMENT_PROJECT_SKILL = ['requirement_project_id', 'skill_id', 'level_id', 'status', 'updated_at', 'updated_by',
                                 'created_at', 'sent_to',
                                 'is_delete']

# col of skill
COL_SKILL = ['id', 'name', 'is_delete']

# col of hobby
COL_HOBBY = ['id', 'name', 'is_delete', 'image']

# col of language
COL_LANGUAGE = ['id', 'name', 'is_delete']

# col of role
COL_ROLE = ['id', 'name', 'is_delete']

# col of soft skill
COL_SOFT_SKILL = ['id', 'name', 'is_delete']

