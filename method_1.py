
print('Welcome to Home Serice Application')


class users():
    users_list = [
        {'name': 'Sanjay', 'email': 'sanjay@gmail.com', 'password': 'sanjay'}]

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def sign_up(self):
        single_user = {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
        for i in range(len(users.users_list)):
            if users.users_list[i]['email'] == single_user['email']:
                return "User already exist"
        else:
            users.users_list.append(single_user)
            return "You added as a new user"


def main():
    name = input("Enter your name:")
    email = input("Enter your email ID:")
    password = input("Enter your password:")

    user = users(name, email, password)
    print(user.sign_up())


if __name__ == "__main__":
    main()
