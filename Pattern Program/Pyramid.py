def pattern(n):
    k=n
    #k=2*n-2
    for i in range (0,n):
        for j in range (0,k):
            print(end=" ")
        k=k-1
        for j in range (0,i+1):
            print('* ',end="")
        print("\r")

pattern(5)


def pattern2(n):

    k=2*n-2
    for i in range (0,n):
        for j in range (0,k):
            print(end=" ")
        k=k-1
        for j in range (0,i+1):
            print('* ',end="")
        print("\r")

pattern2(5)