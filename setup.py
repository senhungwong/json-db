import setuptools

with open('readme.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='jsondb',
    version='1.0.0',
    description='Lightweight NoSQL JSON document database',
    long_description=long_description,
    author='Sen Hung Wong',
    author_email='0x53656e@gmail.com',
    url='https://github.com/senhungwong/json-db',
    packages=['jsondb'],
    keywords=['json', 'nosql', 'document-database', 'odm'],
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: MIT License",
        "Operating System :: OS Independent"
    )
)
