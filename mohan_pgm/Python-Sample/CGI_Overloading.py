def add(instanceOf, *args):
    if instanceOf == 'int':
        result = 0
    if instanceOf == 'str':
        result = ''
    for i in args:
        result = result + i
    return result
 
print (add('int', 100,4,5))
print (add('str', 'I',' am',' in', ' Python'))


