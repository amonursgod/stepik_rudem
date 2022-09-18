#add input.txt file with k, output is saved to output.txt
routes = ["","","","AHG","ABIG","ABCJG"]

with open("input.txt",'r') as input_file:
    k=int(input_file.readline())//100

remainder3 = k % 3
multiples3 = k // 3

if remainder3 == 0:
    result = routes[3]*multiples3
elif remainder3 == 1:
    result = routes[4]+routes[3]*(multiples3-1)
elif remainder3 == 2:
    result = routes[5]+routes[3]*(multiples3-1)

with open("output.txt",'w+') as output_file:    
    output_file.writelines(result)
