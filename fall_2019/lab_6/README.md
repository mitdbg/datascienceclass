# Lab 6
*Assigned: Wednesday, October 30th.*

*Due: Wednesday, November 13th 11:59*

In this lab, you will explore in more details a subset of the functionality of [dask](dask.org), a parallel data processing library for Python. In the take home portion, you will implement a task-parallel version of a SQL operator, as well as measure and plot the runtime of a small parallel data processing task using dask.


## Setup

To start, check out/update the files for `lab_6`:

```bash
# Path to the directory containing your local clone
# of https://github.com/mitdbg/datascienceclass (this repo).
$ cd /path/to/datascienceclass

# Pull (fetch + merge) the latest changes from this repo.
$ git pull

# Change to lab 6's working directory.
$ cd lab_6/
```

**NOTE:** The commands above only pull the latest changes from this repo onto the local clone you have of it.  If you're using a "private fork" setup, and are trying to sync it with with the latest changes from this repo, then please refer to [this post](https://stackoverflow.com/questions/10065526/github-how-to-make-a-fork-of-public-repository-private) on specifics of how to do that.

**IMPORTANT! Make sure your Docker container is assigned enough CPU and Memory:**  We want to assign more than one core to Docker so that we can actually observe the effects of parallelism for this lab (e.g., at least 4 or 8 cores, and at least 2GB or 4GB of RAM). If you're using Docker for Mac, then it already assigns half of all your machine's cores and 2GB of RAM to Docker VM.  You can inspect how many are currently assigned, or change those values by referring to the instructions at https://docs.docker.com/docker-for-mac/#resources. For **Windows or otherwise Docker Toolbox Users**: You may need to manually increase the amount of cpu cores and memory for your Docker VM.  Please look at https://gist.github.com/scotthaleen/f7ba55ca3cedd4a8097f2f139177ddc7 for how to do so.

**IMPORTANT! (For Docker Toolbox Users only):** Before proceeding we need to get the IP address of the virtual machine running our docker container. to do this run the below command in the Docker Quickstart Terminal (or whatever terminal you have properly set up to run docker), and jot down the IP address returned. We will need to the IP address later in the lab! Do not proceed before doing this.

```bash
$ docker-machine.exe ip default
192.168.99.100
```

In the above example, the IP address you need to remember is ``192.168.99.100``, but yours may differ.

Startup your docker instance, and enter `lab 6`'s working directory.  We'll use the same base image as in lab1 to create a new container for this lab:
```bash
# We specify the same "6.s080:lab1" base image, mount /lab6
# from current dir (-v) set it as working directory (-w),
# and enable the ports we'll use for our jupyter server.
$ docker run -v "`pwd`":/lab6 -ti \
  -w"/lab6" \
  --name lab6-container \
  -p 8166:8166 \
  -p 8787:8787 \
  6.s080:lab1

# Install onto the image the additional requirements for
# this lab, and unzip the larger dataset.
$ ./install.sh

# Start out the jupyter server.
$ ./run.sh
```

If you accidentally exit your container (*e.g.,* by using **ctrl+d**), you can come back to it by running:
```bash
$ docker start -i lab6-container
```
## Reversed Lecture

In the reversed lecture we will perform some parallel data analysis tasks over three datasets in a jupyter notebook.

### Datasets

The `lab6/data` directory contains the same Spotify 218k songs dataset we used in lab4. We'll use it during the reverse lecture, in addition to two other datasets: a larger timeseries dataset we'll create using dask itself, and a publicly available collection of JSON data.

### Opening the Notebook

Follow the lab 6 setup steps for creating and starting your container, and ctrl+click one of the http URLs that show up in your Docker shell after running `./run.sh`, e.g.,:

