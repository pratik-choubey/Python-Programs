#Palindrome string
#method 1
def IsPalindrome(string):
    if string == string[::-1]:
        return True
    return False 
if __name__ == "__main__":
    if IsPalindrome("aa5bhbhfseaa"):
        print("Palindrome string Hain")  
    else:
        print("Nai hain palindrome")     
# method 2
s = "aaaaaa"
l=len(s)//2
for i in range(l):
    if s[i]==s[l-i-1]:
        flag=True
    else:
        flag=False
        break
if flag:
    print("palindrome")
else:
    print("not palindrome")