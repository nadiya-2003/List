n = int(input())  
my_list = []
for i in range(n):
    element = int(input()) 
    my_list.append(element) 
smallest = my_list[0]
for number in my_list:
    if number < smallest:
        smallest = number 
print(smallest)
