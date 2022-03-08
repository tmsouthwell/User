


class User:
    def __init__(self, first_name, last_name, account_balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_balance = account_balance

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User:{self.first_name},Balance:{self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        
        
bob = User("Bob", "Smith", 500)
print(bob.account_balance)

guido = User("Guido", "Parma", 1000)
print(guido.account_balance)

guido.make_withdrawal(100)
print(guido.account_balance)

guido.display_user_balance()

bob.transfer_money(guido, 100)
print(guido.account_balance)

bob.display_user_balance()

# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150