def pageCount(n, p):
    #
    # Write your code here.
    #
    return min(p//2, n//2-p//2)



print(pageCount(5,4))