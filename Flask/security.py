from user import User
# users=[
# {
#     'id':1,
#     'username':'bob',
#     'password':'bob123'
# }
# ]
#
# username_mapping={'bob':{
# 'id':1,
# 'username':'bob',
# 'password':'bob123'
# }}
#
#
# userid_mapping={1:{
# 'id':1,
# 'username':'bob',
# 'password':'bob123'
# }}

# users=[
# User(1,'bob','bob123')
# ]

# username_mapping={u.username:u for u in users}
# userid_mapping={u.id:u for u in users}

def authenticate(username,password):
    # user=username_mapping.get(username,None)
    user=User.find_by_username(username)
    if user and user.password==password:
        return user

def identity(payload):
    user_id=payload['identity']
    # return userid_mapping.get(user_id,None)
    return User.find_by_id(user_id)
