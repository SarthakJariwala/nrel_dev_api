# nrel-dev-api
> Python API for NREL (National Renewable Energy Lab) developer API.


*NOTE: In order to use the NREL developer API, you will need an API key from NREL. You can get one [here](https://developer.nrel.gov/signup/). The process is simple and only requires your name and email (where you will receive the API key).*

## Install

`pip install nrel_dev_api`

## How to use

## SolarResourceData

```python
"""Get solar resource data for a specific location"""

NREL_API_KEY = "DEMO_KEY"

# create a class
solar_resource_data = SolarResourceData(api_key=NREL_API_KEY, lat=40, lon=-105)

# perform the get request
solar_resource_data.get()
```




    {'version': '1.0.0',
     'warnings': [],
     'errors': [],
     'metadata': {'sources': ['Perez-SUNY/NREL, 2012']},
     'inputs': {'lat': '40', 'lon': '-105'},
     'outputs': {'avg_dni': {'annual': 6.06,
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
        'dec': 4.47}}}}



## PVWatts V6

```python
"""Estimate the energy production of grid-connected photovoltaic (PV) energy systems 
using NREL's PVWatts V6 API based on a few simple inputs."""

# create PVWattsV6 class
pvwatts_v6 = PVWattsV6(api_key=NREL_API_KEY,
                       system_capacity=4,
                       lat=40,
                       lon=-105,
                       azimuth=180,
                       tilt=40,
                       array_type=1,
                       module_type=1,
                       losses=10
                      )

# request the estimate
pvwatts_v6.get()
```




    {'inputs': {'system_capacity': '4',
      'module_type': '1',
      'losses': '10',
      'array_type': '1',
      'tilt': '40',
      'azimuth': '180',
      'lat': '40',
      'lon': '-105',
      'dataset': 'nsrdb',
      'radius': '100',
      'timeframe': 'monthly',
      'dc_ac_ratio': '1.2',
      'gcr': '0.4',
      'inv_eff': '96'},
     'errors': [],
     'warnings': [],
     'version': '1.0.2',
     'ssc_info': {'version': 45,
      'build': 'Linux 64 bit GNU/C++ Jul  7 2015 14:24:09'},
     'station_info': {'lat': 40.0099983215332,
      'lon': -105.0199966430664,
      'elev': 1581.839965820312,
      'tz': -7.0,
      'location': 'None',
      'city': '',
      'state': 'Colorado',
      'solar_resource_file': 'W10502N4001.csv',
      'distance': 2029},
     'outputs': {'ac_monthly': [474.4326171875,
       484.3903503417969,
       595.7704467773438,
       592.0599365234375,
       591.2662353515625,
       589.3538208007812,
       583.2352905273438,
       586.4593505859375,
       584.8131713867188,
       561.72314453125,
       486.1260375976562,
       445.6881713867188],
      'poa_monthly': [141.4809417724609,
       145.5711975097656,
       184.7876434326172,
       181.5513763427734,
       186.4280853271484,
       190.5132904052734,
       188.7499694824219,
       190.5398101806641,
       188.2213134765625,
       175.4444122314453,
       146.3170471191406,
       131.1568298339844],
      'solrad_monthly': [4.563901424407959,
       5.198971271514893,
       5.960891723632812,
       6.051712512969971,
       6.013809204101562,
       6.350442886352539,
       6.088708877563477,
       6.146445274353027,
       6.274043560028076,
       5.659497261047363,
       4.877234935760498,
       4.230865478515625],
      'dc_monthly': [497.9421081542969,
       511.1524963378906,
       634.3223266601562,
       623.7313842773438,
       617.8812866210938,
       615.4278564453125,
       609.3965454101562,
       612.7506713867188,
       610.5584106445312,
       588.6157836914062,
       508.0747680664062,
       465.4272155761719],
      'ac_annual': 6575.31884765625,
      'solrad_annual': 5.618043899536133,
      'capacity_factor': 18.76517868041992}}


