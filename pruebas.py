
# import random
import random
  
# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6]
#print(random.choice(list1))
clave = ""
for i in range(60):
    a=random.choice(list1)
    clave = f"{clave}{a}"
print(clave)