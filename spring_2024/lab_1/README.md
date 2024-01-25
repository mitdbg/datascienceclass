# Lab 0: Setting Up Your Environment

* **Learning Objective**: Learn to connect to a remote server to work on this lab.
* **Deliverables**: Ability to `ssh` into your assigned EC2 instance (i.e. machine), create a private mirror of the course repository, and run a simple program to test that your environment is working. We will be using pre-configured EC2 instances for (at least some of) the labs in this course to ensure that everyone has a consistent environment. You are not required to turn anything in for lab 0, but you will be responsible for raising any issues with the setup of your environment to the course TAs in a timely fashion.

## 1. Accessing Your EC2 Instance
**Please pay careful attention to security instructions (bolded and italicized) in this section.**

To access your environment, I will email each of you a username (e.g. `user123`) and a private key via Outlook. You will need the username and private key to `ssh` into an EC2 instance. Before taking any further action, please make sure you adhere to the following guidelines:
1. ***Do not upload your private key to Github (or any other third-party service).*** Even though you will create a private mirror of this Github repo (more details below), it is still good practice to never push your key(s) to services such as Github. ***If you do this by accident -- do not panic***, just email the course staff as soon as possible so we can delete the compromised key and issue you a new one.
2. ***Only share your private key with a project partner via MIT's Slack or MIT's Outlook service (both encrypt data in transit). Do not share your key with anyone else.***

With these guidelines in mind, please open the email titled "Accessing Your 6.S079 Environment" from `mdrusso@mit.edu`. Make note of your username, the hostname of the machine you are supposed to access (read the email), and download the attached .pem key file. It is generally good practice to store your ssh key in the `~/.ssh/` directory on your laptop:
```sh
# if ~/.ssh doesn't already exist on your laptop, you should first run `mkdir ~/.ssh`
$ mv ~/Downloads/user123.pem ~/.ssh/
$ chmod 400 ~/.ssh/user123.pem
```
The second command restricts the file's access permissions to be read-only. We strongly recommend that you create an entry in your `ssh` config to simplify your `ssh` command:
```
# Optional, but recommended:
# create an ssh config if you don't already have one
$ touch ~/.ssh/config

# add (or append) the following entry to the file:
# 
Host datascience
  HostName ec2-12-3-45-678.compute-1.amazonaws.com  # substitute with your EC2 hostname
  User user123                                      # substitute with your username
  IdentitiesOnly=yes
  PreferredAuthentications publickey
  PasswordAuthentication no
  StrictHostKeyChecking no
  IdentityFile ~/.ssh/user123.pem                   # substitue with path to your .pem key
```
As a final reminder: please make sure that you set the `HostName` based on the machine you were assigned to in the "Accessing Your 6.S079 Environment" email. It is important for us to evenly distribute students to machines to minimze the likelihood that any one machine is overloaded at a given time. To summarize, if the number in your username modulo 3 equals:
- 0 --> use instance: `ec2-11-1-11-11.compute-1.amazonaws.com`
- 1 --> use instance: `ec2-22-2-22-22.compute-1.amazonaws.com`
- 2 --> use instance: `ec2-33-3-33-33.compute-1.amazonaws.com`

For example, `user123` would compute `123 % 3 = 0` and set their HostName to be `ec2-11-1-11-11.compute-1.amazonaws.com`.

To `ssh` to your machine you can run the following:
```sh
# assuming you created an entry in your ~/.ssh/config:
$ ssh datascience

# if you did not create an entry in ~/.ssh/config:
$ ssh -i path/to/user123.pem user123@ec2-11-1-11-11.compute-1.amazonaws.com
```

Finally, if you are working with a project partner you may choose to use just one of your usernames so that you can both work on the same copy of code. To do this, you will need to share your private key with your project partner ***by sending it to them via MIT's Slack or MIT's Outlook service***. Details for how to submit your code as a group will follow at the end of this README.

## 2. Setting Up Course Environment
In this section you will create a **private** mirror of the course repository under your user account on the EC2 instance. The steps involved are somewhat tedious, but you will only need to do them once, and then you will be able to `git pull` all future labs directly to your machine.

