Table of Contents
=================
- [Lab 6: Ray Dune](#lab-0-setting-up-your-environment)
  * [1. Accessing Your EC2 Instance](#1-accessing-your-ec2-instance)
  * [2. Additional Setup](#2-additional-setup)
  * [3. Setup Lab 6 Environment](#3-setup-lab-6-environment)
  * [4. Lab Overview](#4-lab-overview)
    * [The Dataset](#the-dataset)
    * [TODO: More Subsections (If Necessary)](#todo-more-subsections-if-necessary)
  * [5. Submission Instructions](#6-submission-instructions)
    * [Before You Submit: Push Your Changes](#before-you-submit-push-your-changes)
    * [Submitting as an Individual](#submitting-as-an-individual)
    * [Submitting as a Group](#submitting-as-a-group)

---
# Lab 6: Title Goes Here
---
* **Assigned: April 11th**
* **Due: April 23rd, 11:59:00 PM ET.**


image goes here

## 1. Accessing Your EC2 Instance
If the number in your username modulo 2 equals:
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
Execute the following commands in order to pull lab 6 down onto your machine:
```bash
# ssh to EC2
$ ssh datascience

# navigate to your private repository
$ cd your-private-repo

# fetch and merge lab 6
$ git checkout main
$ git fetch upstream
$ git merge upstream/main
```
Remember than you can then commit any changes to your private remote repository by running:
```bash
# add any new changes and make a commit message
$ git add some-file.txt another-file.txt
$ git commit -m "adding my files"

# push new changes from course repo to your private mirror
$ git push origin main
```

[*Back to top*](#table-of-contents)

## 3. Setup Lab 6 Environment
Inside the `lab_6` directory of your repository you should see a script called `setup.sh`. Simply execute the script as follows:
```bash
# --- on the EC2 machine ---
$ cd your-private-repo/lab_6/
$ bash setup.sh
```

[*Back to top*](#table-of-contents)

## 4. Lab Overview

**Task 1** Filling the blanks in `spark-code/Task1.py` which is Spark program that output the top-100 most frequent words in Dune novel series by Frank Herbert using with Spark's RDD (https://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-operations) APIs.
Your program should replace the set of punctuations (in bracket) with whitespace before start counting: [:=,!'".?] .
Then your program should turn all the words into lower case.

Output the top-100 words along with their frequency in the following format to standard output:
    
    word,freq
    ...
    thought, 1092
    will, 1080
    fremen, 1053
    leto, 1036
    alia, 1033
    now, 997
    ...
    

Note that if two words have the same frequency, break tie by outputting the lexigraphically smaller word first.

**Task 2**  Building on top of Task 1, Filling the blanks in `spark-code/Task2.py` that output the top-100 most frenquent words in the novel that are not stop-words using Spark's RDD and DataFrame APIs.Your program should replace the set of punctuations (in bracket) with whitespace before start counting: [:=,!'".?]. Then your program should turn all the words into lower case.
    
Output the top-100 words along with their frequency in the following format to standard output:
    
    word,freq
    ...
    thought, 1092
    fremen, 1053
    leto, 1036
    alia, 1033
    would, 970
    stilgar, 932
    know, 829
    must, 827
    asked, 817
    ...
    
Note that if two words have the same frequency, break  tie by outputting the lexigraphically smaller word first.

**How to submit Spark programs to our Spark Cluster**

Assuming the current directory is `lab_6/`, run the following script
```bash
bash submit-spark-job.sh spark-code/Task1.py
```
This script submits `spark-code/Task1.py` to our Spark cluster and stores the program standard output to `spark-code/Task1.py.stdout` and error output to `spark-code/Task1.py.stderr`.

Submission of Task2 can be done similarly.

**Note about submission**
When it's time to submit, you will need to zip the `spark-code` folder which includes the stdout/stderr log files of the programs along with the code. See the [section 5](#5-submission-instructions) for more detailed instructions.

## 5. Submission Instructions

### Before You Submit: Push Your Changes
Please make sure to push your code to your private repository:
```bash
$ git add -A # or, limit to the set of files you want to keep
$ git commit -m "pushing final state of lab 6"
$ git push origin main
```
We may not use the same machine(s) from lab-to-lab so in order to keep your changes you will need to check them into your private repository. Labs are designed to be independent -- so if you forget to push your changes it should not be the end of the world -- but it's better to be safe than sorry.

**What to submit for grading**

Zip the `spark-code` folder which includes the stdout/stderr log files of the programs along with the code. 

### Submitting as an Individual
To submit responses as an individual, simply run:
```sh
# Zip the contents of the submission folder
zip -r submission.zip spark-code dune
```

Submit the generated `submission.zip` file to Gradescope.

### Submitting as a Group
To submit responses as a group, simply run:
```sh
# Zip the contents of the submission folder;
zip -r submission.zip spark-code dune
```

Have one member of the group submit the generated `submission.zip` file to Gradescope. **The member who submits the assignment must then add their partner as a group member on the Gradescope submission: [details](https://help.gradescope.com/article/m5qz2xsnjy-student-add-group-members).**
