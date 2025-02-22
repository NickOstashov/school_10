import uuid


class User:
    def __init__(self, name, user_password, user_mail):
        # свойства из параметров
        self.user_name = name
        self.password = user_password
        self.mail = user_mail

        # свойства задаваемые автоматически при создании экземляра
        self.friend_list = list()
        self.messages = list()
        self.uuid = str(uuid.uuid4())

    def print_info(self):
        print("user_name: ", self.user_name)
        print("password: ", self.password)
        print("mail: ", self.mail)
        print("friend_list: ", self.friend_list)
        print("messages: ", self.messages)
        print("uuid: ", self.uuid)

    def add_friend(self, other_user : "User"):
        self.friend_list.append(other_user)
        other_user.friend_list.append(self)

user_1 = User("Вася Пупкин", "123", "vasia@mail.ru")

user_2 = User("Федя", "321", "fedua@mail.ru")

user_1.add_friend(user_2)

print("USER_1 INFO")
user_1.print_info()
print()
print("USER_2 INFO")
user_2.print_info()
