NREL Dev API
============

|PyPI| |Status| |Python Version| |License|

|Read the Docs| |Tests| |Codecov| |pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/nrel_dev_api.svg
   :target: https://pypi.org/project/nrel_dev_api/
   :alt: PyPI
.. |Status| image:: https://img.shields.io/pypi/status/nrel_dev_api.svg
   :target: https://pypi.org/project/nrel_dev_api/
   :alt: Status
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/nrel_dev_api
   :target: https://pypi.org/project/nrel_dev_api
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/nrel_dev_api
   :target: https://opensource.org/licenses/Apache-2.0
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/nrel_dev_api/latest.svg?label=Read%20the%20Docs
   :target: https://nrel_dev_api.readthedocs.io/
   :alt: Read the documentation at https://nrel_dev_api.readthedocs.io/
.. |Tests| image:: https://github.com/SarthakJariwala/nrel_dev_api/workflows/Tests/badge.svg
   :target: https://github.com/SarthakJariwala/nrel_dev_api/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/SarthakJariwala/nrel_dev_api/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/SarthakJariwala/nrel_dev_api
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


Access data and analysis services that NREL (National Renewable Energy Lab) provides using a python API.

.. note:: In order to use `nrel_dev_api`, you will need an API key from NREL. You can get one `here <https://developer.nrel.gov/signup/>`_.


Installation
------------

You can install *nrel_dev_api* via pip_ from PyPI_:

.. code:: console

   pip install -U nrel_dev_api


Usage
-----

Set API Key
+++++++++++

Globally set your NREL developer API key.

.. code:: python

   from nrel_dev_api import set_nrel_api_key

   set_nrel_api_key(NREL_API_KEY)


Accesing Solar Data and Resources
+++++++++++++++++++++++++++++++++

++++++++++
PVWatts V6
++++++++++

Estimate the energy production of grid-connected photovoltaic (PV) energy systems using NREL's PVWatts V6 API based on a few simple location and system inputs.

.. code:: python

   from nrel_dev_api.solar import PVWattsV6

   # create PVWattsV6 class and pass the necessary location and system inputs
   pvwatts_v6 = PVWattsV6(system_capacity=4,
                        address="Seattle, WA",
                        azimuth=180,
                        tilt=40,
                        array_type=1,
                        module_type=1,
                        losses=10
                        )

   # You can also view the details about the station.
   pvwatts_v6.station_info

+++++++++++++++++++++++++++++++++++++++++++++++
Query National Solar Radiation Database (NSRDB)
+++++++++++++++++++++++++++++++++++++++++++++++

.. code:: python

   from nrel_dev_api.solar import NSRDB_DataQuery

   nsrdb_data_query = NSRDB_DataQuery(api_key=NREL_API_KEY, wkt="POINT(91.287 23.832)")

   # check the outputs
   nsrdb_data_query.outputs

Get solar resource data for a specific location

.. code:: python

   from nrel_dev_api.solar import SolarResourceData

   # get solar resource data for a specific latitude and longitude
   solar_resource_data = SolarResourceData(api_key=NREL_API_KEY, lat=40, lon=-105)

   # the output data is stored in the outputs attribute
   solar_resource_data.outputs

Get information on the closest climate data for a location.

.. code:: python

   from nrel_dev_api.solar import SolarDatasetQuery

   # create a dataset query class
   solar_dataset_query = SolarDatasetQuery(api_key=NREL_API_KEY, address="San Francisco, CA")

   # get the output
   solar_dataset_query.outputs


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the `Apache 2.0 license`_,
*nrel_dev_api* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

This project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.

.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Apache 2.0 license: https://opensource.org/licenses/Apache-2.0
.. _PyPI: https://pypi.org/
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/SarthakJariwala/nrel_dev_api/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
.. _Usage: https://nrel_dev_api.readthedocs.io/en/latest/usage.html
