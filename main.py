class User:
    pass # should be added for an empty class/function

# PacalCase (for class) vs camelCase (not used in Python much) vs snake_case (for pretty much everything)

# attributes of an objects can be entered one by one, this method is error prone
user_1 = User()
user_1.id = "001"
user_1.username = "eugene"

user_2 = User()
user_2.id = "002"
user_2.username = "alina"

print(user_1.id, user_1.username)
print(user_2.id, user_2.username)
print("\n")

# Constructor or initializing an object - uses init function

class UserAdvanced:

    def __init__(self, user_id, username): # attributes
        print("new user being created...") # this line will be executed every time new object from this class is created
        self.id = user_id
        self.username = username # name of the parameter is typically same as name of the attribute, like this line, not the case in the previous line
        self.followers = 0 # default value, not required during initializations
        self.following = 0

    def follow(self, user): # method
        user.followers += 1
        self.following += 1

user_advanced_1 = UserAdvanced("001", "angela")
user_advanced_2 = UserAdvanced("002", "sam")

user_advanced_1.follow(user_advanced_2) # method for user_advanced_1 following user_advanced_2

print(f"user ID = {user_advanced_1.id}, username = {user_advanced_1.username}, followers = {user_advanced_1.followers}, following = {user_advanced_1.following}")
print(f"user ID = {user_advanced_2.id}, username = {user_advanced_2.username}, followers = {user_advanced_2.followers}, following = {user_advanced_2.following}")
