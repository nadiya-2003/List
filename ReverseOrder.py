'''
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
'''




list_input = input("Enter the list elements (space-separated): ")
elements = list_input.split()
reversed_elements = []
for i in range(len(elements) - 1, -1, -1):
    reversed_elements.append(elements[i])
print(" ".join(reversed_elements))
