Usage
=====

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
