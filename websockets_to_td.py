import asyncio
import websockets
import socket

TD_HOST = 'localhost'
TD_PORT = 9010

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((TD_HOST, TD_PORT))

async def handler(websocket, path):
    print(f"WebSocket client connected: {path}")
    try:
        async for message in websocket:
            print(f"Received: {message}")
            tcp_socket.sendall((message + '\n').encode('utf-8'))
    except websockets.ConnectionClosed:
        print("WebSocket connection closed.")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 1234):
        print("WebSocket server running on ws://0.0.0.0:1234")
        await asyncio.Future()  # run forever

asyncio.run(main())
