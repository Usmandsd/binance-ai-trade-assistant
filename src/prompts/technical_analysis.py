"""
Technical analysis engine.
Calculates basic indicators from candle data.
"""

def calculate_sma(prices: list, period: int = 14) -> float:
    """Calculate Simple Moving Average."""
    if len(prices) < period:
        return sum(prices) / len(prices)

    return sum(prices[-period:]) / period


def calculate_momentum(prices: list) -> str:
    """Determine basic price momentum."""

    if len(prices) < 2:
        return "Neutral"

    if prices[-1] > prices[-2]:
        return "Bullish"

    if prices[-1] < prices[-2]:
        return "Bearish"

    return "Neutral"


def analyze_candles(candles: list) -> dict:
    """Analyze candle closing prices."""

    if not candles:
        return {
            "trend": "Unknown",
            "momentum": "Unknown",
            "sma": 0,
        }

    closes = [float(candle[4]) for candle in candles]

    sma = calculate_sma(closes)
    current_price = closes[-1]

    if current_price > sma:
        trend = "Bullish"
    elif current_price < sma:
        trend = "Bearish"
    else:
        trend = "Neutral"

    momentum = calculate_momentum(closes)

    return {
        "trend": trend,
        "momentum": momentum,
        "sma": sma,
    }
