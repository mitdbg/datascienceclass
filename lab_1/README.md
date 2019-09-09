# Lab 0: Setting up your environment

* **Learning Objective**: Learn to use Docker for the rest of the labs in the course.
* **Deliverables**: Get your environment up and running. While you are not required to turn anything in, for the interactive lecture and following labs you are expected to know how to use the Docker functionality outlined below. If you have problems setting up your environment, the time to ask questions is now. 

We will be using Docker for the labs in this course to ensure that everyone has a consistent environment. Fortunately, there are detailed online tutorials for setting up Docker. If you are interested in learning more about DockerAfter installing Docker you will build a docker image, run it in a container and ensure that you can access the tools required for the interactive lecture.

While the content of this Lab is straightforward, it is wise to get an early start to allow time to fix any issues that may arise setting up your environment.

## 1. Installing Docker


A docker installation typically requires 10-20GB of hard disk space. Completing this lab will require downloading about 1GB, and thus will be easiest to complete with a good internet connection.

Docker provides tutorials for installation on [OS X](https://docs.docker.com/v17.12/docker-for-mac/install/) and [Windows](https://docs.docker.com/v17.12/docker-for-windows/install/). For linux varients please follow instructions for your distribution [here](https://docs.docker.com/v17.12/install/#docker-ce).

Some OS X users may prefer installing Docker via [homebrew](https://brew.sh/), in which case the following commands suffice:

```bash
$ brew cask install docker       # Install Docker
$ open /Applications/Docker.app  # Start Docker
```

On some older systems, the above installation procedures may not work. For instance, Windows 10 users who do not use Pro or Enterprise editions cannot use the above setup. In these cases, use the Docker Toolbox instead. The Docker Toolbox sets up a virtual machine using Oracle VirtualBox where Docker can run. Instructions are [here](https://docs.docker.com/v17.12/toolbox/overview/)

If you do not have a machine capable of running Docker, contact the course staff on Piazza as soon as possible.

Install Docker using the instructions for your system.

Verify that your installation is working properly by running ``docker run hello-world`` on a command line. You should see the following output if docker was installed correctly.

        Unable to find image 'hello-world:latest' locally
        latest: Pulling from library/hello-world
        1b930d010525: Pull complete
        Digest: sha256:6540fc08ee6e6b7b63468dc3317e3303aae178cb8a45ed3123180328bcc1d20f
        Status: Downloaded newer image for hello-world:latest

        Hello from Docker!
        This message shows that your installation appears to be working correctly.

        To generate this message, Docker took the following steps:
         1. The Docker client contacted the Docker daemon.
         2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
            (amd64)
         3. The Docker daemon created a new container from that image which runs the
            executable that produces the output you are currently reading.
         4. The Docker daemon streamed that output to the Docker client, which sent it
            to your terminal.

        To try something more ambitious, you can run an Ubuntu container with:
         $ docker run -it ubuntu bash

        Share images, automate workflows, and more with a free Docker ID:
         https://hub.docker.com/

        For more examples and ideas, visit:
         https://docs.docker.com/get-started/

## 2. Setting Up Course Environment

In this section, we guide you through starting the docker container and running commands inside the container to ensure that it is working properly. 

1. Clone the lab repository:

```bash
$ git clone https://github.com/mitdbg/datascienceclass.git   # https
```

or

```bash
$ git clone git@github.com:mitdbg/datascienceclass.git       # ssh
```

2. Navigate to the lab_1 directory:

```
$ cd datascienceclass/lab_1/
```

3. Build the docker image we'll use for the course :

```bash
$ docker build -t 6.s080:lab1 .
```

This command reads the ``Dockerfile`` and creates an image containing the necessary dependencies for the lab, including python, sqlite, etc. We tag this image 6.s080:lab1. This may take a while, especially on a slow internet connection. However it does not actually start a container where you can run commands. 

To check that the image was created as expected run ``docker images``.
The image you just built should be at the top. The output should look something like the following. Note the repository set as ``6.s080`` and the tag ``lab1``.

        REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
        6.s080              lab1                10c46680a265        47 seconds ago      807MB
        ubuntu              latest              3556258649b2        2 weeks ago         64.2MB
        hello-world         latest              fce289e99eb9        7 months ago        1.84kB
        
Note that the image id on your machine will be different.

4. Start a container using the image we built above:

```bash
$ docker run -v "`pwd`":/lab1 -ti --name lab1-container 6.s080:lab1
```

The ``-v "`pwd`":/lab1`` option in this command maps the folder you are in to the docker container so any work you do inside the ``/lab1`` directory in your container will remain on your local file system in the ``6.S080_labs/lab_0`` directory. If you are running this from a windows shell you may have to replace ``"`pwd`"`` with the full path to the lab directory, e.g. ``"/c/Users/your_user_name/.../lab_0"``. You should now have a shell inside the container like the following

        root@9ceb15d6ed26:/lab1#
        
Note that the container id ``9ceb15d6ed26`` will be different on your own machine.

5. To exit the container, press **Ctrl+d**, or type **exit** and press **Enter**.

6. If you accidentally exit the container, you can start it again by running 

```bash
$ docker start -i lab1-container
```

7. To see recently run containers, run:

```bash
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS                     PORTS               NAMES
47bb9ac15b77        6.s080:lab1         "/bin/bash"         About a minute ago   Exited (0) 2 seconds ago                       lab1-container
33ca1b2e45ba        hello-world         "/hello"            6 minutes ago        Exited (0) 6 minutes ago                       brave_snyder
```

8. Make sure that files edited inside the container can be viewed outside. In the container run:

```bash
$ echo foo >> bar.txt
```

and ensure that the file bar.txt contains "foo" on your local file system. Edit bar.txt in your favorite text editor, replacing "foo" with "baz", and make sure that your changes are visible inside the container by running ``cat bar.txt``.
        
## 3. Running commands

You should now be able to build images from a Dockerfile (like the one in this directory), start and run a container from an image, exit the container, and start it again.

For this section all commands should be run inside the shell of the docker container.

In this section we will make sure that your environment is set up properly by running a few commands. If your environment is set up correctly, the following should be trivial to complete.

We will explain these tools in more detail in the interactive lecture, but for now we will make sure that you can run them as expected.


First we will make sure that you can run SQLite. To start a sqllite session run ``sqlite3`` inside your lab1 container.
You should now have a sqlite terminal as follows.


        SQLite version 3.22.0 2018-01-22 18:45:57
        Enter ".help" for usage hints.
        Connected to a transient in-memory database.
        Use ".open FILENAME" to reopen on a persistent database.
        sqlite>
        
run ``select time()`` and ``select 1`` to make sure it is working. Then exit sqlite with Ctrl+d

        sqlite> select time();
        19:02:05
        sqlite> select 1;
        1
        

Next, we will make sure the python environment is set up properly. Start a python terminal with ``python3`` inside the container.


## 4. Before the Lecture

Before the lecture, start the lab1-container and follow along.

# Lab 1: Basic Tools (SQL / Pandas)

Lab 1 will be released shortly before the lecture. It will have an in-class portion and a take-home portion.
In the lab we will explore the publicly available Federal Election Comission regarding funding
of political campaigns and politcal action comittees (PACs) in the 2016 eleciton.
