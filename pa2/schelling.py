#  CS121: Schelling Model of Housing Segregation
#
#   Ravi Bakhai & Spencer Ho
#
#   Program for simulating of a variant of Schelling's model of
#   housing segregation.  This program takes four parameters:
#
#    filename -- name of a file containing a sample grid
#
#    R - The radius of the neighborhood: home (i, j) is in the
#        neighborhood of home (k,l) if |k-i| + |l-j| <= R.
#
#    threshold - minimum acceptable threshold for ratio of neighbor
#    value to the total number of homes in his neighborhood.
#
#    max_steps - the maximum number of passes to make over the
#    neighborhood during a simulation.
#
#  Sample use: python3 schelling.py tests/sample-grid.txt 1 0.51 3
#

import os
import sys
import utility

def is_satisfied(grid, R, threshold, location):

    '''
    Is the homeowner at the specified location satisfied?
   
    Inputs:
        grid: (list of lists of strings) the grid 
        R: (int) radius for the neighborhood
        threshold: (float) satisfaction threshold
        location: (int, int) a grid location

    Returns:
        True, if the location's neighbor score is at or above the threshold
    '''
    
    x = location[0]
    y = location[1]
    own_color = grid[x][y]
    n = []
    s = 0
    p = 0
    total_homes = 0
    a = R
    b = -R
    c = R 
    d = -R
    if (x + R) >len(grid):
        a = a + (len(grid) - (x + R))
    if (x - R) < 0:
        b = b - (x - R)
    if (y + R) >len(grid):
        c = c + (len(grid) - (y + R))
    if (y - R) < 0:
        d = d - (y - R) 
    e = max(0, min(a, abs(d)) - 1)
    f = max(0, min(abs(b), c) - 1)

    for i in range(x + b, x + a + 1):
        if i != x
            total_homes = total_homes + 1
            if own_color == grid[i][y]:
                s = s + 1
            if grid[i][y] == "O":
                p = p + 1        
    for j in range(y + d, y + c + 1):
        if j != y
            total_homes = total_homes + 1
            if own_color == grid[x][j]:
                s = s + 1
            if grid[x][j] == "O":
                p = p + 1
    for k in range(max(b, d), min(a, c) + 1):
        if (x + k != x) and (y + k != y)
            total_homes = total_homes + 1
            if own_color == grid[x + k][y + k]:
                s = s + 1
            if grid[x + k][y + k] == "O":
                p = p + 1  
    for l in range(e, f + 1):
        if (x + k != x) and (y + k != y)  
            total_homes = total_homes + 1      
            if own_color == grid[x + l][y + l]:
                s = s + 1
            if grid[x + l][y - l] == "O":
                p = p + 1               
    satisfaction_thresh = (s + (p / 2)) / (total_homes)
    print(a, b, c, d, e, f, satisfaction_thresh)
    if satisfaction_thresh >= threshold:
        return True
    else:                    
        return False            
                      

        
def open_locations(grid, R, location):

    '''
    Determines the list of open locations in the given neighborhood based on 
    orginal location.
    
    Inputs:
        grid: (list of lists of strings) the grid
        R: (int) radius for the neighborhood
        location: the inputed location coordinates
    
    Returns: 
        returns the o which is the list of open locations within
        the neighborhood
    '''

    o = [] #openlist
    a = list_neighbors(grid, R, location)
    for i in a:
        if grid[i[0]][i[1]] =="O":
            o.append(a)
    return o  

def open_locations_original(grid):

    '''
    Determines the list of open locations across the entire grid.
    
    Inputs:
        grid: (list of lists of strings) the grid
    
    Returns:
        returns o which is the list of open homes in the entire grid
    '''

    o = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "O":
                o.append((i, j))
    return o  

def unsatisfied_locations_total(grid, R, threshold):

    '''
    Determines the full list of unsatisfied homes across the entire grid.
    
    Inputs:
        grid: (list of lists of strings) the grid
        R: (int) radius for the neighborhood
        threshold: (float) satisfaction threshold
    
    Returns:
        returns unsatisfied which is the list of unsatisfied homes in the
        grid
    '''

    unsatisfied = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != "O" and is_satisfied(grid, R, threshold, (i, j)) == False:
                unsatisfied.append((i, j))
    return unsatisfied            

