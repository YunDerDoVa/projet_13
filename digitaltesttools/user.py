from door.models import User


def get_user_dict(num):
    return {'username': 'User' + str(num), 'email': 'example' + str(num) + '@email.com', 'password': 'password'}


def create_test_users(number_of_users):
    users = []

    for i in range(number_of_users):
        data = get_user_dict(i)
        user = User.objects.create(username=data['username'], password=data['password'], email=data['email'])
        users.append(user)

    return users
