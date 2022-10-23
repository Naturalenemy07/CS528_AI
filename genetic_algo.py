from mimetypes import init
import numpy as np
import gen_chrom as gc
import random

distance_array = np.array([[0,25.1,21.9,31.7,45.4],[25.1,0,44.9,18,68.6],[21.9,44.9,0,50.7,27.7],[31.7,18,50.7,0,74.4],[45.4,68.6,27.7,74.4,0]])
mut_rate = 0.05
init_pop_size = 10

# initiate global variable for sub population, build structured array (chromosome, fitness)
dtype=[('chrom', np.ndarray),('fit', np.float32)]
# initialize first chromosome, assign a fitness of 0.0
sub_pop = np.array([(gc.gen_permtx(5), 0.0)], dtype=dtype)
arr_size = distance_array.shape[0]

def gen_pop(num):
    global sub_pop
    '''
    This function generates a structured array of size "num", that contains a chromosome and fitness score initialized to 0.0.  Calls upon gen_chrom (gc)
    to generate the permutation matrices (chromosome).  Returns the completed sub population containing "num" number of chromosomes. 
    '''    
    # append new (chromosome, fitness) to the sub_pop structured array, will total to "num" number of chromosome-fitness pairs
    # does not check for identical chromosomes, not too concerned with "twins"
    for i in range(num-1):
        sub_pop = np.append(sub_pop, np.array([(gc.gen_permtx(arr_size), 0.0)],dtype=dtype))
        
    return sub_pop

def row_swap(arr1, arr2):
    pass

def fitness_function(chrom):
    '''
    This function takes the chromosome and returns the total distance travelled
    '''
    dist = 0
    for row in range(0,arr_size-1):
        # returns position "1" in row
        dis_row = int(np.where(chrom[row]==1)[0])
        dis_col = int(np.where(chrom[row+1]==1)[0])
        dist_int = distance_array[dis_row][dis_col]
        dist += dist_int
    return "{:.1f}".format(dist)

def selection():

    pass

def crossover():
    pass

def mutate(rate,chrom):
    mut_int = int(rate*100)
    num_sel = random.randint(0,100)
    
    # if number is less than mutation, swap, if not pass
    if num_sel <= mut_int:
        # select row
        row1 = random.randint(0,arr_size-1)
        row2 = random.randint(0,arr_size-1)
        while row2 == row1:
            row2 = random.randint(0,arr_size-1)

        #swap row in array
        chrom[[row1,row2]] = chrom[[row2,row1]]
    
    return chrom

###########################
#### Genetic Algorithm ####
###########################

# generate population
subpop = gen_pop(init_pop_size)

# get fitness for each chromosome
for i in range(0, subpop.size):
    subpop[i]['fit'] = fitness_function(subpop[i]['chrom'])

# go through all in population, apply mutation
for i in range(0,subpop.size):
    subpop[i]['chrom'] = mutate(mut_rate, subpop[i]['chrom'])
