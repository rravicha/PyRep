# var[-2] in for loop will not print the same during print rather it prints previous values
var = ['a','b','c','d']
print(var[-1])
for var[-2] in var:
  print(var[-2])
