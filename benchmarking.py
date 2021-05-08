#benchmarking

import time
import sorting_fucntions as sf
from random import randint
import numpy as np
import pandas as pd


global array

def random_array(n):
    #global array
    array = []
    for _ in range(0,n,1):
        array.append(randint(0 , 100))
        
    return array

#def random_array2(n):
    #array= np.random.randint(1,100, size=(1,n))

    #return array
#input_array = random_array(100)

num_runs =  10 #number of times to test the function
#results = [] # array to stroe results for each test


#benchmarking the function

def timer(algorithm,input_array):
    
    #for _ in range(num_runs):
        #random_array(100)
        # log the start time in seconds
        start_time = time.time()
        
        # call the function that you want to benchmark

        algorithm(input_array)
       

        #sf.merge_sort(array)

        #log the end time in seconds
        end_time = time.time()
        
        #calculate the elapsed time
        time_elapsed = end_time - start_time
        return time_elapsed
        
        #results.append(time_elapsed)

def main():

    input_sizes = [100,250,500]

    
    num_runs =  10

    bubble_list =[]
    temp_bubble_list = []

    for n in input_sizes:
        #print (n)
        #input_array = []
        input_array = random_array(n)
        #print(input_array) #testing to see if diff unsorted array created each time
        

        for _ in range(num_runs): #or number of runs
            #input_array = random_array(n)
                temp_bubble_list.append(timer(sf.bubble_sort,input_array))
            #print(temp_bubble_list)

        bubble_list.append(np.around(np.mean(temp_bubble_list)*1000,3))



        
            #print (n)
            #input_array = []
            
            #print(input_array) #testing to see if diff unsorted array created each time
        


       

    algorithm_df = pd.DataFrame()

    algorithm_df['Bubble Sort'] = bubble_list
    #algorithm_df["Merge Sort"] = merge_list

    return algorithm_df

def display_df():

    df = main()
    print(df.T)

if __name__ == "__main__":
    display_df()
