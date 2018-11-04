#palindrome
n=int(input("Enter number:"))
copy=n
rev=0
while copy>0:
    rev=rev*10+copy%10
    copy//=10
if rev==n:
    print("Palindrome")
else:
    print("Not")
