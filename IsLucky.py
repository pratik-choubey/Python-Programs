# if we have 7 in given three digits number then print yes and if not print no
T = int(input())
ans = []
for i in range(T):
    l = input().split(" ")
    if "7" in l:
        ans.append("yes")
    else:
        ans.append("no")
for i in ans:
    print(i)
