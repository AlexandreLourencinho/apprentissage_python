first_list = []

first_list.append(4)
print(first_list)
first_list.append(5)
first_list.remove(5)

print(first_list)

first_list.append(5)
first_list.append(5)
first_list.remove(5)
print(first_list)
# indices : 0 1 2... mais aussi de la fin ! -1 -2 ....(-1 = le dernier)
print(first_list[1]) #should be 5
print(first_list[-1]) #should also be 5
print(first_list[0]) #should be 4
print(first_list[-2]) #also 4
