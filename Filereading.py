
##import io
##my_file_handle=open('c:\\code\\SAPPM.txt')
##my_file_handle.read()
##for line in my_file_handle:
## print(line)
##my_file_handle.close()
####
##import io
##import hashlib
##import datetime
##hash_object = hashlib.md5((datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
##    print(hash_object.hexdigest())

import datetime
import time
import hashlib
# Open the file with read only permit
f = open('c:\\code\\TEST.txt')
outF = open('c:\\code\\TEST_HASH.txt', "w")
# use readline() to read the first line 
line = f.readline()
# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty 
while line:
    # in python 2+
    # print line
    # in python 3 print is a builtin function, so
    # open a (new) file to write
    dtstamp = str(time.time())
    line = line + dtstamp
    #print(line)
    hash_object = hashlib.md5(line.encode())
    #outF.write(line)
    outF.writelines(hash_object.hexdigest())
    outF.write("\n")
    
    #print(line)
    # use realine() to read next line
    line = f.readline()
f.close()

outF.close()

#datetime hashcode generation
outFn = open('c:\\code\\TEST_HASH.txt', "a+")
dtstamp = str(time.time())
#print(dtstamp)
#dtstamp = str(time.time())
hash_object1 = hashlib.md5(dtstamp.encode())
outFn.writelines(hash_object1.hexdigest())
outFn.close()

#LGRhashcode for filename
fname = 'TEST_HASH.txt'
fname = fname + str(time.time())
hash_object2 = hashlib.md5(fname.encode())
outFn1 = open('c:\\code\\TEST_HASH_HASH.txt', "w")
outFn1.writelines(hash_object2.hexdigest())
outFn1.close()

#HASH CODE for Filename
# Open the file with read only permit
f = open('c:\\code\\WE_LGR.txt')
outF = open('c:\\code\\LGRhashfile.txt', "w")
# use readline() to read the first line 
line = f.readline()
# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty 
while line:
    # in python 2+
    # print line
    # in python 3 print is a builtin function, so
    # open a (new) file to write
    dtstamp = str(time.time())
    line = line + dtstamp
    #print(line)
    hash_object = hashlib.md5(line.encode())
    #outF.write(line)
    outF.writelines(hash_object.hexdigest())
    outF.write("\n")
    
    #print(line)
    # use realine() to read next line
    line = f.readline()
f.close()

outF.close()



