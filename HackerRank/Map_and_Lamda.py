cube = lambda x:x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    List=[0,1]
    if n==1:
        return List[:1]
    if n==0:
        return []
    for i in range(2,n):
        List.append(List[-2]+List[-1])
    return List

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))