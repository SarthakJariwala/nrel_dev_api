# AUTOGENERATED! DO NOT EDIT! File to edit: 00_solar.ipynb (unless otherwise specified).

__all__ = ['SolarResourceData']

# Cell
import requests

class SolarResourceData:
    """Returns various types of solar data for a location.
    The service from NREL currently returns data for
    average Direct Normal Irradiance, average Global Horizontal Irradiance,
    and average Tilt at Latitude. The data outout format can be json or xml
    """

    BASE_URL = "https://developer.nrel.gov"
    QUERY_URL = "/api/solar/solar_resource/v1."

    def __init__(self, api_key, lat=None, lon=None, address=None, output_format="json"):

        self._params = {"api_key": api_key}

        # if address is not specified latitude and longitude must be specified
        if not address:
            self._params.update({"lat" : lat, "lon" : lon})
        else:
            self._params.update({"address": address})

        self.output_format = output_format

    def get(self):
        resp = requests.get(self.BASE_URL + self.QUERY_URL + f"{self.output_format}", params=self._params)
        content = resp.json()
        return content
