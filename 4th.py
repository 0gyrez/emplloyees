import pickle
import random
# програма по невідомим причинам поломалась, я її тестив і все було ок, але шось пішло не так
def random_adding(data):
  count = input_int("Enter count employees: ", error_text = "Try again!")
  for i in range(count):     
      new_employee = {
      "name":random.choice(read_names()),
      "age":random.randint(21,50),
      "experience":random.randint(1, 120)
      }
      data.append(new_employee) 
  print_employee(data)    
  

def add_employee(data):
  print("Add employee")
  name = input("Enter name: ")
  age = input_int("Enter new age: ", error_text = "Enter digit!")
  experience = input("Enter experience(in mounth): ")
  new_employee =  {
    "name":name,
    "age":age,
    "experience":experience
    }
  data.append(new_employee)
  print("New employee was created")
  return data


def del_employee(data):
  print("Delete employee")
  name = input("Enter name: ")
  find = find_name(data, name)
  if find:
     data.remove(find)
     print(name, "deleted")
  else:
     print("Nothing found: ")
  return data


def search_employee(data):
    print("search")
    choise = input("Enter choise\n"
             "1 - search in name\n"
             "2 - search in start with\n"
             "3 - search in age\n"
             "Your choise: ")
    founded = []
    if choise == '1':
        name = input("Enter name: ")
        #founded = list(filter(lambda x: x["name"] == name, data))
        data_sorted = sorting(data, key = lambda x: x["name"])
        index = bin_search(data_sorted, name, key = lambda x: x["name"])
        founded.append(data_sorted[index])
    elif choise == '2':
      let = input("Enter let: ")
      founded = list(filter(lambda x: x["name"].startswith(let), data))
    elif choise == '3':
        age = input_int("Enter  age: ", error_text = "Enter digit!")
        #founded = list(filter(lambda x: x["age"] == age, data))
        data_sorted = sorting(data, key = lambda x: x["age"])
        index = bin_search(data, age, key = lambda x: x["age"])
        founded.append(data_sorted[index])
    if len(founded) == 0:    
         print("Nothing found")         
    print_employee(founded)
    return


def edit_employee(data):
    print("Edit employee")
    name = input("Enter name: ")
    employee = find_name(data, name)
    if employee:
      new_name = input("Enter new name: ")
      new_age = input_int("Enter new age: ", error_text = "Enter digit!")
      new_experience = input("Enter new experience(in mounth): ")
      employee["name"] = new_name
      employee["age"] = new_age
      employee["experience"] = new_experience
      print("change  completed")
    else:
      print("Nothing Found!")
    return data


def find_name(data, name):
    for elem in data:
        if elem["name"] == name:
           return elem
    return None


def print_employee(data):
  for elem in data:
    print(f'Ім"я: {elem["name"]}, Вік: {elem["age"]}, Досвід(в місяцях): {elem["experience"]}')
  return


def input_int(text, error_text):
  x = input(text)
  while not x.isnumeric():
    print(error_text)
    x = input(text)
  return int(x)


def sorting(data, key):
  for i in range(len(data)):
      min_index = i
      for j in range(i, len(data)):
        if key(data[j]) < key(data[min_index]):
          min_index = j
      data[i], data[min_index] = data[min_index], data[i]
  return data


def bin_search(data, elem, key):
  start = 0
  end = len(data) - 1
  while start <= end:
    midle = (start + end) // 2
    if key(data[midle]) > elem:
      end = midle - 1
    elif key(data[midle]) < elem:
      start = midle + 1
    elif key(data[midle]) == elem:
      return midle   


def sort_employee(data):
  choise = str(input("Enter sortning Name/Age: "))
  if choise == "Name":
    print_employee(sorting(data, key = lambda x: x['name']))
  elif choise == "Age":
    print_employee(sorting(data, key = lambda x: x['age']))
  else:
    print("Try again!")
    sort_employee(data)
    

def read_names():
   Names = []
   with open("Names.txt", 'r') as file:
     for name in file:
         name = name.replace("\n","")
         Names.append(name)
   return Names


def main():
  try:
     inf = open("data.pickle", "rb")
     data = pickle.load(inf)
     inf.close()
  except FileNotFoundError:
     data = []

  while True:
    print("*"*14)
    choise = input("Enter action:\n"
                 "1 - add employee\n"
                 "2 - delete employee\n"
                 "3 - search employee\n"
                 "4 - change employee\n"
                 "5 - save all\n"
                 "6 - show employee\n"
                 "7 - sort employee\n"
                 "8 - add random employee\n"
                 "Another key - Exit\n"
                 "Your choise: ")
    if choise == '1':
        add_employee(data)
    elif choise == '2':
         del_employee(data)
    elif choise == '4':
         data = edit_employee(data)
    elif choise == '3':
         search_employee(data)
    elif choise == '5':
        with open("data.pickle", 'wb') as save:
          pickle.dump(data, save)
        print("Succesfull save")
    elif choise == '6':
       print_employee(data)
    elif choise == '7':
          data = sort_employee(data)
    elif choise == '8':
       data = random_adding(data)
    else:
     break
main()