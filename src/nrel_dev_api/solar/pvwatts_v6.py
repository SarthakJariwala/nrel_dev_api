from typing import Optional
from typing import Union

from .._core import check_api_key
from .._core import get_request


__all__ = ["PVWattsV6"]

# TODO - add attributes in docstring, add checks for data inputs
class PVWattsV6:
    """Estimate the energy production of grid-connected photovoltaic (PV) energy systems
    using NREL's PVWatts API based on a few simple inputs.
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
