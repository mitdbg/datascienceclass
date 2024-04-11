Table of Contents
=================
- [Lab 6: Ray Dune (The Battle for Arrakis)](#lab-6-ray-dune-the-battle-for-arrakis)
  * [1. Accessing Your EC2 Instance](#1-accessing-your-ec2-instance)
  * [2. Additional Setup](#2-additional-setup)
  * [3. Setup Lab 6 Environment](#3-setup-lab-6-environment)
  * [4. The Battle for Arrakis](#4-the-battle-for-arrakis)
    * [Spark (30 pts)](#spark-30-pts)
    * [Ray (70 pts)](#ray-70-pts)
  * [5. Submission Instructions](#5-submission-instructions)
    * [Before You Submit: Push Your Changes](#before-you-submit-push-your-changes)
    * [Submitting as an Individual](#submitting-as-an-individual)
    * [Submitting as a Group](#submitting-as-a-group)

---
# Lab 6: Ray Dune (The Battle for Arrakis)
---
* **Assigned: April 11th**
* **Due: April 23rd, 11:59:00 PM ET.**


![dune](dune.jpeg)

---
---
---
> *\"The person who controls ~~the spice~~ Ray controls the universe. A process cannot be understood by stopping it. Understanding must move with the flow of the process, must join it and flow with it.
> \-- Dune\" \-- Your TAs Trying to Teach you Ray (and Spark)*
---
---
---
You awaken on the planet [Arrakis](https://dune.fandom.com/wiki/Arrakis) -- the home of the [Fremen](https://dune.fandom.com/wiki/Fremen) people -- amidst a terrible war started between members of [The Great Houses](https://dune.fandom.com/wiki/House). As depicted in Frank Herbert's [novels](https://en.wikipedia.org/wiki/Dune_novel), and the recent [Hollywood smash hit](https://en.wikipedia.org/wiki/Dune_franchise) trilogy, [Spice](https://dune.fandom.com/wiki/Spice_Melange) is the most valuable substance in the universe. Without Spice interplanetary travel is impossible. The Great Houses fight for control of your home planet Arrakis and its vital Spice fields.

You are a fierce Fremen warrior and lead four groups of Fedaykin -- the most skilled of the Fremen fighters. In consultation with the [Reverend Mother](https://dune.fandom.com/wiki/Reverend_Mother) and leaders of the [Bene Gesserit](https://dune.fandom.com/wiki/Bene_Gesserit) (wise people), you come up with a clever plan to expel The Great Houses from Arrakis.

The plan is simple: **destroy the Spice fields.**

The destruction of Spice will bring an end to The Great Houses' war over Arrakis and allow peace to prevail on your home planet. However, in an effort to maximize the chances of the plan's success, the Bene Gesserit have gone behind your back and secretly funded another Fremen warrior -- **your rival**.

You and your rival are given instructions to destroy the planet's Spice fields in opposite hemispheres (you in the northern hemisphere, your rival in the southern hemisphere). That being said, it is clear that the Bene Gesserit only intend for one of you to become the leader once the destruction is over. **In order to prevail as the leader of the Fremen, you must destroy more Spice fields than your rival.** Failure to do so will likely result in permanent exile from Arrakis.

---
Credit for [the inspiration of this lab](https://www.cs.cornell.edu/courses/cs3410/2016sp/projects/pa3/pa3.html) belongs to the CS 3410 course staff at Cornell

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

## 4. The Battle for Arrakis

### Spark (30 pts)
Before you and your Fremen warriors can leave to destroy the Spice fields of Arrakis, you decide it would be a good idea to read up on the planet's history. Unfortunately, your warriors are not great readers and are in a rush to leave, so you decide to create a condensed summary of the history for them.

**Task 1** Fill in the blanks in `spark-code/Task1.py` which is Spark program that outputs the top-100 most frequent words in Dune novel series by Frank Herbert using [Spark's RDD APIs](https://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-operations).

Your program should:
1. first, replace the following set of punctuation [:=,!'".?] with whitespace
2. then, lower case all of the words
3. finally, compute the word frequencies

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

Note that if two words have the same frequency, break the tie by outputting the lexigraphically smaller word first.

**Task 2**  Building on top of Task 1, fill in the blanks in `spark-code/Task2.py` to output the top-100 most frequent words in the novel that are NOT stop-words using Spark's RDD and DataFrame APIs.

Your program should:
1. first, replace the set of punctuation [:=,!'".?] with whitespace
2. then, lower case all of the words
3. then, remove stop-words
4. finally, compute the word frequencies

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
    
Note that if two words have the same frequency, break the tie by outputting the lexigraphically smaller word first.

**How to submit Spark programs to our Spark Cluster**

Assuming the current directory is `lab_6/`, run the following script
```bash
bash submit-spark-job.sh spark-code/Task1.py
```
This script submits `spark-code/Task1.py` to our Spark cluster and stores the program standard output to `spark-code/Task1.py.stdout` and error output to `spark-code/Task1.py.stderr`.

Submission of Task2 can be done similarly.

**Note about submission**
When it's time to submit, you will need to zip the `spark-code` folder which includes the stdout/stderr log files of the programs along with the code. See the [section 5](#5-submission-instructions) for more detailed instructions.

### Ray (70 pts)
TODO


## 5. Submission Instructions
### Before You Submit: Push Your Changes
Please make sure to push your code to your private repository:
```bash
$ git add -A # or, limit to the set of files you want to keep
$ git commit -m "pushing final state of lab 6"
$ git push origin main
```

### Submitting as an Individual
To submit responses as an individual, you will need to zip your spark code and log files as well as your Dune game code. To do this, simply run:
```sh
# Zip the contents of the submission folder
zip -r submission.zip spark-code dune
```

Submit the generated `submission.zip` file to Gradescope.

### Submitting as a Group
To submit responses as a group, you will need to zip your spark code and log files as well as your Dune game code. To do this, simply run:
```sh
# Zip the contents of the submission folder;
zip -r submission.zip spark-code dune
```

Have one member of the group submit the generated `submission.zip` file to Gradescope. **The member who submits the assignment must then add their partner as a group member on the Gradescope submission: [details](https://help.gradescope.com/article/m5qz2xsnjy-student-add-group-members).**
