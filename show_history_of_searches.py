'''
This program is to simulate how the search shows the history of search commands
'''
hist={}
counter=0
while True:
    counter+=1
    print("Enter your query, Blank to show History")
    cmd=input()
    if cmd=="hist":
        print(hist)
    else:
        hist[counter]=cmd



