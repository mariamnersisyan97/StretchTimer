from setuptools import setup

# Setup modular application
setup(
    name='application',
    packages=['application'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
