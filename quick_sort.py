def quick_sort(list, low, high):
    if low < high:
        i = low
        j = high
        k = list[low]
        while i < j:
            while (i < j) and (list[j] >= k):
                j = j - 1
            list[i] = list[j]
            while (i < j) and (list[i] <= k):
                i = i + 1
            list[j] = list[i]
        list[i] =k
        quick_sort(list, low, i - 1)
        quick_sort(list, j + 1, high)
    return list


if __name__ == '__main__':
    list = [123,345,412,34,236,23,56,6,213,6,8,123,687,0,4,576,12,6,98,3,987,2,89,0,2]
    result = quick_sort(list, 0, len(list) - 1)
    print(result)