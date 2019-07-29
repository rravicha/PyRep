import pickle

#example_dict = "my password"

##pickle_out = open("dict.pickle","wb")
##pickle.dump(example_dict, pickle_out)
##pickle_out.close()

#_________________________________________________________

pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)
print(example_dict) 
