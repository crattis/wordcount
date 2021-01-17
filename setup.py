import pathlib
from setuptools import setup

# The directory that contains this file
HERE = pathlib.Path(__file__).parent

# the text of the README file
README = (HERE / "README.md").read_text()

# this call to setup() does all the work
setup(name='',
      version='0.0.1',
      description='',
      long_description=README,
      long_description_content_type='text/markdown',
      url=None,
      author='',
      author_email='',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.9.0',
      ],
      packages=[''],
      include_package_data=True,
      # package_data={'': ['*.cfg', '*.txt']},
      # install_requires=['importlib_resources'],
      entry_points={"console_scripts":
                    ["{name}={name}.__main__:main",
                     ]},
      )
