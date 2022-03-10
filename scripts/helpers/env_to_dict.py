import os
from shared.utils.constants import ROOT
from shared.utils.array import Array

env_path = os.path.join(ROOT, '.env')

class Env:

    _secret_key: str
    _debug: str

    def __init__(self) -> None:
        pass
    
    @property
    def secret_key(self) -> str:
        return self._secret_key

    @property
    def debug(self) -> bool:
        return self._debug == 'True'

def use_env() -> Env:
    with open(env_path, 'r') as f:
        env_raw = f.read()
    env = Env()
    Array(env_raw.split('\n')).filter(lambda x: len(x) > 0).map(lambda x: x.split('=')).forEach(lambda x: setattr(env, '_%s' % x[0].lower(), x[1]))
    return env
