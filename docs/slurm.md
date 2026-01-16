[![Documentation Status](https://readthedocs.org/projects/su-hpc-tutorials/badge/?version=latest)](https://su-hpc-tutorials.readthedocs.io/en/latest/?badge=latest)
## Slurm Job Submission at SU-HPC Cluster

On Tosun cluster you can find Slurm submission script templates in a the folder: `/cta/share/`

Copy the one you need to your work folder and modify it as required:


`mkdir /$HOME/<username>/workfolder`

`cd /$HOME/<username>/workfolder/`

`cp /cta/share/jobscripts/example_submit.sh /$HOME/<username>/workfolder/my_experiment.sh`


`emacs my_experiment.sh`  
OR  
`vim my_experiment.sh`


## Submitting jobs to the queue
Jobs are submitted to the system with the command below:

`sbatch myscript.sh`

See the page about Slurm Queueing System Commands for more information on creating job submission scripts.


## Slurm Partitions (Job Queues)

Slurm Resource Manager has partitions which are job queues. These partitions has different limits and member nodes. You can see the active partitions and their limits with `sinfo` command on the cluster.

## [The Slurm Cheat Sheet](https://www.google.com/url?q=https://slurm.schedmd.com/pdfs/summary.pdf&sa=D&ust=1570008089861000)


## Essential Slurm Commands

| Command | Description | Example
| --------| ----------- | --------|
| `sbatch [script]`| Submit a batch job | `$ sbatch job.sub` |
| `scancel [job_id]` | Kill a running job or cancel queued one | `$ sbatch job.sub` |
`squeue` | List running or pending jobs | `$ squeue` |
| `squeue -u [userid]` | List running or pending jobs | `$ squeue -u mdemirkol`


## Submitting a Slurm Job Script

The job flags are used with `SBATCH` command.  The syntax for the Slurm directive in a script is  `#SBATCH`.  Some of the flags are used with the `srun` and `salloc` commands, as well for interactive jobs.

<a id="t.3dfacbe3b6b4ac376d3dc1e2da925d8ec90b580e"></a><a id="t.1"></a>

<table class="c52">

<tbody>

<tr class="c61">

<td class="c38" colspan="1" rowspan="1">

<span class="c40 c30 c39">Resource

</td>

<td class="c59" colspan="1" rowspan="1">

<span class="c40 c30 c39">Flag Syntax

</td>

<td class="c19" colspan="1" rowspan="1">

<span class="c40 c30 c39">Description

</td>

<td class="c68 c82" colspan="1" rowspan="1">

<span class="c40 c30 c39">Notes

</td>

</tr>

<tr class="c10">

<td class="c75" colspan="1" rowspan="1">

<span class="c29 c7">partition

</td>

<td class="c88" colspan="1" rowspan="1">

<span class="c43 c45 c7">--partition=short

</td>

<td class="c87" colspan="1" rowspan="1">

<span class="c43 c45 c7">Partition is a queue for jobs.

</td>

<td class="c85" colspan="1" rowspan="1">

<span class="c43 c45 c7">default on

</td>

</tr>

<tr class="c10">

<td class="c37" colspan="1" rowspan="1">

<span class="c29 c7">qos

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c43 c45 c7"> --qos=short

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c7 c73">QOS is quality of service value<span class="c43 c45 c7"> (limits or priority boost)

</td>

<td class="c27" colspan="1" rowspan="1">

<span class="c43 c45 c7">default on

</td>

</tr>

<tr class="c10">

<td class="c37" colspan="1" rowspan="1">

<span class="c29 c7">time

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c43 c45 c7">--time=01:00:00

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c43 c45 c7">Time limit for the job.

</td>

<td class="c27" colspan="1" rowspan="1">

<span class="c43 c45 c7">1 hour; default is 2 hours

</td>

</tr>

<tr class="c10">

<td class="c37" colspan="1" rowspan="1">

<span class="c29 c7">nodes

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c43 c45 c7">--nodes=1

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c43 c45 c7">Number of compute nodes for the job.

</td>

<td class="c27" colspan="1" rowspan="1">

<span class="c43 c45 c7">default is 1

</td>

</tr>

<tr class="c10">

<td class="c37" colspan="1" rowspan="1">

<span class="c29 c7">cpus/cores

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c43 c45 c7">--ntasks-per-node=4

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c43 c45 c7">Corresponds to number of cores on the compute node.

</td>

<td class="c27" colspan="1" rowspan="1">

<span class="c43 c45 c7">default is 1

</td>

</tr>

<tr class="c10">

<td class="c37" colspan="1" rowspan="1">

<span class="c29 c7">resource feature

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c43 c45 c7">--gres=gpu:1

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c43 c45 c7">Request use of GPUs on compute nodes

</td>

<td class="c27" colspan="1" rowspan="1">

<span class="c43 c45 c7">default is no feature

</td>

</tr>

<tr class="c79">

<td class="c37" colspan="1" rowspan="1">

<span class="c29 c7">memory

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c43 c45 c7">--mem=15500

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c43 c45 c7">Memory limit per compute node for the  job.  Do not use with mem-per-cpu flag.

</td>

<td class="c27" colspan="1" rowspan="1">

<span class="c43 c45 c7">default limit is 15500 MB per core in beegfs[101-108] nodes

</td>

</tr>

<tr class="c79">

<td class="c37" colspan="1" rowspan="1">

<span class="c29 c7">memory

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c43 c45 c7">--mem-per-cpu=4000

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c43 c45 c7">Per core memory limit.  Do not use the mem flag,

</td>

<td class="c27" colspan="1" rowspan="1">

<span class="c43 c45 c7">default limit is 15500 MB per core in beegfs[101-108] nodes

</td>

</tr>

<tr class="c10">

<td class="c37" colspan="1" rowspan="1">

<span class="c29 c7">account

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c43 c45 c7">--account=users

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c43 c45 c7">Users may belong to groups or accounts.

</td>

<td class="c27" colspan="1" rowspan="1">

<span class="c43 c45 c7">default is the user's primary group.

</td>

</tr>

<tr class="c61">

<td class="c37" colspan="1" rowspan="1">

<span class="c29 c7">job name

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c43 c45 c7">--job-name="hello_test"

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c43 c45 c7">Name of job.

</td>

<td class="c27" colspan="1" rowspan="1">

<span class="c43 c45 c7">default is the JobID

</td>

</tr>

<tr class="c61">

<td class="c37" colspan="1" rowspan="1">

<span class="c29 c7">constraint

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c43 c45 c7">--constraint=gpu

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c43 c45 c7">compute-nodes

</td>

<td class="c27" colspan="1" rowspan="1">

<span class="c43 c45 c7">AVAIL_FEATURES

</td>

</tr>

<tr class="c61">

<td class="c37" colspan="1" rowspan="1">

<span class="c29 c7">output file

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c43 c45 c7">--output=test.out

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c43 c45 c7">Name of file for stdout.

</td>

<td class="c27" colspan="1" rowspan="1">

<span class="c43 c45 c7">default is the JobID

</td>

</tr>

<tr class="c10">

<td class="c37" colspan="1" rowspan="1">

<span class="c7 c29">email address

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c43 c45 c7">--mail-user=username@sabanciuniv.edu

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c43 c45 c7">User's email address

</td>

<td class="c27" colspan="1" rowspan="1">

<span class="c43 c7 c45">required

</td>

</tr>

<tr class="c10">

<td class="c37" colspan="1" rowspan="1">

<span class="c29 c7">email notification

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c43 c45 c7">--mail-type=ALL

<span class="c43 c45 c7">--mail-type=END

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c43 c45 c7">When email is sent to user.

</td>

<td class="c27" colspan="1" rowspan="1">

<span class="c43 c45 c7">omit for no email

</td>

</tr>

</tbody>

</table>

## 

## Running a GUI on the Cluster 

Some applications provide the capability to interact with a graphical user interface (GUI). Large-memory applications and computationally steered applications can offer such capability. With Slurm, once a resource allocation is granted for an interactive session (or a batch job when the submitting terminal if left logged in), we can use `srun` to provide X11 graphical forwarding all the way from the compute nodes to our desktop using srun.



For example, to run an X terminal:

`srun --x11 -A users -p short -n1 --qos=users --pty $SHELL`

Note that the user must have X11 forwarded to the login node for this to work -- this can be checked by running `xclock` at the command line.

Additionally, the --x11argument can be augmented in this fashion --x11=[batch|first|last|all] to the following effects:

*   --x11=first This is the default, and provides X11 forwarding to the first compute hosts allocated.
*   --x11=last This provides X11 forwarding to the last of the compute hosts allocated.
*   --x11=all This provides X11 forwarding from all allocated compute hosts, which can be quite resource heavy and is an extremely rare use-case.
*   --x11=batch This supports use in a batch job submission, and will provide X11 forwarding to the first node allocated to a batch job. The user must leave open the X11 forwarded login node session where they submitted the job.

## Job Reason Codes

These codes identify the reason that a job is waiting for execution. A job may be waiting for more than one reason, in which case only one of those reasons is displayed.


<a id="t.9aa0fe54d84fd9007f94a96abe92ee9227ca6cfc"></a><a id="t.2"></a>

<table class="c52">

<tbody>

<tr class="c76">

<td class="c68 c86" colspan="1" rowspan="1">

<span class="c40 c39">State

</td>

<td class="c68 c81" colspan="1" rowspan="1">

<span class="c40 c39">Code

</td>

<td class="c33" colspan="1" rowspan="1">

<span class="c40 c39">Meaning

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">PENDING

</td>

<td class="c14" colspan="1" rowspan="1">

PD

</td>

<td class="c6" colspan="1" rowspan="1">

Job is awaiting resource allocation.

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">RUNNING

</td>

<td class="c14" colspan="1" rowspan="1">

R

</td>

<td class="c6" colspan="1" rowspan="1">

Job currently has an allocation.

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">SUSPENDED

</td>

<td class="c14" colspan="1" rowspan="1">

S

</td>

<td class="c6" colspan="1" rowspan="1">

Job has an allocation, but execution has been suspended.

</td>

</tr>

<tr class="c84">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">COMPLETING

</td>

<td class="c14" colspan="1" rowspan="1">

CG

</td>

<td class="c6" colspan="1" rowspan="1">

Job is in the process of completing. Some processes on some nodes may still be active.

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">COMPLETED

</td>

<td class="c14" colspan="1" rowspan="1">

CD

</td>

<td class="c6" colspan="1" rowspan="1">

Job has terminated all processes on all nodes.

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">CONFIGURING

</td>

<td class="c14" colspan="1" rowspan="1">

CF

</td>

<td class="c6" colspan="1" rowspan="1">

 Job has been allocated resources, but are waiting for them to become ready for use

</td>

</tr>

<tr class="c89">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">CANCELED

</td>

<td class="c14" colspan="1" rowspan="1">

CA

</td>

<td class="c6" colspan="1" rowspan="1">

Job was explicitly cancelled by the user or system administrator.

The job may or may not have been initiated.

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">FAILED

</td>

<td class="c14" colspan="1" rowspan="1">

F

</td>

<td class="c6" colspan="1" rowspan="1">

Job terminated with non-zero exit code or other failure condition.

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">TIMEOUT

</td>

<td class="c14" colspan="1" rowspan="1">

TO

</td>

<td class="c6" colspan="1" rowspan="1">

Job terminated upon reaching its time limit.

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">PREEMPTED

</td>

<td class="c14" colspan="1" rowspan="1">

PR

</td>

<td class="c6" colspan="1" rowspan="1">

Job has been suspended by an higher priority job on the same ressource.

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">NODE_FAIL

</td>

<td class="c14" colspan="1" rowspan="1">

NF

</td>

<td class="c6" colspan="1" rowspan="1">

Job terminated due to failure of one or more allocated nodes.

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">InvalidQOS

</td>

<td class="c14" colspan="1" rowspan="1">



</td>

<td class="c6" colspan="1" rowspan="1">

The job's QOS is invalid.

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">PartitionNodeLimit

</td>

<td class="c14" colspan="1" rowspan="1">



</td>

<td class="c6" colspan="1" rowspan="1">

The number of nodes required by this job is outside of it's partitions current limits. Can also indicate that required nodes are DOWN or DRAINED.

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">PartitionTimeLimit

</td>

<td class="c14" colspan="1" rowspan="1">



</td>

<td class="c6" colspan="1" rowspan="1">

The job's time limit exceeds it's partition's current time limit.

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">QOSJobLimit

</td>

<td class="c14" colspan="1" rowspan="1">



</td>

<td class="c6" colspan="1" rowspan="1">

The job's QOS has reached its maximum job count.

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">QOSResourceLimit

</td>

<td class="c14" colspan="1" rowspan="1">



</td>

<td class="c6" colspan="1" rowspan="1">

The job's QOS has reached some resource limit.

</td>

</tr>

<tr class="c20">

<td class="c8" colspan="1" rowspan="1">

<span class="c26">QOSTimeLimit

</td>

<td class="c14" colspan="1" rowspan="1">



</td>

<td class="c6" colspan="1" rowspan="1">

The job's QOS has reached its time limit.

</td>

</tr>

</tbody>

</table>



Please follow the links for more...



[JOB REASON CODES](https://www.google.com/url?q=https://slurm.schedmd.com/squeue.html%23lbAF&sa=D&ust=1570008089914000)

[JOB STATE CODES](https://www.google.com/url?q=https://slurm.schedmd.com/squeue.html%23lbAG&sa=D&ust=1570008089914000)



## QoS settings

<a id="t.001774065333135c85f7249b6b7fd6da4434d52b"></a><a id="t.3"></a>

<table class="c52">

<tbody>

<tr class="c56">

<td class="c49 c68" colspan="1" rowspan="1">

<span class="c43 c40 c30 c39">Command

</td>

<td class="c16 c68" colspan="1" rowspan="1">

<span class="c43 c40 c30 c39">Description

</td>

</tr>

<tr class="c56">

<td class="c49" colspan="1" rowspan="1">

<span class="c40 c30 c55 c7 c57">users

<span class="c34 c7">MaxSubmitJobsPerUser=10

<span class="c34 c7">MaxTRES=cpu=40

<span class="c34 c7">MaxNodes=2

<span class="c34 c7">--account=users

<span class="c77 c51 c55 c7">--qos=short

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c15 c7">All users

<span class="c7 c15">All partitions

<span class="c43 c77 c51 c7">

</td>

</tr>

<tr class="c56">

<td class="c49" colspan="1" rowspan="1">

<span class="c57 c40 c30 c55 c7">cuda

<span class="c34 c7">MaxSubmitJobsPerUser=10

<span class="c34 c7">MaxTRES=cpu=40

<span class="c34 c7">MaxNodes=2

<span class="c34 c7">--account=cuda

<span class="c7 c34">--qos=cuda

<span class="c34 c7">--gres=gpu:1

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c15 c7">All users

<span class="c15 c7">Includes cuda partitions

<span class="c15 c7">

</td>

</tr>

</tbody>

</table>



# <span class="c43 c72 c40">Software

## System software

*   Various operating systems are being used in our systems. If you need a particular OS please let us know.
*   [Slurm resource manager](https://www.google.com/url?q=https://slurm.schedmd.com/&sa=D&ust=1570008089922000)


### Compilers and parallel programming libraries

*   GNU Compiler (GCC, GFortran)
*   Java, Python, Perl, Ruby
*   OpenMPI - library for MPI message passing for use in parallel programming over Infiniband and Ethernet
*   ...and more.

### 

### Libraries

*   Please run the `module avail` command from your ssh console to view a list of available applications.


### Application software

*   Gaussian, Blast, Namd, Gromacs and many more.
*   Please run the `module avail` command from your ssh console to view a list of available applications.





