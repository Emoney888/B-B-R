import requests

def fetch_brett_data():
    data = {
        "price_usd": 0.055,
        "market_cap": 550000000,
        "volume_24h": 25000000,
        "brett_dominance": 1.7,
        "btc_dominance": 52.4,
        "fear_greed_index": 86,
        "altseason_index": 82
    }
    return data

def get_indicator_status():
    return {
        "price": True,
        "volume": True,
        "dominance": True,
        "btc_dominance": False,
        "market_cap": True,
        "fear_greed": True,
        "altseason": True,
        "mvrv_z": False,
        "nup": False
    }

def get_current_alignment(status):
    return sum(status.values()) / len(status)
