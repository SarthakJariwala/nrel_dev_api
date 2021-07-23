import requests
import warnings
from typing import Dict, Any
from requests import Response

__all__ = ["get_request", "BASE_URL", "set_nrel_api_key", "check_api_key"]

BASE_URL = "https://developer.nrel.gov"


def get_request(query_url: str, params: Dict[str, Any]) -> Response:
    """Process the get request and returns the complete response"""

    resp = requests.get(BASE_URL + query_url, params=params)

    content : Dict[str, Any] = resp.json()

    # if any warnings are encountered, bring them up to the user
    if content.get("warnings"):
        warnings.warn(message=str(content["warnings"]), category=UserWarning)

    return resp


_API_KEY = None


def set_nrel_api_key(api_key: str) -> None:
    """Globally set the API key"""
    global _API_KEY

    if api_key:
        _API_KEY = api_key


def check_api_key() -> str:
    """Check if API Key has been set.
    If not set, a ValueError will be raised.
    If set, returns the API KEY.
    """
    global _API_KEY

    if _API_KEY is None:
        raise ValueError(
            """Please provide your NREL Developer API Key.
            You can set it using `set_nrel_api_key` function or pass it as `api_key` parameter."""
        )
    else:
        return _API_KEY
