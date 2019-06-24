""" Installer for cc-pyspark
See:
https://github.com/colbyford/cc-pyspark
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
      name='ccpyspark',
      version='0.0.1',
      description='Process Common Crawl data with Python and Spark',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/colbyford/cc-pyspark',
      author='Common Crawl and Colby T. Ford',
      author_email='colby.ford@uncc.edu',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      python_requires='>=2.7',
      install_requires=['botocore','boto3','ujson','warcio','idna','beautifulsoup4','lxml']
      )
