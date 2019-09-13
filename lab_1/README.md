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
$ docker build -t 6.s080:lab1 .
```

This command reads the ``Dockerfile`` and creates an image containing the necessary dependencies for the lab, including python, sqlite, etc. We tag this image 6.s080:lab1. This may take a while, especially on a slow internet connection. However it does not actually start a container where you can run commands. 

To check that the image was created as expected run ``docker images``.
The image you just built should be at the top. The output should look something like the following. Note the repository set as ``6.s080`` and the tag ``lab1``.

        REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
        6.s080              lab1                10c46680a265        47 seconds ago      807MB
        ubuntu              latest              3556258649b2        2 weeks ago         64.2MB
        hello-world         latest              fce289e99eb9        7 months ago        1.84kB
        
Note that the image id on your machine will be different.

4. Start a container using the image we built above:

```bash
$ docker run -v "`pwd`":/lab1 -ti --name lab1-container 6.s080:lab1
```

The ``-v "`pwd`":/lab1`` option in this command maps the folder you are in to the docker container so any work you do inside the ``/lab1`` directory in your container will remain on your local file system in the ``6.S080_labs/lab_1`` directory. If you are running this from a windows shell you may have to replace ``"`pwd`"`` with the full path to the lab directory, e.g. ``"/c/Users/your_user_name/.../lab_1"``. You should now have a shell inside the container like the following

        root@9ceb15d6ed26:/lab1#
        
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
47bb9ac15b77        6.s080:lab1         "/bin/bash"         About a minute ago   Exited (0) 2 seconds ago                       lab1-container
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


        SQLite version 3.22.0 2018-01-22 18:45:57
        Enter ".help" for usage hints.
        Connected to a transient in-memory database.
        Use ".open FILENAME" to reopen on a persistent database.
        sqlite>
        
run ``select time()`` and ``select 1`` to make sure it is working. Then exit sqlite with Ctrl+d

        sqlite> select time();
        19:02:05
        sqlite> select 1;
        1
        

Next, we will make sure the python environment is set up properly. Start a python terminal with ``python3`` inside the container.


## 4. Before the Lecture

Before the lecture, start the lab1-container and follow along.

# Lab 1: Basic Tools (SQL / Pandas)

* **Learning Objective**: Learn to load data and manipulate it using both Pandas and SQL
* **Deliverables**: Students will submit python source code, SQL queries, and answer some questions. Answers will be submitted through Greadescope.

This lab will use both Pandas and SQL to explore  Federal Election Commission data from the 2016 election.

## Part 1. A brief walkthrough of tools (In class)

Given a data set in a tabular format, one approach for answering questions over it is to write a program that iterates over each row in the data to answer a query over it. ``data/dist_pop.txt`` contains a simple table mapping congressional districts to their estimated 2017 population (according to the [Census Bureau](https://www.census.gov/programs-surveys/acs/news/data-releases.2017.html)). As you likely know, each state has a number of representatives proportional to their population (minimum 1), and each state has 2 senators regardless of population. We might want to know what the average population in a district is, or what is the maximum or minimum number of people in a district. Say we want to sum over all districts in each state to get each state's population, then sort by the least populous states (To find out which state has the fewest citizens per senator) To answer this simple questions we would have to go through several steps. 

1. Read the file line by line
2. Parse each line into distinct columns, skipping the header
3. Set the proper types of each cell
4. Keep a running sum of the totals we are interested in some data structure.
5. Sort the results
7. Write the output


While coding up this query in python is relatively straightforward, doing this for each query on each dataset we have is tedious, slow, and error prone. Fortunately since these kinds of tasks are very common, a range of tools are available so you don't have to code it up every time.

**To get started, run ``bash setup.sh`` in the container. This installs some missing dependencies.**

### Pandas
One of the most popular tools for working with relatively small datasets (i.e. that fit in the main memory of a single machine) is a python library called Pandas. Pandas uses an abstraction called dataframes to manipulate tabular data. It natively supports reading data from a variety of common file formats including CSVs, fixed-width files, columnar formats, HDF5, and JSON. It also allows you to import data from common database management systems (DBMSs). A comprehensive list is [here](https://pandas.pydata.org/pandas-docs/stable/reference/io.html).

#### 1. Reading and parsing files
First, lets start up the container, and have a look at the first few lines of data file for district population.

```bash
        root@40dc0f9821c8:/lab1# head data/dist_pop.txt
        state|district_id|district name|population
        AK|0|Congressional District (at Large) (115th Congress), Alaska|739795.0
        AL|1|Congressional District 1 (115th Congress), Alabama|713410.0
        AL|2|Congressional District 2 (115th Congress), Alabama|673776.0
        AL|3|Congressional District 3 (115th Congress), Alabama|710488.0
        AL|4|Congressional District 4 (115th Congress), Alabama|685553.0
        AL|5|Congressional District 5 (115th Congress), Alabama|718713.0
        AL|6|Congressional District 6 (115th Congress), Alabama|700401.0
        AL|7|Congressional District 7 (115th Congress), Alabama|672406.0
        AR|1|Congressional District 1 (115th Congress), Arkansas|722287.0
