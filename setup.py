from setuptools import find_packages, setup  # prefer setuptools over distutils

with open('LICENSE') as file:
    license = file.read()

with open('README.rst') as file:
    long_description = file.read()

with open('VERSION') as file:
    version = file.read()

setup(
    name='testimony',
    version=version,
    url='https://github.com/SatelliteQE/testimony/',
    author='Suresh Thirugn',
    author_email='sthirugn@redhat.com',
    packages=find_packages(),
    install_requires=['Click', 'termcolor', 'docutils', 'pyyaml'],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points="""
        [console_scripts]
        testimony=testimony.cli:testimony
    """,
    description='Testimony inspects and reports on the python test cases.',
    long_description=long_description,
    license=license,
)
