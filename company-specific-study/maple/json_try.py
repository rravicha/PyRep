d={"carrier":"cigna",
	"sbm":None,
	"ffm":True}
print(d)

import json
with open("som.json","w") as f:
	json.dump(d,f)

import os
os.system("cat som.json")