class User:

    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1



user1 = User("saha", 100)
user2 = User("sara", 200)

print(user1.user_name, user2.user_id)
print(user2.user_name, user1.user_id)
print(user1.follower)