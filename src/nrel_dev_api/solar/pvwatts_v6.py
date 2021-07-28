from typing import Optional
from typing import Union

from .._core import check_api_key
from .._core import get_request


__all__ = ["PVWattsV6"]

# TODO - add checks for data inputs


class PVWattsV6:
    """
    Use PVWatts API from NREL to estimate energy production.

    Estimate the energy production of grid-connected photovoltaic (PV) energy systems
    using NREL's PVWatts API based on a few simple inputs.

    Parameters
    ----------
    system_capacity:
        Nameplate capacity (kW).

    module_type:
        Module type.
        0 - Standard
        1 - Premium
        2 - Thin Film

    losses:
        System losses (percent).

    array_type:
        Array type.
        0 - Fixed Open Rack
        1 - Fixed Roof Mounted
        2 - 1 Axis
        3 - 1 Axis Backtracking
        4 - 2 Axis

    tilt:
        Tilt angle (degrees).

    azimuth:
        Azimuth angle (degrees).

    address:
        The address to use. Required if lat/lon or file_id not specified.

    lat:
        The latitude for the location to use.
        Required if address or file_id not specified.

    lon:
        The longitude for the location to use.
        Required if adress or file_id not specified.

    file_id:
        Reference to a specific climate data file to use.
        Must be a valid id returned by the `SolarDatasetQuery` API.
        Required if lat/lon or address not specified.

    dataset:
        The climate dataset to use.
        Should not be passed if using file_id to specify the climate data file.
        Options - nsrdb, tmy2, tmy3, intl.

    radius:
        The search radius to use when searching
        for the closest climate data station (miles).
        Use radius=0 to use the closest station regardless of the distance.

    timeframe:
        Granularity of the output response. Options - monthly, hourly.

    dc_ac_ratio:
        DC to AC ratio. Must be positive.

    gcr:
        Ground coverage ratio.

    inv_eff:
        Inverter efficiency at rated power.
    """

    QUERY_URL = "/api/pvwatts/v6.json"

    def __init__(
        self,
        system_capacity: Union[int, float],
        module_type: int,
        losses: Union[int, float],
        array_type: int,  # TODO - provide string options
        tilt: Union[int, float],
        azimuth: Union[int, float],
        api_key: Optional[str] = None,
        lat: Union[int, float, None] = None,
        lon: Union[int, float, None] = None,
        address: Optional[str] = None,
        file_id: Optional[str] = None,
        dataset: str = "nsrdb",
        radius: int = 100,
        timeframe: str = "monthly",
        dc_ac_ratio: float = 1.2,
        gcr: float = 0.4,
        inv_eff: Union[int, float] = 96,
    ):

        if api_key is None:
            api_key = check_api_key()

        self._params = {
            "api_key": api_key,
            "system_capacity": system_capacity,
            "module_type": module_type,
            "losses": losses,
            "array_type": array_type,
            "tilt": tilt,
            "azimuth": azimuth,
        }

        # only one of lat/lon, file_id, address needs to be specified
        if not address and not file_id:
            self._params.update({"lat": lat, "lon": lon})

        if not file_id and not lat and not lon:
            self._params.update({"address": address})

        if not address and not lat and lon:
            self._params.update({"file_id": file_id})

        # if file_id is specified, dataset info is not required
        if not file_id:
            self._params.update({"dataset": dataset})

        self._params.update(
            {
                "radius": radius,
                "timeframe": timeframe,
                "dc_ac_ratio": dc_ac_ratio,
                "gcr": gcr,
                "inv_eff": inv_eff,
            }
        )

        r = get_request(self.QUERY_URL, self._params)

        # get the complete response as dict
        self.response = r.json()

        # only the outputs category
        self.outputs = self.response["outputs"]

        # station info for the specified lat/lon
        self.station_info = self.response["station_info"]

        # get the inputs provided
        self.inputs = self.response["inputs"]
