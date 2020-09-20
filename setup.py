from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    readme_content = f.read()
setup(
    name='slugify-cli',
    version='0.3',
    description='Slugify CLI Tool',
    long_description=readme_content,
    long_description_content_type='text/markdown',
    url='https://github.com/ermalism/slugify-cli',
    author='ermalism',
    author_email='ismajliermal@gmail.com',
    license='WTFPL',
    packages=['slugify-cli'],
    scripts=['bin/slugify-cli'],
    python_requires='>3.5.2',
    zip_safe=False,
    download_url='https://github.com/ermalism/slugify-cli/archive/v0.3.tar.gz'
)
