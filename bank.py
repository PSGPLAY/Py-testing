class Bank:
   def __init__(self, balance, acc_number):
      self.balance = balance
      self.acc_number = acc_number
   
   def withdraw(self, amount):
      if amount > self.balance:
         print("Insufficient balance")
      else:
         self.balance -= amount
         print("##################################################################################")
         print(f"Withdraw of {amount} was successful and the new balance is {self.balance}")
   
   def deposite(self, amount):
      self.balance += amount
      print("##################################################################################")
      print(f"Deposite of {amount} was successful and the new balance is {self.balance}")
   
   def show_balance(self):
      print("##################################################################################")
      print(f"The balance of account number {self.acc_number} is {self.balance}")
   
acc1 = Bank(1000, "1234567890")

while True:
   print("##################################################################################")
   print("Press 1 to withdraw\nPress 2 to deposite\nPress 3 to show balance\nPress 4 to exit")
   choise = int(input("Enter your choice: "))

   if choise == 1:
      amount = int(input("Enter amount to withdraw: "))
      acc1.withdraw(amount)
      
   elif choise == 2:
      amount = int(input("Enter amount to deposite: "))
      acc1.deposite(amount)
   elif choise == 3:
      acc1.show_balance()
   elif choise == 4:
      print("Thank you for using our services")
      break
   else:
      print("Invalid choice, please try again")