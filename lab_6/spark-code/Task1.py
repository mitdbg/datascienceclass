#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys
from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":
    ## The following files are stored on HDFS 
    # /user/hadoop/lab6-data/dune-1.txt
    # /user/hadoop/lab6-data/dune-2.txt
    # /user/hadoop/lab6-data/dune-3.txt

    spark = SparkSession\
        .builder\
        .appName("DuneWordCount")\
        .getOrCreate()

    # Your input RDD
    dune_rdd = spark.read.text("/user/hadoop/lab6-data/dune-*.txt").rdd

    # The task: Output the top-100 most frequent words in Dune novel series by Frank Herbert 
    #   by writing a Spark program with its RDD (https://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-operations) APIs.
    # Your program should replace the set of punctuations (in bracket) with whitespace before start counting: [:=,!'".?]
    # Then your program should turn all the words into lower case.

    # Output the top-100 most frequent words along with their frequency in the following format to standard output:
    #
    # word,freq
    # ...
    # thought,1092
    # will,1080
    # fremen,1053
    # leto,1036
    # alia,1033
    # now,997
    # ...
    #

    # Note that if two words have the same frequency, break tie by outputting the lexigraphically smaller word first.

    #########################################
    # YOUR CODE GOES HERE
    # DO NOT MAKE CHANGES IN OTHER PLACES

    ####################################
    spark.stop()