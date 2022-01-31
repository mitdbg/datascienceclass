import sqlite3 as sql
import pandas as pd
import argparse

def runSQL(query_num):
	with sql.connect("lab1.sqlite") as conn, open("queries/q{}.sql".format(query_num)) as in_query:
		cur = conn.cursor()
		df = pd.read_sql_query(in_query.read(), conn)
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
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", "-q", help="Run a specific query", type=int)
    args = parser.parse_args()

    queries = range(1, 11)
    if args.query != None:
        queries = [args.query]
    for query in queries:
        print("\nQuery {}".format(query))
        if query <= 6:
            print("\nPandas Output")
            print(pandas_queries[query-1]())
        print("\nSQLite Output")
        df = runSQL(query)
        print(df)