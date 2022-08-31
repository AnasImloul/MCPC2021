def solve(A, N):
    We want to rearrange the array in such a way
    # that the successive differences between odd indices
    # or the successive differences between odd indices 
    # is minimized # because we have complete freedom to choose
    # we can even sort the array
    # because sorting is just a specific rearrangement
    # then we can even try to find what are the N/2 successive numbers
    # we know that abs(A[i+1] - A[i]) == A[i+1] - A[i]
    # then the successive differences of N/2 numbers are simply A[i+N/2-1] - A[i]
    # As a result, we will try to get the minimum of this value (A[i+N/2-1] - A[i]).
    
    A.sort()
    half = N//2 - 1
    return min(A[i+half] - A[i] for i in range(N-half))
    
    
test = """9
19 4 14 1 11 13 17 3 12"""

N,A = test.splitlines()

A = list(map(int, A.split()))
N = int(N)


print(solve(A,N))