1. To begin, you'll need to go to Github and create an empty **private** repository (see reference image below):
- Do *not* add a README, gitignore, or license; this may create conflicts later
- Be sure to select the option to make the repository **private** (it is public by default)
- [Click here to create Github repo](https://github.com/new)
- Click the "Create Repository" button at the bottom of the page (not shown in image)

![create-repo](../readme-imgs/create-repo.png)

2. On the page for your repository, copy and store the SSH URL for your repository (see image below) you will need this in step 4.
![repo-ssh](../readme-imgs/repo-ssh.png)

3. We'll now create an SSH key and add it to your Github account. First, `ssh` to your EC2 instance, create a key-pair, and start the `ssh-agent`. Then, copy the public key and add it to your Github profile. See the code block below for detailed instructions. Finally, [follow Github's instructions here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account) for adding the public key to your Github profile. (When adding the key, keep the default "Authentication Key").
```bash
# ssh to EC2
$ ssh datascience

# create key-pair and start ssh-agent;
# use your github email address; just hit enter three times when prompted
$ ssh-keygen -t ed25519 -C "your_github_email@example.com"
$ eval "$(ssh-agent -s)"

# print the public key so you can copy it
$ cat ~/.ssh/id_ed25519.pub

# Finally, follow the instructions linked above to add this key to your Github profile.
```

4. Now we're ready to create our private mirror. On the EC2 instance, execute the following:
```bash
# on EC2 instance;
# clone the course repository
$ git clone --bare https://github.com/mitdbg/datascienceclass.git
$ cd datascienceclass.git

# push this to the private repository you created in step 1.
# you will need to change the URL to match what is shown by the SSH
# tab in your empty repository (see image in step 2.) 
$ git push --mirror git@github.com/your-github-username/your-private-repo.git

# remove the public course repository
$ cd ..
$ rm -rf datascienceclass.git

# now clone your private repository
$ git clone git@github.com/your-github-username/your-private-repo.git
$ cd your-private-repo/spring_2024/lab_1/
```

At this point you should be working on your own copy of the course repository. In the next sub-section we'll show how to (1) make and commit changes to your repository, and (2) pull new updates from the course repository into your private mirror.

### Committing Changes and Pulling Updates
As you work on the lab you should commit your changes to your remote repository frequently. To do so, simply make changes as usual and then push them to the `origin` remote repository:
```bash
# From inside your mirror repo
$ touch file.txt
$ git add file.txt
$ git commit -m "adding file.txt"
$ git push origin master # or your branch name
```
If you followed the steps above, `origin` will point to your remote private repository. In order to pull updates from the course repository you'll need to add a new remote repo which we'll call `public`:
```bash
# From inside your mirror repo;
# add remote repository `public` to track course repo
$ git remote add public https://github.com/mitdbg/datascienceclass.git

# pull changes from course repo; creates a merge commit
$ git pull public master

# ...resolve any merge conflicts...

# push new changes from course repo to your private mirror
$ git push origin master # or your branch name
```

### Basic Workflow for Developing on Remote Server
The most barebones way to develop on a remote server is to use a text editor such as `vim` or `emacs` to edit files directly in the terminal. However, many programmers prefer to use an IDE such as VSCode, Atom, Sublime, etc. to help them write programs. One simple way to accomplish this is to create a clone of a repository on one's local machine where they can edit files in their preferred IDE. Once changes are made, they can be committed and pushed from the local machine and then pulled down and run on the remote server. This workflow looks like the following:
```bash
# In terminal 1, on your local machine;
# clone your private mirror
$ git clone git@github.com/your-github-username/your-private-repo.git
$ cd your-private-repo/spring_2024/lab_1/


# push changes to your private repo from local
$ touch script.py
# ... make code changes ...
$ git add script.py
$ git commit -m "made change to script.py"
$ git push

# In terminal 2, which has an ssh session open to the remote server;
# pull (and run) changes that were pushed from local
$ git pull
$ python script.py
```

### Optional: Setup Remote Development for VSCode
The downside of the basic workflow described above is that it can be tedious to constantly push and pull changes, especially when debugging minor issues. As a result, we recommend that:
1. Students check if their preferred IDE supports remote SSH development, or
2. Students use VSCode and its remote development functionality if they don't already have a preferred IDE

The download page for VSCode and instructions for setting up remote development can be found at the following links:
- VSCode download: https://code.visualstudio.com/download
- Remote Development Setup: https://code.visualstudio.com/docs/remote/ssh

