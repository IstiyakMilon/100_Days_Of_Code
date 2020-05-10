def binarySort()

for i in range(n - 1):
        if a[i + 1] < a[i]:
            swap_count += 1
            a[i + 1], a[i] = a[i], a[i + 1]
            break
    else:
        break