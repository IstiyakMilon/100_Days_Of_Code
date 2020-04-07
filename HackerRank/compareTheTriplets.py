def compareTriplets(a, b):
    point_a=0
    point_b=0
    for i in range(3):
        if a[i]>b[i]:
            point_a+=1
            print(point_a, 'a')
        elif a[i]<b[i]:
            point_b+=1
            print(point_b, 'b')
       
    return [point_a, point_b]


print(compareTriplets([17, 28, 30],[99, 16, 8]))