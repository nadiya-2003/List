n = int(input())  # Size of the list
my_list = []
for i in range(n):
    element = int(input()) 
    my_list.append(element) 
even_list = []
odd_list = []
for number in my_list:
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number) 
print("The even list", even_list)
print("The odd list", odd_list)
