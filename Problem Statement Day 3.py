print("How many test cases u wanna enter")
n=input()
for x in n:
    m=input("Enter your string: ")
    Test_list = list(m)

    for i in range(0, len(Test_list) - 1):
        if ord(Test_list[i]) > 64 and ord(Test_list[i])< 91:
            Test_list[i] = chr(ord(Test_list[i]) + 32)

    Test_list=[] #list initialisation for storing duplicated characters
    for i in range(0, len(Test_list) - 2):
        for j in range(i+1, len(Test_list) - 1):
            if ord(Test_list[j])+1==ord(Test_list[j + 1]):
                Test_list.append(Test_list[j])
                Test_list.append(Test_list[j + 1])
            break
        i=i+2
    print(Test_list)
    for i in range(0, len(Test_list)-1):
        if ord(Test_list[i]) > 97 and ord(Test_list[i])< 122:
            Test_list[i] = chr(ord(Test_list[i]) - 32)
    print(Test_list)
    '''for i in range(0, len(Test_list) - 2):
        for j in range(i+1, len(Test_list) - 1):
            if ord(Test_list[j])+1==ord(Test_list[j + 1]):
                Test_list[j:j+1]=''.join(Test_list[j:j+1])
            break
        i=i+2
    print(Test_list)'''
