from setuptools import setup

setup(
    name='diderot',
    version='0.1',
    description='Diderot - Test Driven Development for RDF/OWL Ontologies',
    long_description='Diderot - Test Driven Development for RDF/OWL Ontologies',
    packages=['diderot'],
    package_data = {
        'rules': ['*.n3']
    },
    author='Icaro Medeiros',
    author_email = 'icaro.medeiros@gmail.com',
    license = 'PSF',
    url = 'http://github.com/icaromedeiros/marvin',
    platforms = [ 'Python 2.6 and newer' ],
    install_requires=[
        "ez_setup",  # Fuxi needs it for installation
        "FuXi==1.4.production"
    ]
)