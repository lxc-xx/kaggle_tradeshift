#!/usr/bin/env python
import sys
import numpy as np

LABEL_SIZE = 33

def main(argv):
    if len(argv) != 1:
        print "Usage: make_submission.py pred_folder"
        sys.exit(1)
    
    sub_array = []
    for i in range(1, LABEL_SIZE+1):
        sub_array.append(np.load(argv[0]+"/"+str(i)+ ".npy").tolist())


    print "id_label,pred"
    for i in range(len(sub_array[0])):
        for l in range(LABEL_SIZE):
            print str(1700000+i+1) + "_y" + str(l+1) + "," + str(sub_array[l][i])

if __name__ == "__main__":
    main(sys.argv[1:])
