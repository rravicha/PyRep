'''
regular expressions
'''
import re
var="Dhoni is better than Kohli"

var1=re.match('Dhoni',var,re.I)#re.I will ignore the case
var1=re.search('is',var,re.I)#re.I will ignore the case
# print(var1)

var2="<html><head></head><body></body></html>"
var2_re=re.search("<.*?>",var2)
# print(var2_re.group())
var3=" Indiakk is my Country and it is actually united 123.1 states of ethnic groups of more than 45 group out of which 1 and  2 groups are legacy"
var3_re=re.findall("\w+",var3)
var3_re=re.findall("\w{5}",var3)#will get words only which has 5 or more char
var3_re=re.findall("\D{5}",var3)# will bisect exactly by 5
var3_re=re.findall(" [A-Z]\w{5}",var3)
var3_re=re.findall("\d{1,3}.\d{1}",var3)#match 3 digits followed by a dot and one digit

var4="Cats are Smarter than dogs"
var4_re=re.match('.*are.*',var4)
# print(var4_re.group())
var4_re=re.match('(.*)are(.*)',var4)#group it
var4_re=re.match('(.*) are (.*?) (.*)',var4)#group it
# print(var4_re.group())
# print(var4_re.group(1))
# print(var4_re.group(2))
# print(var4_re.group(3))

var4_re=re.sub('a','A',var4)
# print(var4_re)








