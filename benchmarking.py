#benchmarking

import time
import sorting_fucntions as sf
from random import randint
import numpy as np
import pandas as pd
import copy

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



#global input_sizes





def sort(algorithm):

    #input_sizes = [100,250,500,750,1000,1250,2500,3750,5000,6250,7500,8750,10000]
    global input_sizes
    global results
    #input_sizes =[100,250,500,750,1000,1250,2500]
    input_sizes = [10,20,30,300]
    

    num_runs =  11

    #https://stackoverflow.com/questions/2402646/python-initializing-multiple-lists-line

    results = []
    

    
        #input_array = random_array(n)
        
        
        #print(temp_bubble_list)
    
    
    
        #print(n)
    
    for n in input_sizes:
        i = 1
        temp_list = []
        while i < num_runs:
        #for _ in range(num_runs): #or number of runs
        
            print (n)
            #input_array = []
            input_array = random_array(n)
            #print(input_array) #testing to see if diff unsorted array created each time
            temp_list.append(timer(algorithm,input_array))
            #print(temp_list)
            i += 1



        results.append(np.around(np.mean(temp_list)*1000,3))
        return results 


    #algorithm_df = pd.DataFrame()
    #algorithm_df['Input_Size'] = input_sizes

    #algorithm_df['Bubble Sort'] = results

    #algorithm_df["Merge Sort"] = merge_list

    #return algorithm_df

   

def main():     

    sort(sf.bubble_sort)


def display_df():

    bubble_sort_r = sort(sf.bubble_sort)

    output = pd.DataFrame(bubble_sort_r,sort, input_sizes)

    return output

#def display_df2():

    #df = main()
    #print(df.T)

if __name__ == "__main__":
    display_df()



####
        for _ in range(num_runs):
        #for _ in range(num_runs): #or number of runs
            #input_array = random_array(n)
            #print(input_array)                     
            temp_bubble_results.append(timer(sf.bubble_sort,random_array(n)))
            #print(temp_bubble_results)
            #print(input_array) 
            #input_array = random_array(n)
            #print(input_array) 


####