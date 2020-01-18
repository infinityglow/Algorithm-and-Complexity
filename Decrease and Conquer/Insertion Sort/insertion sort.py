import random
import time
from array import generator


# implementation of insertion sort
# to sort a random array with 10,000 elements
# two metrics ("number of comparison" and "consumed time") for efficiency evaluation
# time complexity: Θ(n^2) for the worst and average case, and Θ(n) for the best case
# space complexity Θ(1)
# stability: stable


def insertion_sort(array):
    cnt = 0
    for i in range(len(array)-1):
        v = array[i]
        j = i - 1
        while True:
            cnt += 1
            if j < 0 or array[j] <= v:
                break
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = v
    return cnt

time_in_total = 0
epoch = 5  # num of iteration
total_comparison = 0

# instantiate a generator
gen = generator(10000, 1)

# best case Θ(n)
print("Best Case: ")
for i in range(epoch):
    array = gen.best()
    time_start = time.time()
    comparison = insertion_sort(array)
    time_finish = time.time()
    total_comparison += comparison
    time_in_total += time_finish - time_start
    print("Epoch {}: \n  number of comparison: {}\n  time consumed: {:.4f} s".format(i+1, comparison, time_finish-time_start))
print("average number of comparison: %d" % (total_comparison/epoch))
print('average time consumed: {:.4f} s'.format(time_in_total/epoch))

# average case Θ(n^2 / 4)
total_comparison = 0; time_in_total = 0
print("Average Case: ")
for i in range(epoch):
    array = gen.avg()
    time_start = time.time()
    comparison = insertion_sort(array)
    time_finish = time.time()
    total_comparison += comparison
    time_in_total += time_finish-time_start
    print("Epoch {}: \n  number of comparison: {}\n  time consumed: {:.4f} s".format(i+1, comparison, time_finish-time_start))
print("average number of comparison: %d" % (total_comparison/epoch))
print('average time consumed: {:.4f} s'.format(time_in_total/epoch))

# worst case Θ(n^2)
total_comparison = 0; time_in_total = 0
print("Worst Case: ")
for i in range(epoch):
    array = gen.worst()
    time_start = time.time()
    comparison = insertion_sort(array)
    time_finish = time.time()
    total_comparison += comparison
    time_in_total += time_finish-time_start
    print("Epoch {}: \n  number of comparison: {}\n  time consumed: {:.4f} s".format(i+1, comparison, time_finish-time_start))
print("average number of comparison: %d" % (total_comparison/epoch))
print('average time consumed: {:.2f} s'.format(time_in_total/epoch))

