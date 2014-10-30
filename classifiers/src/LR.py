#!/usr/bin/env python

import sys
import os
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression

def main(argv):
    if len(argv) != 5:
        print "./LR.py train.npy train_lable.npy test.npy save_folder label_idx"
        sys.exit(1);

    output_folder = argv[3]
    label_idx = int(argv[4])

    os.system("mkdir " + output_folder)

    print "Loading training data"
    train_array = np.load(argv[0])
    print "Loading training label"
    train_label_array = np.load(argv[1])
    print "Loading test data"
    test_array = np.load(argv[2])
    
    print "building LR on label " + str(label_idx)
    lr = LogisticRegression()
    model = lr.fit(train_array[:, 1:], train_label_array[1:, label_idx]) 

    print "predicting label " + str(label_idx)
    nb_pred = lr.predict(test_array[:,1:])
    print "save the result"
    with open(output_folder + "/" + str(label_idx) + ".pred", 'w') as pred_file:
        pred_file.write("\n".join([ str(x) for x in nb_pred.tolist()]))
    with open(output_folder+"/"+str(label_idx) + ".npy", 'wb') as npy_file:
        np.save(npy_file, nb_pred)

if __name__ == "__main__":
    main(sys.argv[1:])
