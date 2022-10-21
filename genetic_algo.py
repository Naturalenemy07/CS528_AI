import numpy as np
import gen_chrom as gc

distance_array = np.array([[0,25.1,21.9,31.7,45.4],[25.1,0,44.9,18,68.6],[21.9,44.9,0,50.7,27.7],[31.7,18,50.7,0,74.4],[45.4,68.6,27.7,74.4,0]])
def gen_pop(num):
    '''
    This function generates a structured array of size "num", that contains a chromosome and fitness score initialized to 0.0.  Calls upon gen_chrom (gc)
    to generate the permutation matrices (chromosome).  Returns the completed sub population containing "num" number of chromosomes. 
    '''
    # build structured array (chromosome, fitness)
    dtype=[('chrom', np.ndarray),('fit', np.float32)]
    
    # initialize first chromosome, assign a fitness of 0.0
    sub_pop = np.array([(gc.gen_permtx(5), 0.0)], dtype=dtype)
    
    # append new (chromosome, fitness) to the sub_pop structured array, will total to "num" number of chromosome-fitness pairs
    # does not check for identical chromosomes, not too concerned with "twins"
    for i in range(num-1):
        sub_pop = np.append(sub_pop, np.array([(gc.gen_permtx(5), 0.0)],dtype=dtype))
        
    return sub_pop


def fitness_function(chrom):
    '''
    This function takes the chromosome and returns the total distance travelled
    '''
    dist = 0
    for row in range(0,4):
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

def mutate():
    pass
