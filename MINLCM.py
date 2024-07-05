# def LcmIs(x,y):
#     if x > y:
#         greater = x
#     else:
#         greater = y
#     while(True):
#         if(greater % x == 0 and greater % y == 0):
#             LCM = greater
#             break
#         greater += 1
#     return LCM
# def LcmIs(x, y):
#     from fractions import gcd # or can import gcd from `math` in Python 3
#     return x * y // gcd(x, y)
T = int(input())
for _ in range(T):
    lis = []
    X,K = input().split()
    X=int(X)
    K=int(K)
    print(X*2," ",((X*K)-1)*(X*K))
    # lis = [LcmIs(i,j) for i in range(int(X),(int(X)*int(K))+1) for j in range(i,(int(X)*int(K)+1)) if i!=j]
    # for i in range(int(X),(int(X)*int(K))+1):
    #     for j in range(i,(int(X)*int(K)+1)):
    #         if i==j:
    #             continue
    #         lcm = LcmIs(i,j)
    #         lis.append(lcm)
    # print(min(lis),max(lis))