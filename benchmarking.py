#benchmarking

import time
import sorting_fucntions as sf
from random import randint


def random_array(n):
    array = []
    for _ in range(0,n,1):
        array.append(randint(0 , 100))
    return array

array = random_array(100000)

#log the start time in seconds
start_time = time.time()

#call the function that you want to benchmark


#log the end time in seconds
end_time = time.time()


#calculate the elapsed time in seconds
time_elapsed = end_time - start_time

## example below note time has already been imported

num_runs =  10 #number of times to test the function
results = [] # array to stroe results for each test


#benchmarking the function



for r in range(num_runs):
    # log the start time in seconds
    start_time = time.time()
    
    # call the function that you want to benchmark
    
    sf.merge_sort(array)

    #log the end time in seconds
    end_time = time.time()
    
    #calculate the elapsed time
    time_elapsed = end_time - start_time
    
    results.append(time_elapsed)

    print(time_elapsed)