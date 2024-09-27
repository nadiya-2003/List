'''
Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
'''


list_input = input("Enter the list elements (space-separated): ")
elements = list_input.split()
elements = [int(num) for num in elements]
elements.sort()
print(" ".join(map(str, elements)))




