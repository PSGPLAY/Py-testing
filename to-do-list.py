tasks = [{"work": True}, {"run": False}]

def add(task, status=False):
   tasks.append({task: status})
   return ""

def see():
   for work in tasks:
      print(work)

def clear():
   tasks.clear()
   print("Your tasks have been cleared.")
   return ""

def remove(task):

   if (task not in tasks):
      print("Task not found.")

   elif(len(tasks) != 0 ):
      for item in tasks:
         if task in item:
            tasks.remove(item)
      for work in tasks:
         print(work)

   else:
      print("Your task list is empty.")
   
   


def change_status(task, status):
   for item in tasks:
      if task in item:
         item[task] = status


while True:
   userInput = input("Enter \"add\", \"see\", \"clear\", \"Change status\" or \"remove\": ").lower()

   if(userInput == "add"):
      userInput = input("Enter task to add: ")
      add(userInput.lower())

   elif(userInput == "see"):
      see()
   
   elif(userInput == "clear"):
      clear()
   
   elif(userInput == "change status"):
      task = input("Enter the task to change it's status: ").lower()
      for item in tasks:
         if task in item:
            print(f'Current status of "{task}" is {item[task]}')
      userInput = input("Enter the status of the task (True/False): ").lower()
      status  = True if userInput == "true" else False
      change_status(task, status)


   elif(userInput == "remove"):
      userInput = input("Enter task to remove: ")
      remove(userInput)
   while True:
      userInput = input("Do you want to continue?(y/n)")
      if(userInput.lower() == "y"):
         break
      elif(userInput.lower() == "n"):
         exit()
      else:
         print("Invalid input. Please enter 'y' or 'n'.")
