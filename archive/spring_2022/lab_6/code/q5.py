import pyspark
import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from time import perf_counter

print("Initializing Spark session...")
spark = SparkSession.builder.config("spark.driver.memory", "32g").config(
  "spark.executor.instances", 4).config("spark.executor.cores", 4).config(
  "spark.driver.cores", "4").getOrCreate()
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

print("Creating dataframe...")

# YOUR CODE GOES HERE
# 1. Read the appropriate JSON files into a single dataframe

MAX_PARTITIONS = 100000
partitions = 1

while (partitions <= MAX_PARTITIONS):
  print(f"Now running for {partitions} partition(s)")

  # YOUR CODE GOES HERE
  # 2. Set the shuffle partitions appropriately

  t_start = perf_counter()
  # YOUR CODE GOES HERE
  # 3. Calculate the top 3 providers. Make sure that pyspark, which uses a lazy 
  # approach like dask, actually performs the computation
  t_end = perf_counter()

  print(f"Duration for {partitions} partition(s): {(t_end-t_start)*1000} ms")
  partitions *= 10
