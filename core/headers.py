import random
from fake_useragent import UserAgent

ua = UserAgent()

def headers(token=None):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": ua.random,
        "Origin": "https://game.genkiminer.fun",
        "Referer": "https://game.genkiminer.fun/"
    }
    if token:
        headers.update({"Authorization": token})

    return headers
