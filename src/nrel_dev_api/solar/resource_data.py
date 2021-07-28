from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

from .._core import check_api_key
from .._core import get_request


__all__ = ["SolarResourceData"]

# TODO - add attributes in docstring, add checks for data inputs
class SolarResourceData:
    """Returns various types of solar data for a location as a dictionary.
    The service from NREL currently returns data for
    average Direct Normal Irradiance, average Global Horizontal Irradiance,
    and average Tilt at Latitude.
    """

    QUERY_URL = "/api/solar/solar_resource/v1.json"

    def __init__(
        self,
        api_key: Optional[str] = None,
        lat: Union[int, float, None] = None,
        lon: Union[int, float, None] = None,
        address: Optional[str] = None,
    ):
        """
        Parameters
        ----------

        api_key:
            NREL developer API key.

        lat:
            Latitude of the location. Required if address is not specified.

        lon:
            Longitude of the location. Required if address is not specified.

        address:
            Address to use. Required if `lat` and `lon` are not specified.
        """

        if api_key is None:
            # check if API key is already set
            api_key = check_api_key()

        self._params: Dict[str, Any] = {"api_key": api_key}

        # if address is not specified latitude and longitude must be specified
        if not address:
            self._params.update({"lat": lat, "lon": lon})
        else:
            self._params.update({"address": address})

        # complete raw response
        r = get_request(self.QUERY_URL, self._params)

        # complete response as a dict
        self.response: Dict[str, Any] = r.json()

        # only the outputs
        self.outputs = self.response["outputs"]

        # get the inputs provided
        self.inputs = self.response["inputs"]
