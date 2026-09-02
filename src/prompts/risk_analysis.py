"""
Risk analysis engine.
Calculates basic trading risk, position size, stop loss,
take profit, and risk/reward ratio.
"""


def calculate_position_size(
    account_balance: float,
    risk_percent: float,
    entry_price: float,
    stop_loss: float,
) -> float:
    """Calculate position size based on account risk."""

    if account_balance <= 0:
        return 0.0

    if risk_percent <= 0:
        return 0.0

    if entry_price <= 0 or stop_loss <= 0:
        return 0.0

    risk_amount = account_balance * (risk_percent / 100)
    price_risk = abs(entry_price - stop_loss)

    if price_risk == 0:
        return 0.0

    return risk_amount / price_risk


def calculate_risk_reward(
    entry_price: float,
    stop_loss: float,
    take_profit: float,
) -> float:
    """Calculate the risk/reward ratio."""

    if entry_price <= 0 or stop_loss <= 0 or take_profit <= 0:
        return 0.0

    risk = abs(entry_price - stop_loss)
    reward = abs(take_profit - entry_price)

    if risk == 0:
        return 0.0

    return reward / risk


def analyze_risk(
    account_balance: float,
    risk_percent: float,
    entry_price: float,
    stop_loss: float,
    take_profit: float,
) -> dict:
    """Analyze basic trading risk."""

    position_size = calculate_position_size(
        account_balance,
        risk_percent,
        entry_price,
        stop_loss,
    )

    risk_reward = calculate_risk_reward(
        entry_price,
        stop_loss,
        take_profit,
    )

    risk_amount = account_balance * (risk_percent / 100)

    if risk_reward >= 2:
        risk_level = "Good"
    elif risk_reward >= 1:
        risk_level = "Moderate"
    else:
        risk_level = "High"

    return {
        "risk_amount": risk_amount,
        "position_size": position_size,
        "risk_reward": risk_reward,
        "risk_level": risk_level,
        "entry_price": entry_price,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
    }
