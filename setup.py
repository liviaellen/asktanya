from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()



setup(name='asktanya',
      version="1.0.9",
      description="Ask-tanya anything! Asktanya is a Python framework to search factual information on the internet.",
      # other arguments omitted
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=find_packages(),
      install_requires=requirements,
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      scripts=['scripts/ask-tanya'],
      zip_safe=False)
