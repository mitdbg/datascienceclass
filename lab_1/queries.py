import sqlite3 as sql
import pandas as pd
import argparse

def runSQL(query_num, store):
    with sql.connect("data/yelp_reviews_10k.db") as conn, open("queries/q{}.sql".format(query_num)) as in_query:
        df = pd.read_sql_query(in_query.read(), conn)
        pd.set_option('display.max_rows', 100)
        if store: df.to_csv(f"submission/sql_sol{query_num}.csv", index=False)
        return df

def Q1Pandas():
    """
    TODO: Write your Pandas query here, return a dataframe to answer the question
    """
    return None

def Q2Pandas():
    """
    TODO: Write your Pandas query here, return a dataframe to answer the question
    """
    return None

def Q3Pandas():
    """
    TODO: Write your Pandas query here, return a dataframe to answer the question
    """
    return None

def Q4Pandas():
    """
    TODO: Write your Pandas query here, return a dataframe to answer the question
    """
    return None

def Q5Pandas():
    """
    TODO: Write your Pandas query here, return a dataframe to answer the question
    """
    return None

def Q6Pandas():
    """
    TODO: Write your Pandas query here, return a dataframe to answer the question
    """
    return None

pandas_queries = [Q1Pandas, Q2Pandas, Q3Pandas, Q4Pandas, Q5Pandas, Q6Pandas]
df = None
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", "-q", help="Run a specific query", type=int)
    parser.add_argument("--store", "-s", help="Store", default=False, action='store_true')
    args = parser.parse_args()

    store = args.store

    queries = range(1, 11)
    if args.query != None:
        queries = [args.query]
    for query in queries:
        print("\nQuery {}".format(query))
        if query <= 6:
            print("\nPandas Output")
            df = pandas_queries[query-1]()
            print(df)
            if store: df.to_csv(f"submission/pandas_sol{query}.csv", index=False)
        print("\nSQLite Output")
        df = runSQL(query, store)
        print(df)