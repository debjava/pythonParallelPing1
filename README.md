# How to install all project specific dependencies in virtual environment

## Python Version

`py -V` or `python -V`

current python version: **3.7.4**

## How to create a virtual environment

syntac is `py -m venv` <enviornment name>

In this case, the example is given below.

* Step 1: Execute the command using `py -m venv env`

* Step 2: Activate using the command `.\env\Scripts\activate`

* Step 3: Verify using the command `where python`

## Install dependencies in Virtual environment

### Ensure proper version of PIP
In the virtual environment use the following command,

`pip list`

After executing, you may get the following details.

>(env) E:\pydev-1-2020\projectDependencyInstall>pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0
You are using pip version 19.0.3, however version 20.0.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
>

### Upgrade PIP version
Execute the following command to upgrade to higher version of pip.

`py -m pip install --upgrade pip`

or

`python -m pip install --upgrade pip`

### Final step to install dependencies

After activating the virtual environment, execute the following command

`pip install -e .`

or

`pip install .`

### How to run

In Eclipse or Pycharm, run the file `Main.py`


### Performance Benchmark

**For 500 IP Addresses, parallel execution using Python Multi Processing**

Pool Size = 100, Total Time Taken:  26.1414336  seconds

Pool Size = 200, Total Time Taken:  21.209076600000003  seconds

Pool Size = 250, Total Time Taken:  22.6237878  seconds

Pool Size = 300, Total Time Taken:  26.2321263  seconds

Pool Size = 500, Total Time Taken:  38.721342  seconds

**For 500 IP Addresses, sequential execution using Python**

Total Time Taken:  1695.5716734  seconds
