import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import asyncio
from websockets import connect

# Load environment variables from the .env file
load_dotenv()

# Access the Alpaca keys
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_API_SECRET = os.getenv("ALPACA_API_SECRET")


# Set up Alpaca API
api = tradeapi.REST(ALPACA_API_KEY, ALPACA_API_SECRET, base_url="https://paper-api.alpaca.markets")

"""
# WebSocket feed for real-time market data
def on_message(ws, message):
    print(f"Received Message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Connection closed")

def on_open(ws):
    # Subscribe to ETF tickers (e.g., SPY for S&P 500 ETF)
    ws.send('{"type": "subscribe", "symbols": ["SPY"]}')

if __name__ == "__main__":
    # WebSocket URL for Alpaca real-time data
    ws_url = "wss://stream.data.alpaca.markets/v2/sip"

    # Run WebSocket
    import websocket
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(ws_url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.run_forever()

"""
try:
    account = api.get_account()
    print("Connection successful!")
    print("Account status:", account.status)
    print("Cash balance:", account.cash)
except Exception as e:
    print(f"Error: {e}")
