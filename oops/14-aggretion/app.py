
class person:
    def __init__(self, name):
        self.__name = name

    def __hello(self):
        print("Hello, everybody")
    def welcome(self):
        self.__hello()
person1 =person("faisal")
print(person1.welcome())
# class student:
#     def __init__(self, name):
#         self.name = name
# s1=student("faisal")
# del s1.name
# print(s1.name)

# class Account:
#     def __init__(self, balance, account_number,password):
#         self.account_number = account_number
#         self.balance = balance
#         self.__password = password  # Private attribute
#     def resset_password(self):
        
#         print(acc1.__password)    

# acc1=Account(1000, 123456789, "1234")
# print(acc1.balance, acc1.account_number)
# print(acc1.resset_password())

# acc1.__balance = 2000

