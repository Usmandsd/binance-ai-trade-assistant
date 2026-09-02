def calculate_risk(analysis: dict) -> dict:
    """Calculate a simple risk score from market analysis."""

    score = 50
    reasons = []

    trend = str(analysis.get("trend", "")).lower()
    momentum = str(analysis.get("momentum", "")).lower()
    rsi = analysis.get("rsi", 50)

    if "bullish" in trend:
        score -= 10
        reasons.append("Bullish trend")
    elif "bearish" in trend:
        score += 15
        reasons.append("Bearish trend")

    if "bullish" in momentum:
        score -= 10
        reasons.append("Bullish momentum")
    elif "bearish" in momentum:
        score += 15
        reasons.append("Bearish momentum")

    if rsi >= 70:
        score += 15
        reasons.append("RSI indicates overbought conditions")
    elif rsi <= 30:
        score += 10
        reasons.append("RSI indicates oversold conditions")

    score = max(0, min(100, score))

    if score <= 30:
        risk_level = "Low"
    elif score <= 60:
        risk_level = "Moderate"
    else:
        risk_level = "High"

    if not reasons:
        reasons.append("Limited market signals available")

    return {
        "risk_level": risk_level,
        "risk_score": score,
        "reasons": reasons,
  }
