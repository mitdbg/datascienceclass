# Lab 4
*Due: Friday April 1st*

The aim of this lab is to implement a text "question and answer" system in Python. Given a corpus of text arranged in *pages* (e.g. tweets, tech support FAQs) and a user-provided string, the goal is to return the page that is most similar to the query string. We will try out the different approaches described in class and then use the resulting system in the context of different datasets.


# Before the lab
To start, check out/update the files for `lab_4`:

```bash
# Path to the directory containing your local clone
# of https://github.com/mitdbg/datascienceclass (this repo).
cd /path/to/datascienceclass

# Pull (fetch + merge) the latest changes from this repo.
git pull

# Change to lab 4's working directory.
cd spring_2022/lab_4/

# Build docker
docker build -t 6s079_lab4 .

# Run
docker run -p 8888:8888 --name lab4-container -v "`pwd`":/lab4 6s079_lab4

# Copy the url starting with: http://127.0.0.1:8888/lab?token=...
# Paste in your browser.
```

If you've never used jupyter before, make sure to skim the [following tutorial](https://realpython.com/jupyter-notebook-introduction/) beforehand. Jupyter is a fairly intuitive tool, so you don't need a deep introduction.

# Submission
You should submit your notebook to Gradescope under the "Lab 4" assignment.
