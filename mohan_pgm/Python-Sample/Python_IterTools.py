from itertools import count
for i in count(7):
    if i>14:
        break
    print(i)             
# -------------------------------------------------------------------
from itertools import cycle
c=0
for i in cycle(["Dhoni","kohli","ashwin"]):
                if c>7:
                    break
                print(i)
                c+=1 
# -------------------------------------------------------------------
from itertools import repeat
for i in repeat([1,2,3],4):
                print(i)             
# -------------------------------------------------------------------
list_data = ["Dhoni", "kohli", "Ashwin"]
output_Data = iter(list_data)
print(next(output_Data))
print(next(output_Data))
print(next(output_Data))
# ------------------------------------------------------------------
list_data = ["Dhoni", "kohli", "Ashwin"]
print(list_data.__len__())
print(list_data.__getitem__(2))
# --------------------------------------------------------------------
list_in = iter(["Messi","Ronaldo","Kaka"])
list_in2 = iter(list_in)

print(next(list_in2))
print(next(list_in2))
print(next(list_in2))
--------------------------------------------------------------------------