```
>>>> Starting up jupyter notebook server...

[I 20:37:42.988 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[I 20:37:43.199 NotebookApp] Serving notebooks from local directory: /lab6
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

For the out of class portion of this lab, your objective is to answer programming assignments using two of the Python parallel data processing libraries we've seen in class: `multiprocessing` and `dask`.

### Submission Instructions

Like previous labs, submission will come in two parts.

1. Submit your writeup to Gradescope. Your writeup should include all student's names, mit email addresses, and the commit id of your code at the top of the page. The PDF should include your answers for the questions in the next section below.

2. Submit your code (including instructions on how to run it, if necessary) to a **Private** github repository, add the TAs for the course as collaborators on github.com (Usernames: MattPerron and jmftrindade) or github.mit.edu (Usernames: mperron and jfon). Note that we will only look at commits made before the deadline.

#### Part 1

**Q1:** In this question, you will use `multiprocessing` to implement a parallel web data scraper, whose base code is available in the [`scraper/`](scraper/) directory.  Specifically, we provide you most of the actual scraping code, and you only need to fill out the multiprocessing parts. Code for this question should be submitted in your github repo in the same [`scraper/scraper.py`](scraper/scraper.py) file we provide here. In your PDF writeup, please report the runtimes for running your scraper using different number of workers (e.g., 1, 2, and 4) **(30 pts).**

**UPDATE (Nov 7th 2019):** We've updated the scraper assignment slightly to instead scrape from a collection of local HTML files which we now include under the [`scraper/downloaded_html/`](scraper/downloaded_html/) directory. This is to avoid additional sources of non-determinism that were unrelated to concurrency issues. Specifically: regexlib.com arbitrarily reorders its list of regexes upon page refresh, which was leading the number of scraped regexes to vary across different runs of an otherwise correct solution.

#### Part 2

Here you will use the `Dask` `Bag` and `DataFrame` APIs you've seen during the in-class portion of the lab to answer some questions below.  In each question, you will scale your cluster from 1 up to 8 cores (or however many cores or machine has) in multiples of 2, **as we did for Q4 during the in-class portion of this lab**. You will measure and plot the total runtime for each of the cluster configurations (bar plot with `x` axis as #cores, `y` axis as runtime in milliseconds) for the following tasks:

**Q2** Using the same timeseries dask dataframe from in-class portion, compute a rolling 5m average `y` value for data only from January 2018. How does the min and the max runtimes you observed using dask compare to what you observed when using pandas? **(35 pts)**

**Q3** Using the same mybinder.org JSON data from in-class portion: who were the top 2 providers of notebooks in August 2019, and how many total runs did each of the 2 have? **(35 pts)**

**NOTE: For all questions in part 2 above, please submit your plots and code snippets inline in your PDF. Please also submit the code for your answers in your github repo, either as a single Python script called `part2.py`, or as a jupyter notebook called `part2.ipynb`.**

#### Part 3: extra credit (optional)

For all questions below, please include instructions on how to run your code as part of the PDF submission.

**Q4** The included [`queue_test.py`](queue_test.py) (Python2.X, Python3.X version at [`queue_test-python3.py`](queue_test-python3.py)) script implements a parallel aggregate operation over a single column of input JSON data (unzip [`data/json.zip`](data/json.zip) before running it). Use this code as example to implement a parallel filter (choose any column and filter value, let us know which ones you chose in your writeup). **(10 pts)**

**Q5** Similar to Q4, only this time implement a [`hash join`](https://en.wikipedia.org/wiki/Hash_join#Classic_hash_join). **(20 pts)**

**Q6** Pick one or more JSON datasets from https://github.com/jdorfman/awesome-json-datasets and write a script using either `dask`'s `Bag` or `multiprocessing` to answer a non-trivial question (i.e., more than just a single-column filter) about the data you picked. **(20 pts)**

**Q7** The [recipe scrapers GitHub project](https://github.com/hhursev/recipe-scrapers) provides an impressive collection of scrapers for food recipe websites. However, their example usage shows only one URL scraped at a time. Write a script that uses their library (`pip install recipe-scrapers` and `scrape_me` class) and the parallel data analytics libraries we've seen so far to scrape multiple recipes in parallel. **(20 pts)**

Optionally, include feedback in your write as below. (This does not count toward your writeup above)

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
