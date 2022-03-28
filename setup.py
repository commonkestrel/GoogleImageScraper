from setuptools import find_packages, setup

setup(
    name='GoogleImageScraper',
    packages=find_packages(include=['GoogleImageScraper']),
    version='1.0.1',
    description='A package used for scraping results from Google Images and either getting the URLs or downloading the images to the local machine',
    author='Jibble',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    python_requires='>=3',
    test_suite='tests',
)