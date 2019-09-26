import pandas as pd
import argparse
import sklearn as skl
import score
import os

# You can add functions, and imports as neccesary for your ER algorithm
# you may find the scoring code useful for training and running locally

def run(directory):
    r1 = pd.read_csv(os.path.join(directory, "retailer1.csv"))
    r2 = pd.read_csv(os.path.join(directory, "retailer2.csv"))
    # TODO: This function should produce a csv file in the lab_3
    # directory using the name given by the follwing variable
    # e.g. "test_output.csv" for the test set. with the same format 
    # as data/train/matches.csv including the header
    # Please do not modify the output_filename
    output_filename = "test_output.csv"


def train(directory):
    train_matches = pd.read_csv(os.path.join(directory, "matches.csv"))
    r1 = pd.read_csv(os.path.join(directory, "retailer1.csv"))
    r2 = pd.read_csv(os.path.join(directory, "retailer2.csv"))
    
    # TODO: This function should produce a csv file in the lab_3
    # directory named train_output.csv with the same format 
    # as data/train/matches.csv including the header
    # Please do not modify the output_filename
    output_filename = "train_output.csv"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_directory")
    parser.add_argument("--train", action="store_true")
    args = parser.parse_args()
    if args.train:
        train(args.input_directory)
    else:
        run(args.input_directory)



