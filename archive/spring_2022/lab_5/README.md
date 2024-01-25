# Lab 5
*Due: Wednesday April 13th*

In this lab, you will learn how to use a few data visualization tools in Python. In the in class portion we will introduce a subset of the functionality of Matplotlib, Seaborn, and Altair. In the take home portion, you will create an interesting visualization with these tools on a dataset of your choice.


# Before the lab
To start, check out/update the files for `lab_5`:

```bash
# Path to the directory containing your local clone
# of https://github.com/mitdbg/datascienceclass (this repo).
cd /path/to/datascienceclass

# Pull (fetch + merge) the latest changes from this repo.
git pull

# Change to lab 5's working directory.
cd lab_5/

# Build docker
docker build -t 6s079_lab5 .

# Run
docker run -p 8888:8888 --name lab5-container -v "`pwd`":/lab5 6s079_lab5

# Copy the url starting with: http://127.0.0.1:8888/lab?token=...
# Paste in your browser.
```

# Take Home
For the out of class portion of this lab, your objective is to build a visualization of a dataset of choosing. You are free to use any visualization tool, e.g., Seaborn, Altair, Vega, D3, or custom code.  Your visualization can be a static visualization, an animation, or an interactive tool. You may choose to make one or several plots or visualizations, depending on the data you choose and the goal of your presentation. For example data sets, you see the list of data sets we provided as a part of the final project, [available here](https://docs.google.com/document/d/1pnuV0PYvAtwPSbM6wueu6vlTjllSLfPTGh-stWpE_Fo/edit#heading=h.lpo62ee9zux6).

In addition, please submit a writeup of no more than 750 words describing what your visualization shows, why you feel it is compelling, how you made it,  and what alternative approaches or presentations you considered in making your visualization.

For some inspirational visualizations with code, you might look at:

* https://altair-viz.github.io/gallery/index.html 
* https://seaborn.pydata.org/examples/index.html
* https://d3js.org
* https://vega.github.io/vega/examples/

Feel free to use the same data set that you are planning to use for your final project for this lab.

Your project will be evaluated based on the following criteria (25 points each):

* Insightfulness of visualization - Does the visualization show something interesting, surprising, or unexpected, or that isn’t immediately obvious from the raw data?

* Technical complexity -  Making a good visualization usually requires significant iteration and preprocessing of the data.  What was involved in building your visualization?  You don’t need to write a lot of code to get full credit, but you shouldn’t just  re-use a pre-made visualization on an unmodified dataset.   Either build some kind of new visualization, or show us that you preprocessed the data in some interesting way.

* Quality of presentation -  Is it clear what you are showing?   Are the types of visualizations you use appropriate for the data types and scale of data you are presenting? Does your visualization use color, labels, and symbols properly and effectively?

* Writeup - Does your writeup describe why you chose your visualization and what it shows clearly and effectively?

When submitting your visualization, you can either upload a notebook, static visualization as a PDF, or a link to a video or a URL. Make sure you explain how to view your visualization. If you need help with sharing your visualization, please contact the course staff.

# Submission Instructions.
We will use gradescope for this assignment. Your submission should include:
1. A WRITEUP.md containing your writeup.
2. A README.md explaining how to view your visualization.
    * For example, if uploading a notebook, just say "Run notebook in filename.ipynb".
    * If uploading a PDF, just say "View PDF file filename.pdf"
3. Any file needed for your visualizations.