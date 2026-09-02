"""
Binance AI Trade Assistant
Built for the Binance Agent OS Mini Hackathon.

This MVP provides a simple AI-agent structure for crypto
market analysis. Binance Agent OS / MCP integration can
be connected through the tools layer.
"""

import os
from dotenv import load_dotenv


load_dotenv()


class BinanceTradeAssistant:
    """AI assistant for crypto market analysis."""

    def __init__(self):
        self.name = "Binance AI Trade Assistant"

    def analyze(self, symbol: str) -> str:
        """
        Analyze a trading pair.

        Args:
            symbol: Trading pair such as BTC/USDT.

        Returns:
            A formatted market-analysis request.
        """
        symbol = symbol.upper().strip()

        if not symbol:
            return "Please enter a valid trading pair."

        return f"""
🤖 Binance AI Trade Assistant
━━━━━━━━━━━━━━━━━━━━━━━━━━

Trading Pair: {symbol}

📊 Market Analysis
• Trend: Pending
• Momentum: Pending
• Volume: Pending
• Support: Pending
• Resistance: Pending
• Risk Level: Pending

🔎 Status:
Market data connection is ready to be connected
through the Binance Agent OS / MCP tools.

⚠️ This tool provides market analysis for educational
purposes only and is not financial advice.
"""


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

        print(assistant.analyze(symbol))


if __name__ == "__main__":
    main()
