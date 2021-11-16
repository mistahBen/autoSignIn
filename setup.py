from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = 'autosignin for Google accounts'
LONG_DESCRIPTION = 'autosignin for Google accounts. First package attempt.'

# Setting up
setup(

        name="signin",
        version=VERSION,
        author="Ben Alexander",
        author_email="ben@tuhax.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires="requirements.txt",
        keywords=['python', 'first package', 'selenium bot'],
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
        ]
)
