import requests

uname = 'shanksauce315'
pword = 'test12345'
response = requests.post('http://127.0.0.1:8080/loginForm',
                         json={'username': uname, 'password': pword})
# print(response.json())
access_token = response.json()['access_token']
# headers = {'Authorization': f'Bearer {access_token}'}
# response = requests.get('http://127.0.0.1:8080/protected', headers=headers)
# print(response.json())  # {'message': 'Hello, example@example.com!'}
