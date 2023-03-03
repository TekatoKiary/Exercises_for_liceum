from requests import post, delete, get

# Делается в пустом sql файле
print(post('http://localhost:8080/api/v2/user',
           json={'surname': 'Ridley',
                 'name': 'Scott',
                 'age': 18,
                 'position': 'captain',
                 'speciality': 'research engineer',
                 'address': 'modul_4',
                 'email': 'scott_chief@mars.org',
                 'hashed_password': '153'}).json())

print(post('http://localhost:8080/api/v2/user',
           json={'surname': 'Rick',
                 'name': 'Cooper',
                 'age': 16,
                 'position': 'assistanc',
                 'speciality': 'middle engineer',
                 'address': 'modul_4',
                 'email': 'Mister_Cooper@mars.org',
                 'hashed_password': '498'}).json())

print(post('http://localhost:8080/api/v2/user',
           json={'surname': 'Rick',
                 'name': 'Cooper',
                 'age': 16,
                 'position': 'assistanc',
                 'speciality': 'middle engineer',
                 'address': 'modul_4',
                 'hashed_password': '498'}).json())  # Некорректный запрос: отсутствует параметр email.

print(get(f'http://localhost:8080/api/v2/user').json())

print(get(f'http://localhost:8080/api/v2/user/1').json())

print(get(f'http://localhost:8080/api/v2/user/3').json())  # Некорректный запрос.

print(delete('http://localhost:8080/api/v2/user/2').json())
