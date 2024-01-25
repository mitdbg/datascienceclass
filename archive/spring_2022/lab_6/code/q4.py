import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import sequence, to_timestamp, explode, col, rand
from pyspark.sql.window import Window
from pyspark.sql import functions as F
from time import perf_counter


print("Initializing Spark session...")
spark = SparkSession.builder.config("spark.driver.memory", "32g").config(
  "spark.executor.instances", 4).config("spark.executor.cores", 4).config(
  "spark.driver.cores", "4").getOrCreate()
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

print("Creating timeseries...")
sdf = spark.sql("""SELECT sequence(to_timestamp('2021-01-01'), """
  """to_timestamp('2021-12-31'), interval 1 second) as time""").withColumn(
  "time", explode(col("time"))).withColumn("x", rand()).withColumn(
  "y", rand()).withColumn("id", rand() * 1000).withColumn("id", col("id").cast('int'))

WINDOW_SECONDS = 5 * 60
MAX_PARTITIONS = 100000
partitions = 1

while (partitions <= MAX_PARTITIONS):
        print(f"Now running for {partitions} partition(s)")

        # YOUR CODE GOES HERE
        # 1. Set the shuffle partitions appropriately

        # YOUR CODE GOES HERE
        # 2. Create a window that covers the most recent WINDOW_SECONDS (inclusive), 
        # partitioned and ordered by timestamp.

        t_start = perf_counter()
        # YOUR CODE GOES HERE
        # 3. Compute the rolling average. Make sure that pyspark, which uses a lazy 
        # approach like dask, actually performs the computation
        t_end = perf_counter()

        print(f"Duration for {partitions} partition(s): {(t_end-t_start)*1000} ms")

        partitions *= 10
