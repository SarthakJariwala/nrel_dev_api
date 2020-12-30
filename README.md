# nrel-dev-api
> Access data and analysis services that NREL (National Renewable Energy Lab) provides using a python API.


*NOTE: In order to use the NREL developer API, you will need an API key from NREL. You can get one [here](https://developer.nrel.gov/signup/). The process is simple and only requires your name and email (where you will receive the API key).*

## Install

`pip install --upgrade nrel_dev_api`

## How to use

### PVWatts V6

Estimate the energy production of grid-connected photovoltaic (PV) energy systems using NREL's PVWatts V6 API based on a few simple location and system inputs.

```python
#hide_output
from nrel_dev_api.solar import PVWattsV6

# create PVWattsV6 class and pass the necessary location and system inputs
pvwatts_v6 = PVWattsV6(api_key=NREL_API_KEY,
                       system_capacity=4,
                       address="Seattle, WA",
                       azimuth=180,
                       tilt=40,
                       array_type=1,
                       module_type=1,
                       losses=10
                      )

# the output data is stored in the outputs attribute
pvwatts_v6.outputs
```

You can also view the details about the station.

```python
pvwatts_v6.station_info
```




    {'lat': 47.61000061035156,
     'lon': -122.3399963378906,
     'elev': 48.70000076293945,
     'tz': -8.0,
     'location': 'None',
     'city': '',
     'state': 'Washington',
     'solar_resource_file': 'W12234N4761.csv',
     'distance': 1048}



### SolarResourceData

Get solar resource data for a specific location

```python
#hide_output
from nrel_dev_api.solar import SolarResourceData

# get solar resource data for a specific latitude and longitude
solar_resource_data = SolarResourceData(api_key=NREL_API_KEY, lat=40, lon=-105)

# the output data is stored in the outputs attribute
solar_resource_data.outputs
```

### SolarDatasetQuery

Get information on the closest climate data for a location.

```python
#hide_output
from nrel_dev_api.solar import SolarDatasetQuery

# create a dataset query class
solar_dataset_query = SolarDatasetQuery(api_key=NREL_API_KEY, address="San Francisco, CA")

# get the output
solar_dataset_query.outputs
```
