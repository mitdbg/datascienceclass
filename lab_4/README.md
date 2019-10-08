Table of Contents
=================
- [Lab 4](#lab-4)
- [Setup](#setup)
- [Datasets](#datasets)
- [Quick intro to jupyter](#quick-intro-to-jupyter)
  * [Opening the notebook](#opening-the-notebook)
  * [Running the notebook](#running-the-notebook)

# Lab 4
*Assigned: Wednesday, October 2nd.*
*Due: N/A (no deliverables for this one)*

In this lab, you will use some of the ML algorithms and techniques we've seen so far in class for 3 different tasks over a music tasks: similarity, genre prediction, popularity prediction. We will walk you through these tasks using the included [ML_reverse_lecture.ipynb](ML_reverse_lecture.ipynb) jupyter notebook.

There are no deliverables for this lab. We'll ask you some questions during class for you to answer on clicker. We also highlight tasks for you to try out on your own; some of these during class. We strongly encourage you to complete them after class if necessary.

# Setup

To start, check out/update the files for `lab_4`:

```bash
# Path to the directory containing your local clone
# of https://github.com/mitdbg/datascienceclass (this repo).
$ cd /path/to/datascienceclass

# Pull (fetch + merge) the latest changes from this repo.
$ git pull

# Change to lab 4's working directory.
$ cd lab_4/
```

**NOTE:** The commands above only pull the latest changes from this repo onto the local clone you have of it.  If you're using a "private fork" setup, and are trying to sync it with with the latest changes from this repo, then please refer to [this post](https://stackoverflow.com/questions/10065526/github-how-to-make-a-fork-of-public-repository-private) on specifics of how to do that.

**IMPORTANT! (For Windows/Docker Toolbox Users only):** Before proceeding we need to get the IP address of the virtual machine running our docker container. to do this run the below command in the Docker Quickstart Terminal (or whatever terminal you have properly set up to run docker), and jot down the IP address returned. We will need to the IP address later in the lab! Do not proceed before doing this.

```bash
$ docker-machine.exe ip default
192.168.99.100
```

In the above example, the IP address you need to remember is ``192.168.99.100``, but yours may differ.

Startup your docker instance, and enter `lab 4`'s working directory.  We'll use the same base image as in lab1 to create a new container for this lab:
```bash
# We specify the same "6.s080:lab1" base image, mount /lab4
# from current dir (-v) set it as working directory (-w),
# and enable the ports we'll use for our jupyter server.
$ docker run -v "`pwd`":/lab4 -ti \
  -w"/lab4" \
  --name lab4-container \
  -p 8888:8888 \
  6.s080:lab1

# Install onto the image the additional requirements for
# this lab, and unzip the larger dataset.
$ ./install.sh

# Start out the jupyter server.
$ ./run.sh
```

If you accidentally exit your container (*e.g.,* by using **ctrl+d**), you can come back to it by running:
```bash
$ docker start -i lab4-container
```

# Datasets

The `lab4` directory contains two datasets under data directory. We'll use both during the reverse lecture:

1. `top2018_with_genre.txt`: The same dataset you used for [Part 3 of lab 2](https://github.com/mitdbg/datascienceclass/tree/master/lab_2/#top2018csv), with an additional genre_column.  See [Spotify API's audio features](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/) for more documentation on what each of the columns mean.

2. `spotify_songs.csv`: A Kaggle dataset with 218k spotify songs. These have the same features as above, plus a `popularity` rank varying from 1 to 100.


# Quick intro to jupyter

We will use a jupyter notebook for the entire duration of the lab. If you're not familiar with jupyter, think of it as an interactive python environment. If you'd like to learn more about jupyter, or if you've never used it before, take a look at their [official documentation](https://jupyterbook.org/intro.html) or at this [DataCamp tutorial](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook). You'll only need to edit and execute cells for this lab; no need to create a new notebook.

## Opening the notebook

We've done most of the heavylifting for you to be able to run a notebook server from your lab 4 Docker container.  You only need to follow the lab 4 setup steps for creating and starting your container, and ctrl+click one of the URLs that show up in your Docker shell after running `./install.sh`, e.g.,:

```
>>>> Starting up jupyter notebook server...

[I 20:37:42.988 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[I 20:37:43.199 NotebookApp] Serving notebooks from local directory: /lab4
[I 20:37:43.199 NotebookApp] The Jupyter Notebook is running at:
[I 20:37:43.199 NotebookApp] http://<docker_id>:8888/?token=<token>
[I 20:37:43.199 NotebookApp]  or http://127.0.0.1:8888/?token=<token>
[I 20:37:43.199 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 20:37:43.208 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///root/.local/share/jupyter/runtime/nbserver-60-open.html
    Or copy and paste one of these URLs:
        http://<docker_id>:8888/?token=<token>
     or http://127.0.0.1:8888/?token=<token>

```

**IMPORTANT! (For Windows/Docker Toolbox Users only):** Here is where we will need the IP address we took note of above. When accessing the notebook, replace ``127.0.0.1`` in the above URL with the IP address you noted above. With the example IP address, you will need to visit ``http://192.168.99.100:8888/?token=<token>`` (though your IP address is likely different).

If your shell doesn't support ctrl+click to open an URL, copy and paste the URL onto your browser.  I also find that the `http://127.0.0.1:8888/?token=<token>` URL works reliably, while the `<docker_id>` URL less so. Let us know if you have problems opening the server URL. **Make sure you open a `http://` URL, and not the `file:///` URL, as the latter refers to a local file within your container, and is unacessible from your host browser.**

## Running the notebook

To execute code from a cell, you can either click "Run" at the top, or type shift+Enter after clicking a cell.  You can either run the entire notebook (`Restart & Run All` from the `Kernel` drop-down), or run each cell individually.  If you choose the latter, note that it is important that you run cells in order, as later cells depend on earlier ones.

Once you open your notebook on the browser, and check that the cells are rendering correctly (e.g., try the first one available), we're good to go from there.
