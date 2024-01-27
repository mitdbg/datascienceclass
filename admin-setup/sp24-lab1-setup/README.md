## Steps to Recreate Lab 1 Dataset
This document provides a high-level description of how I created the final gzipped tar archive in `lab_1/data/yelp-data.tar.gz` for the Spring 2024 course.

1. Download the full Yelp Dataset from Kaggle: https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset/data
  - Note: I only downloaded the business, review, and user files
2. Filter for the first 10k reviews by executing `cat yelp_academic_dataset_review.json | head -n 10000 > yelp_reviews_10k.json`
3. Execute `./sample_and_parse_reviews.sh` to get the business_ids and user_ids for the first 10k reviews. These are written to `yelp_business_ids_10k.txt` and `yelp_user_ids_10k.txt`, respectively.
4. Run `python filter_for_businesses_and_users.py` to construct the parquet files and sqlite database which constitute the first 10k reviews and their respective businesses and users.
5. Finally, run `tar -czvf yelp-data.tar.gz businesses_10k.pq reviews_10k.pq users_10k.pq yelp_reviews_10k.db` to create the tar archive.  
