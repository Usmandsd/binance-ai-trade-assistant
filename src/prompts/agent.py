"""
Binance AI Trade Assistant
Main agent controller.
"""

from tools.market_data import get_ticker, get_klines
from tools.technical_analysis import analyze_market
from tools.risk_analysis import calculate_risk


class BinanceTradeAssistant:
    """AI assistant for crypto market analysis."""

    def __init__(self):
        self.name = "Binance AI Trade Assistant"

    def analyze(self, symbol: str) -> dict:
        """Run the complete market-analysis workflow."""

        symbol = symbol.upper().strip()

        if not symbol:
            return {"error": "Please enter a valid trading pair."}

        try:
            # Get current market data
            market = get_ticker(symbol)

            # Get historical candles
            candles = get_klines(
                symbol,
                interval="1h",
                limit=100,
            )

            # Run technical analysis
            technical = analyze_market(candles)

            # Calculate risk
            risk = calculate_risk(technical)

            return {
                "symbol": market["symbol"],
                "price": market["price"],
                "change_24h": market["change_24h"],
                "volume_24h": market["volume_24h"],
                "high_24h": market["high_24h"],
                "low_24h": market["low_24h"],
                "trend": technical["trend"],
                "momentum": technical["momentum"],
                "rsi": technical["rsi"],
                "sma_10": technical["sma_10"],
                "sma_20": technical["sma_20"],
                "risk_level": risk["risk_level"],
                "risk_score": risk["risk_score"],
                "risk_factors": risk["reasons"],
            }

        except Exception as error:
            return {
                "error": f"Unable to analyze {symbol}: {error}"
            }


def main():
    """Run the assistant from the command line."""

    assistant = BinanceTradeAssistant()

    print("\n🤖 Binance AI Trade Assistant")
    print("Type 'exit' to quit.\n")

    while True:
        symbol = input("Enter trading pair: ")

        if symbol.lower() == "exit":
            print("\nGoodbye! 👋")
            break

        result = assistant.analyze(symbol)

        print("\n📊 MARKET ANALYSIS")
        print("━━━━━━━━━━━━━━━━━━━━")

        if "error" in result:
            print(f"❌ {result['error']}")
            continue

        print(f"Trading Pair: {result['symbol']}")
        print(f"Price: ${result['price']:,.2f}")
        print(f"24h Change: {result['change_24h']:.2f}%")
        print(f"24h Volume: {result['volume_24h']:,.2f}")
        print(f"24h High: ${result['high_24h']:,.2f}")
        print(f"24h Low: ${result['low_24h']:,.2f}")

        print("\n📈 TECHNICAL ANALYSIS")
        print(f"Trend: {result['trend']}")
        print(f"Momentum: {result['momentum']}")
        print(f"RSI: {result['rsi']}")
        print(f"SMA 10: {result['sma_10']}")
        print(f"SMA 20: {result['sma_20']}")

        print("\n🛡️ RISK ASSESSMENT")
        print(f"Risk Level: {result['risk_level']}")
        print(f"Risk Score: {result['risk_score']}/100")

        print("\nRisk Factors:")
        for reason in result["risk_factors"]:
            print(f"- {reason}")

        print(
            "\n⚠️ Educational analysis only — "
            "not financial advice."
        )


if __name__ == "__main__":
    main()
