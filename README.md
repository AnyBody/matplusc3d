===============================
matplusc3d
===============================


Command line tool for adding virtual makers to Coda Motion C3D files from the
information in exported Mat files.


* Free software: BSD license
* Documentation: https://matplusc3d.readthedocs.io.


Features
--------

* C3D files from the Coda Motion system only contain the dynamic markers.
  Virtual markers can only be exported to MatLAB `.mat` files. This script
  can adds virtual markers information from MatLAB files into the C3D files.


Install
-------

The easiest way to install is through the Anaconda Python Distribution and the conda package manager.
You can download it here: https://conda.io/miniconda.html

The package depend on [btk](), which unfortunantly is Python2.7 only. Thus, if you installed the Python 2.7
version you can just open a command prompt and run.

```cmd
C:\> conda install -c melund matplusc3d
```


### If you use Python 3.5

If you installed the Python 3.5 version of Anaconda/mini-conda (which you really should), then you need to first create a
Python 2.7 environment and activate it. :

```cmd
C:\> conda create -n py27 python=2.7
```


```cmd
C:\> activate py27

(py27) C:\>
```

The `py27` environement active you can run the install command above


Usage
------

When installed, the script `matplusc3d` will be available. Give it a c3file as argument:

```
(py27) C:\> matplusc3d filename.c3d
```

it will then look for a similarly named filename.mat in the same folder and combine the files.

To view the help:

```cmd
(py27) C:\>matplusc3d --help
Usage: matplusc3d-script.py [OPTIONS] [filename.c3d]

  Command line tool for adding virtual makers to Coda Motion C3D files from
  the information in exported Mat files.

  The tool assumes the c3d and mat files have the same filename but
  different extensions. If called without arguments the tool will find all
  matching c3d/mat files in the working directory.

Options:
  --overwrite  Overwrite existing c3dfiles. If not set, a file new file
               'filename_updated.c3d' will be created
  --help       Show this message and exit.

(py27) C:\>
```




Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

