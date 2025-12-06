# Sabancı Üniversitesi - Conda Virtual Environment Management Guide

**Date:** 28.10.2025

## Table of Contents

- [How to create and remove virtual environments on Conda](#how-to-create-and-remove-virtual-environments-on-conda)
  - [1. Resource Allocation from the headnode](#1-resource-allocation-from-the-headnode)
  - [2. Loading and Initializing Conda](#2-loading-and-initializing-conda)
  - [3. Creating a New Environment](#3-creating-a-new-environment)
  - [4. Activating an Environment](#4-activating-an-environment)
  - [5. Deactivating an Environment](#5-deactivating-an-environment)
  - [6. Removing an Environment](#6-removing-an-environment)

---

## How to create and remove virtual environments on Conda

### 1. Resource Allocation from the headnode

The login nodes have a strict CPU usage limit to ensure they remain responsive for all users.

Operations like `conda create`, `conda install`, or `pip install` are computationally intensive. If you run them directly on the login node, your process will be automatically terminated for exceeding the CPU limit by a script in the system.

To prevent this, you must first allocate an interactive session on the headnode using `srun`. All environment management commands should be run from within this session.

```bash
[dsimsek@login:~$] srun --account=users --qos=qos-all-mdt --partition=vsc-all-mdt --ntasks=1 --cpus-per-task=1 --nodes=1 --pty /bin/bash
```

This command will allocate resources from the headnode in order to create the virtual environment.

### 2. Loading and Initializing Conda

Then you must load the cluster's Conda module to make the `conda` command available.

```bash
[dsimsek@login:~$] module load conda/miniconda_20250420
```

Next, initialize Conda for your current shell session. This hooks Conda into your shell, enabling the `activate` command and showing the `(base)` prompt.

```bash
[dsimsek@login:~$] eval "$(conda shell.bash hook)"
(base) [dsimsek@login:~$]
```

### 3. Creating a New Environment

Now you can safely create your environment. The command below creates one named `deneme` with Python 3.6.

```bash
(base) [dsimsek@login:~$] conda create --name=deneme python=3.6
```

Conda will show you a plan and ask you to confirm. Type `y` and press Enter.

Using `conda create --name deneme` (as shown in the screenshots) installs the environment to your `$HOME` directory (`/cta/users/dsimsek/.conda/envs/deneme` in this case).

For large projects, it is recommended to use the `--prefix` option to install in your group's `/work` or `/scratch` directory:

```bash
conda create --prefix /path/to/your/work/my_project_env python=3.6
```

### 4. Activating an Environment

To use the packages within your new environment, you must activate it. Your shell prompt will change to show the active environment's name.

```bash
(base) [dsimsek@login:~$] conda activate deneme
(deneme) [dsimsek@login:~$]
```

You can list all your environments with `conda env list`. The active environment is marked with an asterisk (`*`).

### 5. Deactivating an Environment

When you are finished with the environment, use `conda deactivate` to return to the `(base)` environment.

```bash
(deneme) [dsimsek@login:~$] conda deactivate
(base) [dsimsek@login:~$]
```

### 6. Removing an Environment

To completely delete an environment and all its installed packages, use `conda remove -n [name] --all`.

```bash
(base) [dsimsek@login:~$] conda remove -n deneme --all
```

You will be asked to confirm the deletion. Type `y` and press Enter.

---

**End of Guide**
