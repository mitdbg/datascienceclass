# Lab 6
*Assigned: Wednesday, April 13th.*

*Due: Friday, April 22nd 11:59pm*

In this lab, you will explore parallel data processing libraries for Python.


# Setup

To start, check out/update the files for `lab_6`:

```bash
# Path to the directory containing your local clone
# of https://github.com/mitdbg/datascienceclass (this repo).
$ cd /path/to/datascienceclass

# Pull (fetch + merge) the latest changes from this repo.
$ git pull

# Change to lab 6's working directory.
$ cd spring_2022/lab_6/
```

**NOTE:** The commands above only pull the latest changes from this repo onto the local clone you have of it.  If you're using a "private fork" setup, and are trying to sync it with with the latest changes from this repo, then please refer to [this post](https://stackoverflow.com/questions/10065526/github-how-to-make-a-fork-of-public-repository-private) on specifics of how to do that.

**IMPORTANT! Make sure your Docker container is assigned enough CPU and Memory:** Since we will explicitly investigate parallelism in this lab, it is necessary to ensure that the Docker container is given enough resources for the tasks at hand. The command below will specify 4GB of memory and 2 CPUs for the Docker container. Please revise these settings as appropriate based on the actual hardware characteristics of your computer (e.g. if your computer has `n` cores and `M` GB of memory, you can assign `n-1` cores and `M-1` GB of memory to docker). 

Startup your docker instance, and enter `lab 6`'s working directory.  We'll use the same base image as in lab1 to create a new container for this lab:
```bash
# We specify the same "6.s079:lab1" base image, mount /lab6
# from current dir (-v) set it as working directory (-w),
# and enable the ports we'll use for our jupyter server.
$ docker run -v "`pwd`":/lab6 -ti \
  -w"/lab6" \
  --name lab6-container \
  --memory="4g" \
  --cpus="2.0" \
  -p 8166:8166 \
  -p 8787:8787 \
  6.s079:lab1

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
# Part 1: Reversed Lecture

In the reversed lecture we will perform some parallel data analysis tasks over three datasets in a jupyter notebook.

### Datasets

The `lab6/data` directory contains a Kaggle dataset with 218k spotify songs. These have the same features as the sample dataset in `lab2`, plus a `popularity` rank varying from 1 to 100. We'll use it during the reverse lecture, in addition to two other datasets: a larger timeseries dataset we'll create using dask itself, and a publicly available collection of JSON data.

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


### Running the Notebook

To execute code from a cell, you can either click "Run" at the top, or type shift+Enter after clicking a cell.  You can either run the entire notebook (`Restart & Run All` from the `Kernel` drop-down), or run each cell individually.  If you choose the latter, note that it is important that you run cells in order, as later cells depend on earlier ones.

Once you open your notebook on the browser, and check that the cells are rendering correctly (e.g., try the first one available), we're good to go from there.

# Part 2: Take Home

For the out of class portion of this lab, your objective is to answer programming assignments using three Python parallel data processing libraries: `multiprocessing`, `dask` and `pyspark`.  

## Tool 1: `multiprocessing`

**Q1 (10 pts):** In this question, you will use `multiprocessing` to implement a parallel web data scraper, whose base code is available in [`code/q1.py`](code/q1.py).  Specifically, we provide you most of the actual scraping code, and you only need to fill out the multiprocessing parts using `Process` and `Queue`. This 
follows along the lines of the examples presented in lecture 18. Take a look at `q1_example.py` for inspiration. In order to avoid additional sources of non-determinism that are unrelated to concurrency issues, the given code actually scrapes from a collection of local HTML files, found under the [`data/downloaded_html/`](data/downloaded_html/) directory. Below are some usage instructions for the `q1.py` script:

```
# Usage
$ python3 q1.py -h
usage: q1.py [-h] -i INPUT_CSV -o OUTPUT_CSV -n N_WORKERS [--redownload_html]

Scrapes regexes from http://regexlib.com.

arguments:
  -h, --help            show this help message and exit
  -i INPUT_CSV, --input_csv INPUT_CSV
                        Relative path of input CSV file containing regex
                        category and URLs to scrape.
  -o OUTPUT_CSV, --output_csv OUTPUT_CSV
                        Relative path of output CSV file containing scraped
                        regexes for each category.
  -n N_WORKERS, --num_workers N_WORKERS
                        Number of workers to use.
  --redownload_html     Redownloads HTML data from regexlib.com

