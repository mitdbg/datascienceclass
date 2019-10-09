# Lab 5 
*Assigned: Wednesday, October 8th.*

*Due: Wednesday, October, 23rd 11:59*

In this lab, you will learn how to use a few data visualization tools in Python. In the in class portion we will introduce a subset of the functionality of Matplotlib, Seaborn, and Altair. In the take home portion, you will create an interesting visualization with these tools on a dataset of your choice.


## Setup

To start, check out/update the files for `lab_5`:

```bash
# Path to the directory containing your local clone
# of https://github.com/mitdbg/datascienceclass (this repo).
$ cd /path/to/datascienceclass

# Pull (fetch + merge) the latest changes from this repo.
$ git pull

# Change to lab 5's working directory.
$ cd lab_5/
```

**NOTE:** The commands above only pull the latest changes from this repo onto the local clone you have of it.  If you're using a "private fork" setup, and are trying to sync it with with the latest changes from this repo, then please refer to [this post](https://stackoverflow.com/questions/10065526/github-how-to-make-a-fork-of-public-repository-private) on specifics of how to do that.

**IMPORTANT! (For Docker Toolbox Users only):** Before proceeding we need to get the IP address of the virtual machine running our docker container. to do this run the below command in the Docker Quickstart Terminal (or whatever terminal you have properly set up to run docker), and jot down the IP address returned. We will need to the IP address later in the lab! Do not proceed before doing this.

```bash
$ docker-machine.exe ip default
192.168.99.100
```

In the above example, the IP address you need to remember is ``192.168.99.100``, but yours may differ.

Startup your docker instance, and enter `lab 5`'s working directory.  We'll use the same base image as in lab1 to create a new container for this lab:
```bash
# We specify the same "6.s080:lab1" base image, mount /lab5
# from current dir (-v) set it as working directory (-w),
# and enable the ports we'll use for our jupyter server.
$ docker run -v "`pwd`":/lab5 -ti \
  -w"/lab5" \
  --name lab5-container \
  -p 8166:8166 \
  6.s080:lab1

# Install onto the image the additional requirements for
# this lab, and unzip the larger dataset.
$ ./install.sh

# Start out the jupyter server.
$ ./run.sh
```

If you accidentally exit your container (*e.g.,* by using **ctrl+d**), you can come back to it by running:
```bash
$ docker start -i lab5-container
```
## Reversed Lecture

In the reversed lecture we will create some visualizations of our FEC data in a jupyter notebook.

### Datasets

The `lab5/data` directory contains similar datasets to lab 1. We'll use these during the reverse lecture. In particular, this dataset contains ``cand_summary.csv`` containing fundraising information about candidates for federal office going back to the 1980 federal elections, ``pac_summary.csv`` containing fundraising data about political action committees dating to the 2000 election cycle. Finally we have population data estimates in ``dist_pop.txt``.

### Opening the Notebook

Follow the lab 5 setup steps for creating and starting your container, and ctrl+click one of the http URLs that show up in your Docker shell after running `./run.sh`, e.g.,:

```
>>>> Starting up jupyter notebook server...

[I 20:37:42.988 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[I 20:37:43.199 NotebookApp] Serving notebooks from local directory: /lab5
[I 20:37:43.199 NotebookApp] The Jupyter Notebook is running at:
[I 20:37:43.199 NotebookApp] http://<docker_id>:8166/?token=<token>
[I 20:37:43.199 NotebookApp]  or http://127.0.0.1:8166/?token=<token>
[I 20:37:43.199 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 20:37:43.208 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///root/.local/share/jupyter/runtime/nbserver-60-open.html
    Or copy and paste one of these URLs:
        http://<docker_id>:8166/?token=<token>
     or http://127.0.0.1:8166/?token=<token>

```

**IMPORTANT! (For Docker Toolbox Users only):** Here is where we will need the IP address we took note of above. When accessing the notebook, replace ``127.0.0.1`` in the above URL with the IP address you noted above. With the example IP address, you will need to visit ``http://192.168.99.100:8166/?token=<token>`` (though your IP address is likely different).

