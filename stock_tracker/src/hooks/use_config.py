import os
import json
import string
from typing import List, Optional, TypedDict
from stock_tracker.src.utils.constants import STATIC

config_path = os.path.join(STATIC, 'config.json')

class Target(TypedDict):

    market: string
    """주식이 속한 시작 (KOSPI, KOSDAQ, ...)"""
    code: string
    """주식 코드"""
    name: string
    """주식 이름"""
    goal: List[int]
    """목표 주가 (여러개 가능)"""
    bep: int
    """손익분기점"""

class Credentials(TypedDict):

    kakaoAuthorization: str
    """카카오 API 토큰 + 인증 정보 ("Bearer {Access Token}")"""

class Env(TypedDict):

    debug: bool
    secretKey: str

class Config(TypedDict):
    target: List[Target]
    credentials: Credentials
    env: Env

def use_config() -> Optional[Config]:
    try:
        with open(config_path, 'r') as f:
            config = json.loads(f.read())
        return config
    except:
        return None
