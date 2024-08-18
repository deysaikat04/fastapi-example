import json

def read_user():
    with open('data/users.json') as f:
        users = json.load(f)
    return users

def read_user_by_id(id):
    users = read_user()
    for user in users:
        if user['id'] == id:
            return user
    return None
