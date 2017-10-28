def merge(left, right):
    """
    left: left part of the list
    right: right part of the list
    """
    
    result = []
    i, j = 0, 0
    
    # iterate through both lists simultaneously
    while i < len(left) and j < len(right):
        # if element in left list is smaller than the element in the right list
        if left[i] < right[j]:
            # append the element in the left list to the result
            result.append(left[i])
            i += 1
        else:
            # append element from right list to the result
            result.append(right[j])
            j += 1
    
    # if length of left list is bigger than right list, append the remaining
    # elements in the result
    while i < len(left):
        result.append(left[i])
        i += 1
    # if length of right list is bigger than left list, append the remaining
    # elements in the result
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def merge_sort(L):
    # if the list is empty or contains only one element
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        
        return merge(left, right)