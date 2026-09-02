"""
Binance market data tool.
Fetches real-time market data from Binance public API.
"""

import requests


BINANCE_API = "https://api.binance.com/api/v3/ticker/24hr"


def get_ticker(symbol: str) -> dict:
    """Get 24-hour market statistics for a trading pair."""

    symbol = symbol.upper().strip().replace("/", "")

    response = requests.get(
        BINANCE_API,
        params={"symbol": symbol},
        timeout=10,
    )

    response.raise_for_status()
    data = response.json()

    return {
        "symbol": data["symbol"],
        "price": float(data["lastPrice"]),
        "change_24h": float(data["priceChangePercent"]),
        "volume_24h": float(data["volume"]),
        "high_24h": float(data["highPrice"]),
        "low_24h": float(data["lowPrice"]),
    }
