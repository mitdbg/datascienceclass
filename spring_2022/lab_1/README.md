# Lab 0: Setting up your environment

* **Learning Objective**: Learn to use Docker for the rest of the labs in the course.
* **Deliverables**: Get your environment up and running. While you are not required to turn anything in, for the interactive lecture and following labs you are expected to know how to use the Docker functionality outlined below. If you have problems setting up your environment, the time to ask questions is now. 

We will be using Docker for the labs in this course to ensure that everyone has a consistent environment. Fortunately, there are detailed online tutorials for setting up Docker. If you are interested in learning more about DockerAfter installing Docker you will build a docker image, run it in a container and ensure that you can access the tools required for the interactive lecture.

While the content of this Lab is straightforward, it is wise to get an early start to allow time to fix any issues that may arise setting up your environment.

## 1. Installing Docker


A docker installation typically requires 10-20GB of hard disk space. Completing this lab will require downloading about 1GB, and thus will be easiest to complete with a good internet connection.

Docker provides tutorials for installation on [OS X](https://docs.docker.com/v17.12/docker-for-mac/install/) and [Windows](https://docs.docker.com/v17.12/docker-for-windows/install/). For linux varients please follow instructions for your distribution [here](https://docs.docker.com/v17.12/install/#docker-ce).

Some OS X users may prefer installing Docker via [homebrew](https://brew.sh/), in which case the following commands suffice:

```bash
$ brew cask install docker       # Install Docker
$ open /Applications/Docker.app  # Start Docker
```

On some older systems, the above installation procedures may not work. For instance, Windows 10 users who do not use Pro or Enterprise editions cannot use the above setup. In these cases, use the Docker Toolbox instead. The Docker Toolbox sets up a virtual machine using Oracle VirtualBox where Docker can run. Instructions are [here](https://docs.docker.com/v17.12/toolbox/overview/)

If you do not have a machine capable of running Docker, contact the course staff on Piazza as soon as possible.

Install Docker using the instructions for your system.

Verify that your installation is working properly by running ``docker run hello-world`` on a command line. You should see the following output if docker was installed correctly.

```bash
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
1b930d010525: Pull complete
Digest: sha256:6540fc08ee6e6b7b63468dc3317e3303aae178cb8a45ed3123180328bcc1d20f
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

## 2. Setting Up Course Environment

In this section, we guide you through starting the docker container and running commands inside the container to ensure that it is working properly. 

1. Clone the lab repository:

```bash
$ git clone https://github.com/mitdbg/datascienceclass.git   # https
```

or

```bash
$ git clone git@github.com:mitdbg/datascienceclass.git       # ssh
```

2. Navigate to the lab_1 directory:

```
$ cd datascienceclass/lab_1/
```

3. Build the docker image we'll use for the course :

```bash
$ docker build -t 6.s079:lab1 .
```

This command reads the ``Dockerfile`` and creates an image containing the necessary dependencies for the lab, including python, sqlite, etc. We tag this image 6.s079:lab1. This may take a while, especially on a slow internet connection. However it does not actually start a container where you can run commands. 

To check that the image was created as expected run ``docker images``.
The image you just built should be at the top. The output should look something like the following. Note the repository set as ``6.s079`` and the tag ``lab1``.

```sh
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
6.s079              lab1                10c46680a265        47 seconds ago      807MB
ubuntu              latest              3556258649b2        2 weeks ago         64.2MB
hello-world         latest              fce289e99eb9        7 months ago        1.84kB
```
        
Note that the image id on your machine will be different.

4. Start a container using the image we built above:

```bash
$ docker run -v "`pwd`":/lab1 -ti --name lab1-container 6.s079:lab1
```

The ``-v "`pwd`":/lab1`` option in this command maps the folder you are in to the docker container so any work you do inside the ``/lab1`` directory in your container will remain on your local file system in the ``6.s079_labs/lab_1`` directory. If you are running this from a windows shell you may have to replace ``"`pwd`"`` with the full path to the lab directory, e.g. ``"/c/Users/your_user_name/.../lab_1"``. You should now have a shell inside the container like the following

```sh
root@9ceb15d6ed26:/lab1#
```
        
Note that the container id ``9ceb15d6ed26`` will be different on your own machine.

5. To exit the container, press **Ctrl+d**, or type **exit** and press **Enter**.

6. If you accidentally exit the container, you can start it again by running 

```bash
$ docker start -i lab1-container
```

7. To see recently run containers, run:

```bash
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS                     PORTS               NAMES
47bb9ac15b77        6.s079:lab1         "/bin/bash"         About a minute ago   Exited (0) 2 seconds ago                       lab1-container
33ca1b2e45ba        hello-world         "/hello"            6 minutes ago        Exited (0) 6 minutes ago                       brave_snyder
```

8. Make sure that files edited inside the container can be viewed outside. In the container run:

```bash
$ echo foo >> bar.txt
```

and ensure that the file bar.txt contains "foo" on your local file system. Edit bar.txt in your favorite text editor, replacing "foo" with "baz", and make sure that your changes are visible inside the container by running ``cat bar.txt``.
        
## 3. Running commands

You should now be able to build images from a Dockerfile (like the one in this directory), start and run a container from an image, exit the container, and start it again.

For this section all commands should be run inside the shell of the docker container.

In this section we will make sure that your environment is set up properly by running a few commands. If your environment is set up correctly, the following should be trivial to complete.

We will explain these tools in more detail in the interactive lecture, but for now we will make sure that you can run them as expected.


First we will make sure that you can run SQLite. To start a sqllite session run ``sqlite3`` inside your lab1 container.
You should now have a sqlite terminal as follows.

```sh
SQLite version 3.22.0 2018-01-22 18:45:57
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite>
```
        
run ``select time()`` and ``select 1`` to make sure it is working. Then exit sqlite with Ctrl+d

```sh
sqlite> select time();
19:02:05
sqlite> select 1;
1
```     

Next, we will make sure the python environment is set up properly. Start a python terminal with ``python3`` inside the container.


## 4. Before the Lecture

Before the lecture, start the lab1-container and follow along.

# Lab 1: Basic Tools (SQL / Pandas)

* **Learning Objective**: Learn to load data and manipulate it using both Pandas and SQL
* **Deliverables**: Students will submit python source code, SQL queries, and answer some questions. Answers will be submitted through Gradescope.

This lab will use both Pandas and SQL to explore IMDB data from 2015 onwards.

## Part 1. A brief walkthrough of tools (In class)
**To get started, run ``bash setup.sh`` in the container. This installs some missing dependencies and downloads data files.**

### Pandas
One of the most popular tools for working with relatively small datasets (i.e. that fit in the main memory of a single machine) is a python library called Pandas. Pandas uses an abstraction called dataframes to manipulate tabular data. It natively supports reading data from a variety of common file formats including CSVs, fixed-width files, columnar formats, HDF5, and JSON. It also allows you to import data from common database management systems (DBMSs). A comprehensive list is [here](https://pandas.pydata.org/pandas-docs/stable/reference/io.html).

#### 1. Reading and parsing files
First, lets start up the container, and have a look at the first few lines of data file for IMDB titles.

```bash
root@27d54bf8c84b:/lab1# head data/titles.csv
title_id,type,primary_title,original_title,is_adult,premiered,ended,runtime_minutes,genres
tt0011216,movie,"Spanish Fiesta","La fête espagnole",0,2019,,67,Drama
tt0011801,movie,"Tötet nicht mehr","Tötet nicht mehr",0,2019,,,"Action,Crime"
tt0040241,short,"Color Rhapsodie","Color Rhapsodie",0,2021,,6,Short
tt0044326,short,Abstronic,Abstronic,0,2021,,6,Short
tt0044879,short,Mandala,Mandala,0,2021,,3,Short
tt0056840,short,"Aufsätze","Aufsätze",0,2021,,10,Short
tt0060220,short,"Castro Street","Castro Street",0,2020,,10,"Documentary,Short"
tt0060366,short,"A Embalagem de Vidro","A Embalagem de Vidro",0,2020,,11,"Documentary,Short"
tt0062336,movie,"The Tango of the Widower and Its Distorting Mirror","El Tango del Viudo y Su Espejo Deformante",0,2020,,70,Drama
```

Let's open a python shell (in our container), load the data and have a look. We have a file that contains all necessary imports (this is important for outputting plots later). To launch python and automatically run these imports, type ``PYTHONSTARTUP=imports.py python3``

```py
>>> titles = pd.read_csv("data/titles.csv")
>>> titles
        title_id       type                 primary_title                original_title  is_adult  premiered  ended  runtime_minutes                 genres
0        tt0011216      movie                Spanish Fiesta             La fête espagnole         0       2019    NaN             67.0                  Drama
1        tt0011801      movie              Tötet nicht mehr              Tötet nicht mehr         0       2019    NaN              NaN           Action,Crime
2        tt0040241      short               Color Rhapsodie               Color Rhapsodie         0       2021    NaN              6.0                  Short
3        tt0044326      short                     Abstronic                     Abstronic         0       2021    NaN              6.0                  Short
4        tt0044879      short                       Mandala                       Mandala         0       2021    NaN              3.0                  Short
...            ...        ...                           ...                           ...       ...        ...    ...              ...                    ...
2715726  tt9916778  tvEpisode                        Escape                        Escape         0       2019    NaN              NaN    Crime,Drama,Mystery
2715727  tt9916790  tvEpisode                 Tinne Oltmans                 Tinne Oltmans         0       2019    NaN              NaN  Comedy,News,Talk-Show
2715728  tt9916802  tvEpisode                  Luc Janssens                  Luc Janssens         0       2019    NaN              NaN  Comedy,News,Talk-Show
2715729  tt9916810  tvEpisode  Danira Boukhriss Terkessidis  Danira Boukhriss Terkessidis         0       2019    NaN              NaN  Comedy,News,Talk-Show
2715730  tt9916856      short                      The Wind                      The Wind         0       2015    NaN             27.0                  Short

[2715731 rows x 9 columns]
```

Note that Pandas represents all strings as object types and automatically recognizes integers and floats. 


#### 2. Filtering & Aggregation
Now let's get to answering some simple questions! The obvious one is to get the average duration of the titles.
We select the `runtime_minutes` column and compute the mean over it as follows.

```py
>>> titles['runtime_minutes'].mean()
39.21965306698209
```

We can also aggregate over multiple columns simultaneously.  

```py
>>> titles[["premiered", "runtime_minutes"]].max()
premiered           2029.0
runtime_minutes    43200.0
dtype: float64
```

Now let's find the length of the longest movies in each year. We'll first select the columns we want, then group rows by year, and compute the max over the groups

```py
>>> tmp = titles[["premiered", "runtime_minutes"]]
>>> tmp
        premiered  runtime_minutes
0             2019             67.0
1             2019              NaN
2             2021              6.0
3             2021              6.0
4             2021              3.0
...            ...              ...
2715726       2019              NaN
2715727       2019              NaN
2715728       2019              NaN
2715729       2019              NaN
2715730       2015             27.0

[2715731 rows x 2 columns]
>>> year_longest = tmp.groupby('premiered').max()
>>> year_longest
        runtime_minutes
premiered
2015                6000.0
2016                2070.0
2017                5760.0
2018                7777.0
2019               28643.0
2020               43200.0
2021                6000.0
2022                 400.0
2023                 240.0
2024                 360.0
2025                 125.0
2026                 360.0
2027                 360.0
2028                   NaN
2029                  14.0
```

We can sort data with respect to a column as follows:

```py
>>> year_longest.sort_values("runtime_minutes", ascending=False)
        runtime_minutes
premiered
2020               43200.0
2019               28643.0
2018                7777.0
2015                6000.0
2021                6000.0
2017                5760.0
2016                2070.0
2022                 400.0
2024                 360.0
2026                 360.0
2027                 360.0
2023                 240.0
2025                 125.0
2029                  14.0
2028                   NaN
```

Let's filter our new dataframe to get the duration of the longest movie in a few specific years. Using a group by and aggregation makes the "premiered" column an index, since we grouped over it. You can tell since the ``premiered`` header is on a higher line than ``runtime_minutes`` above.

```py
>>> year_longest[year_longest.index == 2019]
        runtime_minutes
premiered
2019               28643.0
>>> year_longest[year_longest.index <= 2020]
        runtime_minutes
premiered
2015                6000.0
2016                2070.0
2017                5760.0
2018                7777.0
2019               28643.0
2020               43200.0
```

It's worth taking a moment to see what is going on here. When we filter a dataset this way, we first create a boolean mask. We then use this mask to filter the data.

```py
>>> year_longest.index <= 2020
array([ True,  True,  True,  True,  True,  True, False, False, False,
False, False, False, False, False, False])
```
        
We can combine these vectors with boolean operations (&, |). For instance we could get longest durations for 2015 or 2020. See below.

```py
>>> year_longest[(year_longest.index == 2020) | (year_longest.index==2015)]
        runtime_minutes
premiered
2015                6000.0
2020               43200.0
```


We can also compute multiple aggregations simultaneously. Suppose we wanted to compute the maximum duration and the number of distinct title genre in each year.

```py
>>> titles[['premiered', 'runtime_minutes', 'genres']].groupby('premiered').agg({'runtime_minutes': ['max'], 'genres': ['nunique']})
        runtime_minutes  genres
                max nunique
premiered
2015               6000.0    1321
2016               2070.0    1291
2017               5760.0    1281
2018               7777.0    1268
2019              28643.0    1239
2020              43200.0    1166
2021               6000.0    1127
2022                400.0     678
2023                240.0     232
2024                360.0      83
2025                125.0      30
2026                360.0      12
2027                360.0      12
2028                  NaN       3
2029                 14.0       1
```
    

#### 3. Joining
        
You can start to do more interesting things when you "join" data from multiple data sources together. ``data/ratings.csv`` contains the ratings of each title.

In addition to doing aggregations like we did for the titles data, we can also filter on conditions. Let's say we wanted to list the movies with a rating > 9 having at least 100 votes.

First we have to find all ratings greater than 9 with at least 100 votes.

```py
>>> ratings = pd.read_csv("data/ratings.csv")
>>> ratings
        title_id  rating  votes
0       tt0011216     6.9     30
1       tt0040241     7.4     15
2       tt0044326     6.8     68
3       tt0044879     6.6     16
4       tt0056840     6.9     93
...           ...     ...    ...
356661  tt9916578     7.6     40
356662  tt9916628     8.6      5
356663  tt9916720     5.4    170
356664  tt9916766     6.7     18
356665  tt9916778     7.3     33

[356666 rows x 3 columns]

>>> excellent = ratings[(ratings['rating'] >= 9) & (ratings['votes'] >= 100)]
>>> excellent
        title_id  rating  votes
200     tt10001184     9.1   1400
201     tt10001588     9.0    155
310     tt10005284     9.2   1503
377     tt10008916     9.7   3321
378     tt10008922     9.4   1666
...            ...     ...    ...
356444   tt9913018     9.0   2387
356493   tt9913328     9.0    236
356495   tt9913336     9.1    225
356633   tt9915898     9.6   1339
356634   tt9915906     9.1    798

[4616 rows x 3 columns]
```

Let's now select titles that are specifically movies.

```py
>>> movies = titles[titles['type'] == 'movie']
>>> movies = movies[['title_id', 'primary_title']] # Select relevant columns
>>> movies
          title_id                                      primary_title
0        tt0011216                                     Spanish Fiesta
1        tt0011801                                   Tötet nicht mehr
8        tt0062336  The Tango of the Widower and Its Distorting Mi...
9        tt0065392                                 Bucharest Memories
10       tt0069049                         The Other Side of the Wind
...            ...                                                ...
2715656  tt9916362                                              Coven
2715679  tt9916428                                The Secret of China
2715689  tt9916538                                Kuambil Lagi Hatiku
2715700  tt9916622        Rodolpho Teóphilo - O Legado de um Pioneiro
2715715  tt9916730                                             6 Gunn    
```

Now that we have our filtered list of movies and a list of excellent ratings that we need to combine. Pandas has a "merge" function for this purpose that we'll use to join the two dataframes. A join takes rows from one dataframe, matches them with rows in another dataframe based on a condition, and outputs a new "merged" dataframe. Here we will join the two dataframes on their `title_id` column. 

```py
>>> excellent_movies = pd.merge(left=movies, right=excellent, on='title_id')
>>> excellent_movies
       title_id                             primary_title  rating   votes
0    tt10042868                         Generation Wrecks     9.1     107
1    tt10127546                        The Lehman Trilogy     9.1     256
2    tt10133066                                Swayamvada     9.0    1136
3    tt10156610                     Ratne price sa Kosara     9.6     147
4    tt10189514                           Soorarai Pottru     9.1  106118
..          ...                                       ...     ...     ...
160   tt9119272  RUTH - Justice Ginsburg in her own Words     9.1     263
161   tt9318514                                    Reason     9.0     147
162   tt9643832                              Gho Gho Rani     9.3     195
163   tt9691482           Kaye Ballard - The Show Goes On     9.9     206
164   tt9820678                       Moscow we will lose     9.2     139
```

Now let's find the top 10 of these movies with the highest rating.
```py
>>> excellent_movies.sort_values("rating", ascending=False)[:10]
       title_id                primary_title  rating  votes
46   tt12980094            Days of Géants II    10.0    188
30   tt11926728               Days of Géants    10.0    205
17   tt11384328                      Hulchul    10.0    754
107  tt16747572       The Silence of Swastik    10.0   4885
79   tt14996298  Veyi Subhamulu Kalugu Neeku    10.0   1909
62   tt14016830           Rite of the Shaman     9.9    121
104  tt16312196                  Maa Kathalu     9.9    708
106  tt16606580                 Half Stories     9.9   1699
28   tt11779744                      Ajinkya     9.9    747
49   tt13181612                   Tari Sathe     9.9    446
```


### TODO: Add some plots?

There are a lot of things you can do with Pandas that we have not covered, including different kinds of aggregation, plots, joins, input and output formats, etc. You are encouraged to use online resources to explore this for yourself when completing the take-home part of this lab.

### SQL

While Pandas is undoubtedly a useful tool and is great for exploring small datasets. There are a number of cases where it may not be the right tool for the task. 

Pandas runs exclusively in memory. With even moderate sized data you may exceed available memory. Additionally, pandas materializes each intermediate result, so the memory consumption can easily reach several times your input data if you are not very careful. Materializing after each operation is also inefficient, even when data fits in memory. If you want to save results, you have to manage a set of output files. With small data sets like we show in this lab, this is not a problem, but as your datasets grow larger or more complex this becomes an increasingly difficult task.

Furthermore, above we had to define all of the physical operations to transform the data. Choosing to or add or remove columns, the order to apply filters, etc.

An alternative to this approach is to use a Database Management System (DBMS) like Postgres or SQLite that supports a declarative query language. Unlike Pandas, a DBMS can usually store data that far exceeds what you can hold in memory. Users most often interact with DBMSs through a declarative query language, typically a dialect of SQL. Unlike pandas, in SQL you define what data to retrieve, instead of the physical operations to retrieve it. This allows the DMBS to automatically optimize your query, choosing the order to apply filters, how to apply predicates, etc.

However, using a DBMS is typically a little harder to get going with. You have to define a schema for the tables you work with, and load all the data in before you can start querying it. If you are doing a one off analysis on some small CSV you downloaded, it is probably easier to use Pandas. If you have some special operation that the DBMS does not natively support, a linear regression for instance, doing this inside a DBMS can be cumbersome. 

In this section we will introduce you to a simple DBMS called SQLite. Perhaps the [2nd most deployed software package](https://www.sqlite.org/mostdeployed.html) of all time! Unlike most DBMSs which run all the time and are accessed over a network. SQLite runs as a library in the same process as your program and stores all it's state in a single file. This makes it easy to deploy, use, and play around with SQL.


#### 1. Exploring the Schema

We give you a database file (`imdb.db`) in which the csv files have been loaded using the `load_data.sql` command.


In the bash shell (in the container), let's open a sqlite shell and have a look at our data. The ``-column -header`` settings pretty print the output into columns with a header. We can see the tables loaded into the database by running ``.tables`` and the schema of these tables with ``.schema [tablename]``. We will then run our first sql query to fetch the first few rows of the titles tables. Note that typically table names, column names, and SQL keywords are not case sensitive.

```sh
root@40ce47bd550e:/lab1# sqlite3 data/imdb.db -column -header
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> .tables
akas      crew      episodes  people    ratings   titles
sqlite> .schema titles
CREATE TABLE IF NOT EXISTS "titles"(
title_id TEXT,
type TEXT,
primary_title TEXT,
original_title TEXT,
is_adult INT,
premiered INT,
ended INT,
runtime_minutes INT,
genres TEXT
);
sqlite> SELECT * FROM titles LIMIT 5;
title_id    type        primary_title   original_title     is_adult    premiered   ended       runtime_minutes  genres
----------  ----------  --------------  -----------------  ----------  ----------  ----------  ---------------  ----------
tt0011216   movie       Spanish Fiesta  La fête espagnole  0           2019                    67               Drama
tt0011801   movie       Tötet nicht me  Tötet nicht mehr   0           2019                                     Action,Cri
tt0040241   short       Color Rhapsodi  Color Rhapsodie    0           2021                    6                Short
tt0044326   short       Abstronic       Abstronic          0           2021                    6                Short
tt0044879   short       Mandala         Mandala            0           2021                    3                Short
``` 

#### 2. Filtering & Aggregation

Now let's get the same data as we did with pandas and see how it looks in SQL. For simplicity, we'll write our queries in a text file ``scratch.sql`` with a text editor and run the SQL query in the file by running ``.read scratch.sql``. We'll show both the query and results separated by ``+++++++++++++++++++++++`` below. We'll start by looking at the average duration.

```sql
SELECT
        AVG(runtime_minutes)
FROM
        titles;

+++++++++++++++++++++++

sqlite> .read scratch.sql
AVG(runtime_minutes)
--------------------
39.2196530669821
```


This matches the result we got from pandas so we are on the right track. We can also aggregate columns simultaneously.

```sql
SELECT
        MAX(premiered),
        MAX(runtime_minutes)
FROM
        titles;

+++++++++++++++++++++++

sqlite> .read scratch.sql
MAX(premiered)  MAX(runtime_minutes)
--------------  --------------------
2029            43200
```

Now as above we'll group by release year again.

```sql
SELECT 
        premiered,
        MAX(runtime_minutes)
FROM 
        titles
GROUP BY 
        premiered;

+++++++++++++++++++++++

sqlite> .read scratch.sql
premiered   MAX(runtime_minutes)
----------  --------------------
2015        6000
2016        2070
2017        5760
2018        7777
2019        28643
2020        43200
2021        6000
2022        400
2023        240
2024        360
2025        125
2026        360
2027        360
2028
2029        14
```
   
and order by descending . Let's just get the first few rows by using ``LIMIT``;

```sql
SELECT 
        premiered,
        MAX(runtime_minutes) AS max_runtime
FROM 
        titles
GROUP BY 
        premiered
ORDER BY
        max_runtime DESC
LIMIT 5;

+++++++++++++++++++++++

sqlite> .read scratch.sql
premiered   max_runtime
----------  -----------
2020        43200
2019        28643
2018        7777
2021        6000
2015        6000
```
        
Like we did with pandas we can also find the ratings that are greater than 9 with more than 100 votes. We'll do that using a `WHERE` clause.

```sql
SELECT 
        *
FROM 
        ratings
WHERE 
        rating >= 9 AND votes >= 100
LIMIT 5;

++++++++++++++++++++++++++++

sqlite> .read scratch.sql
title_id    rating      votes
----------  ----------  ----------
tt10001184  9.1         1400
tt10001588  9           155
tt10005284  9.2         1503
tt10008916  9.7         3321
tt10008922  9.4         1666
```

We'll again join these ratings with their corresponding movies.

#### 3. Joining
To join two or more tables, we first list them in the `FROM` clause. We specify how to join in the `WHERE` clause clause. The `WHERE` clause may further contain additional filters for each individual tables.

Here is how to compute the join we computed using pandas.

```sql
SELECT 
        t.primary_title, t.premiered, r.rating, r.votes
FROM 
        titles AS t, ratings AS r
WHERE
        t.title_id = r.title_id -- Join condition 
        AND t.type = 'movie'
        AND r.rating >= 9 AND r.votes >= 100
ORDER BY
    r.rating DESC
LIMIT 10;
                      
+++++++++++++++++++++++

sqlite> .read scratch.sql
primary_title  premiered   rating      votes
-------------  ----------  ----------  ----------
Hulchul        2019        10          754
Days of Géant  2019        10          205
Days of Géant  2020        10          188
Veyi Subhamul  2022        10          1909
The Silence o  2021        10          4885
Ajinkya        2021        9.9         747
Tari Sathe     2021        9.9         446
Rite of the S  2022        9.9         121
Maa Kathalu    2021        9.9         708
Half Stories   2022        9.9         1699
```    

We now discuss a few useful SQL-only features.


#### 4. Common Table Expressions
Common Table Expressions (CTEs) are a useful mechanism to simplify complex queries. They allow us to compute temporary tables that can be used in other parts of the queries. While the join above is not complex enough to warrent using CTEs, we will use it as an example to get you started. Suppose that, like in our pandas example, we wanted to first compute the set of excellent ratings and the set of movies before using them in the join.

```sql
WITH 
excellent (title_id, rating, votes) AS ( -- Precomputed the excellent ratings
        SELECT * FROM ratings WHERE rating >= 9 AND votes >= 100
),
movies (title_id, primary_title, premiered) AS ( -- Precomputed movies
        SELECT title_id, primary_title, premiered FROM titles WHERE type='movie'
)

SELECT rating, votes, primary_title, premiered  -- Join.
FROM excellent AS e, movies AS m
WHERE e.title_id = m.title_id
ORDER BY rating LIMIT 10;

+++++++++++++++++++++++++++

rating      votes       primary_title  premiered
----------  ----------  -------------  ----------
10          754         Hulchul        2019
10          205         Days of Géant  2019
10          188         Days of Géant  2020
10          1909        Veyi Subhamul  2022
10          4885        The Silence o  2021
9.9         747         Ajinkya        2021
9.9         446         Tari Sathe     2021
9.9         121         Rite of the S  2022
9.9         708         Maa Kathalu    2021
9.9         1699        Half Stories   2022
```

In this query, we first compute the table of excellent ratings and the table of movies using the construct `WITH table_name(column_names...) AS (query)`. We the perform the join using these temporary tables. 

#### 5. Window Functions
Whereas groupby aggregations allow to aggregate partitions of the data, window functions allow to perform computations on each partition without aggregating the data.

For example, suppose that for every given year, we wanted to assign a rank to the set of excellent movies according to their ratings. While groupbys allow to partition by year, they can only compute aggregate data for each year; they cannot assign individual ranks to each row within a partition. We need window functions for this task.


```sql
WITH 
excellent_movies (primary_title, premiered, rating, votes) AS (
        SELECT 
                t.primary_title, t.premiered, r.rating, r.votes
        FROM 
                titles AS t, ratings AS r
        WHERE
                t.title_id = r.title_id -- Join condition 
                AND t.type = 'movie'
                AND r.rating >= 9 AND r.votes >= 100
)
SELECT
        primary_title, premiered, rating, votes,
        RANK() OVER (PARTITION BY premiered ORDER BY rating DESC)
FROM excellent_movies
ORDER BY premiered;

++++++++++++++++++++++++++

primary_title  premiered   rating      votes       year_rank
-------------  ----------  ----------  ----------  ----------
Druglawed      2015        9.5         134         1
Red Right Ret  2015        9.4         140         2
The Ataxian    2015        9.3         214         3
Major!         2015        9.3         245         3
The Epic Jour  2015        9.2         880         5
Darkest Befor  2015        9.1         129         6
The Call       2015        9           191         7
The Last Tear  2015        9           145         7
Love & Contem  2016        9.7         268         1
Time Framed    2016        9.4         285         2
Paint Drying   2016        9.3         444         3
Mirror Game    2016        9.1         25499       4
That Vitamin   2016        9.1         956         4
O Jehovah, ..  2016        9.1         114         4
Legends of Fr  2016        9           520         7
Born Warriors  2016        9           744         7
All the Rage   2016        9           273         7
The Unnamed    2016        9           4903        7
The Barn Thea  2017        9.4         124         1
Genius Montis  2017        9.4         142         1
Mama's Heart.  2017        9.3         536         3
Behind the Al  2017        9.3         278         3
...
```

In this query we first compute the table of excellent movies as a CTE to simplify the query. We then select the rows of this table in addition to a yearly ranking computed as follow:

* First partition rows by year (`PARTITION BY premiered`).
* Order the items within each partition (`ORDER BY rating DESC`).
* Assign a rank to each element in accordance with their order (`RANK()`).

As you can see from the results, the `year_rank` column is order within each year, and resets across different years.

This captures the general idea behind functions: compute a result in accordance with a certain partitioning of the data. Many more this can be done with this idea. A good tutorial can be found [here](https://mode.com/sql-tutorial/sql-window-functions/)


#### 6. Speeding

### Pandas + SQL

One interesting feature of pandas allows you to run a query in a database and return the result as a dataframe, so you can get the best of both worlds!

Here is a simple python program that opens the sqlite database, reads the query from the ``scratch.sql`` file, executes the query and loads the result into a data frame

```python3
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as sql

with sql.connect("lab1.sqlite") as conn, open("scratch.sql") as in_query:
    cur = conn.cursor()
    df = pd.read_sql_query(in_query.read(), conn)
    print(df)
```

## Part 2: Questions

You are allowed to work in pairs for this assignment.

For the rest of the lab we will ask you to answer a few questions about the FEC dataset using pandas and writing SQL queries. You will edit ``queries.py`` and fill in each function with a query to answer the question. The Pandas functions (e.g. Q1Pandas) have a space to fill in your code. Fill in SQL queries in the ``queries`` directory. Do not make other edits to the repository or database, except when instructed.

For convenience, you can run queries one at a time using the ``python3 queries.py -q [query_num]`` command to run a single query (in both Pandas and SQL, whena applicable).

In addition to your code, you will submit results of your code for each of the questions in a PDF. Put each answer on a new page.
Detailed submission instructions are at the bottom of this document.

### TODO: Solve this questions using both SQL and Pandas
1. (5 points) Simple single table query.
2. (5 points) Simple single table query. 
3. (5 points) Simple 2-way join.
4. (10 points) Multiway join Query.
5. (10 points) Multiway Query.
6. (15 points) Complex subqueries. Best done with CTEs.
7. (15 points) Complex subqueries. Best done with CTEs.

### TODO: Solve these using only SQL
1. (15 points) Window functions
2. (15 points) Window Functions.
3. (10 points) Timed Query?

### TODO: Fill in questions and submission instructions.


