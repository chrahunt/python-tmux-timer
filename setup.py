import setuptools
from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='tmux_timer',
    version='0.1.0',
    author='Chris Hunt',
    author_email='chrahunt@gmail.com',
    description='Command-line timer for tmux',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chrahunt/python-tmux-timer',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['tmux_timer=tmux_timer.command_line:main']
    },
    install_requires=[],
    python_requires='>=2.7',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
)