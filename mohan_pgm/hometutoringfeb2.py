#Differene between mutable and immutable

#Changing index in the List
var = ["dhoni","ashwin","rahul"]
print(var[0])

var[0] = "kohli"
print(var) #Returns the output of the modified Data output(List is mutable)

#changing index in the string
newvar = "rohit"
print(newvar[0])

newvar[0] = "m"
print(newvar) #Returns the error.(String is immutable)

#List In Built Functionality

#append() --> Append add single data(Sigle index) into the list
var = ["Dhoni","Ashwin","Dravid"]
var.append("kohli")
print(var)
#output --> ["Dhoni","Ashwin","Dravid","kohli"]

#Adding more than one data in append
var = ["Dhoni","Ashwin","Dravid"]
var.append("kohli","pandya")
print(var)
#output --> Error(Appends had the capacity to add only one data on one index)

#Adding more than one data in the form of list to  append
var = ["Dhoni","Ashwin","Dravid"]
var.append(["kohli","pandya"])
print(var)
#output --> ["Dhoni","Ashwin","Dravid",["kohli","pandya"]]

#Insert() --> insert is to insert data onto the specific position
var = ["Dhoni","Ashwin","Dravid"]
var.insert(1,"kohli") #Inserts data on the specified position and pushes data into next index positions
print(var)
#output --> ["Dhoni","kohli","Dravid","kohli"]

#extend() --> Append add multiple data(multiple index) into the list    
var = ["Dhoni","Ashwin","Dravid"]
var.extend(["kohli","pandya"])
print(var)
#output --> ["Dhoni","Ashwin","Dravid","kohli","pandya"]

#sort() --> Sort the given data in specified order
var = ["Dhoni","Ashwin","Lukaku"]
var.sort() # Sorts the data by keeping first letter of a string(Default=Ascending)
print(var)
#output --> ["Ashwin","Dhoni","Lukaku"]

#sort() --> if two or more data contains same starting letter then it considers second letter
var = ["Dhoni","Ashwin","Aagon"]
var.sort() # Sorts the data by keeping first letter of a string(Default=Ascending)
print(var)
#output --> ["Aagon","Ashwin","Dhoni"]

#sort() --> if list contains mixed cases it does upper sort first and then lower
var = ["Dhoni","Ashwin","aagon"]
var.sort() # Sorts the data by keeping first letter of a string(Default=Ascending)
print(var)
#output --> ["Ashwin","Dhoni","aagon"]

#sort() --> if list contains mixed cases with numbers
var = ["Dhoni","Ashwin",6,"aagon",4]
var.sort()
print(var)
#output --> Error --> Sorting needs data to be in the format of the array(similar data type)

#sort(revere = True) --> sorts the given datat in the form of descending keeping upper and lower starting prirority as usual
var = ["Dhoni","Ashwin","aagon"]
var.sort(reverse = True) # Sorts the data by keeping first letter of a string(Default=Ascending)
print(var)
#output --> ["Dhoni","Ashwin","aagon"]

#Note: Sorting can be done for the numbers as well.
#print(var.sort()) -->Not Possible because function will not return anything

#Sorted() --> Does similar sort() function but return the data on the same line
var = ["Dhoni","Ashwin","aagon"]
print(sorted(var)) # Sorts the data by keeping first letter of a string(Default=Ascending)

#Sorted(reverse=True) --> Does similar sort() function but return the reversed data on the same line
var = ["Dhoni","Ashwin","aagon"]
print(sorted(var,reverse=True)) # Sorts the data by keeping first letter of a string(Default

#pop() --> Removed last index data (Last in First out)
var = ["Dhoni","Ashwin","aagon"]
var.pop()
print(var)
#output --> ["Dhoni","Ashwin"]

#pop(1) --> 1 inside pop removes the first index in my var(Defaut = Last index)
var = ["Dhoni","Ashwin","aagon"]
var.pop(1)
print(var)
#output --> ["Dhoni","aagon"]

#remove() --> Removes the given data from the list(no Default )
var = ["Dhoni","Ashwin","aagon"]
var.remove("Dhoni")
print(var)
#output --> ["Ashwin","aagon"]

#clear() --> Clear removes all the data from list
var = ["Dhoni","Ashwin","aagon"]
var.clear()
print(var)
#output --> []

#del --> Deletes the complete list from the memory
var = ["Dhoni","Ashwin","aagon"]
del var
print(var)
#output --> we cant see var in output since we deleted it earlier


#----------------------------------Tuples---------------

var = ("Dhoni","Ashwin","aagon")
print(var)
print(type(var))

#always add a ,(Comma) when tuple contains only one data
var = ("Dhoni",)
print(var)
print(type(var))

#Note: We cant use functionality which does index based modifications in tuples
# we can use only two function in tuples (index and count)

#Case 1 : Tuples were used mostly like(IPAddress, Password)
#Case 2 : Use List when there is need for change of data(scores,marks)
#Case 3 : Tuples always occupies lesser system memory than List
import sys

tuple_var = ("Dhoni","Ashwin","aagon")
print(sys.getsizeof(tuple_var)) # 40 

list_var = ["Dhoni","Ashwin","aagon"]
print(sys.getsizeof(list_var)) # 48

#output -> tuples takes lesser system memory than that of list

#-----------------Memory Allocation and Destruction-------

var = "dhoni"
var = "kohli"
print(var)

#Python does automated memory deallocation automatically

# manipulation 1 : var = [3,5,6,2,1] --> find the maximum
# manipulation 2 : var = ["dhoni","ashwin","rahul] --> reverse the string and store the data in new list

















































