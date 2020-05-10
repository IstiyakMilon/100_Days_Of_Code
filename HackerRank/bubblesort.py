n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swap_count=0
while True:
    for i in range(n - 1):
        if a[i + 1] < a[i]:
            swap_count += 1
            a[i + 1], a[i] = a[i], a[i + 1]
            break
    else:
        break
print("Array is sorted in %d swaps." % swap_count)
print("First Element: %d" % a[0])
print("Last Element: %d" % a[n-1])