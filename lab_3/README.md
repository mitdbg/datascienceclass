# Lab 3: Entity Resolution

*Assigned: September 25th, 2019*

*Due: October 7nd, 2019, 11:59 PM*

In this lab, you will take two datasets that describe the same
entities, and identify which entity in one dataset is the same as an
entity in the other dataset.  Our datasets were provided by two large
retailers and contain information on the products they sell.

Rather than have you compete against yourself, we've turned this lab
into a competition: students will submit their best matching
algorihtms and try to beat one-another on a leaderboard to identify
the best algorithm.  You may enter this competition yourself or as a
team of up to two students.  We will give a nice prize to the winning
team or teams.

Unlike previous labs, this lab is significantly more open ended than
previous labs. 

You can work in pairs for this lab.

# Setup

To start, check out/update the files for `lab_3`:

```bash
# Path to the directory containing your local clone
# of https://github.com/mitdbg/datascienceclass (this repo).
$ cd /path/to/datascienceclass

# Pull (fetch + merge) the latest changes from this repo.
$ git pull

# Change to lab 3's working directory.
$ cd lab_3/
```

**NOTE:** The commands above only pull the latest changes from this repo onto the local clone you have of it.  If you're using a "private fork" setup, and are trying to sync it with with the latest changes from this repo, then please refer to [this post](https://stackoverflow.com/questions/10065526/github-how-to-make-a-fork-of-public-repository-private](this post) on specifics of how to do that.

Startup your docker instance, and enter `lab 3`'s working directory.  We'll use the same base image as in lab1 to create a new container for this lab:
```bash
# We specify the same "6.s080:lab1" base image, mount /lab2
# from current dir (-v) set it as working directory (-w).
$ docker run -v "`pwd`":/lab3 -ti \
  -w"/lab3" \
  --name lab3-container \
  6.s080:lab1
```


If you accidentally exit your container (*e.g.,* by using **ctrl+d**), you can come back to it by running:
```bash
$ docker start -i lab3-container
```

**IMPORTANT:** Inside the container run the following script. This unzips the data and fetches some neccesary dependencies
```bash
$ bash RUN_ME_FIRST.sh
```

The ``data`` directory should now contain the data you are to match on in three subdirectories, ``train``, ``test``, and ``val``.

Each of these directories contains the following files.
 * retailer1.csv (a csv of products from retailer 1)
 * retailer2.csv (a csv of products from retailer 2)
 * matches.csv (containing a mapping of retailer1.custom_id to retailer2.custom_id, present only in train)
 
The CSV files per retailer contain columns describing product details. Schema matching
is already done for you, with matching columns from retailer1 and retailer2 sharing the same
name. There are, however additional columns in each dataset. 

