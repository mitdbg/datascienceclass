import requests
import json
import argparse
import sys 
import pandas as pd
import numpy as np

# SUBMISSION SCRIPT, DO NOT MODIFY



def validate_submission_details():
    with open("submission_details.json", "r") as submission_file:
        data = json.load(submission_file)
        if data["submission_url"] == "<submission_url_posted_on_piazza>" or len(data["submission_url"]) < 10:
            print("Please change the submission url in submission_details.json to the one posted on piazza")
            sys.exit(1)
        if data["group_secret"] == "<your_group_secret>":
            print("Please change the group secret field in submission_details.json to one sent to you (or your teammate) by email")
            sys.exit(1)
        if len(data["group_secret"]) != 20:
            print("The group_secret field in submission_details.json does not have the correct length (it should be 20 chars long).")
            sys.exit(1)
        if data["team_name"] == "<your_team_name>" or len(data["team_name"]) == 0:
            print("Please add your team name in submission_details.json to a name of your choosing")
            sys.exit(1)

def validate_submitted_csv(test_output):
    df = pd.read_csv(test_output)
    if len(df.columns) != 2:
        print("Test output contains incorrect number of columns. There should be columns with headers \"id1\" and \"id2\" ") 
        sys.exit(1)
    if "id1" not in df.columns or "id2" not in df.columns:
        print("Incorrect header on test output, should have \"id1\" and \"id2\" headers on your csv")
        sys.exit(1)
    if (len(df) > 2000):
        print("Your submission is too large, your output should have no more than a few hundred rows")
        sys.exit(1)
    if df.dtypes["id1"] != np.int64 or df.dtypes["id2"] != np.int64:
        print('incorrect column types')
        sys.exit(1)


def main(args):
    validate_submission_details()
    validate_submitted_csv(args.test_file)
    with open(args.test_file, "rb") as test_f, open("submission_details.json", "r") as submission_file:
        submit_data = json.load(submission_file)
        payload =  test_f.read()
        params = {"group_secret": submit_data["group_secret"], "team_name" : submit_data["team_name"]}
        r = requests.put(url=submit_data["submission_url"], params= params, data=payload)
        print(r.text)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("test_file", help="file containing test matches (test_output.csv)")
    main(parser.parse_args())
