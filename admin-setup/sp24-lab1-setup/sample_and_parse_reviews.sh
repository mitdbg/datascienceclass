#!/bin/bash

# get first 10k reviews
cat yelp_academic_dataset_review.json | head -n 10000 > yelp_reviews_10k.json 

# get business_ids and user_ids for first 10k reviews
cat yelp_reviews_10k.json | sed -nr 's/.*business_id":"([^"]*).*/\1/p' > yelp_business_ids_10k.txt
cat yelp_reviews_10k.json | sed -nr 's/.*user_id":"([^"]*).*/\1/p' > yelp_user_ids_10k.txt

