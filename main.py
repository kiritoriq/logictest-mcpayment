limit = input("Insert the size of nums: ")
number=0
arr = []
for x in range(int(limit)):
    temp = input("Insert nums #" + str(x) + ": ")
    arr.append(int(temp))

target = input("Insert your target number: ")
i = 0
while i < len(arr):
    j = i+1
    is_continue = 0
    while j < len(arr):
        add = arr[i] + arr[j]
        if(int(add) == int(target)):
            print("["+ str(i) + ", " + str(j) +"]\n")
            print("Because nums[" + str(i) +"] + nums[" + str(j) + "] == " + target)
            is_continue = 1
            break
        else:
            j+=1
    if(is_continue == 1):
        break
    else:
        i+=1