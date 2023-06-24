import json
import redis
from flask import Flask, request

app = Flask(__name__)
redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)

class e:
    pass

def add_user(user_id, user_data):
    user_key = f"user:{user_id}"
    redis_db.hmset(user_key, user_data)


def delete_user(user_id):
    user_key = f"user:{user_id}"
    redis_db.delete(user_key)


def get_user(user_id=None):
    if user_id:
        regex = 'user:'+user_id
    else:
        regex = 'user:*'
    user_keys = redis_db.scan_iter(match=regex)
    user_data = []
    for key in user_keys:
        user_data.append(redis_db.hgetall(key))

    return user_data


def vote_for_user(user_id):
    user_key = f"user:{user_id}:votes"
    redis_db.incr(user_key)


@app.route('/user/<user_id>', methods=['POST'])
def add_or_update_user(user_id):
    user_data = json.loads(request.data)
    add_user(user_id, user_data)
    return "Dodano lub zaktualizowano uzytkownika"


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user_handler(user_id):
    delete_user(user_id)
    return "Usunieto uzytkownika"


@app.route('/user/<user_id>', methods=['GET'])
def get_user_handler(user_id):
    users = get_user(user_id)
    new_users = []
    for user in users:
        u = {}
        for key in user:
            u[key.decode()] = user[key].decode()
        new_users.append(u)

    return json.dumps(new_users[0])


# ?
@app.route('/users', methods=['GET'])
def get_all_users_handler():
    users = get_user()
    new_users = []
    for user in users:
        u = {}
        for key in user:
            u[key.decode()] = user[key].decode()
        new_users.append(u)

    return json.dumps(new_users)


@app.route('/user/<user_id>/vote', methods=['POST'])
def vote_for_user_handler(user_id):
    vote_for_user(user_id)
    return "Zaglosowano!"


if __name__ == '__main__':
    app.run()