from __future__ import print_function, division
import argparse
import csv
import pandas

def main(args):
    df = pandas.read_csv(args.csvFile, index_col=None, header=None)
    needed = df[df[32].isnull()==False].iloc[:, [1,4,32,49]] 
    state = df.loc[0, 1]
    geo_and_dist = []
    for idx, row in needed.iterrows():
        geo_and_dist.append([row.iloc[1], int(row.iloc[2]), row.iloc[3]])
    df = pandas.read_csv("e20171{}0002000.txt".format(state.lower()), index_col=None, header=None)
    for x in geo_and_dist:
        x.append(df[x[0] == df.loc[:, 5]].iloc[0, 6])
    for x in geo_and_dist:
        print(",".join([str(i) if type(i) != str else '"'+i+'"' for i in [state]+x[1:]]))
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csvFile")
    args = parser.parse_args()
    main(args)
