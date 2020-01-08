from heapq import heappop, heappush

def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)

    ordered = []

    # While we have elements left in the heap
    while heap:
        ordered.append(heappop(heap))
    
    return ordered


array = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
print(heap_sort(array))

#
#
#
   # heappush(list, item): Adds an element to the heap, and re-sorts it afterward so that it remains a heap. Can be used on an empty list.
   #heappop(list): Pops (removes) the first (smallest) element and returns that element. The heap remains a heap after this operation, so we don't have to call heapify().
   # heapify(list): Turns the given list into a heap. It is worth noting that this method exists even though we won't be using this since we don't want to change our original array.