```
We can tell a few things already, in particular, this looks like a CSV with a delimiter "|" instead of commas. And it has a header describing all the columns. We can guess at first glance that the first column is always 2 characters the 2nd column are integers, the third is variable length text, and the last is a floating point value (though we can probably treat population as an integer). 

Let's open a python shell (in our container), load the data and have a look. We have a file that contains all necessary imports (this is important for outputting plots later). To launch python and automatically run these imports, type ``PYTHONSTARTUP=imports.py python3``


        Python 3.6.8 (default, Jan 14 2019, 11:02:34)
        [GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import pandas as pd
        >>> dist_pop = pd.read_csv("data/dist_pop.txt")
        >>> dist_pop
                                                           state|district_id|district name|population
        AK|0|Congressional District (at Large) (115th C...                            Alaska|739795.0
        AL|1|Congressional District 1 (115th Congress)                               Alabama|713410.0
        AL|2|Congressional District 2 (115th Congress)                               Alabama|673776.0
        AL|3|Congressional District 3 (115th Congress)                               Alabama|710488.0
        AL|4|Congressional District 4 (115th Congress)                               Alabama|685553.0
        ...                                                                                       ...
        WI|8|Congressional District 8 (115th Congress)                             Wisconsin|732402.0
        WV|1|Congressional District 1 (115th Congress)                         West Virginia|611376.0
        WV|2|Congressional District 2 (115th Congress)                         West Virginia|621635.0
        WV|3|Congressional District 3 (115th Congress)                         West Virginia|582846.0
        WY|0|Congressional District (at Large) (115th C...                           Wyoming|579315.0

        [435 rows x 1 columns]

It looks like it read the data, but it parsed it as a single text column, instead of recognizing that the file is "|" delimited. Let's try again. And check that the types are reasonable.

        >>> dist_pop = pd.read_csv("data/dist_pop.txt", delimiter="|")
        >>> dist_pop
             state  district_id                                      district name  population
        0      AK            0  Congressional District (at Large) (115th Congr...    739795.0
        1      AL            1  Congressional District 1 (115th Congress), Ala...    713410.0
        2      AL            2  Congressional District 2 (115th Congress), Ala...    673776.0
        3      AL            3  Congressional District 3 (115th Congress), Ala...    710488.0
        4      AL            4  Congressional District 4 (115th Congress), Ala...    685553.0
        ..    ...          ...                                                ...         ...
        430    WI            8  Congressional District 8 (115th Congress), Wis...    732402.0
        431    WV            1  Congressional District 1 (115th Congress), Wes...    611376.0
        432    WV            2  Congressional District 2 (115th Congress), Wes...    621635.0
        433    WV            3  Congressional District 3 (115th Congress), Wes...    582846.0
        434    WY            0  Congressional District (at Large) (115th Congr...    579315.0

        [435 rows x 4 columns]
        >>> dist_pop.dtypes
        state             object
        district_id        int64
        district name     object
        population       float64
        dtype: object
        
Note that Pandas represents all strings as object types and recognizes district_id as an integer type, and population as a float.


#### 2. Filtering & Aggregation
Now let's get to answering some simple questions! The obvious one is to get the total population of all states (no DC).
We select the population column and sum over it as follows.

        >>> dist_pop["population"].sum()
        325025206.0

We can also aggregate over multiple columns simultaneously.  

        >>> dist_pop[["population", "district_id"]].max()
    population     1050493.0
    district_id         53.0
    dtype: float64


Now let's see the total population of each state by grouping by state and summing over population. This sums the population for all districts in each state to get the total population. We'll first select the columns we want, then group rows by state, and sum over the groups

        >>> temp = dist_pop[["state", "population"]]
    >>> temp 
        state  population
    0      AK    739795.0
    1      AL    713410.0
    2      AL    673776.0
    3      AL    710488.0
    4      AL    685553.0
    ..    ...         ...
    430    WI    732402.0
    431    WV    611376.0
    432    WV    621635.0
    433    WV    582846.0
    434    WY    579315.0
    >>> state_pop = temp.groupby("state").sum()
    >>> state_pop
               population
        state
        AK       739795.0
        AL      4874747.0
        AR      3004279.0
        ...
    
Let's filter our new dataframe to get the population of a few states. Using a group by and aggregation makes the "state" column an index, since we grouped over it. You can tell since the ``population`` header is on a higher line than ``state`` above.

    >>> state_pop[state_pop.index == "AL"]
           population
    state
    MA      6859819.0
    >>> state_pop[state_pop.index == "CA"]
           population
    state
    CA     39536653.0
    >>> state_pop[state_pop.index == "VT"]
           population
    state
    VT       623657.0

It's worth taking a moment to see what is going on here. When we filter a dataset this way, we first create a boolean mask. We then use this mask to filter the data.

    >>> state_pop.index == "AL"
    array([False,  True, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False])
           
We can combine these vectors with boolean operations (&, |). For instance we could get states beginning with "A" that have population at least 1 million by combining ``state_pop.index.str.startswith("A")`` with a predicate on population. See below.

    >>> filter = (state_pop.index.str.startswith("A")) & (state_pop.population > 1000000)
    >>> filter
    state
    AK    False
    AL     True
    AR     True
    AZ     True
    CA    False
    CO    False
    CT    False
    ...
    >>> state_pop[filter]
           population
    state
    AL      4874747.0
    AR      3004279.0
    AZ      7016270.0

How many states have a population over 8,000,000 (according to 2017 census bureau estimates) and have a state abbreviation containing "A"? (You can use the contains function instead of startwith).

Anyway, let's go back to our state_population data, order by the most populous states and get the top 10.

        >>> state_pop.sort_values("population", ascending=False)[:10]
               population
        state
        CA     39536653.0
        TX     28304596.0
        FL     20984400.0
        NY     19849399.0
        PA     12805537.0
        IL     12802023.0
        OH     11658609.0
        GA     10429379.0
        NC     10273419.0
        MI      9962311.0
        
If we want to see how many districts each of these states has, we can also count the number of districts simultaneously.
But this is starting to get a little complicated.  First let's filter out the columns we want, group and aggregate.

        >>> temp = dist_pop[["state", "district_id", "population"]]
    >>> temp
        state  district_id  population
    0      AK            0    739795.0
    1      AL            1    713410.0
    2      AL            2    673776.0
    3      AL            3    710488.0
    4      AL            4    685553.0
    ..    ...          ...         ...
    430    WI            8    732402.0
    431    WV            1    611376.0
    432    WV            2    621635.0
    433    WV            3    582846.0
    434    WY            0    579315.0
    
    [435 rows x 3 columns]
    >>> temp_agg = temp.groupby("state").agg({"district_id":["count"], "population":["sum"]})
    >>> temp_agg
          district_id  population
            count         sum
    state
    AK              1    739795.0
    AL              7   4874747.0
    AR              4   3004279.0
    AZ              9   7016270.0
    CA             53  39536653.0
    CO              7   5607154.0
    CT              5   3588184.0
    DE              1    961939.0
    FL             27  20984400.0
    GA             14  10429379.0
    HI              2   1427538.0
    IA              4   3145711.0
    ID              2   1716943.0
    IL             18  12802023.0
    
Now we will sort. Not how column names change after we do an aggregation of this type.

    >>> out = temp_agg.sort_values.sort_values(("population", "sum"), ascending=False)
    >>> out = out[10:]
              district_id  population
                    count         sum
        state
        CA             53  39536653.0
        TX             36  28304596.0
        FL             27  20984400.0
        NY             27  19849399.0
        PA             18  12805537.0
        IL             18  12802023.0
        OH             16  11658609.0
        GA             14  10429379.0
        NC             13  10273419.0
        MI             14   9962311.0
        
One interesting thing we can see here is that although North Carolina (NC) has a higher population than Michigan(MI) by 2017 estimates, it has fewer congressional districts. If this continues to be true by the official census in 2020, North Carolina may get a bit more representation in the House of Representatives.

#### 3. Joining
        
You can start to do more interesting things when you "join" data from multiple data sources together. ``data/candidate.txt`` contains data on candidates for federal political office in the 2016 election cycle (President, House, Senate). Details about the meaning of each column are available on the [FEC website](https://www.fec.gov/campaign-finance-data/candidate-master-file-description/).

In addition to doing aggregations like we did for the population data, we can also filter on conditions. Let's say we want to find the district that had the most candidates per capita by using the population and candidate data.

First we have to find all the house candidates in 2016. We'll load the CSV then filter. Note that we also have to filter "CAND_STATUS" retreiving only rows where the column takes values "C" and "N", meaning the candidate met the official requirements to run for office and appeared on a ballot (primary or general). We do this by creating a mask for each condition first. Construct a mask that fulfills this predicate.

    >>> candidates = pd.read_csv("data/candidate.txt", delimiter="|")
    >>> candidates
            CAND_ID                  CAND_NAME  ... CAND_ST  CAND_ZIP
    0     H0AK00097               COX, JOHN R.  ...      AK   99556.0
    1     H0AL02087               ROBY, MARTHA  ...      AL   36101.0
    2     H0AL02095          JOHN, ROBERT E JR  ...      AL   36054.0
    3     H0AL05049  CRAMER, ROBERT E "BUD" JR  ...      AL   35804.0
    4     H0AL05163                 BROOKS, MO  ...      AL   35802.0
    ...         ...                        ...  ...     ...       ...
    7636  S8WA00137             AMUNDSON, THOR  ...      WA   98502.0
    7637  S8WA00186              SENN, DEBORAH  ...      WA   98122.0
    7638  S8WA00194            CANTWELL, MARIA  ...      WA   98111.0
    7639  S8WI00026     FEINGOLD, RUSSELL DANA  ...      WI   53562.0
    7640  S8WI00158            NEUMANN, MARK W  ...      WI   53058.0

[7641 rows x 15 columns]

    >>> house_cand_mask = candidates["CAND_OFFICE"] == "H"
    >>> house_cand_mask
    0        True
    1        True
    2        True
    3        True
    4        True
        ...
    7636    False
    7637    False
    7638    False
    7639    False
    7640    False
    Name: CAND_OFFICE, Length: 7641, dtype: bool
    >>> cand_2016_mask = candidates["CAND_ELECTION_YR"]==2016
    >>> cand_2016_mask
    0       False
    1        True
    2        True
    3       False
    4        True
        ...
    7636     True
    7637    False
    7638    False
    7639     True
    7640    False
    Name: CAND_ELECTION_YR, Length: 7641, dtype: bool
    >>> qual_cand_mask = ((candidates["CAND_STATUS"] == "C") | (candidates["CAND_STATUS"] == "N"))
    >>> qual_cand_mask
    >>> qual_cand_mask
    0        True
    1        True
    2        True
    3       False
    4        True
        ...
    7636     True
    7637    False
    7638    False
    7639     True
    7640    False
    Name: CAND_STATUS, Length: 7641, dtype: bool
    >>> mask = house_cand_mask & qual_cand_mask & cand_2016_mask
    >>> mask
    0       False
    1        True
    2        True
    3       False
    4        True
        ...
    7636    False
    7637    False
    7638    False
    7639    False
    7640    False
    Length: 7641, dtype: bool

Now we'll filter the candidates that meet all our condidions.

        >>> house_cand_2016 = candidates[mask]
        >>> house_cand_2016
                CAND_ID                    CAND_NAME  ... CAND_ST     CAND_ZIP
        1     H0AL02087                 ROBY, MARTHA  ...      AL      36101.0
        2     H0AL02095            JOHN, ROBERT E JR  ...      AL      36054.0
        4     H0AL05163                   BROOKS, MO  ...      AL      35802.0
        6     H0AL07086     SEWELL, TERRYCINA ANDREA  ...      AL      35201.0
        9     H0AR01083     CRAWFORD, ERIC ALAN RICK  ...      AR      72404.0
        ...         ...                          ...  ...     ...          ...
        4357  H8WA09047                POSTMA, JAMES  ...      WA      98388.0
        4359  H8WI01024                RYAN, PAUL D.  ...      WI  535470771.0
        4360  H8WI02121         THERON, DANIEL PETER  ...      WI      53713.0
        4364  H8WI09050  SENSENBRENNER, F. JAMES JR.  ...      WI      53051.0
        4366  H8WY00148        LUMMIS, CYNTHIA MARIE  ...      WY      82001.0

        [2431 rows x 15 columns]

Let's count the number of candidates, and group by state and district by aggregating like we did for the population data. We will also rename the aggregate column "num_candidates" for clarity. We start by taking only columns of interest.

        >>> dist_cand_count = house_cand_2016[["CAND_OFFICE_ST", "CAND_OFFICE_DISTRICT","CAND_ID"]].groupby(["CAND_OFFICE_ST", "CAND_OFFICE_DISTRICT"]).count().rename({"CAND_ID":"NUM_CANDIDATES"}, axis="columns")
        >>> dist_cand_count
                                             NUM_CANDIDATES
    CAND_OFFICE_ST CAND_OFFICE_DISTRICT
    AK             0.0                               11
    AL             1.0                                2
                   2.0                                5
                   3.0                                3
                   4.0                                2
    ...                                             ...
    WI             8.0                                7
    WV             1.0                                3
                   2.0                                7
                   3.0                                4
    WY             0.0                               17

    [447 rows x 1 columns]
        
Now that we have our filtered list of candidates, we need to join it to our population data. Pandas has a "merge" function for  this purpose that we'll use to merge ``dist_cand_count``, the filtered dataframe we just created, and ``dist_pop``. A join takes rows from one dataframe, matches them with rows in another dataframe based on a condition, and outputs a new "merged" dataframe. Here we will join the two dataframes on state and district_id. 

        >>> joined = pd.merge(left=dist_pop, right=dist_cand_count, left_on=["state", "district_id"], right_on=["CAND_OFFICE_ST", "CAND_OFFICE_DISTRICT"])
        >>> joined
            state  district_id  ... population  NUM_CANDIDATES
        0      AK            0  ...   739795.0              11
        1      AL            1  ...   713410.0               2
        2      AL            2  ...   673776.0               5
        3      AL            3  ...   710488.0               3
        4      AL            4  ...   685553.0               2
        ..    ...          ...  ...        ...             ...
        430    WI            8  ...   732402.0               7
        431    WV            1  ...   611376.0               3
        432    WV            2  ...   621635.0               7
        433    WV            3  ...   582846.0               4
        434    WY            0  ...   579315.0              17

        [435 rows x 5 columns]
        
Now let's find the top 10 districts that have the fewest people per candidate. We do this by adding an additional column dividing population by the number of candidates, ordering by it, and selecting the top 10. Let's also remove the district description for convenience.

    >>> most_cand_districts = joined[["state", "district_id", "population", "NUM_CANDIDATES"]]
    >>> most_cand_districts.population/most_cand_districts.NUM_CANDIDATES
    0       67254.090909
    1      356705.000000
    2      134755.200000
    3      236829.333333
    4      342776.500000
           ...
    430    104628.857143
    431    203792.000000
    432     88805.000000
    433    145711.500000
    434     34077.352941
    Length: 435, dtype: float64
    
Now we'll add our new column to our data frame, and sort on it.

        >>> most_cand_districts["per_capita_cand"] = joined.population/joined.NUM_CANDIDATES
    >>> most_cand_districts

        state  district_id  population  NUM_CANDIDATES  per_capita_cand
    0      AK            0    739795.0              11     67254.090909
    1      AL            1    713410.0               2    356705.000000
    2      AL            2    673776.0               5    134755.200000
    3      AL            3    710488.0               3    236829.333333
    4      AL            4    685553.0               2    342776.500000
    ..    ...          ...         ...             ...              ...
    430    WI            8    732402.0               7    104628.857143
    431    WV            1    611376.0               3    203792.000000
    432    WV            2    621635.0               7     88805.000000
    433    WV            3    582846.0               4    145711.500000
    434    WY            0    579315.0              17     34077.352941

    >>> most_cand_districts = most_cand_districts.sort_values("per_capita_cand")[:10]
        >>> most_cand_districts
             state  district_id  population  NUM_CANDIDATES  per_capita_cand
        305    OH            8    730445.0              28     26087.321429
        359    TN            8    716130.0              24     29838.750000
        245    NC           13    781657.0              25     31266.280000
        434    WY            0    579315.0              17     34077.352941
        195    MD            8    761623.0              20     38081.150000
        191    MD            4    761353.0              18     42297.388889
        104    FL           18    772184.0              18     42899.111111
        128    HI            1    714328.0              16     44645.500000
        87     FL            1    770361.0              17     45315.352941
        283    NY           13    802800.0              17     47223.529412


So we can see that Ohio's 8th District had the lowest population per candidate.
Of course we could then go on to find the candidates, find out how much funding they received for their campaigns, etc. Maybe there is a particular reason there were so many candidates in these elections?

As it turns out data actually covers several elections! For instance, there was a special election in June to fill the seat left when Speaker John Boehner retired in late 2015 and another regular election in November. Normally we would go back and correct for this error, but for the sake of brevity we'll leave it here.

One last cool thing we can do with Pandas is quickly display plots. Let's create, save, and view a plot from the data we just generated.

       >>> most_cand_districts.set_index(["state", "district_id"]).plot.bar(y="per_capita_cand")
       >>> plt.savefig("per_capita_cand.png")
       
Have a look at the png you just created, it should show a bar plot of the population per candidate top 10 district
If you did run the first line in a jupyter notebook it even displays the plot for you!

There are a lot of things you can do with Pandas that we have not covered, including different kinds of aggregation, plots, joins, input and output formats, etc. You are encouraged to use online resources to explore this for yourself when completing the take-home part of this lab.

### SQL

While Pandas is undoubtedly a useful tool and is great for exploring small datasets. There are a number of cases where it may not be the right tool for the task. 

Pandas runs exclusively in memory. With even moderate sized data you may exceed available memory. Additionally, pandas materializes each intermediate result, so the memory consumption can easily reach several times your input data if you are not very careful. Materializing after each operation is also inefficient, even when data fits in memory. If you want to save results, you have to manage a set of output files. With small data sets like we show in this lab, this is not a problem, but as your datasets grow larger or more complex this becomes an increasingly difficult task.

Furthermore, above we had to define all of the physical operations to transform the data. Choosing to or add or remove columns, the order to apply filters, etc.

An alternative to this approach is to use a Database Management System (DBMS) like Postgres or SQLite that supports a declarative query language. Unlike Pandas, a DBMS can usually store data that far exceeds what you can hold in memory. Users most often interact with DBMSs through a declarative query language, typically a dialect of SQL. Unlike pandas, in SQL you define what data to retrieve, instead of the physical operations to retrieve it. This allows the DMBS to automatically optimize your query, choosing the order to apply filters, how to apply predicates, etc.

However, using a DBMS is typically a little harder to get going with. You have to define a schema for the tables you work with, and load all the data in before you can start querying it. If you are doing a one off analysis on some small CSV you downloaded, it is probably easier to use Pandas. If you have some special operation that the DBMS does not natively support, a linear regression for instance, doing this inside a DBMS can be cumbersome. 

In this section we will introduce you to a simple DBMS called SQLite. Perhaps the [2nd most deployed software package](https://www.sqlite.org/mostdeployed.html) of all time! Unlike most DBMSs which run all the time and are accessed over a network. SQLite runs as a library in the same process as your program and stores all it's state in a single file. This makes it easy to deploy, use, and play around with SQL.


#### 1. Reading and parsing files

We give you a schema and a script (``load_data.sql``)to load the CSVs into tables in a SQLite database. 

In the bash shell (in the container), load the data into a new database named ``lab1.sqlite`` using the following command.

```bash
        root@c76e03a4b65e:/lab1# sqlite3 lab1.sqlite < load_data.sql
