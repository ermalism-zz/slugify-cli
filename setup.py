from setuptools import setup
setup(
    name='slugify',
    version='0.1',
    description='Slugify CLI Tool',
    url='https://github.com/ermalism/slugify',
    author='ermalism',
    author_email='ismajliermal@gmail.com',
    license='WTFPL',
    packages=['slugify'],
    scripts=['bin/slugify'],
    python_requires='>3.5.2',
    zip_safe=False
)
