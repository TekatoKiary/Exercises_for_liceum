from requests import post, delete, get

# Делается в пустом sql файле
print(post('http://localhost:8080/api/v2/job',
           json={'team_leader': 1,
                 'job': 'deployment of residential modules 1 and 2',
                 'work_size': 50,
                 'collaborators': '2, 3',
                 'is_finished': True}).json())

print(post('http://localhost:8080/api/v2/job',
           json={'team_leader': 2,
                 'job': 'deployment of residential modules 2 and 3',
                 'work_size': 10,
                 'collaborators': '4, 3',
                 'is_finished': False}).json())

print(post('http://localhost:8080/api/v2/job',
           json={'team_leader': 1,
                 'work_size': 50,
                 'collaborators': '2, 3',
                 'is_finished': True}).json()) # Некорректный запрос: отсутствует параметр job.

print(get(f'http://localhost:8080/api/v2/job').json())

print(get(f'http://localhost:8080/api/v2/job/1').json())

print(get(f'http://localhost:8080/api/v2/job/3').json())  # Некорректный запрос.

print(delete('http://localhost:8080/api/v2/job/2').json())
