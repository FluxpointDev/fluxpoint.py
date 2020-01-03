# fluxpoint.py
> :loop: **| Simple Python library for [fluxpoint.dev](https://fluxpoint.dev)**

## Installation
```sh
$ pip install fluxpoint
```

## Example
```py
from fluxpoint import FluxpointClient

flux = FluxpointClient(user_agent='MemeBot/0.0.0/Test', tokens={
    # Fluxpoint Gallery Token
    "gallery": "",

    # Normal token
    "normal": ""
})

flux.gallery.get_album(id='7')
```