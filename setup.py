from setuptools import setup
setup(
    name='slugify-cli',
    version='0.2',
    description='Slugify CLI Tool',
    url='https://github.com/ermalism/slugify',
    author='ermalism',
    author_email='ismajliermal@gmail.com',
    license='WTFPL',
    packages=['slugify-cli'],
    scripts=['bin/slugify-cli'],
    python_requires='>3.5.2',
    zip_safe=False,
    download_url='https://github.com/ermalism/slugify-cli/archive/v0.2.tar.gz'
)
