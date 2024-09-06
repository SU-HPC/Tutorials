[![Documentation Status](https://readthedocs.org/projects/su-hpc-tutorials/badge/?version=latest)](https://su-hpc-tutorials.readthedocs.io/en/latest/?badge=latest)
# SABANCI UNIVERSITY HPC CLUSTER QUICKSTART GUIDE

## Coverage of this QuickStart Guide

It is outside the scope of this manual to explain Linux commands and/or how parallel programs such as MPI work. This manual simply explains how to run jobs on the HPC cluster. SU High Performance Computing Clusters are build on Linux OS. So, using this HPC Cluster requires at a minimum some basic understanding of the [Linux Operating System.](https://www.google.com/url?q=http://en.wikipedia.org/wiki/Linux&sa=D&ust=1570008089847000)

## Getting a Cluster Account  

Sabancı University provides students, educators and researchers two HPC clusters: Sakura and Tosun. As a first step you need to determine which cluster is the most appropriate for you. Please contact your advisor or serdar.acir@sabanciuniv.edu to determine which cluster may better suit your needs.
In order to open an account in any of the clusters, please send an email to [serdar.acir@sabanciuniv.edu](mailto:serdar.acir@sabanciuniv.edu) along with the name of the advisor you are working with (if any), any particular partition that you need to access (if any) and a brief explanation of what you are planning to do on the cluster. In you brief explanation you can mention the name of the software that you want to have access to on the cluster. 

Sabancı HPC support will provide you, a username and a password. Upon first login, you will need to change your password with `passwd` command.
  
## New User Warnings

If you have never used a Cluster, or are not familiar with this cluster, you will probably want to read and follow the examples below to become familiar with how to run jobs on this HPC. It is a common practice by new users to ignore this manual and simply try to run jobs without understanding what they are doing. Unfortunately such an approach can easily impact other critical jobs running on the system and the users currently sharing the cluster with you. If your such action leads to the deterioration of the health of the HPC cluster, your account will be suspended shortly.

- First and foremost do NOT use the Login Nodes for work. Login nodes for 'logging in' only. Your programs are supposed to run on the Compute Nodes.

- Do not submit large number of jobs without first making a small test run to make sure everything works as expected. Start slow and then ramp up with jobs once you are familiar with how things work.

## How to use HPC

When you login to HPC you are connected to what is called the Login Node. The HPC Cluster has several major components:

*   Login nodes
*   Head node
*   Compute nodes

The head node runs all of the cluster critical services.

The login nodes are meant for simple tasks such as submitting jobs, checking on job status, editing (emacs, vi) and performing simple tasks.

The compute nodes are the workhorse of the cluster. For computational work both Serial or Parallel, in Batch mode or Interactive mode, you will be using the compute nodes.


## Getting started

Again, you will need to have a basic understanding of Linux and Linux commands in order to use the system, unless you use an application that has a web or GUI interface to the compute resources.

HPC clusters are shared resources that need to allocate user job requests amongst the available processors and memory in an equitable manner. This is done using a batch job queueing system and a job scheduler. 


## How do I login to the HPC Machines?
`[HPC_cluster] shown below can either be 'tosun.sabanciuniv.edu' or 'sakura.sabanciuniv.edu'. So replace it according to the cluster provided to you.`

### Windows
Use a secure shell client, e.g. [MobaXterm](https://www.google.com/url?q=https://mobaxterm.mobatek.net/features.html&sa=D&ust=1570008089849000)
1.  Here is the direct link to [download the mobaxterm program](https://www.google.com/url?q=http://mobaxterm.mobatek.net/download-home-edition.html&sa=D&ust=1570008089850000)
2.  Once you have mobaxterm installed [follow this guide](https://www.google.com/url?q=http://mobaxterm.mobatek.net/documentation.html&sa=D&ust=1570008089850000)

Note if you have cygwin installed, you can open a cygwin-terminal and then use ssh the same as for Linux and Mac below. If you aren’t sure what cygwin is, you can safely ignore this.

### Linux and Mac
Use `ssh` on the command line

If you are outside of the campus, first:  
`ssh username@flow.sabanciuniv.edu`  
Then  
`ssh username@[HPC_cluster]`  
  
If you are in the campus:  
`ssh username@[HPC_cluster]`

Note: Username is your HPC username, which is provided to you by the HPC support.

## Now that I have connected to the HPC System - What do I do now

![image info](folder_struct.png)

An abstract of the file system in the cluster is given above. When logging into the cluster, default folder is `your_home_folder`. Home folder have the alias `~`. Navigating through the files is done by `cd` command. Going parent direction is done by `cd ..` and going children direction is done by `cd folder_name`. One can reach from every folder to every folder by giving *relative path* from current folder or *absolute path* of target folder. `pwd` command will give your current folder's absolute path. To illustrate, reaching from `test` folder from `your_home_folder` could be done by:
`cd ../test`  
OR  
`cd /cta/test`.

- Listing files in current folders is done by `ls` command
- Moving folders is done by `mv` and `cp` commands.
  - `mv myscript.sh myscript_old.sh` will rename the file
  - `mv script.sh ~/` will move it to your home directory.
  - `cp /cta/share/example/example.sh ~/examples/` will copy `example.sh` to `examples/` directory in your home folder.  

This commands could be executed for every path one have access rights.

### Redirecting Output from/to HPC System

- To review output; `cat` command could be used.
- To copy the output to your local computer use `scp` command; 
    - From local `scp username@tosun:/absolute/path/to/file /relative/path/in/local`
    - From cluster `scp /relative/path/in/local username@local:/absolute/path/to/directory` could be used. 


## How do I edit my files on the HPC system?

Use a command line editor such as ‘vi’  or ‘emacs’. Here are some cheat notes to get you started:

*   [Vi cheat sheet](https://www.google.com/url?q=http://www.lagmonster.org/docs/vi.html&sa=D&ust=1570008089855000)
*   [UNIX tutorial for beginners](https://www.google.com/url?q=http://www.ee.surrey.ac.uk/Teaching/Unix/&sa=D&ust=1570008089855000)

## Home Folder
For Tosun: Home Folder is located at `/cta/users/username/`. 
For SunHPC: Home Folder is located at `/home/username/`. 
This folder is for long term storage to keep your job files. It is a general purpose distributed file system.


## Application software

To see a list of application software that is installed on the HPC, type the the module avail command from your ssh console once you have logged in. This will give a list of applications, along with their version numbers.

If you want any other software installed, or a different version, send a request email [serdar.acir@sabanciuniv.edu](mailto:serdar.acir@sabanciuniv.edu). Please include a detailed information about the software like web page, version, license etc. 

Some software will only run on a single processor, in which case you will probably not see any speedup from running the software on the supercomputer compared to running it on your desktop, unless it requires large memory. However, many standard software packages can take advantage of multiple processors, or have parallel versions (e.g. using MPI) that can. Check the user guide for the software.


# Slurm queuing system

HPCs that are shared among many users typically use a job scheduler system such as Slurm, Torque, SGE or Moab to manage submission and execution of jobs. 

The user needs to create a job script which specifies both the required compute resources, libraries and the job’s application that is to be run.

The script is then should be submitted to the job management system (queueing system) and if the requested resources (processors, memory, etc) are available on the system, the job will run.

If not, it will be put on hold in the queue until the resources become available again. In order to provide a fair share of the resources among users, the priority of jobs in the queue may be varied based on how much resources someone has used, is demanding now, how fast all the jobs can be completed, and so it is possible that jobs may not run in the order in which they have been submitted to the queue.

Users must have a basic understanding of the queueing system, how to create the job submission script, as well as check its progress or delete a job from the queueing system. Some example scripts are available to you şn the system. You can see the example scripts directory location in the welcome message of the Login Node.

## Running jobs

As mentioned, the jobs are managed by a Resource Manager in the HPC Cluster. 
You need to provide the Resource Manager the script that you wrote using the sbatch command at the Login Node.





