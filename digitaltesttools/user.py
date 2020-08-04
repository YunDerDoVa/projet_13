from door.models import User

def create_test_users(number_of_users):

    users = []

    for i in range(number_of_users):
        data = {'username': 'User'+str(i), 'email': 'exemple'+str(i)+'@email.com', 'password': 'password'}
        user = User.objects.create(username=data['username'], password=data['password'], email=data['email'])
        users.append(user)

    return users