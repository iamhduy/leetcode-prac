import heapq
import random
l = [random.randint(0, 20) for i in range(11)]
print("Original:", l)
print("Sorted:  ", sorted(l), sorted(l)[5])

hq = []
for num in l:
    heapq.heappush(hq, num)

print("Heap:    ", hq, hq[5])
