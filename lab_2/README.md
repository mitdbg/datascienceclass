Table of Contents
=================
- [Lab 2](#lab-2)
- [Setup](#setup)
- [Part 1: Wrangler](#part-1-wrangler)
  * [Tasks:](#tasks)
    + [synsets.txt](#synsetstxt)
      - [Questions](#questions)
    + [worldcup-semiclean.txt](#worldcup-semicleantxt)
      - [Questions](#questions-1)
- [Part 2: Unix Tools](#part-2-unix-tools)
  * [grep](#grep)
  * [sed](#sed)
  * [awk](#awk)
  * [Examples](#examples)
  * [Tasks:](#tasks-1)
      - [Questions](#questions-2)
- [Part 3: Choose your own adventure](#part-3-choose-your-own-adventure)
  * [Datasets](#datasets)
    + [wmbr.txt](#wmbrtxt)
    + [lizzo_appearances.json](#lizzo-appearancesjson)
    + [top2018.csv](#top2018csv)
  * [Questions](#questions-3)
- [Handing in your work](#handing-in-your-work)
    + [Feedback (optional, but valuable)](#feedback-optional-but-valuable)

# Lab 2
*Assigned: Wednesday, September 18th.*
*Due: Wednesday, September 25th, 11:59 PM ET.*

In this lab, you will use various types of tools -- from command line tools like `sed` and `awk` to high-level tools like Data Wrangler -- to perform data wrangling and integration tasks from data encoded into a text file.  The goal of this lab is simply to gain experience with these tools and compare and contrast their usage.


# Setup

To start, check out/update the files for `lab_2`:

```bash
# Path to the directory containing your local clone
# of https://github.com/mitdbg/datascienceclass (this repo).
$ cd /path/to/datascienceclass

# Pull (fetch + merge) the latest changes from this repo.
$ git pull

# Change to lab 2's working directory.
$ cd lab_2/
```

**NOTE:** The commands above only pull the latest changes from this repo onto the local clone you have of it.  If you're using a "private fork" setup, and are trying to sync it with with the latest changes from this repo, then please refer to [this post](https://stackoverflow.com/questions/10065526/github-how-to-make-a-fork-of-public-repository-private](this post) on specifics of how to do that.

Startup your docker instance, and enter `lab 2`'s working directory.  We'll use the same base image as in lab1 to create a new container for this lab:
```bash
# We specify the same "6.s080:lab1" base image, mount /lab2
# from current dir (-v) set it as working directory (-w).
$ docker run -v "`pwd`":/lab2 -ti \
  -w"/lab2" \
  --name lab2-container \
  6.s080:lab1

# Install onto the image the additional requirements for
# this lab. Wrangler scripts don't support python3, so we
# need to install python v2:
$ apt install -y python python-pip
```

If you accidentally exit your container (*e.g.,* by using **ctrl+d**), you can come back to it by running:
```bash
$ docker start -i lab2-container
```

The `lab2` directory contains a number of datasets under data directory. **For parts 1 and 2**, you will be answering questions on the following datasets:

1. `synsets.txt`: A dataset of synonyms and their meanings. Each line contains one synset with the following format:
```
ID,<synonyms separated by spaces>,<different meanings separated by semicolons>
```

2. `worldcup-semiclean.txt`: A dataset with a snippet of the following Wikipedia webpage on [FIFA (Soccer) World Cup](http://en.wikipedia.org/wiki/FIFA_World_Cup). Specifically it is a partially cleaned-up wiki source for the table toward the end of the page that lists teams finishing in the top 4. 


# Part 1: Wrangler

Go to the [Data Wrangler website](http://vis.stanford.edu/wrangler/app/).  Load both of the datasets (we recommend cutting out a small subset -- 100~ lines) into Data Wrangler and try playing with the tool.


Some tips using Wrangler:

* Wrangler responds to mouse highlights and clicks on the displayed table cells by suggesting operations on the left sidebar. 
* Hovering over each element shows the result in the table view.  
* Clicking adds the operation.  
* Clear the sidebar by clicking the colored row above the schema row

The [Lecture 4 readings](http://dsg.csail.mit.edu/6.S080/sched.php) on Wrangler are also useful, especially the [video demo](http://vimeo.com/19185801). **Note:** the location of the delete transform has changed since the video was recorded. It is now located at the top menu bar, instead of under the "rows" dropdown menu in the transform editor (shown in the video).

## Tasks:

Use Data Wrangler for the following two datasets.  

### synsets.txt

Generate a list of word-meaning pairs. The output should look like:

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

The `synsets.txt` file is too large to load into the Wrangler GUI, so you need to *use the GUI to wrangle a subset of the data, then run a command line script on the complete data set.*

**note**: `lab_2/wrangler` contains a modified python wrangler module, which you should use for this lab.  This means that the python scripts that you export when using Data Wrangler should be run in the `lab_2/` folder.

#### Questions

**Q1:** Export the Python version of the wrangler script and save it to a file called `wrangler-synsets.py` in the same github repo you created for [`lab1`](../lab1) (5 pts).

**Q2:** Use the script to clean the data (with *e.g.,* `python wrangler-synsets.py data/synsets.txt synsets-clean.txt`), then determine how many unique *words* (this is the first column in `synsets-clean.txt`) there are in the dataset. As mentioned in [Handing in your work](#handing-in-your-work), please paste in your answer for this question the script you wrote to count the number of words. (5 pts).

### worldcup-semiclean.txt

Use Wrangler to generate output as follows, *i.e.,* each line in the output contains a country, a year, and the position of the county in that year (if within top 4).

```
BRA, 1962, 1
BRA, 1970, 1
BRA, 1994, 1
BRA, 2002, 1
BRA, 1958, 1
BRA, 1998, 2
BRA, 1950, 2
...
```

It may help to:

1. Remove one or more transformations that Wrangler applies by default once it loads your data.
2. Modify default transform options (**hint:** for Split transforms, take a look at split "once" vs split "repeatedly").
3. Use the wrap operation, which creates a new row at the specified token (**hint:** are there any tokens in `worldcup-semiclean.txt` that you can use to indicate a new row?).
4. Use the fold operation (**hint:** it is possible to use the *column header* value as key for a fold transform).

**NOTE:** Unlike in the cleaning task for `synsets.txt`, we *do not* require that you export the script Wrangler generates for your cleaning of `worldcup-semiclean.txt`. This dataset is small (less than 200 lines), can be pasted entirely onto Wrangler, and you should use the CSV data export option for this question.

#### Questions

**Q3:** According to the dataset, how often has each country won the world cup? Describe the set of transforms you applied to clean the dataset, and include any code you wrote to count the number of times each country won. (10 pts)


# Part 2: Unix Tools

The set of three `UNIX` tools we saw in class, `sed`, `awk`, and `grep`, can be very useful for quickly cleaning up and transforming data for further analysis (and have been around since the inception of UNIX). 

In conjunction with other unix utilities like `sort`, `uniq`, `tail`, `head`, `paste`, etc., you can accomplish many simple data parsing and cleaning  tasks with these tools. 

You are encouraged to play with these tools and familiarize yourselves with their basic usage.

As an example, the following sequence of commands can be used to answer the question "Find the five twitter user ids (uids) that have tweeted the most".  Note that in the example below, we're using the `zgrep` variant of `grep`, which allows us to operate over [gzipped data](https://en.wikipedia.org/wiki/Gzip).
```bash
$ zgrep "created\_at" data/twitter.json.gz \
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
$ zgrep "created\_at" data/twitter.json.gz \
  | sed 's/.*"user":{"id":\([0-9]*\).*/\1/' \
  | sort \
  | uniq -c \
  | sort -n \
  | tail -5"
```

To get into some details:

## grep

The basic syntax for `grep` is: 
```bash
$ grep 'regexp' filename
```
or equivalently (using UNIX pipelining):
```bash
$ cat filename | grep 'regexp'
```

The output contains only those lines from the file that match the regular expression. Two options to grep are useful: `grep -v` will output those lines that *do not* match the regular expression, and `grep -i` will ignore case while matching. See the manual (`man grep`), [Lecture 4 readings](http://dsg.csail.mit.edu/6.S080/sched.php), or online resources for more details.

## sed
Sed stands for _stream editor_. Basic syntax for `sed` is:
```bash
$ sed 's/regexp/replacement/g' filename
```

For each line in the input, the portion of the line that matches _regexp_ (if any) is replaced with _replacement_. `sed` is quite powerful within the limits of operating on single line at a time. You can use `\(\)` to refer to parts of the pattern match. In the first sed command above, the sub-expression within `\(\)` extracts the user id, which is available to be used in the _replacement_ as `\1`. 

As an example, the command below is what we used to clean `worldcup.txt` and produce `worldcup-semiclean.txt`:

```bash
$ cat data/worldcup.txt \
  | sed \
    's/\[\[\([0-9]*\)[^]]*\]\]/\1/g;
    s/.*fb|\([A-Za-z]*\)}}/\1/g; 
    s/<sup><\/sup>//g;
    s/ <br\/>//g;
    s/|bgcolor[^|]*//g;
    s/|align=center[^|]*//g;
    s/|[0-9] /|/g;
    s/.*div.*//g;
    s/| .*/|0/g;
    s|[()]||g;
    s/ //g;
    /^$/d;' > data/worldcup-semiclean.txt
```

## awk 

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

A few examples to give you a flavor of the tools and what one can do with them.

1. Perform the equivalent of Wrangler's _wrap_ on `labor.csv` (*i.e.,* merge consecutive groups of lines referring to the same record)
```bash
$ cat data/labor.csv \
  | awk \
    '/^Series Id:/ {print combined; combined = $0}
    !/^Series Id:/ {combined = combined", "$0;}
    END {print combined}'
```

2. On  `crime-clean.txt`, the following command does a _fill_ (first row of output: "Alabama, 2004, 4029.3".

```bash
$ cat data/crime-clean.txt \
   | grep -v '^,$' \
   | awk '/^[A-Z]/ {state = $4} !/^[A-Z]/ {print state, $0}'
```
    
3. On `crime-clean.txt`, the following script cleans the data as was done in the Wrangler demo in class. The following works assuming perfectly homogenous data (as the example on the Wrangler website is).

```bash
$ cat data/crime-clean.txt \
   | grep -v '^,$' \
   | sed 's/,$//g; s/Reported crime in //; s/[0-9]*,//' \
   | awk -F',' \
     'BEGIN {printf "State, 2004, 2005, 2006, 2007, 2008"} 
      /^[A-Z]/ {print c; c=$0}  
      !/^[A-Z]/ {c=c", "$0;}    
      END {print c}'
```

4. On `crime-unclean.txt` the following script performs the same cleaning as above, but allows incomplete information (*e.g.,* some years may be missing).
```bash
$ cat data/crime-unclean.txt \
   | grep -v '^,$' \
   | sed 's/Reported crime in //;' \
   | awk -F',' \
     'BEGIN {
     printf "State, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008"}
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


## Tasks:

Perform the above cleaning tasks over `synsets.txt` and `worldcup-semiclean.txt`, only this time using Unix tools. Hints:

1. Use `awk`'s `split` function, and `for loop` constructs (*e.g.,* [arrays in awk](http://www.math.utah.edu/docs/info/gawk_12.html)).

No need to re-answer the questions in the Wrangler section, but recompute them to ensure your answers are consistent.

#### Questions

**Q4:** Submit the scripts you wrote to perform the cleaning tasks as part of your answer for this question in Gradescope. In particular, prefix each script section with a line or two describing what they do. (10 pts)

**Q5:** From your experience, briefly discuss the pro and cons between using Data Wrangler as compared to lower levels tools like sed/awk? (5 pts)

# Part 3: Choose your own adventure

In this part you will look at music data in different formats (CSV, JSON, and text) and answer questions on the data.  You will have to use one or more of the data wrangling approaches we covered above (*i.e.,* Unix tools and Wrangler) to clean your data, as well as any of the tools we covered in lab1 (*i.e.,* SQL and Pandas) to perform queries over the clean data.

You may find that using a common format (*e.g.,* CSV or JSON) for the cleaned datasets will significantly help you integrate them.  Functions such as [`pandas.read_json()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html) may also come in handy.

## Datasets

### wmbr.txt
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

**Note:** All fields are present for every song, but some of them might be empty. Some artist names contain typos (*e.g.,* "Billie Ellish" and "Billie Eilish" both occur), some songs may be repeated, and artists may collaborate (*e.g.,* "Dua Lipa" or  "Cardi B" both have songs in collaboration with other artists).  It is your job to make sure that your data cleaning scripts can correctly handle these cases.  Hint: [`pandas.unique()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.unique.html) or the `uniq` Unix tool may come in handy.

### lizzo_appearances.json

A JSON file scraped from Wikipedia containing a list of appearances of the artist [Lizzo](https://en.wikipedia.org/wiki/Lizzo) at different events.  Sample snippet:

```
{"Year":"2014","Title":"Made in Chelsea: NYC","Notes":"Season 1, episode 4"},{"Year":"2014","Title":"Late Show with David Letterman","Notes":"Season 22, episode 29"}
```

**Note:** Entries in the JSON file are not separated by a new line.  Special characters (*e.g.,* accents, backslashes) may be present. It is your job to make sure that your data cleaning scripts can correctly handle these cases. 

### top2018.csv

A CSV file containing the [top 100 Spotify songs in 2018](https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018) with attributes such as "danceability", "loudness", "time_signature", etc.

## Questions

**Q6:** Submit your cleaning scripts and queries. If using wrangler to clean `wmbr.txt`, include it as `wrangler-wmbr.py` in your github repo. For any other code (*e.g.,* SQL queries, pandas, or Unix scripts), submit as part of PDF answers in Gradescope. (15 pts)

**Q7:** Which artists have either played or recorded live at WMBR? Show your answer sorted by artist name, in ascending order. (5 pts)

**Q8:** List the DJs that have played at least one song off of a [Stranger Things](https://en.wikipedia.org/wiki/Stranger_Things) season soundtrack, with the number of tracks each of them played. Show your answer sorted by number of times played, in descending order. (5 pts)

**Q9:** What was the ratio of [Billie Eilish](https://en.wikipedia.org/wiki/Billie_Eilish) songs to overall number of songs played at WMBR *over the years* of 2017, 2018, and 2019?  Make sure to include all 3 years (even if the ratio is 0), and show your answer sorted by year in descending order. (10 pts)

**Q10:** For the years in which [Lizzo](https://en.wikipedia.org/wiki/Lizzo) appeared on talk shows, list all the songs where she was either lead singer or collaborator (e.g., "featured" also counts) that were played at WMBR, together with how many times they were played. Show your answer sorted first by number of times played in descending order, and second by track name in ascending order. Note: here we assume that talk shows are identifiable by explicitly having the word "show" on its title. (15 pts)

**Q11:** For the artists whose songs were played at WMBR, and made to the top 100 tracks at Spotify in 2018, who had the most danceable track, and what was it? Note: here we consider collaborations, so "Calvin Harris, Dua Lipa" means you'd also include "Dua Lipa" in your search for artists in the top 100. (15 pts)

# Handing in your work

*This lab is due at 11:59pm Wednesday September 25th, 2019.*

Almost exactly the same submission format as in [lab_1](../lab_1). That is, you will submit your PDF with answers to [Gradescope](https://www.gradescope.com/courses/61617/assignments) and your code to the **same private github repo**. The only changes for this lab are:
*  save your `students.txt` and Wrangler scripts as separate files under a `lab_2` directory; paste your other scripts (*e.g.,* those using Unix tools, pandas, or SQL queries) inline with your PDF answers.  For this lab, with the exception of exported Wrangler scripts (which are rather long), all other scripts should be submitted as part of your answers in Gradescope.  We expect most of your script answers to be relatively short.  If your "non-Wrangler" scripts end up being too long (e.g., more than 200 lines), then note that in your Gradescope answer, adding a link to the corresponding file in your repo.

As a reminder, answers to each question should:
* be in tabular form
* start a new page
* include at the top of each answer *both students' names, MIT ids, a link to the repository of your code, and the commit hash*

### Feedback (optional, but valuable)

**Q12:** If you have any comments about this lab, or any thoughts about the
class so far, we would greatly appreciate them.  Your comments will
be strictly used to improve the rest of the labs and classes and have
no impact on your grade.

Some questions that would be helpful:

* Is the lab too difficult or too easy?  
* How much time (minutes or hours) did you spend on it?
* Did you look forward to any exercise that the lab did not cover?
* Which parts of the lab were interesting or valuable towards understanding the material?
* How is the pace of the course so far?
