from requests import get, post

print(post('http://localhost:5000/api/news').json())

print(post('http://localhost:5000/api/news',
           json={'team_leader': 'Заголовок'}).json())

print(post('http://localhost:5000/api/news',
           json={'team_leader': 2,
                 'job': 'Текст новости',
                 'work_size': 4,
                 'collaborators': '2, 6',
                 'start_date': 44,
                 'end_date': 45}).json())