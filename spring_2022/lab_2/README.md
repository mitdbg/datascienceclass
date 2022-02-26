Table of Contents
=================
- [Lab 2](#lab-2)
- [Setup](#setup)
- [Development & Submission](#development--submission)
  * [Development](#development)
  * [Submission](#submission)
  * [Autograder](#autograder)
- [Datasets](#datasets)
- [Part 1: Unix tools (30 points)](#part-1-unix-tools-30-points)
  * [General-purpose tools](#general-purpose-tools)
  * [Tool 1: grep](#tool-1-grep)
  * [Tool 2: sed](#tool-2-sed)
  * [Tool 3: awk](#tool-3-awk)
  * [Examples](#examples)
  * [Part 1 Questions](#part-1-questions)
- [Part 2: Missing value imputation (20 points)](#part-2-missing-value-imputation-20-points)
  * [Exploring the data](#exploring-the-data)
  * [Part 2 Questions](#part-2-questions)
- [Part 3: Working across formats (50 points)](#part-3-working-across-formats-50-points)
  * [Part 3 Questions](#part-3-questions)

# Lab 2
*Assigned: Wednesday, February 16th.*
*Due: Monday, February 28th, 11:59 PM ET.*

In this lab, you will deal with the all-too-frequent problem of bringing your data into a format that makes analysis possible. The 3 parts of the lab will take you through several  tasks commonly involved in this process:
- In part 1, you will use the command line tools `sed` and `awk` to efficiently clean and transform data originating in inconvenient formats.
- In part 2, you will deal with the issue of missing values, examining appropriate ways to impute them based on your intended analysis.
- In part 3, you will perform analysis tasks that involve datasets in 3 different formats: a simple text file, a JSON file and a CSV file.

Let's get started!

[*Back to top*](#table-of-contents)

# Setup

To start, check out/update the files for `lab_2`:

```bash
# Path to the directory containing your local clone
# of https://github.com/mitdbg/datascienceclass (this repo).
$ cd /path/to/datascienceclass

# Pull (fetch + merge) the latest changes from this repo.
$ git pull

# Change to lab 2's working directory.
$ cd spring_2022/lab_2/
```

**NOTE:** The commands above only pull the latest changes from this repo onto the local clone you have of it.  If you're using a "private fork" setup, and are trying to sync it with with the latest changes from this repo, then please refer to [this post](https://stackoverflow.com/questions/10065526/github-how-to-make-a-fork-of-public-repository-private) on specifics of how to do that.

Startup your docker instance, and enter `lab 2`'s working directory.  We'll use the same base image as in lab1 to create a new container for this lab:
```bash
# We specify the same "6.s079:lab1" base image, mount /lab2
# from current dir (-v) set it as working directory (-w).
$ docker run -v "`pwd`":/lab2 -ti \
  -w"/lab2" \
  --name lab2-container \
  6.s079:lab1
```

If you exit your container (*e.g.,* by using **ctrl+d**), you can come back to it by running:
```bash
$ docker start -i lab2-container
```

[*Back to top*](#table-of-contents)

# Development & Submission

## Development

Create a subdirectory of `lab_2` into which you should place your solution files:
```
root@4d2bb3edd81c:/lab2/# mkdir submission
root@4d2bb3edd81c:/lab2/# cd submission
```

Any code you write for this lab should assume that it will be run from within the `submission` directory. Please use relative paths of the form `../data/<dataset>` to access datasets from within your code. 

Please also place any output of your code, as specifiecd by each question below, within the `submission` directory. For `.sh` scripts, the output redirection should happen within your code. For example, you should observe the following:

```
root@4d2bb3edd81c:/lab2/submission# ls
q1.sh
root@4d2bb3edd81c:/lab2/submission# ./q1.sh
root@4d2bb3edd81c:/lab2/submission# ls
q1.csv q1.sh
```

Please also note that new files you create are by default not executable. Trying to run them will give rise to a "Permission denied" error. In order to avoid this for your `q[X].sh` files, make sure you edit the permissions to make the files executable:
```
root@4d2bb3edd81c:/lab2/submission# ./q1.sh
bash: ./q1.sh: Permission denied
root@4d2bb3edd81c:/lab2/submission# chmod +x q1.sh
root@4d2bb3edd81c:/lab2/submission# ./q1.sh
root@4d2bb3edd81c:/lab2/submission# ls
q1.csv q1.sh
```


## Submission

Make sure you are registered on Gradescope for this class. The course ID is `ZRE8VN`.

Check the contents of your `submission` directory. It should contain 15 files, as follows:

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

Submit the generated `submission.zip` file to Gradescope. You are free to submit unliited times until the deadline.

## Autograder

We provide you with an autograder on Gradescope, which will run your code and compare the output `.csv` files with our reference results. The only exception is question 8, which regards data cleaning and permits for more than one possible solution; this question will be graded manually. 

Is is important that you follow the instructions on development provided above, so that the autograder can find your files and function correctly.

[*Back to top*](#table-of-contents)

# Datasets

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

11. `worldcup.txt`: A snippet of the following Wikipedia webpage on the [FIFA (Soccer) World Cup](https://en.wikipedia.org/wiki/FIFA_World_Cup#Teams_reaching_the_top_four), corresponding to the table toward the end of the page that lists teams finishing in the top 4. 

[*Back to top*](#table-of-contents)

# Part 1: Unix tools (30 points)

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
  | tail -5"
```

To get into some details:

## General-purpose tools

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

-  `sort` can be used to sort the lines of a text file. It provides many useful flags for specifying things like case sensitivity, sort key location (i.e. which filed in each line to sort by) etc. You can see the complete list of flags using `sort --help`

- `uniq` can be used to remove *adjacent* duplicate lines from a file. Specifying the flag `-c` will prepend the count of such duplicates to each printed line.

- `wc` can be used to count characters (`-c`), words (`-w`) or lines (`-l`) in a text file.

## Tool 1: `grep`

The basic syntax for `grep` is: 
```bash
$ grep 'regexp' filename
```
or equivalently (using UNIX pipelining):
```bash
$ cat filename | grep 'regexp'
```

The output contains only those lines from the file that match the regular expression. Two options to grep are useful: `grep -v` will output those lines that *do not* match the regular expression, and `grep -i` will ignore case while matching. See the manual (`man grep`), [Lecture 4 readings](http://dsg.csail.mit.edu/6.S080/sched.php), or online resources for more details.

## Tool 2: `sed`
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

## Tool 3: `awk` 

Finally, `awk` is a powerful scripting language. The basic syntax of `awk` is: 
```bash
$ awk -F',' \
  'BEGIN{commands}
  /regexp1/ {command1}
  /regexp2/ {command2}
  END{commands}' 
```

For each line, the regular expressions are matched in order, and if there is a match, the corresponding command is executed (multiple commands may be executed for the same line). `BEGIN` and `END` are both optional. The `-F','` specifies that the lines should be _split_ into fields using the separator `','` (single comma), and those fields are available to the regular expressions and the commands as `$1`, `$2`, etc.  See the manual (`man awk`), [Lecture 4 readings](http://dsg.csail.mit.edu/6.S080/sched.php), or online resources for further details. 

## Examples 

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

## Part 1 Questions

*Hint: Look into `awk`'s `split` function, and `for loop` constructs (*e.g.,* [arrays in awk](http://www.math.utah.edu/docs/info/gawk_12.html)).

**Q1 (10 pts):** Starting with `synsets.txt`, write a script that uses the above tools as appropriate to generate a list of word-meaning pairs and outputs it to `q1.csv` in the `submission` directory. The output should look like:

```
'hood,(slang) a neighborhood
1530s,the decade from 1530 to 1539
...
angstrom,a metric unit of length equal to one ten billionth of a meter (or 0.0001 micron)
angstrom, used to specify wavelengths of electromagnetic radiation
angstrom_unit,a metric unit of length equal to one ten billionth of a meter (or 0.0001 micron)
angstrom_unit, used to specify wavelengths of electromagnetic radiation
...
```

Save your script as `q1.sh` in the `submission` directory. Make sure you include comments describing your approach.

**Q2 (5 pts):** Starting with `q1.csv`, write another script that determines the number of unique *words* (that is, the number of distinct entries in the first column of `q1.csv`) that appear in this dataset and outputs it to `q2.csv` in the `submission` directory. Save your script as `q2.sh` in the `submission` directory. Make sure you include comments describing your approach.

**Q3 (10 pts):** Starting with `worldcup-semiclean.txt`, write a script that uses the above tools as appropriate to generate output as follows and outputs it to `q3.csv` in the `submission` directory, *i.e.,* each line in the output contains a country, a year, and the position of the county in that year (if within top 4):

```
BRA,1958,1
BRA,1962,1
BRA,1970,1
BRA,1994,1
BRA,2002,1
BRA,1950,2
BRA,1998,2
...
```

Save your script as `q3.sh` in the `submission` directory. Make sure you include comments describing your approach.

**Q4 (5 pts):** According to `q3.csv`, how often has each country won the world cup? Write a script to compute this, by generating output as follows and outputting it to `q4.csv` in the `submission` directory:

```
BRA,5
GER,4
ITA,4
...
```

Save your script as `q4.sh` in the `submission` directory. Make sure you include comments describing your approach.

[*Back to top*](#table-of-contents)

# Part 2: Missing value imputation (20 points)

In this part we will examine the impact of different data imputation approaches on the results of an analysis on `salaries.csv`. As is often the case when using user survey data, this dataset contains many missing values, which we must decide how to handle.

## Exploring the data

Let's launch a python shell (within our container), import the data and examine the resulting dataset:
```
$ docker start -i lab2-container
root@4d2bb3edd81c:/lab2# cd submission
root@4d2bb3edd81c:/lab2/submission# python3
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
502       1093               microsoft        redmond, wa             WA               US  ...        30000.0       10000.0              8000                                                NaN  3/21/16 14:19
503       1094               (private)         boston, ma             MA               US  ...            0.0           0.0                 0  Retirement benefits very good... ~7% to ~14% (...  3/21/16 14:22
504       1097                 dropbox      san francisco            NaN              NaN  ...        25000.0           0.0             40000                                                NaN  3/21/16 14:19
505       1098  pricewaterhousecoopers          australia            NaN               AU  ...            0.0        2000.0                 0                                                NaN  3/21/16 14:20
506       1100                   apple          sunnyvale            NaN              NaN  ...        20000.0       10000.0            100000                                                NaN  3/21/16 14:20

[507 rows x 18 columns]
```

We can now examine the degree of prevalence of null values in the dataset:
```
>>> print(data.isnull().sum())
salary_id                      0
employer_name                  1
location_name                  0
location_state               309
location_country             255
location_latitude            255
location_longitude           255
job_title                      0
job_title_category             0
job_title_rank               364
total_experience_years        15
employer_experience_years      9
annual_base_pay                0
signing_bonus                 96
annual_bonus                  92
stock_value_bonus            112
comments                     421
submitted_at                   0
dtype: int64
```

As you can see, certain fields have been filled in by every user. Such fields include both information that was probably generated by the survey form itself (e.g. `salary_id`, `submitted_at`), as well as information that all users happened to consider essential to their responses (e.g. `location_name`, `job_title`). However, most fields contain at least a few null values. Interestingly, some of these fields we might also have considered essential (e.g. `employer_name`). 

## Part 2 Questions

**Q5 (5 pts):** The easiest way to deal with missing values is to simply exclude the incomplete records from our analysis. In lecture, two deletion approaches were presented: pairwise deletion, where we only exclude records that have missing values in the column(s) of interest, and listwise deletion, where we exclude all records that have at least one missing value. Use pairwise deletion to determine the mean and standard deviation of `annual_bonus` among the survey respondents and submit your code as `q5a.py`; your code should write its output into `q5a.csv` in the `submission` directory, in the format `<mean>, <std>`, where each of the values has been truncated to 0 decimal digits. Then, use listwise deletion for the same task instead and submit your code as `q5b.py`; your code should write its output into `q5b.csv` in the `submission` directory, in the format `<mean>, <std>`, where each of the values has been truncated to 0 decimal digits.

**Q6 (5 pts):** A slightly more sophisticated approach is to replace all missing values in a column with the same value (often the average of the existing values in the same column, or a special value like 0). Use this approach to determine the mean and standard deviation of `annual_bonus` among the survey respondents and submit your code as `q6.py`; your code should write its output into `q6.csv` in the `submission` directory, in the format `<mean>, <std>`, where each of the values has been truncated to 0 decimal digits.

**Q7 (10 pts):** Imputing missing values with the same value preserves the number of data points, but can create skew in the dataset. One way to combat this issue is by instead determining each imputed value from other existing values for the same record. Based on all respondents that report a **non-zero** `annual_bonus`, calculate the average `annual_bonus`/`annual_base_pay` ratio. Then, assume any respondent that didn't include `annual_bonus` information will actually receive that same ratio of their `annual_base_pay` as an annual bonus. Use this approach to determine the mean and standard deviation of  `annual_bonus` among the survey respondents and submit your code as `q7.py`; your code should write its output into `q7.csv` in the `submission` directory, in the format `<mean>, <std>`, where each of the values has been truncated to 0 decimal digits.

[*Back to top*](#table-of-contents)

# Part 3: Working across formats (50 points)

In this part you will look at music data in different formats (`lizzo_appearances.json`, `top2018.csv` and `wmbr.txt`) and answer questions on the data.  You will have to use both the Unix tools we covered above and Pandas to clean and perform queries over the clean data.

You may find that using a common format (*e.g.,* CSV or JSON) for the cleaned datasets will significantly help you integrate them.  Functions such as [`pandas.read_json()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html) may also come in handy.

## Part 3 Questions

**Q8 (10 pts):** Clean and *wrap* (see Part 1 of this lab) the data in `wmbr.txt` to obtain an easily queriable representation of the same information. Note that all fields are present for every song, but some of them might be empty. Some artist names contain typos (*e.g.,* "Billie Ellish" and "Billie Eilish" both occur), some songs may be repeated, and artists may collaborate (*e.g.,* "Dua Lipa" or  "Cardi B" both have songs in collaboration with other artists).  It is your job to make sure that your data cleaning scripts can correctly handle these cases (hint: the `uniq` Unix tool may come in handy). Submit the cleaned up data as `q8.csv`. Note that there is some flexibility in your choice of cleaning approaches, but the resulting file should be formatted consistently. Also submit your code as `q8.sh`, including comments on the transformations you applied.

**Q9 (5 pts):** Which artists have either played *live* or recorded *live* at WMBR? Output your answer to `q9.csv` in the `submission` directory, with one artist per line, sorted by artist name, in ascending lexicographical order. Submit your code as `q9.sh` if you used command line tools, or as `q9.py` if you used Pandas.

**Q10 (5 pts):** List the DJs that have played at least one song off of a [Stranger Things](https://en.wikipedia.org/wiki/Stranger_Things) season soundtrack. Output your answer to `q10.csv` in the `submission` directory, with one record per line (each record should have two columns - the DJ name, and the number of such tracks they played), sorted first by number of tracks played in descending order, and then by DJ name in ascending lexicographical order. Submit your code as `q10.sh` if you used command line tools, or as `q10.py` if you used Pandas.

**Q11 (10 pts):** What was the ratio of [Billie Eilish](https://en.wikipedia.org/wiki/Billie_Eilish) songs to overall number of songs played at WMBR *over the years* of 2017, 2018, and 2019?  Make sure to include all 3 years (even if the ratio is 0). Output your answer to `q11.csv` in the `submission` directory, with one record per line (each record should have two columns - the year and the ratio with 4 digits of precision after the decimal point, with appropriate rounding), sorted first by year in descending order. Submit your code as `q11.sh` if you used command line tools, or as `q11.py` if you used Pandas.

**Q12 (10 pts):** For the years in which [Lizzo](https://en.wikipedia.org/wiki/Lizzo) appeared on talk shows, use Pandas to list all the songs where she was either lead singer or collaborator (e.g., "featured" also counts) that were played at WMBR, together with how many times they were played. Note that entries in `lizzo_appearances.json` are not separated by a new line.  Special characters (*e.g.,* accents, backslashes) may be present. Output your answer to `q12.csv` in the `submission` directory, with one record per line (each record should have two columns - the song title and the number of times it was played), sorted first by number of times played in descending order, and then by track name in ascending order. Submit your code as `q12.py`. Note: here we assume that talk shows are identifiable by explicitly having the word "show" on its title. 

**Q13 (10 pts):** For the artists whose songs were played at WMBR, and made to the top 100 tracks at Spotify in 2018, who had the most danceable track, and what was it? Note: here we consider collaborations, so "Calvin Harris, Dua Lipa" means you'd also include "Dua Lipa" in your search for artists in the top 100. Output your answer to `q13.csv` in the `submission` directory, with a single line with three columns: the artist name, song title and danceability score. Submit your code as `q13.sh` if you used command line tools, or as `q13.py` if you used Pandas.

[*Back to top*](#table-of-contents)
