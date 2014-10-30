#!/usr/bin/env python
import sys
import numpy as np

def main(argv):
    if len(argv) != 2:
        print "Usage: csv2npy.py csv_file npy_file"
        sys.exit(1)

    csv_array = []
    idx = 0
    with open(argv[0], 'r') as csv_file:
        for line in csv_file:
            csv_array.append([str(x) for x in line.rstrip('\n').split(',')])
            idx += 1
            print idx

    csv_array = np.array(csv_array)
    
    np.save(argv[1], csv_array)




if __name__ == "__main__":
    main(sys.argv[1:])
