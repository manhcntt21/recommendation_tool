import pandas as pd

# col of people
p_col = ['id', 'birthdate', 'location', 'updated_by', 'name', 'title', 'created_at', 'updated_at', 'picture', 'competence_notes', 'company_id',
         'associations_updatet_at', 'nationality', 'nationality2', 'marital_status', 'email', 'department_id', 'user_code']
people = pd.read_csv('../data/recommendation_systems/skills/people.csv', header=0, sep=',', names=p_col, encoding='latin-1')

# col of people skills
ps_col = ['id', 'person_id', 'skill_id', 'level', 'interest', 'certificate', 'core_competence']
people_skills = pd.read_csv('../data/recommendation_systems/skills/people_skills.csv', header=0, sep=',', names=ps_col, encoding='latin-1')

# col of skills
s_col = ['id', 'title', 'radar', 'portfolio', 'default_set', 'created_at', 'updated_at', 'category_id']
skills = pd.read_csv('../data/recommendation_systems/skills/skills.csv', header=0, sep=',', encoding='latin-1')


# col of enjoyed project
pc_col = ['id', 'person_id', 'project_id', 'completion_time', 'success_rate']
project = pd.read_csv('../data/recommendation_systems/skills/projects_custom.csv', sep=',', names=pc_col, encoding='latin-1')

print(project[['id', 'person_id']].loc[2])

# a = [3, 5, 7, 9, 10, 12, 14 ,15 ,16 ,18, 20, 22, 24, 26, 29, 30, 33, 35]
# b = [3, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 29, 30]
# c = [1, 2, 3, 5, 9, 13, 18, 19, 22, 25, 30]
# d = [1, 2, 5, 6, 7, 9, 12, 13, 14, 16, 17, 18, 22, 24, 25, 26, 29, 30]
#
# import random
#
# random.seed(0)
# count = 0
# for i in range(200):
#     result = []
#     a1 = random.sample(a, 2)
#     b1 = random.sample(b, 2)
#     c1 = random.sample(c, 1)
#     d1 = random.sample(d, 1)
#     result.append(a1[0])
#     result.append(a1[1])
#     result.append(b1[0])
#     result.append(b1[1])
#     result.append(c1[0])
#     result.append(d1[0])
#     # convert to set
#     result_set = set(result)
#     if len(result_set) == len(result):
#         count = count + 1
#         print(tuple(result))
#
# print(count)

