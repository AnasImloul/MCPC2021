from random import *


# A function that creates a N-sized array which sum is S
# example randomlist(4,18) -> [2,7,4,5]
def randomlist(N, S):
    
    # First of all try to create an array that's close to being an anwser
    # at most the error of A is N (e.g abs(sum(A) - S) <= N)
    A = [random() for i in range(N)]
    s = sum(A)
    A = [int(S*a/s) + 1 for a in A]
    
    # update the sum of the array
    s = sum(A)
    
    #if we already found such array
    # return it
    if s == S:
        return A
        
    #otherwise
    # do this until s == S
    # choose a random index which value if decremented won't result in a negative value
    # decrement it by one
    # repeat until s == N
    # note that it is guaranteed that s >= S
    j = 0
    while s != S:
        index = randint(0,N-1)
        if (S>=N and A[index] <= 1) or (S<N and A[index] <= 0):
            continue
        A[index] -= 1
        s -= 1
    
    return A


# a function that checks if there is a subsequence in A which sum is divisible by X
def possible(A,N,X):
    cumsum = [0 for i in range(N+1)]
    
    for i in range(N):
        cumsum[i+1] = cumsum[i] + A[i]
    
    for i in range(N):
        for j in range(i+1,N+1):
            if (cumsum[j] - cumsum[i]) % X == 0 and not (i==0 and j==N):
                return True
    return False


# a brute force approach to find the solution of this problem
def solve1(N,S,X):
    for i in range(20000):
        A = randomlist(N,S)
        if not possible(A,N,X):
            print(A)
            return True
    return False



# a more refined version of solve1
# it was achieved by testing multiple cases on solve1
# until a patterm was emerged



# function returns True if adhm can win else returns False
def solve(N,S,X):
    
    # if S < N means that there is always a zero in the array
    # since every number divides zero then methat can choose [0] and he will win
    if S < N:
        return False
    else:
        # if X >= N then X > S (because )
        # if X >= S then methat can't find a winning subsequence
        # since any subsequence have a sum that is less than S -> less than X
        # and we know that K is divisible by X implies K == 0 or K >= X
        # and since S >= N adhm can make an array with no zeros
        # then methat can never win
        # example : N,S,X = 6,10,17 -> array = [1,1,1,1,6] -> no winning subsequence exists
        if X >= N:
            return True
        
        # otherwise there is always a way for methat to win
        else:
            return False
            
# Try testing if the result of solve is the same as the result of solve1


           
tests = """
4 6 6
4 3 3
99 220 106
2354 3455 1234
"""

for test in tests.splitlines():
    try:
        N,S,X = map(int, test.split())
    except:
        continue
        
    print("adhm" if solve(N,S,X) else "methat")
    
