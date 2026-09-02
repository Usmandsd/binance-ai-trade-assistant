"""
Market data tools for Binance AI Trade Assistant.
"""

import requests


BINANCE_API_URL = "https://api.binance.com/api/v3"


def get_ticker(symbol: str) -> dict:
    """
    Get the current price and 24-hour statistics
    for a Binance trading pair.
    """

    symbol = symbol.upper().replace("/", "")

    response = requests.get(
        f"{BINANCE_API_URL}/ticker/24hr",
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


if __name__ == "__main__":
    print(get_ticker("BTCUSDT"))
