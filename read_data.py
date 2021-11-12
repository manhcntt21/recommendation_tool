import pandas as pd
import matplotlib.pyplot as plt

# col of people
e_col = ['id', 'birthdate', 'location', 'updated_by', 'name', 'created_at', 'updated_at', 'marital_status', 'email',
         'department_id',
         'user_code', 'active', 'email_company', 'phone_number']

# col of allocation
a_col = ['id', 'employee_id', 'joining_date', 'work_load', 'status', 'updated_at', 'updated_by', 'sent_to',
         'created_at', 'is_delete', 'requirement_project_skill_id']

# col of employee certificate
ec_col = ['id', 'employee_id', 'cert_type', 'status', 'updated_at', 'updated_by', 'created_at', 'is_delete',
          'cert_value']

# col of employee expected skill
ees = ['id', 'employee_id', 'skill_id_expected', 'level_id_expected', 'created_at', 'updated_at', 'is_delete']

# col of employee hobby
eh = ['id', 'employee_id', 'hobby_id', 'status', 'created_at', 'updated_at', 'updated_by', 'sent_to', 'is_delete']

# col of employee role
er = ['id', 'role_id', 'employee_id', 'level_id', 'status', 'updated_at', 'updated_by', 'sent_to',
      'created_at', 'is_delete']

# col of employee skill
es = ['id', 'employee', 'skill_id', 'interest', 'certificate', 'core_competence', 'level_id', 'status', 'updated_at',
      'updated_by', 'sent_to', 'created_at', 'is_delete']
# col of employee soft skill
ess = ['id', 'employee_id', 'softskill_id', 'score', 'is_delete', 'created_at', 'updated_at']

# col of project
p = ['id', 'name', 'customer_id', 'started_at', 'ended_at', 'effort', 'status', 'created_at', 'updated_at', 'is_delete']

# col of requirement project
rp = ['id', 'project_id', 'role_id', 'level_id', 'status', 'updated_at', 'updated_by', 'created_at', 'sent_to',
      'is_delete']

# col of requirement project skill
rps = ['requirement_project_id', 'skill_id', 'level_id', 'status', 'updated_at', 'updated_by', 'created_at', 'sent_to',
       'is_delete']

# col of skill
s = ['id', 'name', 'is_']
def read_data(col, path):
    data = pd.read_csv(path, header=0, sep=',', names=col, encoding='utf-8')
    print(data.head())
    return data


if __name__ == '__main__':
    base = './data/vss_exm/'
    # employee = read_data(e_col, base + 'employee.csv')
    # allocation = read_data(a_col, base + 'allocation.csv')
    # employee_certificate = read_data(ec_col, base + 'employee-certificate.csv')
    # employee_expected_skill = read_data(ees, base + 'employee-expectedskill.csv')
    # employee_hobby = read_data(eh, base + 'employee-hobby.csv')
    # employee_role = read_data(er, base + 'employee-role.csv')
    employee_skill = read_data(es, base + 'employee-skills.csv')
    # employee_soft_skill = read_data(ess, base + 'employee-softskill.csv')
    # project = read_data(p, base + 'project.csv')
    # requirement_project = read_data(rp, base + 'requirement-project.csv')
    # requirement_project_skill = read_data(rps, base + 'requirement-project-skill.csv')


