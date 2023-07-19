import requests
import json

class GitHub:
    def __init__(self) :
       self.api_url = "https://api.github.com"
    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()
    def getRepos(self, username):
        repo = requests.get(self.api_url+'/users/'+username+'/repos')
        return repo.json()
    def creatRepos(self, name , token, sec):
        headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
        }
        data = {
        "name": name,
        "private": sec
        }
        response = requests.post(self.api_url+'/user/repos',headers= headers , json=data)
        if response.status_code == 201:
            print(f"Repository created: {name}")
        else:
            print(f"Error code: {response.status_code}, Error message: {response.json()['message']}")
    

github = GitHub()
while True:
    secim = input('1-Find User\n2-Get Public Repositories\n3-Create Repositories\n4-Exit\n')
    if secim=='4':
        break
    elif secim=='1':
        user = input("username: ")
        result = github.getUser(user)
        print(f"name: {result['name']}\nid: {result['id']}\nbio: {result['bio']}\nfollowers: {result['followers']}\tfollowing: {result['following']}")
    elif secim=='2':
        user = input('username: ')
        repo = github.getRepos(user)
        for r in repo:
            print(r['name'])
    elif secim=='3':
        name = input('your repository name:')
        token = input('your personal access token: ')
        sec= input('private or public: ')
        if(sec=='private'):
            sec=True
        else:
            sec=False
        github.creatRepos(name, token , sec)
    else:
        print('wrong choice')