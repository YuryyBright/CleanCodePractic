### using: mypy, pylint

# CODE FORMATING https://github.com/psf/black/tree/main

### the function without documentation
def data_from_response(response: dict) -> dict:
    if response["status"] != 200:
        raise ValueError
    return {"data": response["payload"]}


### the function with documentation
def data_from_response_v2(response: dict) -> dict:
    """If the response is OK, return its payload.
    - response: A dict like::
    {
    "status": 200, # <int>
    "timestamp": "....", # ISO format string of the current
    date time
    "payload": { ... } # dict with the returned data
    }
    - Returns a dictionary like::
    {"data": { .. } }
    - Raises:
    - ValueError if the HTTP status is != 200
    """
    if response["status"] != 200:
        raise ValueError
    return {"data": response["payload"]}



