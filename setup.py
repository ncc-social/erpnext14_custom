from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext14_custom/__init__.py
from erpnext14_custom import __version__ as version

setup(
	name="erpnext14_custom",
	version=version,
	description="Customisations for ERPNext 14",
	author="NCC",
	author_email="social@ncc.gov.gh",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
