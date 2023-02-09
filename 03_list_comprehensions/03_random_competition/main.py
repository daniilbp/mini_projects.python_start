import random

team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]

winners = [team_1[skill] if team_1[skill] >= team_2[skill] else team_2[skill] for skill in range(20)]

print('Первая команда:', team_1)
print('Вторая команда:', team_2)
print('Победители тура:', winners)
