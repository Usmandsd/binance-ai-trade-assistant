"""
Binance market data tools.
"""

import requests


BINANCE_API_URL = "https://api.binance.com/api/v3"


def get_ticker(symbol: str) -> dict:
    """Get current 24-hour market statistics."""

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


def get_klines(
    symbol: str,
    interval: str = "1h",
    limit: int = 100,
) -> list:
    """
    Get historical candlestick data from Binance.

    Args:
        symbol: Trading pair, e.g. BTC/USDT.
        interval: Candle interval, e.g. 1h.
        limit: Number of candles to retrieve.
    """

    symbol = symbol.upper().replace("/", "")

    response = requests.get(
        f"{BINANCE_API_URL}/klines",
        params={
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        },
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    candles = []

    for candle in data:
        candles.append([
            candle[0],  # timestamp
            candle[1],  # open
            candle[2],  # high
            candle[3],  # low
            candle[4],  # close
            candle[5],  # volume
        ])

    return candles
