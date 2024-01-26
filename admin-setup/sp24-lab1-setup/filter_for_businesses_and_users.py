import pandas as pd

import json
import sqlite3

def get_id_set(file):
    ids = set()
    with open(file, 'r') as f:
        for line in f:
            ids.add(line.strip())
    
    return ids


def filter_for_ids(file, ids, key):
    rows = []
    with open(file, 'r') as f:
        for idx, line in enumerate(f):
            if idx % 10000 == 0:
                print(f"file {file} -- row {idx}")

            row = json.loads(line)
            if key == 'user_id':
                row['num_friends'] = 0 if row['friends'] == "" else len(row['friends'].split(','))
                row.pop('friends')

            if row[key] in ids:
                rows.append(row)

    return rows


if __name__ == "__main__":
    # get first 10k business and user ids
    business_ids = get_id_set('yelp_business_ids_10k.txt')
    user_ids = get_id_set('yelp_user_ids_10k.txt')

    # iterate over businesses and users to filter for rows
    print("filtering business, user rows")
    business_rows = filter_for_ids('yelp_academic_dataset_business.json', business_ids, key='business_id')
    user_rows = filter_for_ids('yelp_academic_dataset_user.json', user_ids, key='user_id')

    # construct dataframes
    print("creating business, user dataframes")
    business_df = pd.DataFrame(business_rows)
    user_df = pd.DataFrame(user_rows)

    # read reviews into dataframe
    print("creating reviews dataframe")
    reviews = []
    with open('yelp_reviews_10k.json', 'r') as f:
        for line in f:
            reviews.append(json.loads(line))

    reviews_df = pd.DataFrame(reviews)

    # write dataframes to parquet
    print("writing dataframes")
    business_df.to_parquet("business_10k.pq", index=False)
    user_df.to_parquet("user_10k.pq", index=False)
    reviews_df.to_parquet("reviews_10k.pq", index=False)

    # convert columns to be valid for sqlite
    business_df.loc[:, 'attributes'] = business_df.attributes.apply(lambda d: json.dumps(d))
    business_df.loc[:, 'hours'] = business_df.hours.apply(lambda d: json.dumps(d))

    # write dataframes to sqlite
    print("writing sql db")
    con = sqlite3.connect("yelp_reviews_10k.db")
    business_df.to_sql(name="businesses", con=con, if_exists='append')
    user_df.to_sql(name="users", con=con, if_exists='append')
    reviews_df.to_sql(name="reviews", con=con, if_exists='append')
