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

**IMPORTANT! Make sure your Docker container is assigned enough CPU and Memory:** Since we will explicitly investigate parallelism in this lab, it is necessary to ensure that the Docker container is given enough resources for the tasks at hand. The command below will specify 4GB of memory and 2 CPUs for the Docker container. Please revise these settings as appropriate based on the actual hardware characteristics of your computer. 

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

The take-home part will be uploaded by the end of day on Wednesday, April 13th.

