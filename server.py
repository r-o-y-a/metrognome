from pythonosc import dispatcher, osc_server
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
import json
import websockets
import asyncio
from queue import Queue

network_ip = '172.20.10.2'

data_queue = Queue()

def osc_handler(address, *args):
    if address == "/data":
        data_queue.put(args)

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/data", osc_handler)

async def serve_osc_server(loop):
    osc_server_instance = osc_server.AsyncIOOSCUDPServer(("127.0.0.1", 57121), dispatcher, loop)
    transport, protocol = await osc_server_instance.create_serve_endpoint()
    return transport, protocol

def serve_webpage():
    class MyHandler(SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            super().end_headers()

    httpd = HTTPServer(('0.0.0.0', 8080), MyHandler)
    print("Web server serving at port 8080...")
    httpd.serve_forever()

async def send_osc_data(websocket, path):
    while True:
        if not data_queue.empty():
            # Fetch data from queue without overwriting
            args = data_queue.get()
            json_data = json.dumps({"data": args})
            await websocket.send(json_data)
        await asyncio.sleep(0.01)

async def main():
    loop = asyncio.get_running_loop()
    await serve_osc_server(loop)
    start_server = websockets.serve(send_osc_data, network_ip, 8081)
    await start_server
    await asyncio.sleep(float("inf"))

# Start the web server in a separate thread
web_thread = threading.Thread(target=serve_webpage)
web_thread.start()

asyncio.run(main())
