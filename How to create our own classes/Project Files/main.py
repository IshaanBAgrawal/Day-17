class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Ishaan")
user_2 = User('002', 'Ruby')

user_1.follow(user_2)

print(user_1.id)
print(user_1.username)
print(f"Followers : {user_1.followers}")
print(f"Following : {user_1.following}")

print()

print(user_2.id)
print(user_2.username)
print(f"Followers : {user_2.followers}")
print(f"Following : {user_2.following}")
