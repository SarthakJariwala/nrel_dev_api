# AUTOGENERATED! DO NOT EDIT! File to edit: 04_solar.nsrdb.ipynb (unless otherwise specified).

__all__ = ['NSRDB_DataQuery']

# Cell
from .._core import get_request

class NSRDB_DataQuery:
    """Returns information on the closest NSRDB datasets for a location
    including a set of links that can be used to download the data.
    """

    QUERY_URL = "/api/solar/nsrdb_data_query.json"

    def __init__(self,
                 api_key,
                 wkt=None,
                 address=None,
                 lat=None,
                 lon=None,
                 dataset_type=None,
                 show_empty=False,
                ):

        self._params = {"api_key": api_key}

        # if well-known text is not provided look for address or lat/lon
        if not wkt:
            if not address:
                self._params.update({"lat" : lat, "lon" : lon})
            else:
                self._params.update({"address" : address})
        else:
            self._params.update({"wkt" : wkt})

        if dataset_type:
            self._params.update({"type" : dataset_type})

        if show_empty:
            self._params.update({"show_empty" : show_empty})

        r = get_request(self.QUERY_URL, self._params)

        # complete response as a dictionary
        self.response = r.json()

        self.outputs = self.response["outputs"]
