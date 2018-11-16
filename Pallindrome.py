def reverse(s):
    return s[::-1]
def IsPallindrome(s):
    rev=reverse(s)

    if(s==rev):
        return True
    else:
        return False
s=input()
r=IsPallindrome(s)
if r==1:
    print("YES")
else:
    print("NO")