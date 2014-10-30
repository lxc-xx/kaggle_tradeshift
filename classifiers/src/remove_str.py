#!/usr/bin/env python

import sys

with open(sys.argv[1], 'r') as feat_type_file:
    feat_type = [line.rstrip('\n') for line in feat_type_file]


    with open(sys.argv[2], 'r') as feat_file:
        print feat_file.readline().rstrip('\n')
        for line in feat_file:
            datum = line.rstrip('\n').split(',')
            output = []
            for idx in range(len(datum)):
                if idx == 0:
                    output.append(datum[idx])
                elif feat_type[idx] == "NUM":
                    output.append(datum[idx])
                elif feat_type[idx] == "BIN":
                    if datum[idx] == "YES":
                        output.append("1.0");
                    else:
                        output.append("0.0");
                else:
                    output.append("0.0");
            print ','.join(output)
