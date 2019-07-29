#--------------------------ZIP-----------------------#
name = [ "Dhoni", "Kohli", "Ashwin", "Raina" ]
roll_no = [7, 14, 99, 24 ]
team = [ "csk", "rcb", "kip", "csk" ]
mapped = zip(name, roll_no, team)
finaloutput = set(mapped)
print(finaloutput)


#--------------------------UNZIPPING-----------------#

unzip_1, unzip_2, unzip_3 = zip(*finaloutput)

print("Name of the Players", unzip_1)
print("Jersey Number", unzip_2)
print("Jersey Number", unzip_3)

#------------------------Practial Orientation-------------#

Indian_Legends = ["Sachin", "Ganguly", "Dravid", "Kumble"]

Records = ["Runs", "Captaincy", "Defence", "Wickets"]

for x, y in zip(Indian_Legends, Records):
    print(x +" holds records for "+ y)

#----------------------------------------------------------#
