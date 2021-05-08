import time
import sorting_fucntions as sf
from random import randint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def random_array(n):
    #global array
    array = []
    for _ in range(0,n,1):
        array.append(randint(0 , 100))
        
    return array


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
    global input_sizes
    #input_sizes = [100,250]
    input_sizes = [100,200,300,500]
    #input_sizes = [100,250,500,750,1000,1250,2500]
    
    #input_sizes = [100,250,500,750,1000,1250,2500,3750,5000,6250,7500,8750,10000]
    
    num_runs =  10

    #create empty arrays to hold the values of each sorting result (code below for visuals)
    # https://stackoverflow.com/questions/2402646/python-initializing-multiple-lists-line
    bubble_results, merge_results,counting_results, insertion_results,timsort_results = ([] for i in range(5))

    for n in input_sizes:
    #for _ in range(num_runs):
        #input_array = random_array(n)
        
        print(n)
        #i = 1
      
        temp_bubble_results, temp_merge_results,temp_counting_results,temp_insertion_results, temp_timsort_results = ([] for i in range(5))


        for _ in range(num_runs):
        #for n in input_sizes:
            #print(n)

            temp_bubble_results.append(timer(sf.bubble_sort,random_array(n)))
            print(temp_bubble_results)
            temp_counting_results.append(timer(sf.counting_sort,random_array(n)))
            temp_insertion_results.append(timer(sf.insertion_sort,random_array(n)))
            temp_timsort_results.append(timer(sf.timsort,random_array(n)))
            temp_merge_results.append(timer(sf.merge_sort,random_array(n)))
            
          
        bubble_results.append(np.around(np.mean(temp_bubble_results)*1000/10,3))
        #print(bubble_results)
        counting_results.append(np.around(np.mean(temp_counting_results)*1000/10,3))
        insertion_results.append(np.around(np.mean(temp_insertion_results)*1000/10,3))
        timsort_results.append(np.around(np.mean(temp_timsort_results)*1000/10,3))
        merge_results.append(np.around(np.mean(temp_merge_results)*1000/10,3))
        
        
    algorithm_df = pd.DataFrame()
    algorithm_df['Size'] = input_sizes
    algorithm_df['Bubble Sort'] = bubble_results
    algorithm_df['Merge Sort'] = merge_results
    algorithm_df['Counting Sort'] = counting_results
    algorithm_df['Insertion Sort'] = insertion_results
    algorithm_df['Tim Sort'] = timsort_results

#set array size as index for tabel for display purposes
    algorithm_df.set_index("Size", inplace = True)

    return algorithm_df

def print_df():

    df = main()
    print(df.T)


    #plot graph of results
    plt.figure(figsize=(15,10))
    plt.plot(df.index,df['Bubble Sort'],label = "Bubble Sort")
    plt.plot(df.index,df['Merge Sort'],label = "Merge Sort")
    plt.plot(df.index,df['Counting Sort'],label = "Counting Sort")
    plt.plot(df.index,df['Insertion Sort'],label = "Insertion Sort")
    plt.plot(df.index,df['Tim Sort'],label = "Selction Sort")

    #input_sizes = df.T._columns
    #val_max = int(df.values.max())

    plt.title("Alogrithms Benchmarking")
    plt.xlabel("Input Size n")
    plt.ylabel("Running Time")

    plt.show()





if __name__ == "__main__":
    print_df()