If you would like help with setting up remote development with VSCode, please come to my (Matthew Russo)'s office hours, or speak with me after class.

## 3. Setup Lab 1 Environment
In this section you will execute a setup script to prepare your python virtual environment. You'll then write and execute a simple python script to ensure that your environment is working.

Inside the `spring_2024/lab_1/` directory of your repository you should see a script called `setup.sh`. Simply navigate into that directory and execute the script as follows:
```bash
# on the EC2 machine
$ cd spring_2024/lab_1/
$ chmod u+x setup.sh
$ ./setup.sh
```
The script may take a few minutes to complete, as it will install and setup a virtual environment to house your python dependencies. Once the script has finished you should see a virtual environment has been created in a directory called `venv`.
```bash
# on the EC2 machine
$ ls
TODO
```

Finally, you can activate your virtual environment to start working, as it has all of the dependencies for this lab:
```bash
$ source venv/bin/activate
$ # begin working on the lab
```
We've included a rule in the repository's `.gitignore` which should prevent your virtual environment from being included in changes that you push to your remote repository. If for any reason you see `git` suggesting that you could/should push your `venv/` folder, we would advise you not to push it. We recommend this because virtual environments are relatively large and users should be able to recreate a virtual environment from a `requirements.txt`, `pyproject.toml`, or similar file which specifies all of a project's dependencies.

# Lab 1: Basic Tools (SQL / Pandas)

* **Learning Objective**: Learn to load data and manipulate it using both Pandas and SQL
* **Deliverables**: Students will submit python source code, SQL queries, and answer some questions. Answers will be submitted through Gradescope.

This lab will use both Pandas and SQL to explore IMDB data from 2015 onwards.

## Part 1. A brief walkthrough of tools
**To get started, run ``bash setup.sh`` in the container. This installs some missing dependencies and downloads data files.**

