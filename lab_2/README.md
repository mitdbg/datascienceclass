Table of Contents
=================
- [Lab 2: Data Cleaning and Wrangling](#lab-2-data-cleaning-and-wrangling)
  * [1. Accessing Your EC2 Instance](#1-accessing-your-ec2-instance)
  * [2. Additional Setup](#2-additional-setup)
  * [3. Lab 2 Content](#3-lab-2-content)
    * [Datasets](#datasets)
    * [Running Updates](#running-updates)
    * [Part 1: Data Cleaning Using Unix Tools (30 Points)](#part-1-data-cleaning-using-unix-tools-30-points)
      * [General-Purpose Tools](#general-purpose-tools)
      * [Tool 1: `grep`](#tool-1-grep)
      * [Tool 2: `sed`](#tool-2-sed)
      * [Tool 3: `awk`](#tool-3-awk)
      * [Examples](#examples)
    * [Part 1: Questions](#part-1-questions)
    * [Part 2: Missing Value Imputation (20 Points)](#part-2-missing-value-imputation-20-points)
      * [Exploring the Data](#exploring-the-data)
    * [Part 2: Questions](#part-2-questions)
    * [Part 3: Working across formats (50 Points)](#part-3-working-across-formats-50-points)
    * [Part 3: Questions](#part-3-questions)
  * [4. Submission Instructions](#4-submission-instructions)
    * [Before You Submit: Push Your Changes](#before-you-submit-push-your-changes)
    * [Submission](#submission)
    * [Submitting as an Individual](#submitting-as-an-individual)
    * [Submitting as a Group](#submitting-as-a-group)

---
# Lab 2: Data Cleaning and Wrangling
---

* **Assigned: Feb 22nd** 
* **Due: March 05, 11:59:00 PM ET.**
* **Deliverables**: You will learn to write bash scripts and python scripts to perform data cleaning, deal with missing values, and perform end-to-end data analysis. Solutions will be uploaded to gradescope for grading. 

In this lab, you will deal with the all-too-frequent problem of bringing your data into a format that makes analysis possible. The 3 parts of the lab will take you through several  tasks commonly involved in this process:
- In part 1, you will use the command line tools `sed` and `awk` to efficiently clean and transform data originating in inconvenient formats.
- In part 2, you will deal with the issue of missing values, examining appropriate ways to impute them based on your intended analysis.
- In part 3, you will perform analysis tasks that involve datasets in 3 different formats: a simple text file, a JSON file and a CSV file.

Let's get started!

## 1. Accessing Your EC2 Instance
First, please read the post announcing the release of Lab 2 on Piazza (TODO: link to post when lab is released). If the number in your username modulo 2 equals:
- 0 --> use instance: `ec2-3-133-220-165.us-east-2.compute.amazonaws.com`
- 1 --> use instance: `ec2-18-218-56-187.us-east-2.compute.amazonaws.com`

For example, `user123` would compute `123 % 2 = 1` and set the HostName in their `~/.ssh/config` entry for `datascience` to be `ec2-18-218-56-187.us-east-2.compute.amazonaws.com`.

To `ssh` to your machine you can run the following:
```sh
# assuming you created an entry in your ~/.ssh/config:
$ ssh datascience

# OR, if you did not create an entry in ~/.ssh/config:
$ ssh -i path/to/user123.pem user123@ec2-12-3-45-678.compute-1.amazonaws.com
```

[*Back to top*](#table-of-contents)

## 2. Additional Setup
Execute the following commands in order to pull lab 2 down onto your machine:
```bash
# ssh to EC2
$ ssh datascience

# navigate to your private repository
$ cd your-private-repo

# fetch and merge lab 2
$ git checkout main
$ git fetch upstream
$ git merge upstream/main
```
If you also have a clone of your private repo on your local machine, be sure to update it as well using the "fetch and merge" instructions above. Remember than you can then commit any changes to your private remote repository by running:
```bash
# add any new changes and make a commit message
$ git add some-file.txt another-file.txt
$ git commit -m "adding my files"

# push new changes from course repo to your private mirror
$ git push origin main
```

Finally, inside the `lab_2` directory of your repository you should see a script called `setup.sh`. Simply execute the script as follows:
```bash
# --- on the EC2 machine ---
$ cd your-private-repo/lab_2/
$ bash setup.sh
```

[*Back to top*](#table-of-contents)

## 3. Lab 2 Content

### Datasets

The `lab2` directory contains 11 datasets under the `data` subdirectory. Here is a quick overview:


1. `crime-clean.txt`: A dataset of the reported crime rate in each US state + D.C., for each year between 2004 and 2008, inclusive.

2. `crime-unclean.txt`: A version of `crime-clean.txt` where some data is missing.

3. `labor.csv`: A small dataset of labor information, with each field of each record presented on a separate line.

4. `lizzo_appearances.json`

A JSON file scraped from Wikipedia containing a list of appearances of the artist [Lizzo](https://en.wikipedia.org/wiki/Lizzo) at different events.  Sample snippet:

```
{"Year":"2014","Title":"Made in Chelsea: NYC","Notes":"Season 1, episode 4"},{"Year":"2014","Title":"Late Show with David Letterman","Notes":"Season 22, episode 29"}
```
5. `salaries.csv`: A dataset resulting from a [web survey of salaries](https://data.world/brandon-telle/2016-hacker-news-salary-survey-results) for different positions.

6. `synsets.txt`: 
A dataset of synonyms and their meanings. Each line contains one synset with the following format:
```
ID,<synonyms separated by spaces>,<different meanings separated by semicolons>
```

7. `top2018.csv`: A CSV file containing the [top 100 Spotify songs in 2018](https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018) with attributes such as "danceability", "loudness", "time_signature", etc.

8. `twitter.json.gz`: A dataset of tweets, compressed using `gzip`.

9. `wmbr.txt`
A text file containing days when songs were played at [WMBR, MIT's student radio](https://wmbr.org/), for a subset of DJs and Artists.  Sample snippet:

```
Date:Nov 22, 2017
Artist:Willow Smith
Song:Wait a Minute [slowed]
Album: 
Label: 
Show:[insert label here]
DJ:Joana
...
Date:Jun 14, 2019
Artist:Billie Eilish
Song:Bury A Friend
Album: 
Label: 
Show:BABEs: The Radio Experience
DJ:Claire Traweek
```

10. `worldcup-semiclean.txt`: A partially cleaned-up version of `worldcup.txt`, after removing wiki source keywords and other formatting.

11. `worldcup.txt`: A snippet of the following Wikipedia webpage on the [FIFA (Soccer) World Cup](https://en.wikipedia.org/wiki/FIFA_World_Cup#Teams_reaching_the_top_four), corresponding to the table toward the end of the page that lists teams finishing in the top 4. The data only includes World Cup 2018 and before.
[*Back to top*](#table-of-contents)

### Running Updates
This section is a rough copy of the running updates post on Piazza. We will do our best to keep the Lab README as up-to-date as possible with the [Piazza post](https://piazza.com/class/ls1w8zxfau34kg/post/112).

#### General
1. See [this follow-up](https://piazza.com/class/ls1w8zxfau34kg/post/118_f2) for a handy script to automatically run, zip, and copy down your solution. (You are meant to run this script on your local machine – i.e. your laptop).

#### Q1
1. See [this note on leading/trailing space](https://piazza.com/class/ls1w8zxfau34kg/post/114) in your solution.

#### Q2

#### Q3

#### Q4

#### Q5

#### Q6

#### Q7
1. See [this clarification](https://piazza.com/class/ls1w8zxfau34kg/post/119) on how we expect you to compute the `annual_bonus`.

#### Q8

#### Q9

#### Q10

#### Q11

#### Q12

#### Q13

### Part 1: Data Cleaning using Unix tools (30 points)

The set of three `UNIX` tools we saw in class, `sed`, `awk`, and `grep`, can be very useful for quickly cleaning up and transforming data for further analysis (and have been around since the inception of UNIX). 

In conjunction with other unix utilities like `sort`, `uniq`, `tail`, `head`, `paste`, etc., you can accomplish many simple data parsing and cleaning  tasks with these tools. 

You are encouraged to play with these tools and familiarize yourselves with their basic usage.

As an example, the following sequence of commands can be used to answer the question "Find the five twitter user ids (uids) that have tweeted the most".  Note that in the example below, we're using the `zgrep` variant of `grep`, which allows us to operate over [gzipped data](https://en.wikipedia.org/wiki/Gzip).
```bash
$ zgrep "created\_at" ../data/twitter.json.gz \
   | sed 's/"user":{"id":\([0-9]*\).*/XXXXX\1/' \
   | sed 's/.*XXXXX\([0-9]*\)$/\1/' \
   | sort \
   | uniq -c \
   | sort -n \
   | tail -5
```

The first stage (`zgrep`) discards the deleted tweets, the `sed` commands extract the first "user-id" from each line, `sort` sorts the user ids, and `uniq -c` counts the unique entries (*i.e.,* user ids). The final `sort -n | tail -5` return the top 5 uids.

Note that, combining the two `sed` commands as follows does not do the right thing -- we will let you figure out why.

```bash
$ zgrep "created\_at" ../data/twitter.json.gz \
  | sed 's/.*"user":{"id":\([0-9]*\).*/\1/' \
  | sort \
  | uniq -c \
  | sort -n \
  | tail -5
```

To get into some details:

#### General-purpose tools

- `cat` can be used to list the contents of a file:

```bash
$ cat ../data/worldcup-semiclean.txt
!Team!!Titles!!Runners-up!!Thirdplace!!Fourthplace!!|Top4Total
|-
BRA
|1958,1962,1970,1994,2002
|1950,1998
...
```

- `tail` is in the same vein, but provides the convenient option of specifying the (1-indexed) starting line. This can be useful when e.g. omitting the header of a CSV file:

```bash
$ tail +3 ../data/worldcup-semiclean.txt
BRA
|1958,1962,1970,1994,2002
|1950,1998
...
```

- Similar to how `tail` can help us omit lines, `cut` can help us omit fields. We can use `-d` to specify the delimiter and `-f` to pick one or more fields to print. By using `--complement -f` we can instead specify which field(s) to *not* print.

```bash
$ cut -d "," -f 1 ../data/synsets.txt
1
2
3
4
...
```

-  `sort` can be used to sort the lines of a text file. It provides many useful flags for specifying things like case sensitivity, sort key location (i.e. which field in each line to sort by) etc. You can see the complete list of flags using `sort --help`

- `uniq` can be used to remove *adjacent* duplicate lines from a file. Specifying the flag `-c` will prepend the count of such duplicates to each printed line.

- `wc` can be used to count characters (`-c`), words (`-w`) or lines (`-l`) in a text file.

#### Tool 1: `grep`

The basic syntax for `grep` is: 
```bash
$ grep 'regexp' filename
```
or equivalently (using UNIX pipelining):
```bash
$ cat filename | grep 'regexp'
```

The output contains only those lines from the file that match the regular expression. Two options to grep are useful: `grep -v` will output those lines that *do not* match the regular expression, and `grep -i` will ignore case while matching. See the manual (`man grep`), [Lecture 4 readings](http://dsg.csail.mit.edu/6.S080/sched.php), or online resources for more details.

#### Tool 2: `sed`
Sed stands for _stream editor_. Basic syntax for `sed` is:
```bash
$ sed 's/regexp/replacement/g' filename
```

For each line in the input, the portion of the line that matches _regexp_ (if any) is replaced with _replacement_. `sed` is quite powerful within the limits of operating on single line at a time. You can use `\(\)` to refer to parts of the pattern match. In the first sed command above, the sub-expression within `\(\)` extracts the user id, which is available to be used in the _replacement_ as `\1`. 

As an example, the command below is what we used to clean `worldcup.txt` and produce `worldcup-semiclean.txt`:

```bash
$ cat ../data/worldcup.txt \
  | sed \
    's/\[\[\([0-9]*\)[^]]*\]\]/\1/g;
    s/.*fb|\([A-Za-z]*\)}}/\1/g; 
    s/data-sort[^|]*//g;
    s/<sup><\/sup>//g;
    s/<br \/>//g;
    s/|style=[^|]*//g;
    s/|align=center[^|]*//g;
    s/|[ ]*[0-9] /|/g;
    s/.*div.*//g;
    s/|[a-z]*{{N\/a|}}/|0/g;
    s|[()]||g;
    s/ //g;
    /^$/d;' > ../data/worldcup-semiclean.txt
```

#### Tool 3: `awk`

Finally, `awk` is a powerful scripting language. The basic syntax of `awk` is: 
```bash
$ awk -F',' \
  'BEGIN{commands}
  /regexp1/ {command1}
  /regexp2/ {command2}
  END{commands}' 
```

For each line, the regular expressions are matched in order, and if there is a match, the corresponding command is executed (multiple commands may be executed for the same line). `BEGIN` and `END` are both optional. The `-F','` specifies that the lines should be _split_ into fields using the separator `','` (single comma), and those fields are available to the regular expressions and the commands as `$1`, `$2`, etc.  See the manual (`man awk`), [Lecture 4 readings](http://dsg.csail.mit.edu/6.S080/sched.php), or online resources for further details. 

#### Examples

A few examples to give you a flavor of the tools and what one can do with them. Make sure that you go through them, since some of the idioms used will be helpful for the questions that follow.

1. Merge consecutive groups of lines referring to the same record on `labor.csv` (a process sometimes called a *wrap*).

   We keep a "running record" in `combined`, which we print and re-intialize each time we encounter a line starting with `Series Id:`. For all other lines, we simply append them (after a comma separator) to `combined`. Finally, we make sure to print the last running record before returning.

```bash
$ cat ../data/labor.csv \
  | awk \
    '/^Series Id:/ {print combined; combined = $0}
    !/^Series Id:/ {combined = combined", "$0;}
    END {print combined}'
```

2. On  `crime-clean.txt`, the following command does a *fill* (first row of output: "Alabama, 2004, 4029.3"). 

   We first use `grep` to exclude the lines that only contain a comma. We then use `awk` to either extract the state (4th word) for lines starting with a capital letter (i.e. those starting with `Reported crime in ...`), or to print the state name followed by the data for lines that contain data.

```bash
$ cat ../data/crime-clean.txt \
   | grep -v '^,$' \
   | awk \
   '/^[A-Z]/ {state = $4} 
    !/^[A-Z]/ {print state, $0}'
```
    
3. On `crime-clean.txt`, the following script converts the data to table format in CSV, where the columns are `[State, 2004, 2005, 2006, 2007, 2008]`. Note that it only works assuming perfectly homogenous data (i.e. no missing/extraneous values, years always in the same order). 

   We again begin by using `grep` to exclude the lines that only contain a comma. We then use `sed` to remove trailing commas, remove the phrase `Reported crime in `, and remove the year (first comma-separated field) from the data lines. Finally, using `awk`, we print the table header and then perform a *wrap* (see example 1 above).

```bash
$ cat ../data/crime-clean.txt \
   | grep -v '^,$' \
   | sed 's/,$//g; s/Reported crime in //; s/[0-9]*,//' \
   | awk \
   'BEGIN {printf "State, 2004, 2005, 2006, 2007, 2008"} \
    /^[A-Z]/ {print c; c=$0}  
    !/^[A-Z]/ {c=c", "$0;}    
    END {print c}'
```

4. On `crime-unclean.txt` the following script performs the same cleaning as above, but allows incomplete information (*e.g.,* some years may be missing).

   We again begin by using `grep` to exclude the lines that only contain a comma. We then use `sed` to remove the phrase `Reported crime in `. Finally, using `awk`, we first split data lines into comma-separated fields (so that `$1` is the year and `$2` is the value); then, whenever we encounter such a line while parsing, we place the value into `array` using the year as an index; finally, whenever we encounter a line with text, we print the previous `state` and the associated `array`, delete `array`, and remember the state in the current line for future printing.

```bash
$ cat ../data/crime-unclean.txt \
   | grep -v '^,$' \
   | sed 's/Reported crime in //;' \
   | awk -F',' \
     'BEGIN {
     printf "State, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008\n"}
     /^[A-Z]/ || /^$/ {
       if(state) {
         printf(state); 
         for(i = 2000; i <= 2008; i++) {
           if(array[i]) {
             printf("%s,", array[i])
           }
           else {
             printf("0,")
           }
         };
         printf("\n");
       } 
       state=$0; 
       delete array
     } 
     !/^[A-Z]/ {array[$1] = $2}'
```

We provided the last example to show how powerful `awk` can be. However if you need to write a long command like this, you may be better off using a proper scripting language, such as `python`!

### Part 1: Questions

**NOTE: for each question you can assume we will run the script from the root of the `submission/` directory (e.g., we will execute `./q1.sh`). Keep this in mind when designing your script so that it reads data files from `../data/` or `qX.csv`.**

*Tip: for the EC2 environment in this class, you may want to use `sed -E` to support extended regular expressions. Note that with extended regular expressions you will not want to use `\(\)` for capture group(s). Instead simply use `()`.*

*Tip: If you're not sure how to get started, try `cat`'ing the dataset you need to process and using `head` or `grep` to filter for a subset of the lines (which will print to the terminal). Then use `grep`, `sed`, and/or `awk` to transform that subset. Once you've got something working on the subset, try it out on the full dataset.*

**Q1 (8 pts):** Starting with `synsets.txt`, write a script that uses the above tools as appropriate to generate a list of word-meaning pairs. Store the results in `q1.csv` in the `submission/` directory.

The output should look like:
```
'hood,(slang) a neighborhood
1530s,the decade from 1530 to 1539
15_May_Organization,a terrorist organization formed in 1979 by a faction of the Popular Front for the Liberation of Palestine but disbanded in the 1980s when key members left to join a faction of al-Fatah
1750s,the decade from 1750 to 1759
1760s,the decade from 1760 to 1769
1770s,the decade from 1770 to 1779
...
deuce,a tie in tennis or table tennis that requires winning two successive points to win the game
two,the cardinal number that is the sum of one and one or a numeral representing this number
2,the cardinal number that is the sum of one and one or a numeral representing this number
II,the cardinal number that is the sum of one and one or a numeral representing this number
deuce,the cardinal number that is the sum of one and one or a numeral representing this number
...
zygotene,the second stage of the prophase of meiosis
zymase,a complex of enzymes that cause glycolysis
zymase, originally found in yeast but also present in higher organisms
zymosis,(medicine) the development and spread of an infectious disease (especially one caused by a fungus)
zymurgy,the branch of chemistry concerned with fermentation (as in making wine or brewing or distilling)
```

In the dataset, there could be multiple words (space-separated) that correspond to a shared set of meanings (semicolon-separated). For example,
```
22,angstrom angstrom_unit A,a metric unit of length equal to one ten billionth of a meter (or 0.0001 micron); used to specify wavelengths of electromagnetic radiation
```
You should break them into 3x2=6 word-meaning pairs
```
angstrom,a metric unit of length equal to one ten billionth of a meter (or 0.0001 micron)
angstrom, used to specify wavelengths of electromagnetic radiation
angstrom_unit,a metric unit of length equal to one ten billionth of a meter (or 0.0001 micron)
angstrom_unit, used to specify wavelengths of electromagnetic radiation
A,a metric unit of length equal to one ten billionth of a meter (or 0.0001 micron)
A, used to specify wavelengths of electromagnetic radiation
```

Your output order for these word-meaning pairs should adhere to the order of their appearance in the dataset. For example, suppose the dataset is the following
```
17,22-karat_gold,an alloy that contains 87 per cent gold
18,24-karat_gold pure_gold,100 per cent gold
```
Your output should be
```
22-karat_gold,an alloy that contains 87 per cent gold
24-karat_gold,100 per cent gold
pure_gold,100 per cent gold
```

Save your script as `q1.sh` in the `submission/` directory and execute it to generate `q1.csv` (also in the `submission/` directory). Make sure you include comments in your script describing your approach.

*Hints for Q1: Look into `awk`'s `split` function, and `for loop` constructs ,e.g.,*
- How to use `split` to create array: [split example](https://stackoverflow.com/a/8009724).
- How to loop over array: [arrays in awk](http://www.math.utah.edu/docs/info/gawk_12.html).


**Q2 (7 pts):** Write another script that uses `q1.csv` as input and outputs a list of the first characters that appear in the words (i.e., the first column) of `q1.csv`, along with their character frequencies in descending order. Write the output to `q2.csv` in the `submission/` directory. Save your script as `q2.sh` (also in the `submission/` directory). Make sure you include comments describing your approach. Your output should look something like this:
```
17957 s
15167 c
...
```

For example, suppose `q1.csv` has the following content,
```
1530s,the decade from 1530 to 1539
angstrom, a metric unit of length equal to one ten billionth of a meter (or 0.0001 micron)
amp, "a typical household circuit carries 15 to 50 amps"
```
Then your script should output
```
2 a
1 1
```

*Hints for Q2: Look at the example in the README above for "Find the five twitter user ids (uids) that have tweeted the most". You should be able to re-use and/or modify some pieces of that script.*

**Q3 (10 pts):** Starting with `../data/worldcup-semiclean.txt`, write a script that uses the above tools as appropriate to generate output as follows and outputs it to `q3.csv` in the `submission/` directory. Each line in the output should contain a country, a year, and the position/place the country finished at the world cup in that year (if it finished within the top 4). Order your output on country (ascending), position (ascending), and then year(ascending). Your final output should **not** include a line for places in which it has not finished (e.g. you should **not** have a line like `KOR,0,1`):

```
...
BRA,1958,1
BRA,1962,1
BRA,1970,1
BRA,1994,1
BRA,2002,1
BRA,1950,2
BRA,1998,2
...
```

Save your script as `q3.sh` in the `submission/` directory. Make sure you include comments describing your approach.

*Hints for Q3: You will likely want to draw inspiration from the techniques shown in the [examples subsection](#examples). This is a tricky problem, so if you pass the autograder with a non-trivial script, you are guaranteed to get full credit. Come to OH and/or ask questions on Piazza if you're stuck!*

**Q4 (5 pts):** How often has each country finished in second place at the World Cup? Write a script to compute this, by generating output sorted by country codename (ascending) as follows and outputting it to `q4.csv` in the `submission/` directory:

```
ARG,3
BRA,2
CRO,1
...
```

Save your script as `q4.sh` (also in the `submission/` directory). Make sure you include comments describing your approach.

*Hints for Q4: Similar to Q2, look at the example in the README above for "Find the five twitter user ids (uids) that have tweeted the most". You should be able to re-use and/or modify some pieces of that script. You will also likely want to use `cut` in some way (although this is not necessary for a correct solution).*

[*Back to top*](#table-of-contents)

### Part 2: Missing value imputation (20 points)

In this part we will examine the impact of different data imputation approaches on the results of an analysis on `salaries.csv`. As is often the case when using user survey data, this dataset contains many missing values, which we must decide how to handle.

#### Exploring the data

Let's launch a python shell, import the data, and examine the resulting dataset:
```bash
user00@ip-172-31-16-69:~/6.S079-xinjing/lab_2$ source venv/bin/activate
(venv) user00@ip-172-31-16-69:~/6.S079-xinjing/lab_2$ cd submission
(venv) user00@ip-172-31-16-69:~/6.S079-xinjing/lab_2/submission$ python3
```
```python
>>> import pandas as pd
>>> data = pd.read_csv("../data/salaries.csv", encoding = "ISO-8859-1")
>>> data
     salary_id           employer_name      location_name location_state location_country  ...  signing_bonus  annual_bonus stock_value_bonus                                           comments   submitted_at
0            1                  opower  san francisco, ca             CA               US  ...         5000.0           0.0       5000 shares                                   Don't work here.  3/21/16 12:58
1            3                 walmart    bentonville, ar             AR               US  ...            NaN        5000.0             3,000                                                NaN  3/21/16 12:58
2            4      vertical knowledge      cleveland, oh             OH               US  ...         5000.0        6000.0                 0                                                NaN  3/21/16 12:59
3            6                  netapp            waltham            NaN              NaN  ...         5000.0        8500.0                 0                                                NaN  3/21/16 13:00
4           12                   apple          cupertino            NaN              NaN  ...         5000.0        7000.0            150000                                                NaN  3/21/16 13:02
..         ...                     ...                ...            ...              ...  ...            ...           ...               ...                                                ...            ...
500       1093               microsoft        redmond, wa             WA               US  ...        30000.0       10000.0              8000                                                NaN  3/21/16 14:19
501       1094               (private)         boston, ma             MA               US  ...            0.0           0.0                 0  Retirement benefits very good... ~7% to ~14% (...  3/21/16 14:22
502       1097                 dropbox      san francisco            NaN              NaN  ...        25000.0           0.0             40000                                                NaN  3/21/16 14:19
503       1098  pricewaterhousecoopers          australia            NaN               AU  ...            0.0        2000.0                 0                                                NaN  3/21/16 14:20
504       1100                   apple          sunnyvale            NaN              NaN  ...        20000.0       10000.0            100000                                                NaN  3/21/16 14:20

[505 rows x 18 columns]
```

We can now examine the degree of prevalence of null values in the dataset:
```python
>>> print(data.isnull().sum())
salary_id                      0
employer_name                  1
location_name                  0
location_state               307
location_country             253
location_latitude            253
location_longitude           253
job_title                      0
job_title_category             0
job_title_rank               362
total_experience_years        15
employer_experience_years      9
annual_base_pay                8
signing_bonus                 94
annual_bonus                  92
stock_value_bonus            112
comments                     419
submitted_at                   0
dtype: int64
```

As you can see, certain fields have been filled in by every user (e.g., `salary_id`). Such fields include both information that was probably generated by the survey form itself (e.g. `salary_id`, `submitted_at`), as well as information that all users happened to consider essential to their responses (e.g. `location_name`, `job_title`). However, most fields contain at least a few null values. Interestingly, some of these fields we might also have considered essential (e.g. `employer_name`). 

### Part 2: Questions

**NOTE: for each question you can assume we will run the script from the root of the `submission/` directory (e.g., we will execute `python q5a.py`). Keep this in mind when designing your script so that it reads data files from `../data/`.**

**NOTE: use `index=False` (e.g., `df.to_csv('qX.csv', index=False)`) when writing your outputs.**

**Q5 (5 pts):** The easiest way to deal with missing values is to simply exclude the incomplete records from our analysis. In lecture, two deletion approaches were presented: pairwise deletion, where we only exclude records that have missing values in the column(s) of interest, and listwise deletion, where we exclude all records that have at least one missing value. Use pairwise deletion to determine the mean `annual_base_pay` for each `job_title_rank` type. Submit your code as `q5a.py` in the `submission/` directory; your code should write its output to `q5a.csv` (also in the `submission/` directory), in the format `<mean>, <std>`, where each of the values has been truncated to 0 decimal digits. Then, use listwise deletion for the same task instead and submit your code as `q5b.py`; your code should write its output to `q5b.csv` (both files in the `submission/` directory). Your csv files should have the following format:
```csv
job_title_rank,annual_base_pay_mean
xxxx,xxxx
...
```

where floating-point values have been truncated to 0 decimal digits (in Pandas, you can do this using `.astype(int)`) and records have been ordered on `job_title_rank` column ascendingly. You may use `pandas.DataFrame.to_csv` for convenience.

**Q6 (5 pts):** A slightly more sophisticated approach is to replace all missing values in a column with the same value. For this question, calculate a mean `annual_bonus` on non-missing records and substitute missing `annual_bonus` value with mean `annual_bonus`. Use this approach to determine the mean and standard deviation of `annual_bonus` among the survey respondents and submit your code as `q6.py` in the `submission/` directory; your code should write its output to `q6.csv` (also in the `submission/` directory), in the format:
```csv
imputed_mean,imputed_std
<mean>,<std>
```
Where each of the values has been truncated to 0 decimal digits.


**Q7 (10 pts):** Imputing missing values with the same value preserves the number of data points, but can create skew in the dataset. One way to combat this issue is by instead determining each imputed value from other existing values for the same record. Our goal will be to impute missing `annual_bonus`es as a function of respondents' `annual_base_pay`.

As a first step, impute missing values for `annual_base_pay` using mean substitution. Then, based on all respondents that report a **non-zero (and non-NaN)** `annual_bonus`, calculate the average `annual_bonus`/`annual_base_pay` (let's call this aggregated average ratio `avg_ratio`). Finally, use `avg_ratio` to impute  `annual_bonus`  (i.e., `annual_base_pay * avg_ratio`) for respondents who didn't include `annual_bonus` information (i.e., is null). As in Q6, compute the mean and standard deviation of `annual_bonus` after imputation among the survey respondents and submit your code as `q7.py` in the `submission/` directory; your code should write its output into `q7.csv` (also in the `submission/` directory), in the format:
```csv
imputed_mean,imputed_std
<mean>,<std>
```
Where each of the values has been truncated to 0 decimal digits.

[*Back to top*](#table-of-contents)

### Part 3: Working across formats (50 points)

In this part you will look at music data in different formats (`lizzo_appearances.json`, `top2018.csv` and `wmbr.txt`) and answer questions on the data.  You will have to use both the Unix tools we covered above and Pandas to clean and perform queries over the clean data.

You may find that using a common format (*e.g.,* CSV or JSON) for the cleaned datasets will significantly help you integrate them.  Functions such as [`pandas.read_json()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html) may also come in handy.

#### Part 3: Questions

**NOTE 1: we anticipate you will have questions about Q8; while you are working on the lab, please periodically check Piazza / the [running updates](#running-updates) section above for clarifications that we issue throughout the lab. Once you submit a solution earning full-credit, you do not need to check for updates anymore. Even if we make an update to the autograder that would invalidate one of your solutions, we will honor your best submission grade.**

**NOTE 2: after reading Q8 below you may be wondering: how much data cleaning do I need to do? E.g. do I need to manually check the name of every artist to find and come up with rules to correct typos? The answer is: you only need to perform such cleaning operations as necessary in order to answer Q9-13 correctly.**

**NOTE 3: Some of the column values in `wmbr.txt` contain commas. If you simply parse the data into CSV format, this may cause problems because certain rows will have more commas than others. To overcome this, place your column values inside of double quotes "". For example, a row of your final CSV output might look like the following:**
```csv
"Apr 11, 2019","Billie Eilish","Bad Guy","When We All Fall Asleep, Where Do We Go?"," ","Breakfast of Champions","Yurij"
```

**Q8 (10 pts):** Clean and *wrap* (see Example 1 in the [examples subsection](#examples)) the data in `wmbr.txt` (https://wmbr.org/) to obtain an easily queriable representation of the same information. Note that all fields are present for every song, but some of them might be empty. Some artist names contain typos (*e.g.,* "Billie Ellish" and "Billie Eilish" both occur) and artists may collaborate (*e.g.,* "Dua Lipa" or  "Cardi B" both have songs in collaboration with other artists). It is your job to make sure that your data cleaning scripts can correctly handle these cases. Submit the cleaned up data as `q8.csv` in the `submission/` directory. Note that there is some flexibility in your choice of cleaning approaches, but the resulting file should be formatted consistently. Submit your code as `q8.sh` (also in the `submission/` directory), including comments on the transformations you applied. We will not grade on the content of `q8.csv`. Instead, you earn all the points of this question if you earn the full points of at least 2 of the next 5 questions.

**Q9 (5 pts):** How many song plays at WMBR are about love? A song play is related to love if one of its ['Song', 'Show', 'Album'] entries contains 'love' (case-insensitive). Output your answer as a number (see format below) to `q9.csv` in the `submission/` directory. Submit your code as `q9.sh` if you used command line tools, or as `q9.py` if you used Pandas (also in the `submission/` directory). The output should look like:
```
num_love_song_plays
<num>
```

*NOTE: use `index=False` (e.g., `df.to_csv('q9.csv', index=False)`) when writing your output (if using Python).*

**Q10 (5 pts):** Find the DJ that played the most songs off of [Stranger Things](https://en.wikipedia.org/wiki/Stranger_Things) album. Output your answer to `q10.csv` in the `submission/` directory, with one record per line. Each record should have two columns - the DJ name, and the number of times they have played a track from Stranger Things (see example output below). Sort first by number of tracks played in descending order, and then by DJ name in ascending lexicographical order. Submit your code as `q10.sh` if you used command line tools, or as `q10.py` if you used Pandas (also in the `submission/` directory). An example output is as follows:
```csv
dj,num_plays
asdf,10
bcd,10
xyz,9
def,8
...
```

*NOTE: use `index=False` (e.g., `df.to_csv('q10.csv', index=False)`) when writing your output (if using Python).*

**Q11 (10 pts):** What was the ratio of [Billie Eilish](https://en.wikipedia.org/wiki/Billie_Eilish) song plays to the overall number of song plays at WMBR *over each year* among 2017, 2018, and 2019?  Make sure to include all 3 years (even if the ratio is 0). Output your answer to `q11.csv` in the `submission/` directory, with one record per line. Each record should have two columns - the year and the ratio with 4 digits of precision after the decimal point, with appropriate rounding (see example below). Sort by year in descending order. Submit your code as `q11.sh` if you used command line tools, or as `q11.py` if you used Pandas (also in the `submission/` directory). An example output is as follows:
```csv
year,ratio
2019,0.3333
2018,0.0206
2017,0.0001
```

*NOTE: use `index=False` (e.g., `df.to_csv('q11.csv', index=False)`) when writing your output (if using Python).*

**Q12 (10 pts):** For the years in which [Lizzo](https://en.wikipedia.org/wiki/Lizzo) appeared on talk shows (see `lizzo_appearances.json`; we assume that talk shows are identifiable by explicitly having the word "show" in its title), use Pandas to list all the songs where she was either lead singer or collaborator (e.g., "featured" also counts) that were played at WMBR, together with how many times they were played. Note that entries in `lizzo_appearances.json` are not separated by a new line. Special characters (*e.g.,* accents, backslashes) may be present. Output your answer to `q12.csv` in the `submission/` directory, with one record per line. Each record should have two columns - the song title and the number of times it was played (see example below). Sort first by number of times played in descending order, and then by track name in ascending order. Submit your code as `q12.py` (also in the `submission/` directory). An example output is as follows:
```csv
song,num_plays
abc,7
def,7
aaa,6
...
```

*NOTE: use `index=False` (e.g., `df.to_csv('q12.csv', index=False)`) when writing your output (if using Python).*

**Q13 (10 pts):** Of the artists who (a) had at least one song played at WMBR and (b) had at least one song in the top 100 tracks at Spotify in 2018: which artist had the most danceable track, and what was it? Note: the artist's most danceable track may not have been played at WMBR. Also Note: here we consider collaborations, so "Calvin Harris, Dua Lipa" means you'd also include "Dua Lipa" in your search for artists in the top 100. Output your answer to `q13.csv` in the `submission/` directory, with a single row with three columns: the artist name, song title, and danceability score (see example below). Submit your code as `q13.sh` if you used command line tools, or as `q13.py` if you used Pandas (also in the `submission/` directory). An example output is as follows:
```csv
artist,song_title,danceability
asdf,some song,0.567
```

*NOTE: use `index=False` (e.g., `df.to_csv('q13.csv', index=False)`) when writing your output (if using Python).*

[*Back to top*](#table-of-contents)

## 4. Submission Instructions

### Before You Submit: Push Your Changes
Please make sure to push your code to your private repository:
```bash
$ git add -A # or, limit to the set of files you want to keep
$ git commit -m "pushing final state of lab 2"
$ git push origin main
```
We may not use the same machine(s) from lab-to-lab so in order to keep your changes you will need to check them into your private repository. Labs are designed to be independent -- so if you forget to push your changes it should not be the end of the world -- but it's better to be safe than sorry.

### Submission
Check the contents of your `submission` directory. It should contain *at least* the following 15 files:

- Part 1:
  - `q1.sh`
  - `q2.sh`
  - `q3.sh`
  - `q4.sh`
- Part 2:
  - `q5a.py`
  - `q5b.py`
  - `q6.py`
  - `q7.py`
- Part 3:
  - `q8.csv`
  - `q8.sh`
  - `q9.sh` or `q9.py`
  - `q10.sh` or `q10.py`
  - `q11.sh` or `q11.py`
  - `q12.py`
  - `q13.sh` or `q13.py`

Zip the *contents* of the `submission` directory. Make sure you are not zipping the containing directory itself.
```sh
# Zip the contents of the submission directory.
cd submission
zip submission.zip *
```

To pull the zip file from the EC2 instance down to your laptop you can then run:
```bash
# assuming you created an entry in your ~/.ssh/config:
$ scp datascience:~/path/to/submission/submission.zip .

# OR, if you did not create an entry in ~/.ssh/config:
$ ssh -i path/to/user123.pem user123@<your-hostname>:~/path/to/submission/submission.zip .
```

Submit the generated `submission.zip` file to Gradescope.

### Submitting as an Individual
To submit responses as an individual, upload the generated `submission.zip` file to Gradescope.

### Submitting as a Group
To submit responses as a group, have one member of the group submit the generated `submission.zip` file to Gradescope. **The member who submits the assignment must then add their partner(s) as a group member on the Gradescope submission: [details](https://help.gradescope.com/article/m5qz2xsnjy-student-add-group-members).**

[*Back to top*](#table-of-contents)
