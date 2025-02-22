import uuid


class User:
    def __init__(self, name, user_password, user_mail):
        self.user_name = name
        self.password = user_password
        self.mail = user_mail

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

user_1 = User("Вася Пупкин", "123", "vasia@mail.ru")
user_1.print_info()

