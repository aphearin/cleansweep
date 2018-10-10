from setuptools import setup


PACKAGENAME = "knowdust"
VERSION = "0.0.dev"


setup(
    name=PACKAGENAME,
    version=VERSION,
    setup_requires=["pytest-runner"],
    author=["Andrew Hearin", "Eve Kovacs"],
    author_email="ahearin@anl.gov",
    description="Some description",
    long_description="Longer description"
)
