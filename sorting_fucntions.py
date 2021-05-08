#The five sorting fucntions i have selected are as follows

# Bubble sort - simple comparison based sort
#code as per lectures

def bubble_sort(arr):
    n = len(arr)
    for outer in range(n-1, 0, -1):
        for inner in range(0,outer,1):
            if arr[inner] > arr[inner+1]:
                temp = arr[inner]
                arr[inner] = arr[inner+1]
                arr[inner+1] = temp
    #print("results from Bubble sort")
    #print(arr)
    return arr 


#https://www.geeksforgeeks.org/bubble-sort/

def bubble_sort2(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


## Merge sort - efficient comparison based sort
# code adapted from https://realpython.com/sorting-algorithms-python/#the-merge-sort-algorithm-in-python

def merge(left, right):

    # If the first array is empty, then nothing needs

    # to be merged, and you can return the second array as the result

    if len(left) == 0:

        return right


    # If the second array is empty, then nothing needs

    # to be merged, and you can return the first array as the result

    if len(right) == 0:

        return left


    result = []

    index_left = index_right = 0


    # Now go through both arrays until all the elements

    # make it into the resultant array

    while len(result) < len(left) + len(right):

        # The elements need to be sorted to add them to the

        # resultant array, so you need to decide whether to get

        # the next element from the first or the second array

        if left[index_left] <= right[index_right]:

            result.append(left[index_left])

            index_left += 1

        else:

            result.append(right[index_right])

            index_right += 1


        # If you reach the end of either array, then you can

        # add the remaining elements from the other array to

        # the result and break the loop

        if index_right == len(right):

            result += left[index_left:]

            break


        if index_left == len(left):

            result += right[index_right:]

            break


    return result
    #print(result)

def merge_sort(array):

    # If the input array contains fewer than two elements,

    # then return it as the result of the function

    if len(array) < 2:

        return array


    midpoint = len(array) // 2


    # Sort the array by recursively splitting the input

    # into two equal halves, sorting each half and merging them

    # together into the final result

    return merge(

        left=merge_sort(array[:midpoint]),

        right=merge_sort(array[midpoint:]))

#alist = [54,26,93,17,77,31,44,55,20]

#print("results from merge sort")
#print(merge_sort(alist))



# Counting sort - a non comparison sort 

# Counting sort in Python programming
#https://www.programiz.com/dsa/counting-sort
#reviewed https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php also




#data = [4, 2, 2, 8, 3, 3, 1]
#countingSort(data)
#print("Sorted Array in Ascending Order: ")
#print(data)

# Python program for counting sort

# The main function that sort the given string arr[] in
# alphabetical order

#https://codezup.com/implementation-of-counting-sort-algorithm-in-python/

def counting_sort(array):


    maxValue = 0
    for i in range(len(array)):
        if array[i] > maxValue:
            maxValue = array[i]

    buckets = [0] * (maxValue + 1)

    for i in array:
        buckets[i] += 1

    i = 0
    for j in range(maxValue + 1):
         for _ in range(buckets[j]):
             array[i] = j
             i += 1

    return array


#Insertion sort - a simple comparison based sort
# code adapted from lectures






# Tim sort 

def insertion_sort(array, left=0, right=None):

    if right is None:

        right = len(array) - 1


    # Loop from the element indicated by

    # `left` until the element indicated by `right`

    for i in range(left + 1, right + 1):

        # This is the element we want to position in its

        # correct place

        key_item = array[i]


        # Initialize the variable that will be used to

        # find the correct position of the element referenced

        # by `key_item`

        j = i - 1


        # Run through the list of items (the left

        # portion of the array) and find the correct position

        # of the element referenced by `key_item`. Do this only

        # if the `key_item` is smaller than its adjacent values.

        while j >= left and array[j] > key_item:

            # Shift the value one position to the left

            # and reposition `j` to point to the next element

            # (from right to left)

            array[j + 1] = array[j]

            j -= 1


        # When you finish shifting the elements, position

        # the `key_item` in its correct location

        array[j + 1] = key_item


    return array



def timsort(array):

    min_run = 32

    n = len(array)


    # Start by slicing and sorting small portions of the

    # input array. The size of these slices is defined by

    # your `min_run` size.

    for i in range(0, n, min_run):

        insertion_sort(array, i, min((i + min_run - 1), n - 1))


    # Now you can start merging the sorted slices.

    # Start from `min_run`, doubling the size on

    # each iteration until you surpass the length of

    # the array.

    size = min_run

    while size < n:

        # Determine the arrays that will

        # be merged together

        for start in range(0, n, size * 2):

            # Compute the `midpoint` (where the first array ends

            # and the second starts) and the `endpoint` (where

            # the second array ends)

            midpoint = start + size - 1

            end = min((start + size * 2 - 1), (n-1))


            # Merge the two subarrays.

            # The `left` array should go from `start` to

            # `midpoint + 1`, while the `right` array should

            # go from `midpoint + 1` to `end + 1`.

            merged_array = merge(

                left=array[start:midpoint + 1],

                right=array[midpoint + 1:end + 1])


            # Finally, put the merged array back into

            # your array

            array[start:start + len(merged_array)] = merged_array


        # Each iteration should double the size of your arrays

        size *= 2


    return array
#print("results from tim sort")
#print(timsort(alist))
