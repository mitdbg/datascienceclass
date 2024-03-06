Table of Contents
=================
- [Lab 4: Text Processing and Similarity Search](#lab-0-setting-up-your-environment)
  * [1. Accessing Your EC2 Instance](#1-accessing-your-ec2-instance)
  * [2. Colab Setup](#2-additional-setup)
  * [3. Lab Overview](#4-lab-overview)
  * [4. Submission Instructions](#6-submission-instructions)
    * [Before You Submit: Push Your Changes](#before-you-submit-push-your-changes)
    * [Submitting as an Individual](#submitting-as-an-individual)
    * [Submitting as a Group](#submitting-as-a-group)

---
# Lab 4: Text Processing and Similarity Search
---
* **Assigned: TODO.**
* **Due: Apr. 3rd, 11:59:59 PM ET.**

* **Learning Objective**: Learn basic text processing, basic similarity metrics, and use similarity search to build a Q/A system.
* **Deliverables**: You will build a simple Q/A system using various similarity metrics and search tools.

## 1. Accessing Your EC2 Instance
First, please read the post announcing the release of Lab 4 on Piazza (TODO: link to post when lab is released). If the number in your username modulo 2 equals:
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

## 2. Colab Setup

For this lab, we will be using Google Colab, which is a free hosted Jupyter Notebook service.

Please read the brief instructions in the first cell of the Lab 4 notebook (linked below). You will need to create a copy of our notebook in your personal Google account. You can then work on the copy. (Note that MIT offers a free Google workspace account with your MIT email).

The Colab notebook for Lab 4 can be found [here](https://drive.google.com/file/d/1uI0D6wpPJJF8zNEldt5cCZXrKgGS6108/view?usp=sharing).

[*Back to top*](#table-of-contents)

## 3. Lab Overview
In this lab, you will use some of the text similarity concepts presented in the lecture to build a basic question-and-answer service.
All the tasks and questions are described in `6.S079_Lab4.ipynb`. Your job is to fill out the notebook.

### Running Updates
This section is a rough copy of the running updates post on Piazza. We will do our best to keep the Lab README as up-to-date as possible with the Piazza post.

## 4. Submission Instructions
When you've finished Lab 4 and are ready to submit, you will first need to download your .ipynb file. To do this, go to `File > Download > Download .ipynb`. See the reference image below:

![download-ipynb](../lab_3/readme-imgs/download_ipynb.png)

### Submitting as an Individual

Submit the filled and executed `6.S079_Lab4.ipynb` file to Gradescope.

### Submitting as a Group
Have one member of the group submit the `6.S079_Lab4.ipynb` file to Gradescope. **The member who submits the assignment must then add their partner as a group member on the Gradescope submission: [details](https://help.gradescope.com/article/m5qz2xsnjy-student-add-group-members).**
