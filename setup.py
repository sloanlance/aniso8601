try:
    from setuptools import setup
except ImportError:
    from distutils import setup

readme = open('README.rst', 'r')
README_TEXT = readme.read()
readme.close()

setup(
    name='aniso8601',
    version='0.49',
    description='A library for parsing ISO 8601 strings.',
    long_description=README_TEXT,
    author='Brandon Nielsen',
    author_email='nielsenb@jetfuse.net',
    url='https://bitbucket.org/nielsenb/aniso8601',
    packages=['aniso8601'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
