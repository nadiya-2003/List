n = int(input()) 
my_list = []
for i in range(n):
    element = int(input())  
    my_list.append(element) 
largest = my_list[0]
for number in my_list:
    if number > largest:
        largest = number
print(largest)
