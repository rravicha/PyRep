var ="dhoni msd"
print(var[2]) #----> Fetches only the 2nd index
print(var[2:]) #----> Fetches the data starting from 2nd index till end
print(var[2:6]) #----> Fetches the data starting from 2nd index till 6th value
print(var[:5]) #----> Fetches the data till 5nd value


#Dictionary

Point 1 : Dictionary is called key value pair
point 2 : Two Dimensional
point 3 : JSON is similar to dictionary (Java Script Object Notation)
point 4 : Input File format
point 5 : No Index based manipulation only "Key" based manipulation
point 6 : It is kind of hash table concept(Data Table)
point 7 : It is the form of key and value pair

var = {"name":"dhoni","age":37}

# "name" ---> Key
# "age"---> Key

var = {1:"dhoni",2:37}

Tips: keys can be in the form of 'String" or numerics or keywords(True,False)

var = {"Name":"dhoni","Age":37,'Name':"Ashwin"}

Note: Dictionary keys can t be duplicated. if it is duplicated then last value will  be is final value

var = {"name":["dhoni","aswin","shyam"],"age":37}

Note: To have more than one value in value then use list to store it

for x in var:
  print(x) #Returns only keys

for x in var.items():
  print(x) #Returns both keys and values

for x in var.values():
  print(x) #Returns both keys and values

##ex 1 : To find whether dhoni is there in value or not
var = {"name":["dhoni","aswin","shyam"],"age":37}

for x in var.values():
  if "dhoni" in x:
    print("success")


for x in var.values():
  for y in x:
     if y == "dhoni":
       print("success")

var = {"name":["dhoni","aswin","shyam"],"age":[37,76,87]}
  if "dhoni" in x:
    print("success")

  elif 37 in x:
      print("age sucess")

  else:
    print("not fount")


var = {"name":["dhoni","aswin","shyam"],"age":[37,76,87]}

  if "dhoni" in x or if 37 in x:
    print("success")

  else:
    print("not fount")















      




      


      

















