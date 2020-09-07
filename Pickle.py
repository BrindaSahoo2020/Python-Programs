#Example on pickling /unpickling
'''
Note
Pickling is a process in which a Python object is converted into a string representation by a pickle module.
It is then placed into a file with the dump() function.
Unpickling refers to the reverse process,in which the stored string is retrieved and turned back into an object.
'''

import pickle

aashna_dict = {'Math': 45, 'Science': 48, 'SST': 45, 'English1': 47, 'Computer': 46, 'English2': 49}
outfile = open('aashna.txt','wb')
pickle.dump(aashna_dict,outfile)
outfile.close()

infile = open('aashna.txt','rb')
new_dict = pickle.load(infile)
infile.close()
print(new_dict)

if (new_dict == aashna_dict) :
    print("Yahh ! I learnt pickling")
else:
    print("Bad learner")