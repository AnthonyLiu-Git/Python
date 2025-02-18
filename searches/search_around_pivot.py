# Python Program to search an element
# in a sorted and pivoted array


# sorted array arr[] of size n 
def pivoted_binary_search(arr: list, size: int, key: int) -> int:
    """Searches an element key in a pivoted
        Parameters
        ----------
        arr :
            Array to use.
        size : 
            Size of arr.
        key :
            Pivot value.
        Returns
        ---------
        int :
         Element of the array.
         
    >>> pivoted_binary_search([4, 5, 6, 7], 4, 6)
    6
    >>> pivoted_binary_search([4, 5, 6, 7], 2, -10)
    2
    >>> pivoted_binary_search([-18, 2], -18, 3)
    0
    """
    
    pivot = find_pivot(arr, 0, size-1);

    # If we didn't find a pivot, 
    # then array is not rotated at all
    if pivot == -1:
        return binary_search(arr, 0, size-1, key);

    # If we found a pivot, then first
    # compare with pivot and then
    # search in two subarrays around pivot
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binary_search(arr, 0, pivot-1, key);
    return binarys_earch(arr, pivot + 1, n-1, key);

def find_pivot(arr: list, low: int, high: int) -> int:
    """Searches an element key in a pivoted
        Parameters
        ----------
        arr :
            Array to use.
        low : 
            Low value.
        high:
            High value.
        Returns
        ---------
        int:
            Element of the array.
            
        >>> find_pivot([4, 5, 6, 7], 1, 2)
        0
    
    """
    if high < low:
        return -1
    if high == low:
        return low
    
    # low + (high - low)/2;
    mid = int((low + high)/2)
    
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid-1)
    return find_pivot(arr, mid + 1, high)

# Standard Binary Search function*/
def binary_search(arr: list, low: int, high: int, key: int) -> int:
    """Binary search
        ----------
        arr :
            Array to use.
        low : 
            Low value
        high :
            High value
        key : 
            value were looking for.
        
        Returns
        ---------
         int   
            Element of the array.
       
        >>> binary_search([0, 5, 7, 10, 15], 0)
        0
        >>> binary_search([0, 5, 7, 10, 15], 15)
        4
        >>> binary_search([0, 5, 7, 10, 15], 5)
        1
    
    """
    if high < low:
        return -1
        
    # low + (high - low)/2;    
    mid = int((low + high)/2)
    
    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binary_search(arr, (mid + 1), high,
                                            key);
    return binary_search(arr, low, (mid -1), key);
