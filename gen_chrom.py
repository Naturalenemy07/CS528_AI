import random
import numpy as np

def gen_permtx(length):
    # generate positions of non zero integer randomly with no duplicates
    poslist = random.sample(range(length),length)

    # generate length X length numpy array filled with zeros
    blank_nar = np.zeros((length,length), dtype=int)

    # iterate through blank_nar, changing a zero to a one using poslist as position of change at reach row
    for row in range(0,length):
        blank_nar[row,poslist[row]]=1

    return blank_nar
