list = [5,3,8,4,2]

for i in range(len(list)-1):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]

print(list)