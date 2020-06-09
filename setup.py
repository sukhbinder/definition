from setuptools import find_packages, setup

setup(
    name="definition",
    version="1.0",
    packages=find_packages(),
    license="Private",
    description="Definition in words",
    author="sukhbinder",
    author_email="sukh2010@yahoo.com",
    entry_points={
        'console_scripts': ['define = definition.main:main', ],
    },
)
