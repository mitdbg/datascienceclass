# Verta.ai / ModelDB demo

In this lab, [Manasi Vartak](https://www.linkedin.com/in/manasi-vartak/), CEO of [Verta.ai](http://verta.ai) will run a demo of end-to-end model data management features from her company's product.

## Setup

To start, check out/update the files for `verta_demo`:

```bash
# Path to the directory containing your local clone
# of https://github.com/mitdbg/datascienceclass (this repo).
$ cd /path/to/datascienceclass

# Pull (fetch + merge) the latest changes from this repo.
$ git pull

# Change to verta_demo's working directory.
$ cd verta_demo/
```

**NOTE:** The commands above only pull the latest changes from this repo onto the local clone you have of it.  If you're using a "private fork" setup, and are trying to sync it with with the latest changes from this repo, then please refer to [this post](https://stackoverflow.com/questions/10065526/github-how-to-make-a-fork-of-public-repository-private) on specifics of how to do that.

**IMPORTANT! (For Docker Toolbox Users only):** Before proceeding we need to get the IP address of the virtual machine running our docker container. to do this run the below command in the Docker Quickstart Terminal (or whatever terminal you have properly set up to run docker), and jot down the IP address returned. We will need to the IP address later in the lab! Do not proceed before doing this.

```bash
$ docker-machine.exe ip default
192.168.99.100
```

In the above example, the IP address you need to remember is ``192.168.99.100``, but yours may differ.

Startup your docker instance, and enter `verta_demo`'s working directory.  We'll use the same base image as in lab1 to create a new container for this lab:
```bash
# We specify the same "6.s080:lab1" base image, mount /verta_demo
# from current dir (-v) set it as working directory (-w),
# and enable the ports we'll use for our jupyter server.
$ docker run -v "`pwd`":/verta_demo -ti \
  -w"/verta_demo" \
  --name verta_demo-container \
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
$ docker start -i verta_demo-container
```

### Datasets

The `verta_demo/data` directory contains the dataset we'll be using for Manasi's demo.

### Opening the Notebook

Follow the setup steps for creating and starting your container, and ctrl+click one of the http URLs that show up in your Docker shell after running `./run.sh`, e.g.,:

```
>>>> Starting up jupyter notebook server...

[I 20:37:42.988 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[I 20:37:43.199 NotebookApp] Serving notebooks from local directory: /verta_demo
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
