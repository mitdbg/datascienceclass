from __future__ import print_function, division
import pandas as pd
import argparse
from collections import defaultdict


def precision(tp, fp):
    if (tp+fp) == 0:
        return 0.0
    return tp/(tp+fp)

def recall(tp, fn):
    if (tp+fn) == 0:
        return 0.0
    return tp/(tp+fn)

def f1score(p,r):
    if (p+r) == 0:
        return 0.0
    return 2*(p*r)/(p+r)

def get_stats(gt, test):
    tp = 0
    fn = 0
    fp = 0
    for id1 in gt:
        for id2 in gt[id1]:
            if id1 in test and id2 in test[id1]:
                tp += 1
            else:
                fn += 1
    for id1 in test:
        for id2 in test[id1]:
            if id1 not in gt or id2 not in gt[id1]:
                fp += 1
    return tp, fn, fp

def parse_file(fname):
    out_dict = defaultdict(set)
    in_data = pd.read_csv(fname)
    for _, row in in_data.iterrows():
        out_dict[row["id1"]].add(row["id2"])
    return out_dict

def main(args):
    gt = parse_file(args.ground_truth)
    test = parse_file(args.input_data)
    tp, fn, fp = get_stats(gt, test)
    p = precision(tp, fp)
    r = recall(tp, fn)
    f1 = f1score(p, r)
    print("Precision: {}".format(p))
    print("Recall   : {}".format(r))
    print("F1 Score : {}".format(f1))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ground_truth", type= str)
    parser.add_argument("input_data", type=str)
    main(parser.parse_args())

