# Creating Classes
class User:

    def __init__(self, user_id, username, followers=0, following=0):
        self.user_id = user_id
        self.username = username
        self.followers = followers
        self.following = following

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'rick')
user_2 = User('002', 'roland')

user_1.follow(user_2)
print(f'User 1 is following {user_1.following} person.')
print(f'User 2 has {user_2.followers} follower.')
