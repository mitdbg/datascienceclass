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

    # drop review_count columns and rename business `stars` -> `avg_rating` to avoid confusion
    business_df.drop(columns='review_count', inplace=True)
    user_df.drop(columns='review_count', inplace=True)
    business_df.rename(columns={'stars': 'avg_rating'}, inplace=True)

    # add a table for outer join question; contains fake data of Matt's favorite restaurants
    # columns: business_id, name, state, my_stars
    # -------------------------------------------
    # first get restaurants in Illinois (fewest in any state)
    illinois_restaurant_df = business_df[
        (business_df.state == 'IL')
        & business_df.categories.str.contains('restaurant', case=False)
    ].copy()

    # then subsample restaurants deterministically; these rows will
    # join with businesses table; create fake values for my_stars
    sub_illinois_restaurant_df = illinois_restaurant_df[['business_id', 'name', 'state']].head(10)
    sub_illinois_restaurant_df['my_stars'] = sub_illinois_restaurant_df.name.apply(lambda name: (len(name) % 5) + 1.0)

    # add data for restaurants in Massachusetts; Yelp dataset has no restaurants
    # in this state, which means it will necessitate outer join
    matts_restaurant_df = pd.DataFrame([
        {"business_id": "abc100", "name": "Taqueria Jalisco (East Boston)", "state": "MA", "my_stars": 5.0},
        {"business_id": "abc101", "name": "Petit Robert Bistro (South End)", "state": "MA", "my_stars": 4.5},
        {"business_id": "abc102", "name": "Fat Baby (South Boston)", "state": "MA", "my_stars": 4.0},
        {"business_id": "abc103", "name": "Myers + Chang (South End)", "state": "MA", "my_stars": 4.0},
        {"business_id": "abc104", "name": "Aquitaine (South End)", "state": "MA", "my_stars": 4.0},
        {"business_id": "abc105", "name": "Coppa (South End)", "state": "MA", "my_stars": 4.0},
        {"business_id": "abc106", "name": "Tambo 22 Peruvian Kitchen & Bar (Chelsea)", "state": "MA", "my_stars": 4.0},
        {"business_id": "abc107", "name": "Aqua Pazza (North End)", "state": "MA", "my_stars": 4.0},
        {"business_id": "abc108", "name": "South End Buttery (South End)", "state": "MA", "my_stars": 3.5},
        {"business_id": "abc109", "name": "Tatte Bakery (Boston)", "state": "MA", "my_stars": 3.0},
    ])

    # concat restaurants into final set of matt's ratings
    matts_fav_spots_df = pd.concat([matts_restaurant_df, sub_illinois_restaurant_df])

    # write dataframes to parquet
    print("writing dataframes")
    business_df.to_parquet("businesses_10k.pq", index=False)
    user_df.to_parquet("users_10k.pq", index=False)
    reviews_df.to_parquet("reviews_10k.pq", index=False)
    matts_fav_spots_df.to_parquet("matts_fav_spots.pq", index=False)

    # convert columns to be valid for sqlite
    business_df.loc[:, 'attributes'] = business_df.attributes.apply(lambda d: json.dumps(d))
    business_df.loc[:, 'hours'] = business_df.hours.apply(lambda d: json.dumps(d))

    # write dataframes to sqlite
    print("writing sql db")
    con = sqlite3.connect("yelp_reviews_10k.db")
    business_df.to_sql(name="businesses", con=con)
    user_df.to_sql(name="users", con=con)
    reviews_df.to_sql(name="reviews", con=con)
    matts_fav_spots_df.to_sql(name="matts_fav_spots", con=con)
