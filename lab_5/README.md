Table of Contents
=================
- [Lab 5: Title Goes Here](#lab-0-setting-up-your-environment)
  * [1. Accessing Your EC2 Instance](#1-accessing-your-ec2-instance)
  * [2. Additional Setup](#2-additional-setup)
  * [3. Setup Lab 5 Environment](#3-setup-lab-2-environment)
  * [4. Lab Overview](#4-lab-overview)
    * [The Dataset](#the-dataset)
    * [TODO: More Subsections (If Necessary)](#todo-more-subsections-if-necessary)
  * [5. Questions](#5-questions)
    * [Output Format](#output-format)
    * [Running Updates](#running-updates)
    * [Questions](#questions)
  * [6. Submission Instructions](#6-submission-instructions)
    * [Before You Submit: Push Your Changes](#before-you-submit-push-your-changes)
    * [Submitting as an Individual](#submitting-as-an-individual)
    * [Submitting as a Group](#submitting-as-a-group)

---
# Lab 5: Title Goes Here
---
* **Assigned: TODO.**
* **Due: TODO, 11:59:00 PM ET.**

* **Learning Objective**: TODO
* **Deliverables**: TODO

## 1. Accessing Your EC2 Instance
First, please read the post announcing the release of Lab 5 on Piazza (TODO: link to post when lab is released). If the number in your username modulo 2 equals:
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
Execute the following commands in order to pull lab 5 down onto your machine:
```bash
# ssh to EC2
$ ssh datascience

# navigate to your private repository
$ cd your-private-repo

# fetch and merge lab 5
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

[*Back to top*](#table-of-contents)

## 3. Setup Lab 5 Environment
Inside the `lab_5` directory of your repository you should see a script called `setup.sh`. Simply execute the script as follows:
```bash
# --- on the EC2 machine ---
$ cd your-private-repo/lab_5/
$ bash setup.sh
```

[*Back to top*](#table-of-contents)

## 4. Lab Overview
TODO

### The Dataset
TODO

### TODO: More Subsections (If Necessary)

## 5. Questions

You are allowed to work in pairs for this assignment. In addition, you can lookup general tool functionalities on the internet, but not specific solutions to our questions.

TODO: more instructions (if necessary)

### Output Format
TODO (if necessary)

### Running Updates
This section is a rough copy of the running updates post on Piazza. We will do our best to keep the Lab README as up-to-date as possible with the Piazza post.

### Questions
TODO

## 6. Submission Instructions

### Before You Submit: Push Your Changes
Please make sure to push your code to your private repository:
```bash
$ git add -A # or, limit to the set of files you want to keep
$ git commit -m "pushing final state of lab 5"
$ git push origin main
```
We may not use the same machine(s) from lab-to-lab so in order to keep your changes you will need to check them into your private repository. Labs are designed to be independent -- so if you forget to push your changes it should not be the end of the world -- but it's better to be safe than sorry.

### Submitting as an Individual
To submit responses as an individual, simply run:
```sh
# TODO: add instruction(s) to generate final output files

# Zip the contents of the submission folder
cd submission
zip submission.zip *.csv
```

Submit the generated `submission.zip` file to Gradescope.

### Submitting as a Group
To submit responses as a group, simply run:
```sh
# TODO: add instruction(s) to generate final output files

# Zip the contents of the submission folder;
cd submission
zip submission.zip *.csv
```

Have one member of the group submit the generated `submission.zip` file to Gradescope. **The member who submits the assignment must then add their partner as a group member on the Gradescope submission: [details](https://help.gradescope.com/article/m5qz2xsnjy-student-add-group-members).**