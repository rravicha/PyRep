import csv

 

with open('people.csv', 'r') as csvFile:

    #reader = csv.DictReader(csvFile)

    reader = csv.reader(csvFile, delimiter="|")

    for row in reader:

        print(row)

 

csvFile.close()

 

 

import csv

import sys

 

##inputdata = [["Team","Player_Name"], ["CSK","Dhoni"], ["RCB","kohli"]]

##

##print(inputdata)

##with open("june13.csv","w",newline="") as csvfile:

##    w = csv.writer(csvfile)

##    w.writerows(inputdata)

##csvfile.close()

 

 

 

##inputdata = ["Dhoni","Kohli",56]

##

##print(inputdata)

##with open("june13.csv","wt",newline="") as csvfile:

##    w = csv.writer(csvfile)

##    w.writerow(("one","two","three"))

##    w.writerow(inputdata)

##csvfile.close()

 

 

##inputdata = ["Dhoni","Kohli",56]

##

##print(inputdata)

##with open("june13.csv","wt",newline="") as csvfile:

##    w = csv.writer(csvfile,quoting=csv.QUOTE_ALL)

##    w.writerow(("one","two","three"))

##    for i in range(10):

##        w.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)))

##

##csvfile.close()

##

##print (open("june13.csv", 'rt').read())

##

 

##Note:

##

##Quoting

##There are four different quoting options, defined as constants in the csv module.

##

##QUOTE_ALL--->Quote everything, regardless of type.

##QUOTE_MINIMAL--->Quote fields with special characters (anything that would confuse a parser configured with the same dialect and options). This is the default

##QUOTE_NONNUMERIC--->Quote all fields that are not integers or floats. When used with the reader, input fields that are not quoted are converted to floats.

##QUOTE_NONE--->Do not quote anything on output. When used with the reader, quote characters are included in the field values (normally, they are treated as delimiters and stripped).

 

 

 

##import csv

##inputdata = ["Dhoni","Kohli",56]

##

##print(inputdata)

##with open("june13.csv","wt",newline="") as csvfile:

##    w = csv.writer(csvfile,quoting=csv.QUOTE_ALL)

##    w.writerow(("one","two","three"))

##    for i in range(10):

##        w.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)))

###print (open("june13.csv", 'rt',).read())

##csv.register_dialect('pipes', delimiter='*')

##with open('june13.csv', 'r') as f:

##    reader = csv.reader(f, dialect='pipes')

##    for row in reader:

##        print (row)

##csvfile.close()
