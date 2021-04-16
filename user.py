class User:
    def __init__(self, name, email) :
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount) :
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount) :
        self.account_balance -= amount
        return self
    def display_user_balance(self) :
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount) :
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

alex = User("Alex", "alex@python.com")
amy = User("Amy", "amy@python.com")
james = User("James", "james@python.com")

alex.make_deposit(200).make_deposit(500).make_deposit(50).make_withdrawal(100).display_user_balance()

amy.make_deposit(300).make_deposit(150).make_withdrawal(100).make_withdrawal(75).display_user_balance()

james.make_deposit(700).make_deposit(200).make_deposit(300).make_withdrawal(800).display_user_balance()

alex.transfer_money(james, 200).display_user_balance()
james.display_user_balance()
