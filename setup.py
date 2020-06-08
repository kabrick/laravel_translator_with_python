from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='laravel_translator',
    version='0.1',
    packages=['laravel_translator'],
    install_requires=['googletrans'],
    url='https://github.com/kabrick/laravel_translator_with_python',
    license='MIT',
    author='douglas',
    author_email='kabuyedouglas53@gmail.com',
    description='Python package to translate laravel files using the googletrans python package',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