### Pandas
One of the most popular tools for working with relatively small datasets (i.e. that fit in the main memory of a single machine) is a python library called Pandas. Pandas uses an abstraction called dataframes to manipulate tabular data. It natively supports reading data from a variety of common file formats including CSVs, fixed-width files, columnar formats, HDF5, and JSON. It also allows you to import data from common database management systems (DBMSs). A comprehensive list is [here](https://pandas.pydata.org/pandas-docs/stable/reference/io.html).

#### 1. Reading and parsing files
First, lets start up the container, and have a look at the first few lines of the data file for IMDB titles.

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

Let's open a python shell (in our container), load the data and have a look. We have a file that contains all necessary imports. To launch python and automatically run these imports, type ``PYTHONSTARTUP=imports.py python3``

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
Now let's get to answering some simple questions! One obvious one is to get the average duration of the titles.
We select the `runtime_minutes` column and compute the mean over it as follows:

```py
>>> titles['runtime_minutes'].mean()
39.21965306698209
```

We can also aggregate over multiple columns simultaneously:

```py
>>> titles[["premiered", "runtime_minutes"]].max()
premiered           2029.0
runtime_minutes    43200.0
dtype: float64
```

Now let's find the length of the longest movies in each year. We'll first select the columns we want, then group rows by year, and compute the max over the groups:

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
>>> df = titles[['premiered', 'runtime_minutes', 'genres']].groupby('premiered').agg({'runtime_minutes': ['max'], 'genres': ['nunique']})
>>> df
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

After aggregation, the columns of the dataframe are in a different format: group by columns are now treated as indices and aggregate columns have a subcolumn for each aggregate. This makes them more difficult to manipulate. In this lab, the autograder expects you to restore the default format of dataframes, as follows:

```py
>>> df.columns = ['max_runtime_minutes', 'unique_genres']
>>> df = df.reset_index()
>>> df
    premiered  max_runtime_minutes  unique_genres
0        2015               6000.0           1321
1        2016               2070.0           1291
2        2017               5760.0           1281
3        2018               7777.0           1268
4        2019              28643.0           1239
5        2020              43200.0           1166
6        2021               6000.0           1127
7        2022                400.0            678
8        2023                240.0            232
9        2024                360.0             83
10       2025                125.0             30
11       2026                360.0             12
12       2027                360.0             12
13       2028                  NaN              3
14       2029                 14.0              1
```

#### 3. Joining
        
You can start to do more interesting things when you "join" data from multiple data sources together. The file ``data/ratings.csv`` contains the ratings of each title.

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

There are a lot of things you can do with Pandas that we have not covered, including different kinds of aggregation, plots, joins, input and output formats, etc. You are encouraged to use online resources to explore this for yourself when completing the take-home part of this lab.

### SQL

While Pandas is undoubtedly a useful tool and is great for exploring small datasets. There are a number of cases where it may not be the right tool for the task. 

Pandas runs exclusively in memory. With even moderately sized data you may exceed available memory. Additionally, pandas materializes each intermediate result, so the memory consumption can easily reach several times your input data if you are not very careful. Materializing after each operation is also inefficient, even when data fits in memory. If you want to save results, you have to manage a set of output files. With small data sets like we show in this lab, this is not a problem, but as your datasets grow larger or more complex this becomes an increasingly difficult task.

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
        MAX(runtime_minutes),
        COUNT(DISTINCT genres) AS num_genres -- Compute the number of unique genres.
FROM
        titles;

+++++++++++++++++++++++

sqlite> .read scratch.sql
MAX(premiered)  MAX(runtime_minutes)  num_genres
--------------  --------------------  ----------
2029            43200                 1876
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
   
and order by descending. Let's just get the first few rows by using ``LIMIT``;

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
To join two or more tables, we first list them in the `FROM` clause. We specify how to join in the `WHERE` clause. The `WHERE` clause may further contain additional filters for each individual tables.

Here is how to compute in SQL the same join we computed using pandas:

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
Common Table Expressions (CTEs) are a useful mechanism to simplify complex queries. They allow us to precompute temporary tables that can be used in other parts of the queries. While the join above is not complex enough to warrent using CTEs, we will use it as an example to get you started. Suppose that, like in our pandas example, we wanted to first compute the set of excellent ratings and the set of movies before joining them.

```sql
WITH 
excellent (title_id, rating, votes) AS ( -- Precompute excellent ratings
        SELECT * FROM ratings WHERE rating >= 9 AND votes >= 100
),
movies (title_id, primary_title, premiered) AS ( -- Precomputed movies
        SELECT title_id, primary_title, premiered FROM titles WHERE type='movie'
)

SELECT rating, votes, primary_title, premiered  -- Join them.
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

In this query, we first compute the table of excellent ratings and the table of movies using the construct `WITH table_name(column_names...) AS (query)`. We then perform the join using these temporary tables. 

#### 5. Recursive CTEs.
In addition to regular CTEs, you will need recursive CTEs to answer some of the questions in this lab. SQLite has an [excellent tutorial](https://www.sqlite.org/lang_with.html) about them. You should read up to and including section 3.2 of the tutoral. The topic is too complex for this introductory lab, but feel free to ask us questions during office hours.


#### 6. Window Functions
Whereas groupby aggregations let us aggregate partitions of the data, window functions allow us to perform computations on each partition without aggregating the data.

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

This captures the general idea behind window functions: compute a result in accordance with a certain partitioning of the data. Many more things can be done with this idea. A good tutorial can be found [here](https://mode.com/sql-tutorial/sql-window-functions/)




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

You are allowed to work in pairs for this assignment. In addition, you can lookup general SQL or Pandas functionalities on the internet, but not specific solutions to our questions.

For the rest of the lab we will ask you to answer a few questions using pandas and writing SQL queries. You will edit ``queries.py`` and fill in each function with a query to answer the question. The Pandas functions (e.g. Q1Pandas) have a space to fill in your code. Fill in SQL queries in the ``queries`` directory. Do not make other edits to the repository or database, except when instructed.


For convenience, you can run queries one at a time using the python3 queries.py -q [query_num] command to run a single query (in both Pandas and SQL, whena applicable).


In addition to your code, you will submit the results of your code for each of the questions in a PDF. Put each answer on a new page.
Detailed submission instructions are at the bottom of this document.

### Speeding up queries
If you wish to speedup some of the queries at the expanse of additional space. Run the following SQL queries:
```sql
CREATE INDEX ix_people_name ON people (name);
CREATE INDEX ix_titles_type ON titles (type);
CREATE INDEX ix_titles_primary_title ON titles (primary_title);
CREATE INDEX ix_titles_original_title ON titles (original_title);
CREATE INDEX ix_akas_title_id ON akas (title_id);
CREATE INDEX ix_akas_title ON akas (title);
CREATE INDEX ix_crew_title_id ON crew (title_id);
CREATE INDEX ix_crew_person_id ON crew (person_id);
```

### Output Format
For each question, we will specify both the order of the output columns and the order of the output rows. These must be strictly respected for the autograder to work. For Pandas, you must use `dataframe.reset_index()` before outputting the dataframe as we showed in the tutorial. It does not matter how you name the columns as long as they are in the correct order.

### Questions
#### SQL and Pandas
For each of these questions, you get half the points for getting each implementation correctly. For full credit, both implementations should be correct.

1. (Simple aggregation and ordering, 5 pts) Using the crew table, compute the number of distinct actors and actresses. Return the category (`actor` or `actress`) and the count for each category. Order by category (ascending).
2. (Simple filtering and join, 5 pts) Find the action TV shows (`titles.type=tvSeries` and `titles.genres` contains `Action`) released in 2021, with a rating >= 8 and at least 100 votes. Return title_id, name, and rating. Order by rating (descending) and then name (ascending) to break ties.
3. (Simple aggregation and join, 10 pts) Find the movie (`titles.type=movie`) with the most actors and actresses (cumulatively). If multiple movies are tied, return the one with the alphabetically smallest primary title. Return the title_id, primary title, and number of actors.
4. (Simple subquery/CTE, 10 pts) Find the movie with the most actors and actresses (cumulatively). Unlike in question (3), you should return all such movies. Again, return the title_id, primary title and number of actors. Order by primary title (ascending).
5. (Subqueries/CTEs, 10 pts) Find the actors/actresses who played in the largest number of movies. The result set may contain one or many persons. Return the category ('actor' or 'actress'), the name, and the number of appearances. Order the results by name (ascending). Use the `people` table to get the name of actors.
6. (Subqueries/CTEs, 15 pts) Find the actors/actresses with at least 5 movies that have the highest average ratings on their movies. Return the name, the number of titles and the average rating. Order the results by average rating (descending) and then name (ascending).

#### SQL Only
7. (SQL Only: Simple window function, 5 pts) Rank the movies, TV Shows released in 2021 with a rating >= 8 with at least 100 votes. Movies and TV shows should receive separate rankings. Order by type (`movie` or `tvSeries`, ascending), then rating (descending), then name (ascending) to break ties. Return the type, name, rating and rank.
8. (SQL Only: Window Functions, 10 pts) For each year, find the top 3 actors that appear in the most number of above average movies (with a rating >= 5). If multiple actors are tied in the top, return all of them. Return the year, the name, number of above average movies, and the ranking. Sort by year (ascending), ranking (ascending) and name (ascending) to break ties. 
9. (SQL Only: Recursive CTEs, 10 pts) Find the genres of movies with the highest average rating. Note that the text `Action,Thriller` should be treated as two genres (`Action` and `Thriller`). You may reuse the [recursive CTE csv parser](https://stackoverflow.com/questions/24258878/how-to-split-comma-separated-value-in-sqlite). Return the genre and the average rating. Sort by average rating (descending) and genre (ascending) to break ties. Be sure to filter out the null genre (`genres='\N'`).
10. (SQL Only: Recursive CTEs, 10 pts) Degrees of separation. Recursively compute the set of actors that contains:
* Samuel L. Jackson (person_id='nm0000168')
* Actors who played in a movie with Samuel L. Jackson in 2021, played with someone who played with him in a movie in 2021, and so on.
Return the person_id, and the name ordered by name. This query should take no longer than 5 minutes to run (ours takes 2.5 minutes). Make sure you understand the difference between `UNION` and `UNION ALL` in recursive CTEs.

### Submission Instruction
Make sure you are registered on Gradescope for this class. The course ID is `ZRE8VN`.

To submit responses:
```sh
# Generate response for a query in the submission/ folder.
# Do this for every query once implemented.
python queries.py -q [query_num] -s
# Zip the submission folder
cd submission
zip submission.zip *.csv
```

Submit the generated `submission.zip` file to Gradescope.