```

Now let's open a sqlite shell and have a look at our data. The ``-column -header`` settings pretty print the output into columns with a header. We can see the tables loaded into the database by running ``.tables`` and the schema of these tables with ``.schema [tablename]``. We will then run our first sql query to fetch the first few rows of the district population table ``dist_pop``. Note that typically table names, column names, and SQL keywords are not case sensitive.

        root@c76e03a4b65e:/lab1# sqlite3 lab1.sqlite -column -header
        SQLite version 3.22.0 2018-01-22 18:45:57
        Enter ".help" for usage hints.
        sqlite> .tables
        cand_summary  candidate     dist_pop      pac_summary
        sqlite> .schema dist_pop
        CREATE TABLE dist_pop(
          "state" char(2),
          "district_id" INT,
          "district name" varchar(200),
          "population" LONG
        );
        sqlite> SELECT * FROM DIST_POP LIMIT 10;
        state       district_id  district name                                               population
        ----------  -----------  ----------------------------------------------------------  ----------
        AK          0            Congressional District (at Large) (115th Congress), Alaska  739795
        AL          1            Congressional District 1 (115th Congress), Alabama          713410
        AL          2            Congressional District 2 (115th Congress), Alabama          673776
        AL          3            Congressional District 3 (115th Congress), Alabama          710488
        AL          4            Congressional District 4 (115th Congress), Alabama          685553
        AL          5            Congressional District 5 (115th Congress), Alabama          718713
        AL          6            Congressional District 6 (115th Congress), Alabama          700401
        AL          7            Congressional District 7 (115th Congress), Alabama          672406
        AR          1            Congressional District 1 (115th Congress), Arkansas         722287
        AR          2            Congressional District 2 (115th Congress), Arkansas         765193
    

#### 2. Filtering & Aggregation

Now let's get the same data as we did with pandas and see how it looks in SQL. For simplicity, we'll write our queries in a text file ``scratch.sql`` with a text editor and run the SQL query in the file by running ``.read scratch.sql``. I'll show both the query and results separated by ``+++++++++++++++++++++++`` below. We'll start by looking at the total population of the states again.

        SELECT 
                SUM(population)
        FROM 
                DIST_POP;

        +++++++++++++++++++++++
        
        sqlite> .read scratch.sql
        SUM(population)
        ---------------
        325025206

This matches the result we got from pandas so we are on the right track. We can also aggregate columns simultaneously.

        SELECT 
                COUNT(DISTRICT_ID),
                SUM(population)
        FROM 
                DIST_POP;

        +++++++++++++++++++++++
        
        sqlite> .read scratch.sql
        count(district_id)  sum(population)
    ------------------  ---------------
    435                 325025206

Now as above we'll group by state again.

        SELECT 
                STATE,
                SUM(population)
        FROM 
                DIST_POP
        GROUP BY 
                STATE;
        
        +++++++++++++++++++++++
        
        sqlite> .read scratch.sql
        state       SUM(population)
        ----------  ---------------
        AK          739795
        AL          4874747
        AR          3004279
        AZ          7016270
        CA          39536653
        CO          5607154
        CT          3588184
        ...
        
and order by descending population. Let's just get the first few rows by using ``LIMIT``;

        SELECT 
                STATE, 
        SUM(population)
        FROM 
                DIST_POP
        GROUP BY 
                STATE
        ORDER BY 
                SUM(population) desc
        LIMIT 10;
        
        +++++++++++++++++++++++
        
        sqlite> .read scratch.sql
        state       SUM(population)
        ----------  ---------------
        CA          39536653
        TX          28304596
        FL          20984400
        NY          19849399
        PA          12805537
        IL          12802023
        OH          11658609
        GA          10429379
        NC          10273419
        MI          9962311
        
Like we did with pandas we can also add a count of the number of districts too. How would you do that?

Now we'll build up a query that finds the house election with the highest ratio of candidates to the populace. We'll start by looking at the the ``candidate`` table, then we'll filter it down to just the 2016 house candidates using a ``WHERE`` clause.

        SELECT 
                * 
        FROM 
                CANDIDATE
        LIMIT 5; 
        
        +++++++++++++++++++++++
        
        CAND_ID     CAND_NAME     CAND_PTY_AFFILIATION  CAND_ELECTION_YR  CAND_OFFICE_ST  CAND_OFFICE  CAND_OFFICE_DISTRICT  CAND_ICI    CAND_STATUS  CAND_PCC    CAND_ST1        CAND_ST2    CAND_CITY     CAND_ST     CAND_ZIP
        ----------  ------------  --------------------  ----------------  --------------  -----------  --------------------  ----------  -----------  ----------  --------------  ----------  ------------  ----------  ----------
        H0AK00097   COX, JOHN R.  REP                   2014              AK              H            0                     C           N            C00525261   P.O. BOX 1092               ANCHOR POINT  AK          99556
        H0AL02087   ROBY, MARTHA  REP                   2016              AL              H            2                     I           C            C00462143   PO BOX 195                  MONTGOMERY    AL          36101
        H0AL02095   JOHN, ROBERT  IND                   2016              AL              H            2                     C           N                        1465 W OVERBRO              MILLBROOK     AL          36054
        H0AL05049   CRAMER, ROBE  DEM                   2008              AL              H            5                                 P            C00239038   PO BOX 2621                 HUNTSVILLE    AL          35804
        H0AL05163   BROOKS, MO    REP                   2016              AL              H            5                     I           C            C00464149   7610 FOXFIRE D              HUNTSVILLE    AL          35802     

Now we'll filter.

        SELECT
                *
        FROM
                CANDIDATE
        WHERE
                CAND_OFFICE = 'H'
                AND CAND_STATUS IN ('C', 'N')
                AND CAND_ELECTION_YR = 2016
        LIMIT 5;

        +++++++++++++++++++++++
        
        CAND_ID     CAND_NAME     CAND_PTY_AFFILIATION  CAND_ELECTION_YR  CAND_OFFICE_ST  CAND_OFFICE  CAND_OFFICE_DISTRICT  CAND_ICI    CAND_STATUS  CAND_PCC    CAND_ST1    CAND_ST2    CAND_CITY   CAND_ST     CAND_ZIP
        ----------  ------------  --------------------  ----------------  --------------  -----------  --------------------  ----------  -----------  ----------  ----------  ----------  ----------  ----------  ----------
        H0AL02087   ROBY, MARTHA  REP                   2016              AL              H            2                     I           C            C00462143   PO BOX 195              MONTGOMERY  AL          36101
        H0AL05163   BROOKS, MO    REP                   2016              AL              H            5                     I           C            C00464149   7610 FOXFI              HUNTSVILLE  AL          35802
        H0AL07086   SEWELL, TERR  DEM                   2016              AL              H            7                     I           C            C00458976   PO BOX 196              BIRMINGHAM  AL          35201
        H0AR01083   CRAWFORD, ER  REP                   2016              AR              H            1                     I           C            C00462374   34 CR 455               JONESBORO   AR          72404
        H0AR03055   WOMACK, STEV  REP                   2016              AR              H            3                     I           C            C00477745   134 N PLEA              ROGERS      AR          727560701


Now We'll count the candidates in each state and district.

        SELECT
                CAND_OFFICE_ST,
                CAND_OFFICE_DISTRICT,
                COUNT(*) as NUM_CANDIDATES
        FROM
                CANDIDATE
        WHERE
                CAND_OFFICE = 'H'
                AND CAND_STATUS IN ('C', 'N')
                AND CAND_ELECTION_YR = 2016
        GROUP BY
                CAND_OFFICE_ST,
                CAND_OFFICE_DISTRICT
        LIMIT 10;
        
        +++++++++++++++++++++++
        
        CAND_OFFICE_ST  CAND_OFFICE_DISTRICT  NUM_CANDIDATES
        --------------  --------------------  --------------
        AK              0                     11
        AK                                    1
        AL              1                     2
        AL              2                     5
        AL              3                     3
        AL              4                     2
        AL              5                     2
        AL              6                     2
        AL              7                     2
        AR              1                     2

But what is going on with Alaska?! As it turns out, there are errors in the data set that we didn't notice before. Some districts are missing in the publicly released government data! We will cover dealing with dirty data and missing values later in the class, so for now we'll just ignore this and proceed with joining this table with the district population table. 


#### 3. Joining

Below are a couple ways of dealing with this show a couple of ways of doing this. We can do this with a subquery, logically similar to what we did in Pandas.

        SELECT
                state, 
                district_id, 
                num_candidates, 
                population/num_candidates as per_capita_cand
        FROM
                (SELECT
                        CAND_OFFICE_ST,
                        CAND_OFFICE_DISTRICT,
                        COUNT(*) as NUM_CANDIDATES
                FROM
                        CANDIDATE
                WHERE
                        CAND_OFFICE = 'H'
                        AND CAND_STATUS IN ('C', 'N')
                        AND CAND_ELECTION_YR = 2016
                GROUP BY
                        CAND_OFFICE_ST,
                        CAND_OFFICE_DISTRICT
                ) as cand_counts,
                dist_pop
        WHERE
                cand_office_st = state
                and cand_office_district = district_id
        ORDER BY
                per_capita_cand
        LIMIT 10;
                
                      
        +++++++++++++++++++++++
        

        state       district_id  NUM_CANDIDATES  per_capita_cand
        ----------  -----------  --------------  ---------------
        OH          8            28              26087
        TN          8            24              29838
        NC          13           25              31266
        WY          0            17              34077
        MD          8            20              38081
        MD          4            18              42297
        FL          18           18              42899
        HI          1            16              44645
        FL          1            17              45315
        NY          13           17              47223

But this is a bit unweidly, Let's join the two tables (with filters), inspect the output. After we'll add the group by and aggregation back in.

        SELECT state, district_id, cand_id, population
        FROM
                CANDIDATE,
                DIST_POP
        WHERE
                cand_office_st = state
                AND cand_office_district = district_id
        AND CAND_OFFICE = 'H'
        AND CAND_STATUS IN ('C', 'N')
        AND CAND_ELECTION_YR = 2016
        LIMIT 10;
                              
        +++++++++++++++++++++++
        
    state       district_id  CAND_ID     population
    ----------  -----------  ----------  ----------
    AL          2            H0AL02087   673776
    AL          2            H0AL02095   673776
    AL          5            H0AL05163   718713
    AL          7            H0AL07086   672406
    AR          1            H0AR01083   722287
    AR          3            H0AR03055   807421
    CA          7            H0CA03078   750860
    CA          11           H0CA10073   764135
    CA          3            H0CA10149   750271
    CA          9            H0CA11337   774266
        
Note that Alabama's 2nd district has 2 entries(one for each candidate), and the population is repeated for each, since each row in the dist_pop is paired with ALL rows matching the join conditions (cand_office_st = state AND cand_office_district = district_id) in the candidates table, and vice versa (though in this case districts to candidates is a one to many pairing).

Now we'll aggregate over districts to produce the same result as above.

        SELECT
                state, 
                district_id, 
                count(*) as num_candidates,
                population/count(*) as per_capita_cand
        FROM
                CANDIDATE,
                DIST_POP
        WHERE
                cand_office_st = state
                AND cand_office_district = district_id
        AND CAND_OFFICE = 'H'
        AND CAND_STATUS IN ('C', 'N')
        AND CAND_ELECTION_YR = 2016
        GROUP BY
                state, district_id
        ORDER BY
                per_capita_cand
        LIMIT 10;
                              
        +++++++++++++++++++++++
        
        state       district_id  num_candidates  per_capita_cand
        ----------  -----------  --------------  ---------------
        OH          8            28              26087
        TN          8            24              29838
        NC          13           25              31266
        WY          0            17              34077
        MD          8            20              38081
        MD          4            18              42297
        FL          18           18              42899
        HI          1            16              44645
        FL          1            17              45315
        NY          13           17              47223
    
That's about all we have to show for now, but this is just a taste of what you can do with SQL. You are encouraged to play around more as skills like manipulating dataframes and SQL are ubiquitous. Note that other DBMSs may have slightly different dialects of SQL but mostly share a common structure.


#### 4. Dynamic typing in SQLite

One final thing to discuss is a distinct feature of SQLite. Unlike most SQL DBMSs SQLite uses dynamic typing. While you define specific types in the schema, SQLite allows you to write any type of data in any column. When executing queries types are inferred by as set of rules described on the [website](https://www.sqlite.org/datatype3.html). Sometimes this "feature" manifests itself in unexpected ways.
Say we are looking for the PAC with the most debt. We might run a query like the following.

    SELECT 
        cmte_nm,
        debts_owed_by 
    FROM 
        pac_summary
    ORDER BY 
        debts_owed_by DESC
    LIMIT 1;
                              
        +++++++++++++++++++++++
        
    CMTE_NM                                            DEBTS_OWED_BY
    -------------------------------------------------  -------------
    FIRST CONGRESSIONAL DISTRICT DEMOCRATIC COMMITTEE
    
Although the CSV contains no data for this column, SQLite does not automatically set the value to NULL as would be common. We could set all these missing values to NULL, but for this quick analysis it is easier to force the type by casting ``debts_owed_by`` to an floating point value then sorting, as below.

    SELECT 
        cmte_nm,
        cast(debts_owed_by as float) as debts
    FROM 
        pac_summary
    ORDER BY 
        debts DESC
    LIMIT 1;
                              
        +++++++++++++++++++++++
        
    CMTE_NM     debts
    ----------  ----------
    DSCC        20106670.0

We can see that the Democratic Senatorial Campaign Committee ended the campaign season with the most debt of any PAC tracked in this data (at time of reporting).

### Pandas + SQL

One interesting feature of pandas allows you to run a query in a database and return the result as a dataframe, so you can get the best of both worlds!

Here is a simple python program that opens the sqlite database, reads the query from the ``scratch.txt`` file, executes the query and loads the result into a data frame

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

It will be helpful to look at the detailed descriptions of the columns on the FEC website. 
Below we describe each table briefly and link to the detailed description of each column.

With the exception of the individual contributions table that we will create below, do not modify the database file after creation.

``candidate`` contains data on each candidate who filed with the FEC in the 2016 election cycle (2015-2016). It also contains candidates from previous elections so you may have to filter by election year. Details [here](https://www.fec.gov/campaign-finance-data/candidate-master-file-description/). To get official candidates filter ``CAND_STATUS`` to include only ``C`` and ``N`` values. **Note: For all questions below on the candidate table you must filter by ``CAND_STATUS``**.

``cand_summary`` contains summary data about each candidate's campaign committee's financial filings with the FEC. More info [here](https://www.fec.gov/campaign-finance-data/all-candidates-file-description/)

``dist_pop`` contains population data estimates for 2016 from the census bureau. We generated this table. The first column contains the state, the second is the district number, or 0 for states with only 1 congressional district. The third column is a text description. The last column contains the population estimate.

``pac_summary`` contains summary financial information about political action committees. It does not contain data about candidatesMore info [here](https://www.fec.gov/campaign-finance-data/pac-and-party-summary-file-description/)

``committee`` contains detailed info about each committee raising money, including both PACs and candidates campaign committees. See [here](https://www.fec.gov/campaign-finance-data/committee-master-file-description/)

### For the following, implement them in both Pandas + SQL

1. **How many presidential candidates ran in 2016? Return a dataframe with the number. Use the candidate table. (5 pts)**

2. **What third party (not republican, democrat, or independent) fielded the most Senate candidates in 2016? Return a dataframe with the party code and the number of Senate candidates. Use the candidate table. (5 pts)**

3. **Which Super PACs (Independent expenditure-only PAC) had the most total receipts in 2016? Committee type codes are [here](https://www.fec.gov/campaign-finance-data/committee-type-code-descriptions/). Return a dataframe with comittee name and total receipts. List the top 10 ordered by total receipts.  Use the pac_summary table. (5 pts)**

4. **What were the names of candidates, their campaign committe names, and addresses of all 2016 presidential candidates, where the candidate's name contains the substring "HUCK"? Return a dataframe with the candidate name, campaign comittee name, and street address. Use the candidate and committees tables. (5 pts)**

5. **What are the names of the top 20 senate campaign committees that raised the most money per capita for a Senate race in 2016? Return a dataframe with the committee name, state, and total_receipts, and ratio of receipts per person in thir state, ordered by the per capita money raised. Use the candidate, cand_summary, committee, and dist_pop tables. (10 pts)**

6. **List the names of House campaign committees for 2016 and their associated party which raised at least $100,000 and had the lowest proportion of individual contributions to total receipts. List the lowest 10 in ascending order. Return a dataframe with candidate name, party code, individual contributions, total_receipts, and ratio of individual contributions to total receipts. Use the cand_summary, and candidate tables. (10 pts)**

7. **What is the ratio of individual contributions to total receipts in 2016 senate races by party? List the top 10 parties in descending order by their rate of individual contributions to total receipts. Return a data frame with the party code, individual contributions, total receipts, and ratio. Use the cand_summary and candidate tables. (15 pts)**


### For the rest, implement in SQL only

For the following queries you will need to download the individual contributions data from the FEC. This data lists all contributions from individuals and corporations exceeding $200 per election (as required by federal law). See [here](https://www.fec.gov/campaign-finance-data/contributions-individuals-file-description/) for a description of the data. Available in compressed format [here](https://www.fec.gov/files/bulk-downloads/2016/indiv16.zip). The file is about 2GB so it may take some time to download. Unzip and place the ``itcont.txt`` file in the ``data`` directory. In the container, load the data into the database by running ``sqlite3 lab1.sqlite < load_indiv_contrib.sql``. This may take a few minutes depending on your disk.

This will load the data into the ``indiv_contrib`` table in SQL. 

For the remaining questions you only need implement them with SQL, since you are likely to run out of memory with Pandas.
These queries may take significantly longer than previous queries.


8. **Which state had the most total contributions from individuals (as listed in the large individual contributions table)? See the entity type field. Your query should return a relation with columns for state and total contributions. Use the indiv_contrib table.(5 pts)**

9. **Which states had the most contributions from individuals (with proper entity type) per capita to Super PACs (see transaction type)? List the top 5 with their contributions per person. Return a dataframe with the name of the state, and a sum of individual contributions. use the indiv_contrib and dist_pop tables.(10 pts)**

10. **Which candidates for senate in 2016 had the most contributions from individuals (listed in the individual contributions table) with an address outside the state of the race? List the candidate, the state, and the total amount for the top 5 races. Use the indiv_contrib, candidate, and cand_summary tables.(15 pts)**

11. **Finally, come up with a question over the data provided and write a SQL query to answer it. Your query must use data from at least two tables and have a group by and aggregate. Finally output a plot of your results. Include your question, and plot in the submitted PDF. (10 pts)**

### Reflection

12. **Reflect on the experience of using Pandas and SQL. What did you prefer to do in Pandas, what was easier in SQL. Describe in a few sentences. (5 pts)**

### Feedback
13. **(optional, 0 pts) If you have any comments about this lab, or any thoughts about the class so far, we would greatly appreciate them.  Your comments will be strictly used to improve the rest of the labs and classes and have no impact on your grade.**

Some questions that would be helpful:

* Is the lab too difficult or too easy?  
* Did you look forward to any exercise that the lab did not cover?
* Which parts of the lab were interesting or valuable towards understanding the material?
* How is the pace of the course so far?

### Submission Instructions

Sign up with gradescope for the course using your MIT account and the course sign up code **9J4JWK**

The lab is due at 11:59pm Wednesday September 18, 2019.

The submission comes in two parts. 

First create a **private** repository on GitHub (either Public github.com or MIT github at github.mit.edu) for you and your partner to upload your code. Create a file ``students.txt`` in the ``lab_1`` directory that lists the MIT Kerberos id (i.e. the username that comes before your @mit.edu email adddress). of you and your partner, one per line. commit and push your queries.py and all the sql queries in the ``queries`` subdirectory. Add the TAs for the course as collaborators on github.com (Usernames: MattPerron and jmftrindade) or github.mit.edu (Usernames: mperron and jfon).
Note that we will only look at commits made before the deadline.

In addition, submit the answers to each question (in some tabluar form. Monospaced fonts copied from the command line are fine.) as a PDF. Each answer should start a new page. Please include at the top of each problem both students' names, MIT ids, a link to the repository of your code, and the commit hash you are submitting (By running ``git log | head -n 1`` outside the container).
