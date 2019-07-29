##import re
##
##line = "Cats are smarter than dogs"
##
##matchObj = re.match( r'(.*) are .*? .*', line, re.M)
##
##
##
##if matchObj:
##   print ("matchObj.group() : ", matchObj.group())
##   print ("matchObj.group(1) : ", matchObj.group(1))
##   print ("matchObj.group(2) : ", matchObj.group(2))
##else:
##   print ("No match!!")

#__________________________________________________________________________


#_________________________________________________________________________

###!/usr/bin/python3
##import r2
##
##line = "Cats are smarter than dogs";
##
##matchObj = re.match( r'dogs', line, re.M|re.I)
##if matchObj:
##   print ("match --> matchObj.group() : ", matchObj.group())
##else:
##   print ("No match!!")
##
##searchObj = re.se  arch( r'dogs', line, re.M|re.I)
##if searchObj:
##   print ("search --> searchObj.group() : ", searchObj.group())
##else:
##   print ("Nothing found!!")
#______________________________________________________________________________

#!/usr/bin/python3
import re

##phone = "2004- @ 959- 559  @ This is Phone Number"
##
## Delete Python-style comments
##num = re.sub(r'@', "", phone)
##print ("Phone Num : ", num)

### Remove anything other than digits
##num = re.sub(r'\d', "", phone)    
##print ("Phone Num : ", num)

#___________________________________________________________________________

## #!/usr/bin/python3
##import re
##
##line = "Cats are smar "
##
##matchObj = re.match( r'(.*) are (.) .*?', line, re.M|re.I)
##
##if matchObj:
##   print ("matchObj.group() : ", matchObj.group())
##   print ("matchObj.group(1) : ", matchObj.group(1))
##   print ("matchObj.group(2) : ", matchObj.group(2))
##else:
##   print ("No match!!")
##
##
### -- . matches any single character without \n
##
### -- *

#---------------------------------------------------------------------------

import re 


##var = "india is my country"
##
##result =  re.match(r'(.*) my ',var)
 ##
##print(result.group())

#_____________________________________________________________________________

##var = re.compile('[a-z]+')
##
##varmatch = var.match('i')
##
##print(varmatch)
##
##print(varmatch.group())
##
##print(varmatch.start())
##
##print(varmatch.end())
##
##print(varmatch.span())

#____________________________________________________________________________________

somestring = """
Dhoni is running fast even 8 though he is 39 and
Ashwin runs Slow eventhough he is younger and 311"""
##
##findage = re.findall(r'\D{1,2}', somestring)
##
##print(findage)

findnumber = re.findall(r'[A-Z][a-z]*', somestring)

print(findnumber)
##
findnumber_s = re.findall(r'\s[A-Z][a-z]*', somestring)

print(findnumber_s)
##
##
##findnumber_S = re.findall(r'\S[A-Za-z]*', somestring)
##
##print(findnumber_S)
##
##findname2 = re.findall(r'[a-z]*',somestring)
##
###print(findname2)
##
##
##findname3 = re.findall(r'[A-Z]',somestring)
##
###print(findname3)

# "\D" Prints or find only if the numbers are "Numeric"

##findage2 = re.findall(r'\D{1,2}', somestring)
##
###print(findage2)

#-----------------------------------------------------------------------------------------------------------------

###Greedy and Non Greedy
##
##var = "<html><head><\head><title><\ title><\html>"
##
##resultmatch = re.match('<.*>', var)
##
##resultmatch_1 = re.match('<.*?>', var)
##
##print(resultmatch.group())
##
##print(resultmatch_1.group())

#______________________________________________________________________________________________________________________

#Greedy and Non Greedy

#Greedy - When so many end tags gets matched then suitation becomes greedy and matches the last tag in the below tag string.

##var = "<html><head><\head><title><\ title><\html>"
##
##resultmatch = re.match('<.*>', var)
##
##resultmatch_1 = re.match('<.*?>', var)
##
##print(resultmatch.group())
##
##print(resultmatch_1.group())

#---------------------------------------------------------------------------------------------------------

##var = re.compile('[a-z]+')
##
##varmatch = var.match('i')
##
##print(varmatch)
##
##print(varmatch.group())
##
##print(varmatch.start())
##
##print(varmatch.end())
##
##print(varmatch.span())

#---------------------------------------------------------------------------
#To match IP Address 
import re
#var=r"[0-2][0-5][0-5].\d{1}.\d{1}.\d{1}"
#var=r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.\d{2}.\d{1}.\d{1}"
var="^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

if re.match(var,'255.255.255.256'):
  print("Matched")
else:
  print("Not matched")
#-----------------------------------------------------------------------------
#To match email adress
import re
var="^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+$"
if re.match(var,'gandhirajan0311@gmail.com'):
  print("Matched")
else:
  print("Not matched")
