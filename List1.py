'''
Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
Output
1 2 3 4
'''

n = int(input())
my_list = []  
for i in range(n):
    element = int(input()) 
    my_list.append(element)  
for item in my_list:
    print(item, end=' ')  
