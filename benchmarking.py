#benchmarking

import time
import sorting_fucntions as sf
from random import randint



def random_array(n):
    array = []
    for i in range(0,n,1):
        array.append(randint(0 , 100))
        
    return array

print(random_array(100))

#input_array = random_array(100)

num_runs =  10 #number of times to test the function
results = [] # array to stroe results for each test


#benchmarking the function

def timer(algorithm,array):
    
    for r in range(num_runs):
        random_array(100)
        # log the start time in seconds
        start_time = time.time()
        
        # call the function that you want to benchmark

        algorithm(array)
       

        #sf.merge_sort(array)

        #log the end time in seconds
        end_time = time.time()
        
        #calculate the elapsed time
        time_elapsed = end_time - start_time
        
        results.append(time_elapsed)
        print("run",r)
        print(time_elapsed)



timer(sf.bubble_sort,array)

