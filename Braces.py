'''BRACES HACKERRANK CODING CHALLENGE'''
n = input(int("Enter no. of Test Cases"))
print("Enter your input in Braces")
values = []
for i in n:
    value_item = input()
    values.append(value_item)
def Output(x):
    y=set(x)
    return y

Output(values)

