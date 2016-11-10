# Triangulation
A simple Python script to demonstrate the subdivision of a planar object into triangles.

## Requirements

 - [Python 3](https://www.python.org/)

 
## Installation

    python setup.py install

    pyvenv env
    pip install -r requirements.txt


## Usage

**Start**

    source env/bin/activate

**Stop**

    deactivate


## Developer Notes

Here are some notes for myself to understand my development process and the references I used.

### Preparations

Create and launch virtual environment

    pyvenv env
    source env/bin/activate

Install dependencies:

    pip install --upgrade pip
    pip install numpy matplotlib pytest sphinx sphinx_rtd_theme
    pip freeze > requirements.txt


### References

 - [Getting Started With setuptools and setup.py](https://pythonhosted.org/an_example_pypi_project/setuptools.html)
 - [Sphinx for Python documentation](http://gisellezeno.com/tutorials/sphinx-for-python-documentation.html)
 - [pytest - Installation and Getting Started](http://doc.pytest.org/en/latest/getting-started.html)
