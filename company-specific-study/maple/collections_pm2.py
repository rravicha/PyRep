d1=[('name','dhoni'),('age',37),('name','Kohli')]

import collections
d2=collections.defaultdict(list)
for k,v in d1:
	print(k,v)
	d2[k].append(v)

print(d2.items())
