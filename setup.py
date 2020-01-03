from setuptools import setup

def get_all_requirements():
    with open('requirements.txt') as file:
        requirements = file.read().splitliens()

    return requirements

readme = ''

with open('README.md') as file:
    readme = file.read()

setup(
    name='fluxpoint',
    packages=['fluxpoint'],
    version='1.0.0',
    description='Unofficial Python library for Fluxpoint Development',
    long_description=str(readme),
    author='August (Chris)',
    author_email='ohlookitsaugust@gmail.com',
    include_package_data=True,
    keywords=['fluxpoint'],
    install_requires=get_all_requirements(),
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ]
)