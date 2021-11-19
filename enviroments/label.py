import enviroments.constant as constant

GRID_GRAPH = {
    '0': [0, 0],
    '1': [0, 1],
    '2': [1, 0],
    '3': [1, 1],
    '4': [2, 0],
    '5': [2, 1],
}

EMPLOYEE = {
    'employee-skill':
        {'xlabel': 'No. Skills', 'ylabel': 'Employees',
         'title': 'Employee Skill', 'column': 'sum_of_skill', 'file': 'employee-skills.csv',
         'header': constant.COL_EMPLOYEE_SKILL, 'location': GRID_GRAPH['0']},
    'employee-hobby':
        {'xlabel': 'No. Hobbies', 'ylabel': 'Employees',
         'title': 'Employee Hobby', 'column': 'sum_of_hobby', 'file': 'employee-hobby.csv',
         'header': constant.COL_EMPLOYEE_HOBBY, 'location': GRID_GRAPH['1']},
    'employee-expecetedskill':
        {'xlabel': 'No. Skills', 'ylabel': 'Employees',
         'title': 'Employee ExpectedSkill', 'column': 'sum_of_expectedskill', 'file': 'employee-expectedskill.csv',
         'header': constant.COL_EMPLOYEE_EXPECTED_SKILL, 'location': GRID_GRAPH['2']},
    'employee-language':
        {'xlabel': 'No. Languages', 'ylabel': 'Employees',
         'title': 'Employee Language', 'column': 'sum_of_language', 'file': 'employee-language.csv',
         'header': constant.COL_EMPLOYEE_LANGUAGE, 'location': GRID_GRAPH['3']},
    # 'employee-role':
    #     {'xlabel': 'No. Role', 'ylabel': 'Employees',
    #      'title': 'Employee Role', 'column': 'sum_of_role', 'file': 'employee-role.csv',
    #      'header': constant.COL_EMPLOYEE_ROLE, 'location': GRID_GRAPH['4']},
    # 'employee-soft_skill':
    #     {'xlabel': 'No. SoftSkill', 'ylabel': 'Employees',
    #      'title': 'Employee SoftSkill', 'column': 'sum_of_softskill', 'file': 'employee-softskill.csv',
    #      'header': constant.COL_EMPLOYEE_SOFT_SKILL, 'location': GRID_GRAPH['5']},
}


OTHERS_ENTITIES = {
    'skill':
        {'xlabel': 'Skill', 'ylabel': 'Number of Employees',
         'title': 'Skill Statistic', 'column': 'sum_employees', 'column2': 'skill_id', 'file': 'skill.csv',
         'header': constant.COL_SKILL},
    'hobby':
        {'xlabel': 'Hobby', 'ylabel': 'Number of Employees',
         'title': 'Hobby Statistic', 'column': 'sum_employees', 'column2': 'hobby_id', 'file': 'hobbies.csv',
         'header': constant.COL_HOBBY},
    'skill-exptedskill':
        {'xlabel': 'Expected Skill', 'ylabel': 'Number of Employees',
         'title': 'Expected Skill Statistic', 'column': 'sum_employees', 'column2': 'skill_id_expected',
         'file': 'skill.csv',
         'header': constant.COL_SKILL},
    'language':
        {'xlabel': 'Language', 'ylabel': 'Number of Employees',
         'title': 'Language Statistic', 'column': 'sum_employees', 'column2': 'language_name_id',
         'file': 'languages.csv',
         'header': constant.COL_LANGUAGE},
    # 'role':
    #     {'xlabel': 'Role', 'ylabel': 'Number of Employees',
    #      'title': 'Role Statistic', 'column': 'sum_employees', 'column2': 'role_id', 'file': 'role.csv',
    #      'header': constant.COL_ROLE},
    # 'softskill':
    #     {'xlabel': 'SoftSkill', 'ylabel': 'Number of Employees',
    #      'title': 'Softskill Statistic', 'column': 'sum_employees', 'column2': 'softskill_id', 'file': 'softskill.csv',
    #      'header': constant.COL_SOFT_SKILL},
}

if __name__ == '__main__':
    print(EMPLOYEE)