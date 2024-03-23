def combine(source, destination, iBegin1, iBegin2, iEnd2):
    iEnd1 = iBegin2

    for iDestination in range(iBegin1, iEnd2):
        if iBegin1 < iEnd1 and (iBegin2 == iEnd2 or source[iBegin1] < source[iBegin2]):
            destination[iDestination] = source[iBegin1]
            iBegin1 += 1
        else:
            destination[iDestination] = source[iBegin2]
            iBegin2 += 1
    
    return destination


def sort(array): #01
    size = len(array)
    src = array[:]
    des = [0] * size
    num = 2 #05

    while num > 1:
        num = 0
        iBegin1 = 0

        while iBegin1 < size:
            iEnd1 = iBegin1 + 1 #10
            while iEnd1 < size and src[iEnd1 - 1] <= src[iEnd1]:
                iEnd1 += 1

            iBegin2 = iEnd1
            if iBegin2 < size:
                iEnd2 = iBegin2 + 1 #15
            else:
                iEnd2 = iBegin2
            while iEnd2 < size and src[iEnd2 - 1] <= src[iEnd2]:
                iEnd2 += 1

            num += 1 #20
            combine(src, des, iBegin1, iBegin2, iEnd2)
            iBegin1 = iEnd2

        src, des = des, src

    return src

# Example usage
array = [2, 5, 7, 3, 4]
sorted_array = sort(array)
print(sorted_array)  # Output will be the sorted array
