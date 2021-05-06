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
    print(arr)
    #return arr 

#print(arr)
arr = [12,3,6]
sort(arr)





## Merge sort - efficient comparison based sort






# Counting sort - a non comparison sort 







#Insertion sort - a simple comparison based sort








# Heap sort 


