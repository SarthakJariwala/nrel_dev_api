# nrel-dev-api
> Python API for NREL (National Renewable Energy Lab) developer API to access.


{% include note.html content='In order to use the NREL developer API, you will need an API key from NREL. You can get one [here](https://developer.nrel.gov/signup/). The process is simple and only requires your name and email (where you will receive the API key). ' %}

## Install

`pip install nrel_dev_api`

## How to use

```python
"""Get solar resource data for a specific location"""

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


