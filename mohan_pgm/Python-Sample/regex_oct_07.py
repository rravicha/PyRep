import re
##text = "India is my country ands isth endrous"
##v=re.findall(r'\b\w{4}\b',text)
##print(v)



#r'(?<![^A-Z])[A-Z]{3}[a-z][A-Z]{3}(?![A-Z])

import re

var = "India is Myss Country in the world Wor Cat"

var1 = re.findall(r'\b[A-Z][a-z]{2}\b', var)

print(var1)

##
##var = re.compile('^[A-Z]+$')
##var1 = var.match('INdia')
##print(var1.group())
