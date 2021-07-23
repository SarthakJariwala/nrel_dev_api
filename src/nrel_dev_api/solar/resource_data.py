from typing import Union, Dict, Any, Optional
from .._core import get_request, check_api_key


__all__ = ["SolarResourceData"]

# TODO - add attributes in docstring, add checks for data inputs
class SolarResourceData:
    """Returns various types of solar data for a location as a dictionary.
    The service from NREL currently returns data for
    average Direct Normal Irradiance, average Global Horizontal Irradiance,
    and average Tilt at Latitude.
    """

    QUERY_URL = "/api/solar/solar_resource/v1.json"

    def __init__(self, api_key: Optional[str]=None, lat: Union[int, float, None]=None, lon: Union[int, float, None]=None, address: Optional[str]=None):

        if api_key is None:
            # check if API key is already set
            api_key = check_api_key()

        self._params : Dict[str, Any] = {"api_key": api_key}

        # if address is not specified latitude and longitude must be specified
        if not address:
            self._params.update({"lat": lat, "lon": lon})
        else:
            self._params.update({"address": address})

        # complete raw response
        r = get_request(self.QUERY_URL, self._params)

        # complete response as a dict
        self.response : Dict[str, Any] = r.json()

        # only the outputs
        self.outputs = self.response["outputs"]

        # get the inputs provided
        self.inputs = self.response["inputs"]
