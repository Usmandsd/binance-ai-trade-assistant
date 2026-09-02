"""
Risk analysis tools for Binance AI Trade Assistant.
"""


def calculate_risk(analysis: dict) -> dict:
    """
    Calculate a simple risk level from technical indicators.

    This is an educational scoring model, not financial advice.
    """

    if "error" in analysis:
        return {
            "risk_level": "Unknown",
            "risk_score": None,
            "reasons": [analysis["error"]],
        }

    score = 0
    reasons = []

    rsi = analysis.get("rsi", 50)
    trend = analysis.get("trend", "Neutral")

    # RSI risk
    if rsi >= 70:
        score += 30
        reasons.append("RSI indicates potentially overbought conditions.")
    elif rsi <= 30:
        score += 30
        reasons.append("RSI indicates potentially oversold conditions.")
    else:
        score += 10

    # Trend risk
    if trend == "Bullish":
        score += 10
    elif trend == "Bearish":
        score += 20
        reasons.append("Bearish trend increases downside risk.")
    else:
        score += 15
        reasons.append("Neutral trend indicates uncertainty.")

    # Risk classification
    if score >= 40:
        risk_level = "High"
    elif score >= 25:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    if not reasons:
        reasons.append("No major technical risk signal detected.")

    return {
        "risk_level": risk_level,
        "risk_score": min(score, 100),
        "reasons": reasons,
    }
