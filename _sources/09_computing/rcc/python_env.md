# Python on Midway

This material can be found in the [Intro to RCC Workshop](https://rcc.uchicago.edu/support-and-services/workshops-and-training)

## Create a Conda Environment

First ssh into `midway2`
```bash
$ ssh <your_id>@midway2.rcc.uchicago.edu
```

You'll want to load a Python module
```bash
$ module avail python
```
should yield
```
---------------------------- /software/modulefiles2 ----------------------------
python/anaconda-2019.03          python/cpython-3.8.5             
python/anaconda-2020.02(default) python/intel-2020.up1            
python/cpython-3.7.0             
------------------------------- /etc/modulefiles -------------------------------
```

You can load the default python module (python/anaconda-2020.02) using:
```bash
$ module load python
```

Once you have loaded the module, you can create a conda environment for whatever project you're working on

```bash
$ conda create –name=<my-env> python==<python-vers>
$ conda activate <my-env>
```

## Run a Notebook from a login node

**WARNING:** nothing computationally intensive should be run from a login node

```bash
$ module load python
$ # export the login node IP address
$ export IP_ADDR=`ifconfig eno1 | grep 'inet ' |  awk '{print $2}'`
$ # choose a port number
$ export PORT_NUM=$(shuf -i8000-9000 -n1)
$ # launch jupyter
$ jupyter notebook --no-browser --ip=${IP_ADDR} --port $PORT_NUM
```

You can then open the link that the command creates
