##var = "indiaintheindepedence"
##
##print(var.count("in")) #---- Counts the number of occurance of "in" in var.
##print(var.count("in",4)) #--- Counts the number of occurance of "in" starting from 4th index
##print(var.count("in",4,8))#--- Counts the number of occurance of "in" starting from 4th to 8th index
##
##print(var.index("in")) #---prints the first index of the "in" occurance
##print(var.find("in")) #--- same as that of the above index
##
###Difference between find and index
##
### Case 1. Index will throw the error if string is not available
### Case 2. find will throw the output by indicating -1 instead of error.
### Error(Case 1) means process has been killed, whereas -1(Case 2) makes process alive.
##
##print(var.index("z"))
##print(var.find("z"))
#---------------------------------------------------------------------------
##var = " india "
##print(len(var)) # ouput will be : 7 (inclusive of spaces)
##  
##var1 = var.strip() # Strip is used to remove or trim the extra spaces in starting and ending of the string
##print(len(var1)) # output will be : 5 (after the strip)
##
##var = "!!!Customer id 234!!!"
##var1 = var.strip("!") # stripping "!" character in the string (start and end)
##print(var1)
#Note " Strip() -- without arguments means space is the base of the strip
#----------------------------------------------------------------------------

##var = "202"
##var1 = var.zfill(5) # Fills the trailing zero's before the string on the base of length
##print(var1)

#----------------------------------------------------------------------------
##var = "dhoni"
##var1 = var.center(8,"*") # fills the "*" from right to left since "var" is odd
##print(var1)
##
##var = "dhonim"
##var1 = var.center(11,"*") # fills the "*" form left to right since "var" is even
##print(var1)
#--------------------------------------------------------------------------------
##var = "dhoni"
##var1 = var.ljust(8,"*") # fills the "*" right side and keeps string left justification 
##print(var1)
##
##var = "dhoni"
##var1 = var.rjust(8,"*") # fills the "*" left side and keeps string right justification 
##print(var1)
#-------------------------------------------------
##var = "dhoni is my captain"
##var1 = var.split() #---> converts the string to list keeping "space" as the base
##print(var1) 

##var = "dhoni is my captain"
##var1 = var.split("i") #---> converts the string to list keeping "i" as the base
##print(var1) 
#--------------------------------------------

                          #Basics functions

##var = "dhoni msd"
##
##print(var.upper())
##print(var.lower())
##print(var.title())
##print(var.capitalize())
##
##print(var.isupper())
##print(var.islower())
##print(var.istitle())

#-------------------------------------------
var = "20.3.2015"
##if var.startswith("20"):
##  print("success")

if "3" in var:
  print("success")
  
print("3" in var)







