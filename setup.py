from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
README = (this_directory / "README.md").read_text()

setup(
    name='GoogleImageScraper',
    packages=find_packages(exclude=("tests")),
    version='1.0.2',
    description='This is a library for retrieving urls and downloading images from Google Images.',
    author='Jibble',
    license='MIT',
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    python_requires='>= 3',
    test_suite='tests',
    long_description=README,
    long_description_content_type='text/markdown'
)