# Example
$ python3 q1.py -i ../data/input_regexlib_urls.csv -o ../data/scraped_regexes.csv -n 8
```

Run your scraper using different numbers of workers (e.g., 1, 2, and 4) and report the runtimes in `q1.txt`. Also, submit `q1.py` after adding your code.

## Tool 2: `dask`

Here you will use the `Dask` `Bag` and `DataFrame` APIs presented during the in-class portion of the lab.  In each question, you will scale your cluster from 1 up to 8 cores (or however many cores or machine has) in multiples of 2 (as we did during the in-class portion of this lab). You should measure and plot the total runtime for each of the cluster configurations (bar plot with `x` axis as #cores, `y` axis as runtime in milliseconds) for the each of the tasks below. Feel free to use any plotting tool of your choice, including the ones presented in Lab 5. 

**Q2 (10 pts)** Using the same timeseries dataframe from in-class portion, compute a rolling 5m average for all the 2021 data. Then, repeat this task for each cluster size using `pandas`. How do the min and the max runtimes you observed using `dask` compare to what you observed when using `pandas`? Submit your code as `q2.py` and your runtime plot as `q2.jpg`.

**Q3 (10 pts)** Using the same mybinder.org JSON data from in-class portion: who are the top 3 providers of notebooks in 2022 (so far), and how many total runs does each of the 3 have? Submit your code as `q3.py` and your runtime plot as `q3.jpg`. 

## Tool 3: `pyspark`

In this part of the lab, you will use `pyspark`, the Python API for [`Apache Spark`](https://spark.apache.org/), another parallel multi-processing framework. To better exploit the parallelism enabled by Spark, we will be giving you temporary access to a cluster to run your code. To connect to the cluster, you first need to download the SSH key pair posted on [Piazza](https://piazza.com/class/kyxiji1fchcli?cid=233) and store it in the `.ssh` directory of this lab. You also need to either: be on campus; be on a network that requires MIT authentication (e.g. eduroam); or use the [MIT VPN](https://ist.mit.edu/vpn). Then, connect to the cluster and create a working directory using the following sequence of commands (note that you should *not* replace `markakis` with your own id in the first command below):

```
(Locally, outside docker) ssh markakis@istc1.csail.mit.edu -i ./.ssh/id_6s079

(On istc1) mkdir [your-kerberos]
(On istc1) cd [your-kerberos]
```

If you are using WSL, depending on where you have cloned the `datascienceclass` repo, you might get the following warning: ` WARNING: UNPROTECTED PRIVATE KEY FILE!`. This is because WSL mounts your Windows filesystem (`C:\`) at `/mnt/c` using the 9P protocol, which appears to set all permissions to `777`, which `ssh` considers too permissive for the SSH key files. The solution is to move your `datascienceclass` repo inside `/` on WSL, e.g. using `cp -rp /old/path/to/datascienceclass ~/new/path/to/datascienceclass` within a WSL terminal.

To copy code and other files into and out of the cluster, you can use [`scp`](https://devhints.io/scp), like the example below:

```
(Locally) scp -p /path/to/your/local/file markakis@istc1.csail.mit.edu:~/[your-kerberos]/path/to/remote/file
```

The goal is to answer the same questions that you answered for `dask`, but using the `pyspark` API instead. We provide starter code in `code/q4.py` and `code/q5.py`.  You should measure and plot the total runtime for each of the configurations described below (bar plot with `x` axis as #partitions, `y` axis as runtime in milliseconds) for the each of the tasks below. Feel free to use any plotting tool of your choice, including the ones presented in Lab 5. 

**Q4 (15 pts):** In `code/q4.py`, we provide starter code that creates a timeseries dataframe similar to the one used for question 2. Add code to this file to again compute a rolling 5m average for all the 2021 data. One way to get the 5-minute rolling average is to calculate it in a new column, by using [`pyspark.sql.Window`](https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.Window) in combination with [`over()`](https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.Column.over.html). Using `Window` will also partition the data, which is the most impactful parallelization parameter in this case. We can affect this partitioning by toggling the default partitioning variable, [`spark.sql.shuffle.partitions`](https://spark.apache.org/docs/latest/sql-performance-tuning.html#:~:text=1.1.0-,spark.sql.shuffle.partitions,-200). Repeat this task by varying the number of partitions from 1 to 100000 in multiples of 10 and report your results. Which value produces the best perfomance? Why do you think that is the case? Submit `q4.py` after adding your code, as well as `q4.jpg` with your runtime plots and `q4.txt` with your answers to the preceding questions.

**Q5 (15 pts):** Using the same mybinder.org JSON data from in-class portion: who are the top 3 providers of notebooks in 2022 (so far), and how many total runs does each of the 3 have? To simplify the ingestion process, the JSON files have been downloaded into the `jsondata2022` directory on the cluster - that is where your code should read them from (hint: take a look at [`pyspark.sql.DataFrame.unionByName`](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.DataFrame.unionByName.html)). Repeat this task by varying the number of partitions from 1 to 100000 in multiples of 10 and report your results. Which value produces the best perfomance? Why do you think that is the case? The runtime is generally low for all choices of partitions, so repeat the same process for 2021 - the JSON files have been downloaded into the `jsondata2021` directory on the cluster. Are the results different? Submit `q5.py` after adding your code, `q5-2021.jpg` and `q5-2022.jpg` with your runtime plots and `q5.txt` with your answers to the preceding questions.

## Choose your own adventure

**Q6 (40 pts):** Pick one or more JSON datasets from https://github.com/jdorfman/awesome-json-datasets and write a script using any of the tools above to answer a non-trivial question (i.e., more than just a single-column filter) about the data you picked. Submit your code as `q6.py` and your results as `q6.txt`. 

## Submission Instructions

Like previous labs, you should submit your solutions to Gradescope under the "Lab 6" assignment. In particular, you need to submit the following files:

* `q1.py`
* `q1.txt`
* `q2.py` 
* `q2.jpg`
* `q3.py` 
* `q3.jpg`
* `q4.py` 
* `q4.jpg`
* `q4.txt`
* `q5.py` 
* `q5-2021.jpg`
* `q5-2022.jpg`
* `q5.txt`
* `q6.py`
* `q6.txt`