#-----------------------------------------------------------------------

##import re
##var= "My cap 357 sun 75 in 1066"
##var1=re.findall('\d{1,3}',var)
##print(var1)

#-----------------------------------------------------------------
#To match 127.0.0.1 
##import re
##var="\d{1,3}.\d{1}.\d{1}.\d{1}"
##if re.match(var,'127.0.0.1'):
##  print("Matched")
##else:
##  print("Not matched")
#---------------------------------------------------------------
#To didn't match 127.0.0.1 
import re
var="\d{1,3}.\d{1}.\d{1}.\d{1}"
if re.match(var,'1.0.0.1'):
  print("Matched")
else:
  print("Not matched")
#----------------------------------------------------------------
  
##import re
###var=r"[0-2][0-5][0-5].\d{1}.\d{1}.\d{1}"
###var=r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.\d{2}.\d{1}.\d{1}"
##var="^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
##
##if re.match(var,'255.255.255.256'):
##  print("Matched")
##else:
##  print("Not matched")

#----------------------------------------------------------------------

##import re
##var="^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+$"
##if re.match(var,'gandhirajan0311@embedur.com'):
##  print("Matched")
##else:
##  print("Not matched")

#----------------------------------------------------------------------




#Regular Expression to mach the string 
#import re
#var = "cats are dogs smarter"
#var1= re.match("cats",var)
#print(var1)
#print(var1.group())

#Regular Expression to search the string
#import re
#var = "cats are dogs smarter"
#var1= re.search("cats",var)
+#var1= re.search("dogs",var)
#print(var1)
#print(var1.group())

#import re
#var = "cats are dogs smarter"
#var1= re.search("dogs",var)
#print(var1)
#print(var1.group())


###Greedy
##import re
##var ="<html><head><title><head>"
##var1=re.match("<.*>",var)
##print(var1.group())
##
###Non Greedy
##import re
##var ="<html><head><title><head>"
##var1=re.match("<.*?>",var)
##print(var1.group())
##
##
###Greedy
##import re
##var ="<html><head><title><head>"
##var1=re.search("<.*>",var)
##print(var1.group())
##
###Non Greedy
##import re
##var ="<html><head><title><head>"
##var1=re.search("<.*?>",var)
##print(var1.group())

#import re
#var = "dhoni scored 32 of 100 run in 8 overs"
#var1=re.findall("\d{1,2}",var)
#print(var1)

#import re
#var = "dhoni scored 32 of 100 run in 8 overs"
#var1=re.findall("\d{1}",var)
#print(var1)

#import re
#var = "dhoni scored 32 of 100 run in 8 overs"
#var1=re.findall("\d{3}",var)
#print(var1)

##import re
##var = "dhoni scored 32 of 100 run in 8 overs"
##var1=re.findall("\D{3}",var)
##print(var1)

##import re
##var = "cats are dogs"
##var1=re.match("CATS",var)
##print(var1)
##
##import re
##var = "cats are dogs"
##var1=re.match("CATS",var,re.I)
##print(var1.group())
##
##import re
##var = """cats are dogs
##         and nothing"""
##var1=re.match("CATS",var,re.I)
##print(var1.group())

##import re
##var = """cats are dogs
##         and nothing"""
##var1=re.search("and",var)
##print(var1.group())

##import re
##var = "cats are smarter than dogs"
##var1= re.match('(.*) are (.*)' ,var)
##print(var1.group())
##
##import re
##var = "cats are smarter than dogs"
##var1= re.match('.* are .*' ,var)
##print(var1.group())

##import re
##var = "cats are smarter than dogs"
###var1= re.match('(.*) are (.*)' ,var)
##var1= re.match('.* are (.*)' ,var)
##print(var1.group())
##print(var1.group(1))
##print(var1.group(2))

#-------------------------------------------------

##import re
##var = "cats are smarter than dogs"
##var1= re.match('(.*) are (.*) (.*)' ,var)
##print(var1.group())
##print(var1.group(1))
##print(var1.group(2))
##print(var1.group(3))
##print(var1.group(4))

#---------------------------------------------------

##import re
##var = "cats are smarter than dogs"
##var1= re.match('(.*) are (.*) .*? (.*)' ,var)
##print(var1.group())
##print(var1.group(1))
##print(var1.group(2))
##print(var1.group(3))

#------------------------------------------------

##import re
##var = "cats are smarter than dogs"
##var1= re.match('(.*) are (.*) (.*)' ,var)
##print(var1.span())
##print(var1.start())
##print(var1.end())

#------------------------------------------

##import re
##var = "dhoni scored 32 of 100 run in 8 overs"
##var1=re.match("\d{3}",var)
##print(var1)

#---------------------------------------------

import re
var= "My cap 357 sun 75 in 1066"
var1=re.match('\d{1,3}',var)
print(var1)









           

          





