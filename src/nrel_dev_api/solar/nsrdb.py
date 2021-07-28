import warnings
from itertools import chain
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import pandas as pd

from .._core import _API_KEY
from .._core import check_api_key
from .._core import get_request


__all__ = [
    "NSRDB_DataQuery",
    "get_nsrdb_download_links",
    "download_nsrdb_data",
    "LEAP_YEARS",
]


class NSRDB_DataQuery:
    """
    Returns information on the closest NSRDB datasets for a location
    including a set of links that can be used to download the data.
    """

    QUERY_URL = "/api/solar/nsrdb_data_query.json"

    def __init__(
        self,
        api_key: Optional[str] = None,
        wkt: Optional[str] = None,
        address: Optional[str] = None,
        lat: Union[int, float, None] = None,
        lon: Union[int, float, None] = None,
        dataset_type: Optional[str] = None,
        show_empty: bool = False,
    ):
        """
        Parameters
        ----------

        api_key:
            NREL developer API key.

        wkt:
            well-known text (WKT) representation of the geometry for which to extract data. May be a point, multipoint, or polygon geometry.
            Required if neither `lat`/`lon` not address are specified.

        address:
            Address to use. Required if neither `lat`/`lon` nor `wkt` are specified.

        lat:
            Latitude of the location. Required if neither `address` nor `wkt` are specified.

        lon:
            Longitude of the location. Required if neither `address` not `wkt` are specified.

        dataset_type:
            Type of the dataset to include in the response. Options are 'satellite' or 'station'.

        show_empty:
            Return metadata for all datasets including those with no data at the given location.
        """

        if api_key is None:
            api_key = check_api_key()

        self._params: Dict[str, Any] = {"api_key": api_key}

        # if well-known text is not provided look for address or lat/lon
        if not wkt:
            if not address:
                self._params.update({"lat": lat, "lon": lon})
            else:
                self._params.update({"address": address})
        elif wkt:
            self._params.update({"wkt": wkt})
        else:
            raise AttributeError(
                "Need to specify a location. Use lat/lon ot wkt or address."
            )

        if dataset_type:
            self._params.update({"type": dataset_type})

        if show_empty:
            self._params.update({"show_empty": show_empty})

        r = get_request(self.QUERY_URL, self._params)

        # complete response as a dictionary
        self.response = r.json()

        self.outputs = self.response["outputs"]


def get_nsrdb_download_links(
    year: int,
    interval: Optional[int] = None,
    api_key: Optional[str] = None,
    wkt: Optional[str] = None,
    address: Optional[str] = None,
    lat: Union[int, float, None] = None,
    lon: Union[int, float, None] = None,
    dataset_type: Optional[str] = None,
    show_empty: bool = False,
) -> List[str]:
    """
    Get NSRDB dowload links from data query for the specified location.

    Parameters
    ----------

    year:
        The year to use for searching through NSRDB.

    interval:
        Time interval of interest in minutes. Options are 15, 30, 60 (minutes).

    api_key:
        NREL developer API key.

    wkt:
        well-known text (WKT) representation of the geometry for which to extract data. May be a point, multipoint, or polygon geometry.
        Required if neither `lat`/`lon` not address are specified.

    address:
        Address to use. Required if neither `lat`/`lon` nor `wkt` are specified.

    lat:
        Latitude of the location. Required if neither `address` nor `wkt` are specified.

    lon:
        Longitude of the location. Required if neither `address` not `wkt` are specified.

    dataset_type:
        Type of the dataset to include in the response. Options are 'satellite' or 'station'.

    show_empty:
        Return metadata for all datasets including those with no data at the given location.
    """

    if api_key is None:
        api_key = check_api_key()

    nsrdb_data_query = NSRDB_DataQuery(
        api_key=api_key,
        wkt=wkt,
        address=address,
        lat=lat,
        lon=lon,
        dataset_type=dataset_type,
        show_empty=show_empty,
    )

    outputs = nsrdb_data_query.outputs

    available_years = []
    available_intervals = []
    links = []

    # find available years
    for i in range(len(outputs)):
        available_years.append(outputs[i]["availableYears"])

    # if year specified not available, raise Exception
    if year not in list(chain.from_iterable(available_years)):
        raise Exception("No data for the specified year.")

    # if interval is provided, check its availability
    if interval:
        # find avaialble intervals
        for i in range(len(outputs)):
            available_intervals.append(outputs[i]["availableIntervals"])

        # if time interval not available, raise Exception
        if interval not in list(chain.from_iterable(available_intervals)):
            raise Exception("No data for the specified time interval.")

    for i in range(len(outputs)):
        list_of_links = outputs[i]["links"]  # this returns a list of dicts

        for j in range(len(list_of_links)):

            # the str call is to cover 'tmy-*' style named years
            if str(year) in str(list_of_links[j]["year"]):

                # if interval is provided, give those links only
                if interval:
                    if list_of_links[j]["interval"] == interval:
                        links.append(list_of_links[j]["link"])
                else:
                    links.append(list_of_links[j]["link"])

    return links


# these are strings because of easy comparisons made later
LEAP_YEARS = [
    "1992",
    "1996",
    "2000",
    "2004",
    "2008",
    "2012",
    "2016",
    "2020",
    "2024",
    "2028",
    "2032",
]


def download_nsrdb_data(
    link: str,
    email: str,
    api_key: Optional[str] = None,
) -> pd.DataFrame:
    """
    Download NSRDB data from the provided link and returns a pandas DataFrame.

    Parameters
    ----------

    link:
        NSRDB download link. If not known, it can be acquired using `get_nsrdb_download_links()`.

    email:
        Valid email.

    api_key:
        NREL developer API key.
    """

    total_mins_in_year = 365 * 24 * 60

    if not isinstance(link, str):
        raise ValueError(f"Requires a str type. You provided {type(link)} type")

    if api_key is None:
        api_key = check_api_key()

    link = link.replace("yourapikey", api_key)
    link = link.replace("youremail", email)

    # get and split the parameters
    params: List[str] = link.split("?")[-1].split("&")

    for p in params:
        p_split = p.split("=")
        if p_split[0] == "interval":
            interval = p_split[1]
        if p_split[0] == "names":
            year = p_split[1][
                -4:
            ]  # this will catch only the year even from "tmy-*" names in years

            if year in LEAP_YEARS:
                link = link + "&leap_day=true"
                total_mins_in_year += 24 * 60  # add extra mins for the leap year

    df: pd.DataFrame = pd.read_csv(link, skiprows=2)

    try:
        # if this doesn't raise valuerror, then we can go ahead and set the new index
        int(year)
        df = df.set_index(
            pd.date_range(
                f"1/1/{year}",
                freq=interval + "Min",
                periods=total_mins_in_year / int(interval),
            )
        )

    except ValueError:
        warnings.warn(
            "Could not set the index to datetime; please do it manually", UserWarning
        )

    return df
