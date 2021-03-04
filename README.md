# nrel-dev-api
> Access data and analysis services that NREL (National Renewable Energy Lab) provides using a python API.


*NOTE: In order to use the NREL developer API, you will need an API key from NREL. You can get one [here](https://developer.nrel.gov/signup/). The process is simple and only requires your name and email (where you will receive the API key).*

## Install

`pip install --upgrade nrel_dev_api`

## How to use

Globally set your NREL developer API key.

```python
from nrel_dev_api import set_nrel_api_key

set_nrel_api_key(NREL_API_KEY)
```

Alternatively, you can pass the `api_key` parameter as shown [here](#query-national-solar-radiation-database-(nsrdb)).

### PVWatts V6

Estimate the energy production of grid-connected photovoltaic (PV) energy systems using NREL's PVWatts V6 API based on a few simple location and system inputs.

```python
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



### Query National Solar Radiation Database (NSRDB)

```python
from nrel_dev_api.solar import NSRDB_DataQuery

nsrdb_data_query = NSRDB_DataQuery(api_key=NREL_API_KEY, wkt="POINT(91.287 23.832)")

# check the outputs
nsrdb_data_query.outputs
```




    [{'apiDocs': 'https://developer.nrel.gov/docs/solar/nsrdb/msg-iodc/',
      'availableIntervals': [15, 30, 60],
      'enabled': True,
      'displayName': 'MSG IODC: PSM v3',
      'metadataLink': 'https://nsrdb.nrel.gov/current-version',
      'name': 'msg-iodc',
      'ranking': 20,
      'availableYears': [2017, 2018, 2019],
      'apiUrl': 'https://developer.nrel.gov/api/nsrdb/v2/solar/msg-iodc-download',
      'links': [{'year': 2017,
        'interval': 15,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/msg-iodc-download.csv?names=2017&wkt=POINT%2891.287+23.832%29&interval=15&api_key=yourapikey&email=youremail'},
       {'year': 2018,
        'interval': 15,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/msg-iodc-download.csv?names=2018&wkt=POINT%2891.287+23.832%29&interval=15&api_key=yourapikey&email=youremail'},
       {'year': 2019,
        'interval': 15,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/msg-iodc-download.csv?names=2019&wkt=POINT%2891.287+23.832%29&interval=15&api_key=yourapikey&email=youremail'},
       {'year': 2017,
        'interval': 30,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/msg-iodc-download.csv?names=2017&wkt=POINT%2891.287+23.832%29&interval=30&api_key=yourapikey&email=youremail'},
       {'year': 2018,
        'interval': 30,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/msg-iodc-download.csv?names=2018&wkt=POINT%2891.287+23.832%29&interval=30&api_key=yourapikey&email=youremail'},
       {'year': 2019,
        'interval': 30,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/msg-iodc-download.csv?names=2019&wkt=POINT%2891.287+23.832%29&interval=30&api_key=yourapikey&email=youremail'},
       {'year': 2017,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/msg-iodc-download.csv?names=2017&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2018,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/msg-iodc-download.csv?names=2018&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2019,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/msg-iodc-download.csv?names=2019&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'}]},
     {'apiDocs': 'https://developer.nrel.gov/docs/solar/nsrdb/spectral-tmy-india-download/',
      'availableIntervals': [60],
      'enabled': True,
      'displayName': 'SUNY International Spectral',
      'metadataLink': 'https://nsrdb.nrel.gov',
      'name': 'spectral-india-tmy',
      'ranking': 40,
      'availableYears': ['tmy'],
      'apiUrl': 'https://developer.nrel.gov/api/nsrdb/v2/solar/spectral-india-tmy-download',
      'links': [{'year': 'tmy',
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/spectral-india-tmy-download.csv?names=tmy&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'}]},
     {'apiDocs': 'https://developer.nrel.gov/docs/solar/nsrdb/suny-india-data-download/',
      'availableIntervals': [60],
      'enabled': True,
      'displayName': 'SUNY International',
      'metadataLink': 'https://nsrdb.nrel.gov',
      'name': 'suny-india',
      'ranking': 20,
      'availableYears': [2000,
       2001,
       2002,
       2003,
       2004,
       2005,
       2006,
       2007,
       2008,
       2009,
       2010,
       2011,
       2012,
       2013,
       2014],
      'apiUrl': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download',
      'links': [{'year': 2000,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2000&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2001,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2001&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2002,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2002&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2003,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2003&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2004,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2004&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2005,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2005&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2006,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2006&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2007,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2007&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2008,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2008&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2009,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2009&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2010,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2010&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2011,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2011&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2012,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2012&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2013,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2013&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'},
       {'year': 2014,
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-download.csv?names=2014&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'}]},
     {'apiDocs': 'https://developer.nrel.gov/docs/solar/nsrdb/suny-india-tmy-data-download/',
      'availableIntervals': [60],
      'enabled': True,
      'displayName': 'SUNY International TMY',
      'metadataLink': 'https://nsrdb.nrel.gov',
      'name': 'suny-india-tmy',
      'ranking': 20,
      'availableYears': ['tmy'],
      'apiUrl': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-tmy-download',
      'links': [{'year': 'tmy',
        'interval': 60,
        'link': 'https://developer.nrel.gov/api/nsrdb/v2/solar/suny-india-tmy-download.csv?names=tmy&wkt=POINT%2891.287+23.832%29&interval=60&api_key=yourapikey&email=youremail'}]}]



### Get solar resource data for a specific location

```python
from nrel_dev_api.solar import SolarResourceData

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



### Get information on the closest climate data for a location.

```python
from nrel_dev_api.solar import SolarDatasetQuery

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


