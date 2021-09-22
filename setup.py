from setuptools import setup


import codecs
with codecs.open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with codecs.open("VERSION", "r", encoding="utf-8") as fh:
    version = fh.read().strip()


setup(
    name='cast-unknown',
    version=version,
    packages=["cast_unknown"],
    license='MIT',
    description='Cast unknown value to desired type with typing support.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='NateScarlet',
    author_email='NateScarlet@Gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Typing :: Typed'
    ],
    url='https://github.com/NateScarlet/cast-unknown-python',
    install_requires=[
        'six~=1.15',
        'python-dateutil~=2.8'
    ],
    include_package_data=True,
)
