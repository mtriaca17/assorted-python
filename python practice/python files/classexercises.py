# class User():
#     """for info about user"""
#     def __init__(self, first, last, fave_color):
#         self.first = first
#         self.last = last
#         self.fave_color = fave_color
#         self.full_name = first + " " + last
#         self.login_attempts = 0

#     def describe_user(self):
#         print(f'Name: {self.full_name.title()}\nFavorite Color: {self.fave_color.title()}')
    
#     def greet_user(self):
#         """greeting for user"""
#         print(f'\nHello {self.full_name.title()}!!')

#     def increment_login_attempts(self):
#         self.login_attempts += 1
#         print(f'Login Attempts for {self.full_name.title()}: {self.login_attempts}.')

#     def reset_login_attempts(self):
#         self.login_attempts = 0
#         print(f'Login Attempts for {self.full_name.title()}: {self.login_attempts}. Succesfully reset!')

# class Admin(User):
#     def __init__(self, first, last, fave_color):
#         super().__init__(first, last, fave_color)
#         self.privileges = Privileges()

# class Privileges():
#     def __init__(self, privilages = []):
#         self.privileges = privilages
    
#     def add_privilege(self, *privileges):
#         for privilege in privileges:
#             self.privileges.append(privilege)

#     def show_privileges(self):
#         print(f'Admin Privileges: ')
#         for privileges in self.privileges:
#             print(privileges)

# new_admin = Admin('yogi', 'bear', 'picnic basket')
# admin_privileges = Privileges()
# admin_privileges.add_privilege('can ban', 'can add posts', 'can delete posts')
# new_admin.privileges.show_privileges()
# # new_user = User('miguel', 'triaca', 'blue')
# # new_user2= User('kanye','west', 'purple')
# # new_user.describe_user()
# # new_user2.describe_user()
# # new_user2.increment_login_attempts()
# # new_user.increment_login_attempts()
# # new_user.increment_login_attempts()
# # new_user.reset_login_attempts()
# # new_user2.reset_login_attempts()
# # new_user.greet_user()
# # new_user2.greet_user()

