"""Create a class Bank with a class variable bank_name. 
Add a class method change_bank_name(cls, name) that allows changing the bank name.
 Show that it affects all instances."""
class Bank:
    bank_name = "Mcb bank"  # Class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
my_bank= Bank()
my_bank.change_bank_name("js bank")
print(my_bank.bank_name)  # Output: js bank
my_bank2= Bank()
my_bank2.change_bank_name("allied bank")
print(my_bank2.bank_name)  # Output: allied     