def unsatisfied_locations(grid, R, threshold, location):

    '''
    Determines the list of unsatisfied homes within a given neighborhood

    Inputs: 
        grid: (list of lists of strings) the grid
        R: (int) radius for the neighborhood
        threshold: (float) satisfaction threshold
        location: the inputed location coordinates

    Returns:
        returns unsatisfied_list which is the list of unsatisfied homes
        in a given neighborhood
    '''

    unsatisfied_list = []
    a = list_neighbors(grid, R, location)
    for i in a:
        if grid[i[0]][i[1]] != "O" and is_satisfied(grid, R, threshold, i) == False:
            unsatisfied_list.append(i)
    return unsatisfied_list

def relocation(grid, R, threshold, location, open_homes):

    '''
    Determines if home owner relocates, and then updates the list.

    Inputs:
        grid: (list of lists of strings) the grid
        R: (int) radius for the neighborhood
        threshold: (float) satisfaction threshold
        open_homes: The list of open_homes

    Returns:
        True or False 
    '''

    relocation_coor = []
    color = grid[location[0]][location[1]] 
    for new_home in open_homes:   
        grid[new_home[0]][new_home[1]] = color
        grid[location[0]][location[1]] = "O"
        if is_satisfied(grid, R, threshold, new_home) == True:
            open_homes.remove(new_home)
            open_homes.insert(0, location)
            return True
        else:
            grid[location[0]][location[1]] = grid[new_home[0]][new_home[1]]
            grid[new_home[0]][new_home[1]] = "O"
    return False


def one_iteration(grid, R, threshold, open_homes):

    '''
    Runs one iteration of the simulation.

    Inputs:
        grid: (list of lists of strings) the grid
        R: (int) radius for the neighborhood
        threshold: (float) satisfaction threshold
        open_homes: The list of open_homes

    Returns:
        True or False
    '''

    unsatisfied_l = unsatisfied_locations_total(grid, R, threshold)
    iterations = 0
    for unsatisfied_neighbor in unsatisfied_l:
        if is_satisfied(grid, R, threshold, unsatisfied_neighbor) == False:
            if relocation(grid, R, threshold, unsatisfied_neighbor, open_homes) == True:
               iterations = iterations + 1
    if iterations > 0:
        return True
    else:
        return False       
     

def do_simulation(grid, R, threshold, max_steps):

    '''
    Do a full simulation.

    Inputs:
        grid: (list of lists of strings) the grid
        R: (int) radius for the neighborhood
        threshold: (float) satisfaction threshold
        max_steps: (int) maximum number of steps to do

    Returns:
        The function number of steps executed.
    '''  

    open_homes = open_locations_original(grid)
    for i in range(max_steps):
        if one_iteration(grid, R, threshold, open_homes) == False:
            return i + 1
    return max_steps        



            




    assert utility.is_grid(grid), ("The grid argument has the wrong type.  "
                                   "It should be a list of lists of strings "
                                   "with the same number of rows and columns")

    # YOUR CODE HERE
    # REPLACE 0 with an appropriate return value
    return 0


def go(args):
    '''
    Put it all together: parse the arguments, do the simulation and
    process the results.

    Inputs:
        args: (list of strings) the command-line arguments
    '''

    usage = "usage: python schelling.py <grid file name> <R > 0> <0 < threshold <= 1.0> <max steps >= 0>\n"
    grid = None
    threshold = 0.0
    R = 0
    max_steps = 0
    MAX_SMALL_GRID = 20

    if (len(args) != 5):
        print(usage)
        sys.exit(0)

    # parse and check the arguments
    try:
        grid = utility.read_grid(args[1])

        R = int(args[2])
        if R <= 0:
            print("R must be greater than zero")
            sys.exit(0)

        threshold = float(args[3])
        if (threshold <= 0.0 or threshold > 1.0):
            print("threshold must satisfy: 0 < threshold <= 1.0")
            sys.exit(0)

        max_steps = int(args[4])
        if max_steps <= 0:
            print("max_steps must be greater than or equal to zero")
            sys.exit(0)

    except:
        print(usage)
        sys.exit(0)

    num_steps = do_simulation(grid, R, threshold, max_steps)
    if len(grid) < MAX_SMALL_GRID:
        for row in grid:
            print(row)
    else:
        print("Result grid too large to print")

    print("Number of steps simulated: " + str(num_steps))


if __name__ == "__main__":
    go(sys.argv)
