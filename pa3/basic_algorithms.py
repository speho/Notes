# Ravi Bakhai and Spencer Ho
# PA 3
# 10/21/16
# CS121: Analyzing Election Tweets
# Part 1

from util import sort_count_pairs

def find_top_k(items, k):
    '''
    Find the K most frequently occuring items

    Inputs:
        items: a list of items
        k: integer 

    Returns: sorted list of K tuples
    '''

    k_library = {}
    for i in items:
        item = k_library.get(i, 0)
        k_library[i] = item + 1
    highest_to_lowest = sort_count_pairs(list(k_library.items()))
    return highest_to_lowest[0:k]    

    items_dict = {}

    for i in range(len(items)):
        values = items[i]
        v = items_dict.get[values, 0]
        items_dict[values] = v + 1
    return list(items_dict.items())
    


    # YOUR CODE HERE
    # REPLACE RETURN VALUE WITH AN APPROPRIATE VALUE

    # YOUR CODE HERE
    # REPLACE RETURN VALUE WITH AN APPROPRIATE VALUE



def find_min_count(items, min_count):
    '''
    Find the items that occur at least min_count times

    Inputs:
        items: a list of items    
        min)count: integer
        
    Returns: sorted list of tuples
    '''

    k_library = {}
    made_the_cut = []
    for i in items:
        item = k_library.get(i, 0)
        k_library[i] = item + 1
    for j in k_library:
        if k_library[j] >= min_count:
            made_the_cut.append((j, k_library[j]))
    made_the_cut = sort_count_pairs(made_the_cut)
    return made_the_cut
 
def find_frequent(items, k):
    '''
    Find items where the number of times the item occurs is at least
    fraction * len(items).

    Input: 
        items: list of items
        k: integer

    Returns: sorted list of tuples
    '''

    k_library = {}
    for i in items:
        if i in k_library:
            k_library[i] = k_library[i] + 1
        elif (len(k_library) + 1) <= k - 1:
            k_library[i] = 1
        else:
            reject = []
            for j in k_library:
                k_library[j] = k_library[j] - 1
                if k_library[j] == 0:
                    reject.append(j)
            for r in reject:
                del k_library[r]

    return sort_count_pairs(k_library.items())

