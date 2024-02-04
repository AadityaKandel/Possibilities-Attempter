import os
import random

total_numbers_inc = 0
output = 0
total = 0

all_values = []
random_index = []
increment = []
decrement = []

total_increment = 0
total_decrement = 0
possibilities=0

list_gatherer = []
int_gatherer = ""

list_within_list = [] # This will have the list of random_index appended inside itself

# Defining Functions
def w(text):
  print(text)

def check(var):
  if var.isnumeric() == True:
    return 1
  else:
    clear()
    return 0

def clear():
  os.system("cls")

def check_list(value):

  global int_gatherer,list_gatherer
  list_gatherer=[]

  if ',' in value and value[-1] != ',':

    for i in range(len(value)):
      if value[i].isnumeric() == True:
        int_gatherer+=value[i]
      elif value[i] == ",":
        list_gatherer.append(int(int_gatherer))
        int_gatherer = ''
      else:
        pass
    list_gatherer.append(int(int_gatherer))
    int_gatherer = ''

    # print(list_gatherer)
    # print(sum(list_gatherer))
    return True
  else:
    return False

def show_equation():
	global increment,decrement
	a = []
	b = []
	c = 'Equation: '

	for x in increment:
		a.append(str(x))
	for x in decrement:
		b.append(str(x))
	c+=f"{'+'.join(a)}-{'-'.join(b)}"
	print(c)

def initialize():
	global random_index,increment,decrement,total_increment,total_decrement
	random_index = []
	increment = []
	decrement = []
	total_increment=0
	total_decrement=0

w("Possibilities Attempter by Aaditya")
w("\n")

# Number to increase Append each number until or unless the user gives X to cancel
# Number to decrease Same goes here
# Output that must be equal to the value given

while (True):
  clear()
  print(f'[Optional: You can also give lists as 1,2,3,4,5]\n\n\
  Enter all numbers below.\n\
  Total numbers already given: {total_numbers_inc}\n\
  Enter X to goto the next step!\n')
  a = input()

  if a == "X":
    break
  else:
    pass

  if check_list(a) == True:
  	for items in list_gatherer:
  		all_values.append(items)
  	total_numbers_inc+=len(list_gatherer)
  elif check(a) == 1:
    all_values.append(int(a))
    total_numbers_inc+=1
  else:
    pass

while (True):
  clear()
  print('Enter your total value? \n')
  c = input()

  if check(c) == 1:
    total = int(c)
    break
  else:
    pass
clear()

# Increase or decrease = all_values
# Total = total

while (True):
  random_index = []
  if random_index in list_within_list:
    initialize()
    continue #Repeat the loop
  else:
    pass
  for i in range(len(all_values)):
    random_index.append(random.randint(0,1))

  list_within_list.append(random_index)

  for i in range(len(random_index)):
    if random_index[i] == 1:
      increment.append(all_values[i])
    elif random_index[i] == 0:
      decrement.append(all_values[i])

  total_increment = sum(increment)
  total_decrement = sum(decrement)


  answer = total_increment-total_decrement

  if answer == total:
    print(f"\n\nIncrement = {increment}")
    print(f"Decrement = {decrement}")
    print(f"Total: {total}")
    show_equation()
    break

  elif sum(all_values) == total: # This is for anti-theft
  	increment = []
  	for x in all_values:
  		increment.append(x)
  	decrement = []
  	print("\nDecrement doesn't exist")
  	break

  else:
    initialize()
    print(f"Possibilities Attempted = {possibilities}")

  possibilities+=1

print('\n')
os.system("pause")