from setuptools import setup
setup(
    name='slugify',
    version='0.1',
    description='Slugify CLI Tool',
    url='https://github.com/ermalism/slugify-cli',
    author='ermalism',
    author_email='ismajliermal@gmail.com',
    license='WTFPL',
    packages=['slugify'],
    scripts=['bin/slugify'],
    zip_safe=False
)
