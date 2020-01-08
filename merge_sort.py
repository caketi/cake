def merge_sort(array, left_index, right_index):
    if left_index > right_index:
         return
    
    middle = (left_index + right_index)//2 
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)
"""
    We use the // operator to be explicit about the fact that we want integer values for our indices.
    Create copies of our arrays. The first array being the subarray from [left_index,..,middle] and the second from [middle+1,...,right_index]
    We go through both copies (keeping track of pointers in both arrays), picking the smaller of the two elements we're currently looking at, and add them to our sorted array. We move forward in whichever array we've chosen the element from, and forward in the sorted array regardless.
    If we run out of elements in one of our copies - simply add the remaining elements in the other copy to the sorted array.
"""
def merge(array, left_index, right_index, middle):
    """ Make copies of both arrays we're trying to merge
        The second parametrer is non-inclusive, so we have to increase by 1
    """
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle + 1:right_index + 1]

    """ Initial values for variables that we use to keep
        track of where we are in each array
    """
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index
    """
      Go through both copies until we run out of elements in one 
    """
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        """ If our left_copy has the smaller element, put it in the sorted
            part and then move forward in left_copy (by increasing the pointer)
        """
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
       
    
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1
        
        """Regardless of where we got our element from move forward in the sorted 
        port
        """
        sorted_index = sorted_index + 1
    
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

array = [33, 42, 9, 37, 8, 47, 5]
merge_sort(array, 0, len(array)-1)
print(array)
