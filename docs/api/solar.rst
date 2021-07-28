Solar
=====

Access data and analysis services that provide access to solar resource data and NREL models.

--------------

NSRDB - National Solar Radiation Database
+++++++++++++++++++++++++++++++++++++++++

Data query and downloads from the National Solar Radiation Database.

.. autofunction:: nrel_dev_api.solar.get_nsrdb_download_links

.. autofunction:: nrel_dev_api.solar.download_nsrdb_data

.. autoclass:: nrel_dev_api.solar.NSRDB_DataQuery

PV Watts V6
+++++++++++

NREL's PVWatts® API estimates the energy production of grid-connected photovoltaic (PV) energy systems based on a few simple inputs.

.. autoclass:: nrel_dev_api.solar.PVWattsV6

Solar Resource Data
+++++++++++++++++++

Get various types of solar data for a location. The service from NREL currently returns data for average Direct Normal Irradiance, average Global Horizontal Irradiance, and average Tilt at Latitude.

.. autoclass:: nrel_dev_api.solar.SolarResourceData

Solar DatasetQuery
++++++++++++++++++

Get information on the closest climate data for a location.

.. autoclass:: nrel_dev_api.solar.SolarDatasetQuery