Your job is to write a script that will load both datasets and
identify matching venues in each dataset.  Measure the [precision,
recall, and F1-score](https://en.wikipedia.org/wiki/F-score) of your
algorithm against the ground truth in `data/train/matches.csv`.  Once
you're satisfied with an algorithm that has high values for these
training data points, move on to the two test files and produce output
based on your training (if your algorithm requires training).

The output of your script should be a csv matching the format of ``data/train/matches.csv``. 
That is, a csv with columns named id1 and id2, containing the matching ``custom_id`` of retailer1 and
retailer2.

Please write your script in the ``matching.py`` file provided. ``matching.py`` takes command line parameters
to run on the training set, test set, and validation set. And outputs `[set]_output.csv` for each of these.

You can use ``python3 score.py data/train/matches.csv train_output.csv`` To see the precision, recall, and F1 score on
the training set.

 Here are a few notes:
 * The schemas for these datasets are aligned, but this was something that engineers had to do ahead of time when we initially matched our datasets.
 * The two datasets don't have the same exact formatting for some fields: check out the `shipweight` field in each dataset as an example.  You'll have to normalize some of your datasets if you intend to use these columns.
 * There are some missing values to deal with in some columns, that must be dealt with if you want 
 * You might notice matches in matches.csv that you disagree with.  That's fair: our data comes from matching algorithms and crowds, both of which can be imperfect.  If you feel it makes your algorithm's training process better, feel free to blacklist (programmatically) certain training values.
 * There are many different features that can suggest similarity. Field equality is a good one: if the product's brand and model number are equal, the products might be equal.  But this is a relatively high-precision, low-recall feature (`Bob's Pizza` and `Bob's Pizzeria` aren't equal), and so you'll have to add other ones.  For example, [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) between two strings offers finer granularity of how similar two strings are.  You could imagine many tens of features, ranging from field equality to more esoteric but useful ones (e.g., "Does the first numeric value in the address field match?").
 * Since there are many features, you may need some way to combine them.  A simple weighted average of values, where more important values (similar names) are weighed more highly will get you quite far.  In practice, you'd want to build a classifier that takes these features and learns the weights based on the training data.  If you're using Python and want to build a classifier, check out [scikit-learn](http://scikit-learn.org/).  We've seen good results with the decision tree ensemble/random forest techniques.  Note that this step will take time, so only do it if you've hand-rolled your own reasonable matcher already.
 * It's possible to be near 1 for precision/recall/F1 with enough training data and good enough machine learning models, but this could take many engineers several months to get right.
 * These datasets aren't too large, but in practice require matching several million venues across datasets.  Performing an `O(N^2)` comparison on all venues would take too long in those cases so some heuristics are needed to narrow down the likely candidates.
 
 
 Some more implementation hints:
 * Start with a very small subset of columns on each dataset and build from there.
 * You may find it helpful to fill in missing values for some columns.
 * First see how far direct field equality takes you before moving on to more complex tasks like similarity matching. You can do this without n^2 comparisons if you are clever with data structures. Move on to similarity matches like jaccard similairty, and weighted jaccard similarity only afterwards.
 * Test out your similarity metric on a few rows before moving on to the whole dataset.
 * While you must implement some sort of blocking, you do not need to jump directly to using complex techniques like LSH with minhash. Try to find simple ways of blocking up the data using a single field. The goal is to decrease the number of similarity searches you have to use without excluding too many matches.
 * When doing similarity scoring, it is easiset to start with a single column. Check how far this gets you in terms of accuracty. Only after this is working should you consider using weighted averages from several columns.
 * If you want to use machine learning for some parts of this lab, you are welcome to. It is not required to get full credit on this assignment (But it may help move you up the leaderboard).
 * If your implementation is going slow, you may want to try your algorithms on a sample of the data. If you choose this, make sure you sample the data such that there are enough matches in your sample to be interesting.
 * Looking at the Lecture 5 [slides](http://dsg.csail.mit.edu/6.S080/lectures/lec5.pptx) and [code](http://dsg.csail.mit.edu/6.S080/lectures/lec5-code.py) may be very helpful..

# Submission Instructions

## Upload your best results to the leaderboard

To compete in the challenge, you should will need to submit your results 
on the test dataset to the leaderboard server. Details will be posted
on piazza shortly. There you can upload your results and
also see the results of other students so that you can improve your
algorithm and compete for the grand prize!

To make your submission to the leaderboard server. Edit ``submission_details.json``.
This is a json file containing the following.
```json
{
  "submission_url" : "<submission_url_posted_on_piazza>",
  "group_secret" : "<your_group_secret>",
  "team_name" : "<your_team_name>"
}
```

The submission url will be posted on Piazza shortly. The group secret will be emailed to each student registered for the course. Please choose a team name and replace ``<your_team_name>`` with it. There is a limit on team names of 20 characters.

After editing the submission details file, you can submit your matches to the test set to the leaderboard by running ``python3 submit.py test_output.csv`` in the lab3 directory in the container. 

## Submission to Gradescope + Code Submission

In addition to competing in the challenge, please upload a writeup to gradescope as the lab 3 assignment. As in previous labs please include the names of team members, mit email addresses, and the commit id of the code on git.

For your github submission, please include all files needed to generate your ``test_output.csv`` and ``train_output.csv``. Ideally, this should be runnable just by running ``python3 matching.py --all``. 

Create a file students.txt in the lab_1 directory that lists the MIT Kerberos id (i.e. the username that comes before your @mit.edu email adddress). of you and your partner, one per line. commit and push your queries.py and all the sql queries in the queries subdirectory. Add the TAs for the course as collaborators on github.com (Usernames: MattPerron and jmftrindade) or github.mit.edu (Usernames: mperron and jfon). Note that we will only look at commits made before the deadline.

You are free to use either a new **private** repository or use one from previous lab submission. Please include the commit hash in your submission however.

**Grading:** Achieving an F1 score of .7 on the test dataset (reported by the leaderboard) will get you full credit (70 pts) for the coding portion of the lab. This will decrease linearly to 0 points for an F1 score of 0.0. For example, getting an F1 score of .6 on the dataset will earn you 60 of 70 possible points for this section. The remaining 30 points are for the writeup.

The writeup should contain:

**Q0.** (70 pts) No content needed, this is a dummy question so we can add your grades on the test dataset on gradescope.

**Q1.** (30 pts) Answers to the following questions in no more than 3 paragraphs total:
 * Describe your entity resolution technique, as well as its precision, recall, and F1 score on the training dataset.
 * What were the most important features that powered your technique?
 * How did you avoid pairwise comparison of all products across both datasets?
 
**Q2.** Feedback (0 pts, optional) If you have any comments about this lab, or any thoughts about the
class so far, we would greatly appreciate them.  Your comments will
be strictly used to improve the rest of the labs and classes and have
no impact on your grade.

Some questions that would be helpful:

* Is the lab too difficult or too easy?  
* How much time (minutes or hours) did you spend on it?
* Did you look forward to any exercise that the lab did not cover?
* Which parts of the lab were interesting or valuable towards understanding the material?
* How is the pace of the course so far?

