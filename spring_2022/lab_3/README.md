# Lab 3
*Due: Friday March 11th*

The aim of this lab is to implement a complete ML project in python. We will go through the steps of data exploration, cleaning and transformation followed by model training and selection.

The lab consists of two parts. The first part is an interactive tutorial held in class. It is adapted from [Aurélien Géron's excellent ML book](https://github.com/ageron/handson-ml2) with some modifications to make it a classification tutorial instead of a regression one. We will learn to classify neighborhoods by median house value. The tutorial will contains conceptual questions as well as fill-in code that we'll give you a few minutes to write.

In the second part of this lab, we expect you to pick any dataset of your own choosing and go through the steps mentioned above. You should try at least 3 different classes of models, and one of them should be an `xgboost` classifier or regressor. We recommend that you pick a dataset from [Kaggle](https://www.kaggle.com/). We will be very flexible in grading this lab; we just need to see that you've taken the right steps. You should submit your notebook to gradescope.


# Before the lab
To start, check out/update the files for `lab_3`:

```bash
# Path to the directory containing your local clone
# of https://github.com/mitdbg/datascienceclass (this repo).
cd /path/to/datascienceclass

# Pull (fetch + merge) the latest changes from this repo.
git pull

# Change to lab 3's working directory.
cd lab_3/

# Build docker
docker build -t 6s079_lab3 .

# Run
docker run -p 8888:8888 --name lab3-container -v "`pwd`":/lab3 6s079_lab3

# Copy the url starting with: http://127.0.0.1:8888/lab?token=...
# Paste in your browser.
```

If you've never used jupyter before, make sure to skim the [following tutorial](https://realpython.com/jupyter-notebook-introduction/) beforehand. Jupyter is a fairly intuitive tool, so you don't need a deep introduction.

# Submission
You should add your own ML project at the end of the "6.S079_Lab3.ipynb" notebook.
Submit this file to gradescope under the "Lab 3" assignment.