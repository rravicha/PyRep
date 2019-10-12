import requests

#overall we learnt
#requests.get -  url | params,auth,timeout
#requests.post - url | data


#timeout

'''
url="https://httpbin.org/delay/3"
r=requests.get(url,timeout=5)
print(r)
'''
'''
requests - auth


url="https://httpbin.org/basic-auth/susi/pass"
r=requests.get(url,auth=('susi','pass'))
print(r.text)
r=requests.get(url,auth=('susi','pass1'))
print(r)
'''
'''
payload={'username':'susi','password':'pass'}
url="https://httpbin.org/post"
r=requests.post(url,data=payload)
# print(r.text)
# print(r.url)
print(r.json()['form'])
'''

'''
get
'''
# payload={'page':2,'count':25}
# url1="https://httpbin.org/get"
# r=requests.get(url1,params=payload)
# print(r.text)
# print(r.url)








#___________

# print('_'*25)
# import requests

# url="https://goldprice.org/charts/gold_3d_g_INR.png"

# r=requests.get(url)
# with open("graph.png","wb") as f:
#     f.write(r.content)
# print(r.status_code)

