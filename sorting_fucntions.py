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






# Counting sort - a non comparison sort 







#Insertion sort - a simple comparison based sort

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


