f i == 10:

   # for _ in range(10):
        input_array = random_array(100000)
        print(input_array)
        print(i)


        if i == 10:

            temp_bubble_list.append(timer(sf.bubble_sort,input_array))
            print(temp_bubble_list)
            temp_merge_list.append(timer(sf.merge_sort,input_array))
            print(temp_merge_list)
            i = 11
        
        bubble_list.append(np.around(np.mean(temp_bubble_list)*1000,3))
        merge_list.append(np.around(np.mean(temp_merge_list)*1000,3))




        ####




###

    for _ in range(num_runs): #or number of runs
    #input_array = random_array(n)
        for n in input_sizes:
            input_array = random_array(n)
        temp_bubble_list.append(timer(sf.bubble_sort,input_array))
    #print(temp_bubble_list)