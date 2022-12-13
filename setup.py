from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in proshanti_lms/__init__.py
# from proshanti_lms import __version__ as version

setup(
	name="lms",
	version="1.1",
	description="LMS",
	author="TVF",
	author_email="tvft@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
