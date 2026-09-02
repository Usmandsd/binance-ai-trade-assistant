"""
Technical analysis tools for Binance AI Trade Assistant.
"""

import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator


def analyze_market(candles: list) -> dict:
    """
    Analyze historical candle data.

    Each candle should contain:
    timestamp, open, high, low, close, volume
    """

    if len(candles) < 20:
        return {
            "error": "At least 20 candles are required for analysis."
        }

    df = pd.DataFrame(
        candles,
        columns=[
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume",
        ],
    )

    for column in ["open", "high", "low", "close", "volume"]:
        df[column] = pd.to_numeric(df[column])

    # Moving averages
    df["sma_10"] = SMAIndicator(
        close=df["close"],
        window=10,
    ).sma_indicator()

    df["sma_20"] = SMAIndicator(
        close=df["close"],
        window=20,
    ).sma_indicator()

    # RSI
    df["rsi"] = RSIIndicator(
        close=df["close"],
        window=14,
    ).rsi()

    latest = df.iloc[-1]

    # Determine trend
    if latest["sma_10"] > latest["sma_20"]:
        trend = "Bullish"
    elif latest["sma_10"] < latest["sma_20"]:
        trend = "Bearish"
    else:
        trend = "Neutral"

    # Determine momentum
    if latest["rsi"] >= 60:
        momentum = "Strong"
    elif latest["rsi"] <= 40:
        momentum = "Weak"
    else:
        momentum = "Moderate"

    return {
        "trend": trend,
        "momentum": momentum,
        "rsi": round(float(latest["rsi"]), 2),
        "sma_10": round(float(latest["sma_10"]), 2),
        "sma_20": round(float(latest["sma_20"]), 2),
        "price": round(float(latest["close"]), 2),
  }
