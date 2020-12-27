# nrel-dev-api
> Python API for NREL (National Renewable Energy Lab) developer API.


*NOTE: In order to use the NREL developer API, you will need an API key from NREL. You can get one [here](https://developer.nrel.gov/signup/). The process is simple and only requires your name and email (where you will receive the API key).*

## Install

`pip install --upgrade nrel_dev_api`

## How to use

### PVWatts V6

Estimate the energy production of grid-connected photovoltaic (PV) energy systems using NREL's PVWatts V6 API based on a few simple location and system inputs.

```python
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




    {'ac_monthly': [197.7586059570312,
      281.6268005371094,
      370.9747619628906,
      494.173583984375,
      512.7410888671875,
      540.3777465820312,
      592.75146484375,
      578.3128662109375,
      484.0272521972656,
      333.1608276367188,
      233.0740203857422,
      186.9368896484375],
     'poa_monthly': [58.9533576965332,
      83.970703125,
      113.2405624389648,
      153.9364776611328,
      160.2881927490234,
      171.4797973632812,
      192.8575592041016,
      188.4494323730469,
      154.3850555419922,
      102.9901733398438,
      69.81695556640625,
      55.09452438354492],
     'solrad_monthly': [1.901721239089966,
      2.998953580856323,
      3.652921438217163,
      5.131216049194336,
      5.170587062835693,
      5.715993404388428,
      6.221211433410645,
      6.079013824462891,
      5.14616870880127,
      3.322263717651367,
      2.327231884002686,
      1.77724277973175],
     'dc_monthly': [208.4532623291016,
      295.5293273925781,
      388.7458190917969,
      516.7040405273438,
      536.7205200195312,
      565.5615234375,
      619.6510620117188,
      604.18212890625,
      505.6007690429688,
      349.08642578125,
      244.8111724853516,
      196.868896484375],
     'ac_annual': 4805.91552734375,
     'solrad_annual': 4.120377063751221,
     'capacity_factor': 13.7155122756958}



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
# get solar resource data for a specific latitude and longitude
solar_resource_data = SolarResourceData(api_key=NREL_API_KEY, lat=40, lon=-105)

# the output data is stored in the outputs attribute
solar_resource_data.outputs
```




    {'avg_dni': {'annual': 6.06,
      'monthly': {'jan': 5.0,
       'feb': 5.34,
       'mar': 5.94,
       'apr': 6.11,
       'may': 6.36,
       'jun': 7.43,
       'jul': 7.48,
       'aug': 6.65,
       'sep': 6.81,
       'oct': 5.82,
       'nov': 5.11,
       'dec': 4.67}},
     'avg_ghi': {'annual': 4.81,
      'monthly': {'jan': 2.5,
       'feb': 3.43,
       'mar': 4.69,
       'apr': 5.69,
       'may': 6.6,
       'jun': 7.25,
       'jul': 7.14,
       'aug': 6.24,
       'sep': 5.35,
       'oct': 3.85,
       'nov': 2.75,
       'dec': 2.19}},
     'avg_lat_tilt': {'annual': 5.82,
      'monthly': {'jan': 4.79,
       'feb': 5.4,
       'mar': 6.07,
       'apr': 6.11,
       'may': 6.25,
       'jun': 6.47,
       'jul': 6.58,
       'aug': 6.44,
       'sep': 6.53,
       'oct': 5.71,
       'nov': 4.99,
       'dec': 4.47}}}



### SolarDatasetQuery

Get information on the closest climate data for a location.

```python
# create a dataset query class
solar_dataset_query = SolarDatasetQuery(api_key=NREL_API_KEY, address="San Francisco, CA")

# get the output
solar_dataset_query.outputs
```




    {'tmy2': {'id': '0-23234',
      'city': 'SAN FRANCISCO',
      'state': 'CALIFORNIA',
      'timezone': -8,
      'lat': 37.617,
      'lon': -122.4,
      'elevation': 2,
      'distance': 18362},
     'tmy3': {'id': '1-724940',
      'city': 'SAN FRANCISCO INTL AP',
      'state': 'CALIFORNIA',
      'timezone': -8,
      'lat': 37.617,
      'lon': -122.4,
      'elevation': 2,
      'distance': 18362},
     'intl': None,
     'nsrdb': {'id': '3-W122N037-W12242N3777',
      'city': '',
      'state': 'California',
      'country': None,
      'lat': 37.77,
      'lon': -122.42,
      'distance': 1129,
      'timezone': -8,
      'elevation': 55,
      'resolution': 4}}


