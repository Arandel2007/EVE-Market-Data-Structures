try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import emds

required = [
    'python-dateutil<2.0',
    'pytz',
]

packages = [
    'emds',
    'emds.serialization',
    'emds.serialization.unified',
]

scripts = [
]

setup(
    name='emds',
    version=emds.__version__,
    description='EVE Market Data Relay',
    long_description=open('README.rst').read(),
    author='Greg Taylor',
    author_email='gtaylor@gc-taylor.com',
    url='https://github.com/gtaylor/EVE-Market-Data-Structures',
    packages=packages,
    scripts=scripts,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=required,
    license='BSD',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        ),
    )
