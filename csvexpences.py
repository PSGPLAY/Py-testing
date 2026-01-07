import csv
import os


if not os.path.exists('expenses.csv'):
   with open('expenses.csv', mode='w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(['Date '  ' Amount '  ' Description'])


def add(date, amount, description):
   with open("expenses.csv", mode='a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow([f'{date} ' f' {amount} ' f' {description}'])

while True:
   user_input = input("Type Add, View or Quit to perform the action: ").lower()

   if(user_input.lower() == 'add'):

      date = input("Enter the date (YYYY-MM-DD) ")
      amount = float(input("Enter the amount: "))
      description = input("Enter the description: ").lower()
      
      add(date, amount, description)
   
   elif(user_input == "view"):
      with open("expenses.csv", mode='r') as file:
         reader = csv.reader(file)
         for row in reader:
            print(row)

   elif(user_input.lower() == 'quit'):
      break
   