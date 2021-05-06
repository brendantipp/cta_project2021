#The five sorting fucntions i have selected are as follows





# Bubble sort - simple comparison based sort
#code as per lectures

def sort(arr):
    n = len(arr)
    for outer in range(n-1, 0, -1):
        for inner in range(0,outer,1):
            if arr[inner] > arr[inner+1]:
                temp = arr[inner]
                arr[inner] = arr[inner+1]
                arr[inner+1] = temp
    print("results from Bubble sort")
    print(arr)
    #return arr 

#print(arr)
arr = [12,3,6]
sort(arr)





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

alist = [54,26,93,17,77,31,44,55,20]

print("results from merge sort")
print(merge_sort(alist))



# Counting sort - a non comparison sort 







#Insertion sort - a simple comparison based sort
# code adapted from lectures

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print("results from insertion sort")
print(alist)







# Heap sort 


