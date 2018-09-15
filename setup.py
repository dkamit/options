
from setuptools import setup, find_packages
from options.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='options',
    version=VERSION,
    description='MyApp Does Amazing Things!',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Amith D K',
    author_email='amithdevatha1@gmail.com',
    url='https://github.com/dkamit/Options',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'options': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        options = options.main:main
    """,
)
