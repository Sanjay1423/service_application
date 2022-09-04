
class users:
    users_list = [
        {'name': 'Sanjay', 'email': 'sanjay@gmail.com', 'password': 'sanjay'},
        {'name': 'raj', 'email': 'raj@gmail.com', 'password': 'raj'}
    ]

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class check_login(users):
    def sign_up(self):
        single_user = {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

        check_list = list(
            filter(lambda x: x['email'] == self.email and x['password'] == self.password, check_login.users_list))

        if check_list == []:
            check_login.users_list.append(single_user)
            return "You added as a user"

        elif check_list[0]['email'] == self.email:
            return "User already exist"


class Service:

    no_of_services = ['Plumbing', 'Painting', 'Capentering', 'Servicing']
    cities = ['Chennai', 'Coimbatore', 'Ooty', 'Trichy']
    available_servies = {cities[0]: [0, 1, 2, 3], cities[1]: [0, 2, 3], cities[2]: [2, 0], cities[3]: [1, 2]}

    def service_function(self):

        print('Select your City location')
        print('Chennai,Ooty,Coimbatore,Trichy')
        city_name = input().capitalize()

        if city_name in Service.cities:
            print('Available Services\n')
            for i in Service.available_servies[city_name]:
                print(Service.no_of_services[i])
        else:
            print(
                f'Services is not availble for {city_name}. Services available only for ')
            for i in Service.cities:
                print(i)


def main():
    print('Welcome to home service application')
    name = input("Enter your name:")
    email = input("Enter your email ID:")
    password = input("Enter your password:")
    user1 = check_login(name, email, password)
    service = Service()
    print(user1.sign_up())
    service.service_function()


if __name__ == '__main__':
    main()