If your shell doesn't support ctrl+click to open an URL, copy and paste the URL onto your browser.  I also find that the `http://127.0.0.1:8166/?token=<token>` URL works reliably, while the `<docker_id>` URL less so. Let us know if you have problems opening the server URL. **Make sure you open a `http://` URL, and not the `file:///` URL, as the latter refers to a local file within your container, and is unacessible from your host browser.**

### Running the Notebook

To execute code from a cell, you can either click "Run" at the top, or type shift+Enter after clicking a cell.  You can either run the entire notebook (`Restart & Run All` from the `Kernel` drop-down), or run each cell individually.  If you choose the latter, note that it is important that you run cells in order, as later cells depend on earlier ones.

Once you open your notebook on the browser, and check that the cells are rendering correctly (e.g., try the first one available), we're good to go from there.

## Take Home

For the out of class portion of this lab, your objective is to build a visualization of a dataset of choosing.   You are free to use any visualization tool, e.g., Seaborn, Altair, Vega, D3, or custom code.  Your visualization can be a static visualization, an animation, or an interactive tool.  You may choose to make one or several plots or visualizations, depending on the data you choose and the goal of your presentation. For example data sets, you see the list of data sets we provided as a part of the final project, available here:

https://docs.google.com/document/d/1FuzEq25XgX4u0cY1nRSQzduBh0oANnVzXuQjr2cY_cE/edit

For some inspirational visualizations with code, you might look at:

* https://d3js.org
* https://vega.github.io/vega/examples/
* https://seaborn.pydata.org/examples/index.html
* https://altair-viz.github.io/gallery/index.html 

Feel free to use the same data set that you are planning to use for your final project for this lab.

Your project will be evaluated based on the following criteria (25 points each):

* Insightfulness of visualization - Does the visualization show something interesting, surprising, or unexpected, or that isn’t immediately obvious from the raw data?

* Technical complexity -  Making a good visualization usually requires significant iteration and preprocessing of the data.  What was involved in building your visualization?  You don’t need to write a lot of code to get full credit, but you shouldn’t just  re-use a pre-made visualization on an unmodified dataset.   Either build some kind of new visualization, or show us that you preprocessed the data in some interesting way.

* Quality of presentation -  Is it clear what you are showing?   Are the types of visualizations you use appropriate for the data types and scale of data you are presenting? Does your visualization use color, labels, and symbols properly and effectively?

* Writeup - Does your writeup describe why you chose your visualization and what it shows clearly and effectively?

When submitting your visualization, you can either upload a static visualization as a PDF, or a link to a video or a URL.   In addition, please submit a writeup of no more than 750 words describing what your visualization shows, why you feel it is compelling, how you made it,  and what alternative approaches or presentations you considered in making your visualization.  If you need help with sharing your visualization, please contact the course staff.

### Submission Instructions

Like previous labs, submission will come in two parts.

1. Submit your writeup to Gradescope. Your writeup should include all student's names, mit email addresses, and the commit id of your code at the top of the page.

**At the beginning of your submission please indicate how we should view your visualization (website url, python notebook, etc)**

Optionally, include feedback in your write as below. (This does not count toward your 750 word writeup)

If you have any comments about this lab, or any thoughts about the
class so far, we would greatly appreciate them.  Your comments will
be strictly used to improve the rest of the labs and classes and have
no impact on your grade.

Some questions that would be helpful:

* Is the lab too difficult or too easy?  
* How much time (minutes or hours) did you spend on it?
* Did you look forward to any exercise that the lab did not cover?
* Which parts of the lab were interesting or valuable towards understanding the material?
* How is the pace of the course so far?


2. Submit your code to a **Private** github repository, add the TAs for the course as collaborators on github.com (Usernames: MattPerron and jmftrindade) or github.mit.edu (Usernames: mperron and jfon). Note that we will only look at commits made before the deadline.
