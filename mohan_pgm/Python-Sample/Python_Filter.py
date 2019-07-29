#Filter

##iteratingvariable = ["Dhoni","Kohli","Watson","Billings"]
##
##def iterationfunction(iteratingvariable):
##    cskteam = ["Dhoni","Watson","Billings"]
##
##    if iteratingvariable in cskteam:
##        return True
##    else:
##        return False
##
##outputvariable = filter(iterationfunction, iteratingvariable)
##
##print("Team selection")
##
##for v in outputvariable:
##    print(v)

#MAP

##iteratingvar = [ 1,2,3,4]
##
##def multi(var):
##    return var**2
##
###mapvar = list(map(multi, iteratingvar))
##
##mapvar = list(map(lambda x:x**2, iteratingvar))
##print(mapvar)


#REDUCE
##
##from functools import reduce
##itervar = [1,2,3,4]
##print(reduce((lambda x,y: x*2), [1,2,3,4]))

