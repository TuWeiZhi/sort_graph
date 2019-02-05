import random
from matplotlib import pyplot as plt
import matplotlib.animation as animation

def random_list():
    list = []
    for i in range(1,101):
        list.append(random.randint(0,1000))
    return list

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

def init():
    ax.set_xlim(-1, 100)
    ax.set_ylim(-1, 1000)
    pass
# def fast_sort(list):
#     length = len(list)
#     result_list = quick_sort(list, 0, length - 1)

if __name__ == '__main__':
    plt.figure(figsize=(14, 8))
    fig, ax = plt.subplot()

    list = random_list()
    # fast_sort_list = fast_sort(list)
    # print(list)

# x = [1, 2, 3]
# y = [6, 8, 10]
# for i in range(10):
#     y = [i + 1 for i in y]
#     print(len(list))
#     plt.bar([i for i in range(len(list))], list, width=0.5)

# fig, ax = plt.subplot()
    ani = animation.FuncAnimation(fig=fig, init_func=init)
    plt.show()
