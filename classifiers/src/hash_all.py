#!/usr/bin/env python

import sys
import numpy as np

D = 2**20

with open(sys.argv[1], 'r') as feat_type_file:
    feat_type = [line.rstrip('\n') for line in feat_type_file]

    
    feats = np.load(sys.argv[2])

    hash_str_feats = []
    idx = 0
    for feat in feats[1:]:
        hash_str_feat = [0] * len(feat)
        hash_str_feat[0] = int(feat[0])

        for i in range(1,len(feat)):
            hash_str_feat[i] = hash(feat[i])%D

        hash_str_feats.append(hash_str_feat)
        idx += 1
        print idx

    
    with open(sys.argv[3],'wb') as feat_npy: 
        np.save(feat_npy, np.array(hash_str_feats))
