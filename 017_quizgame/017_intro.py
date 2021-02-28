class User:
    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # default value
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1

# user_1 = User()
# user_1.id = '001'
# user_1.username = 'Blub'

user_1 = User('001','Joe')
user_2 = User('002','Bob')

user_1.follow(user_2)


print("u1 follower count:",user_1.followers)
print("u1 following:",user_1.following,"users")
print("u2 follower count:",user_2.followers)
print("u2 following:",user_2.following,"users")

