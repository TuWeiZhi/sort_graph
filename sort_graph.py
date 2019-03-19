import random
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np

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

def bubble_sort():
    for i in range(len(list)):
        for j in range(0, len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                yield list

def init():
    ax.set_xlim(0, 101)
    ax.set_ylim(0, 101)
    return

def update(data):
    for i in range(len(data)):
        lines[i].set_ydata([0, data[i]])

    return lines

def quick_sort_temp():
    result= quick_sort(list, 0, len(list) - 1)
    yield result

if __name__ == '__main__':
    # plt.figure(figsize=(14, 8))
    fig, ax = plt.subplots(figsize=(14, 7))
    n = 100
    # list = np.random.randint(low=1, high=101, size=n)
    resultlist = random.sample(range(1, 101), n)
    list = np.array(resultlist)
    # print(list)
    # print(len(list))
    # print(type(list))
    # fast_sort_list = fast_sort(list)
    # print(list)
    xdata = [[i+1 for i in range(n)], [i+1 for i in range(n)]]
    ydata = [[0 for i in range(n)], list]
# x = [1, 2, 3]
# y = [6, 8, 10]
# for i in range(10):
#     y = [i + 1 for i in y]
#     print(len(list))
#     plt.bar([i for i in range(len(list))], list, width=0.5)
    lines = ax.plot(xdata, ydata, '#A9A9A9', LineWidth=3)
    temp = np.sort(list)
    print(temp)
# fig, ax = plt.subplot()
    ani = animation.FuncAnimation(fig, update, bubble_sort, interval=1, init_func=init)
    ani.save('test_animation.mp4', writer='ffmpeg',fps=1)
    #plt.show()
