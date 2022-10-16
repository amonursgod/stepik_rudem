import numpy as np

# np.int64 = Integer (-9223372036854775808 to 9223372036854775807)
#so this precision is enough for the maximal number 10^6*10^5
#in fact, int32 would also do, but I'll be on the safe side
#if you do something with numpy it will be fast, but forgert speed& memory limits when you work in python
with open("numbers.txt", "r") as input_file:
    n = int(input_file.readline().strip())
    datastring = (input_file.readline()).strip()
    data = np.fromstring(datastring, dtype='int64', sep=' ')
    m_slices = int((input_file.readline()).strip())
    slices = input_file.read().splitlines()
    slices = [(slice.split()) for slice in slices]
    slices =np.asarray(slices).astype('int64')

result = ""

for m in range(m_slices):    
    dataslice = data[int(slices[m][0]-1):int(slices[m][1])]
    ds_to_invert = (-1)*dataslice[1::2]
    ds_unchanged = dataslice[::2]
    sum= np.sum((np.sum(ds_to_invert),np.sum(ds_unchanged)))
    result = result + str(sum)+ " "
    
with open("output.txt", "w+") as output_file:
    #we must remove the last " " symbol in the resulting string!
    output_file.writelines(result[:-1])


    
    
