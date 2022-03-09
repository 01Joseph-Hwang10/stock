from typing import Optional
from requests.models import Response

def use_safe_request(response: Optional[Response]) -> Optional[dict]:
    if response == None:
        return None
    return response.json()