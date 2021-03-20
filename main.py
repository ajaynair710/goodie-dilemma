f = open("input.txt", "r")                                                                                              #input from file
x = int(f.readline().split(': ')[1])
x = int(input())
y = f.readline()
y = f.readline()
y = f.readline()

lines = f.readlines()
f.close()                                                                                                               #close file input
goodies = {}
price_arr = []
for line in lines:
    val = line.split(': ')                                                                                              #separating names of goodies and their cost
    goodies[val[0]] = int(val[1].split('\n')[0])
    price_arr.append(int(val[1].split('\n')[0]))

ans = {k: v for k, v in sorted(goodies.items(), key=lambda item: item[1])}

output = open("output.txt", "w")                                                                                        #opening the output file
output.write("The goodies selected for distribution are: \n\n")

price_arr.sort()                                                                                                        #sort the cost in ascending order and add to a new list
min_val = 100000000
ind = 0

for i in range(len(price_arr) - x):
    if (price_arr[i + x - 1] - price_arr[i]) < min_val:
        min_val = price_arr[i + x - 1] - price_arr[i]
        ind = i

flag = 0
first = 0
for i in ans:
    if ind <= first:
        output.write(i + ": " + str(ans[i]) + "\n")
        x -= 1

    first += 1
    if x == 0:
        break

output.write(
    "\nAnd the difference between the chosen goodie with highest price and the lowest price is " + str(min_val))        #print the difference between max and min
output.close()