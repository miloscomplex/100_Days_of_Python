class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0

    # its required to have self for the first parameter
    def follow(self, user):
        user.followers += 1
        self.folowing += 1

user_1 = User("001", "Jack")
user_2 = User("002", "Jill")

user_1.follow(user_2);
