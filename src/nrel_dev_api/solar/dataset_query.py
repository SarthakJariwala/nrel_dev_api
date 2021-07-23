from typing import Union, Optional
from .._core import get_request, check_api_key


# TODO - add attributes in docstring, add checks for data inputs
class SolarDatasetQuery:

    """Returns information on the closest climate data for a location."""

    QUERY_URL = "/api/solar/data_query/v1.json"

    def __init__(
        self,
        api_key: Optional[str] = None,
        lat: Union[int, float, None] = None,
        lon: Union[int, float, None] = None,
        address: Optional[str] = None,
        radius: int = 100,
        return_all_stations: bool = False,
    ):

        if api_key is None:
            # check if API key is already set
            api_key = check_api_key()

        self._params = {
            "api_key": api_key,
            "radius": radius,
            "all": 0 if return_all_stations is False else 1,
        }

        # if address is not specified latitude and longitude must be specified
        if not address:
            self._params.update({"lat": lat, "lon": lon})
        else:
            self._params.update({"address": address})

        # response
        r = get_request(self.QUERY_URL, self._params)

        # response as a dict
        self.response = r.json()

        # only outputs
        self.outputs = self.response["outputs"]

        # get the inputs provided
        self.inputs = self.response["inputs"]
