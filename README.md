# Triangulation
A simple Python script to demonstrate the subdivision of a planar object into triangles.

## Requirements

 - [Python 3](https://www.python.org/)

 
## Installation

Install dependencies

    pyvenv env
    source env/bin/activate
    pip install -r requirements.txt

Build and install package

    python setup.py build
    python setup.py install


## Usage
Further information about specific parts of the software development process.

### Execute

	python
	ftom triangulation import main
	main.start()
	quit()


Or shorter:

    python
    from triangulation import main; main.start(); quit()


### Virtual Environment

Start

    source env/bin/activate

Stop

    deactivate


### Testing
In the root directory you can execute all tests by calling the following command:

    pytest


### Documentation
Generate an API documentation based on the docstrings in the source code in read-the-docs style:

    cd docs
    make html


## Developer Notes

Here are some notes for myself to understand my development process and the references I used.

### Preparations

Create and launch virtual environment

    pyvenv env
    source env/bin/activate


Install dependencies:

    pip install --upgrade pip
    pip install matplotlib pytest sphinx sphinx_rtd_theme sphinxcontrib-napoleon
    pip freeze > requirements.txt


Autogenerate API documentation template (in root directory):

    sphinx-apidoc -f -o docs/source triangulation


Test new changes by building, installing an then testing in one command:

    python setup.py build && python setup.py install && pytest


### References

 - [Getting Started With setuptools and setup.py](https://pythonhosted.org/an_example_pypi_project/setuptools.html)
 - [Sphinx for Python documentation](http://gisellezeno.com/tutorials/sphinx-for-python-documentation.html)
 - [pytest - Installation and Getting Started](http://doc.pytest.org/en/latest/getting-started.html)
 - [Google Docstring Style](https://google.github.io/styleguide/pyguide.html#Comments)
