from door.models import User


TEST_PASSWORD = 'password'

def get_user_dict(num):
    return {'username': 'User' + str(num), 'email': 'example' + str(num) + '@email.com', 'password': TEST_PASSWORD}


def create_test_users(number_of_users):
    users = []

    for i in range(number_of_users):
        data = get_user_dict(i)
        user = User.objects.create(username=data['username'], email=data['email'])
        user.set_password(data['password'])
        user.save()
        users.append(user)

    return users


def get_or_create_test_users(number_of_users):
    existing_users = User.objects.all()

    diff = number_of_users - existing_users.count()

    users = []

    for user in existing_users:
        users.append(user)

    if diff > 0:
        for i in range(existing_users.count(), number_of_users):
            data = get_user_dict(i)
            user = User.objects.create(username=data['username'], email=data['email'])
            user.set_password(data['password'])
            user.save()
            users.append(user)

    return users
