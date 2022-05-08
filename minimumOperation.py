# you are given a number N. You have to
# find the minimum number of operations required to reach N from 0.
# You have two valid operations available:
# Double the number
# Add one to the number
def minimumOperation(n):
    count=0
    while(n):
        if n%2==0:
            n=n//2
        else:
            n-=1
        count+=1
    return count

print(minimumOperation(7))