
    


def quicksort(dau, cuoi, array):
    z = dau
    y = cuoi
    h=0
    while (dau <= cuoi):
        while(array[dau] < array[int(z+(y-z)/2)]):
            dau += 1
        while (array[cuoi] > array[int(z + (y-z)/2)]):
            cuoi -= 1
        if (array[dau] > array[cuoi]) and (dau < cuoi):
            s = array[dau]
            array[dau] = array[cuoi]
            array[cuoi] = s
            h = 1
        dau += 1
        cuoi -= 1
    if (dau - z > 0) and (h == 1):
        quicksort(z, dau, array)
    if (y-dau > 0) and (h == 1):
        quicksort(dau, y, array)


a = [1, 3, 5, 6, 2]
quicksort(0, 4, a)
print(a)
