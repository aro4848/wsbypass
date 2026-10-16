# wsbypass

python websocket wrapper around curl_cffi. 

normal websocket libraries fail against cloudflare with 403 errors during the upgrade request. this handles the tls handshake with a chrome ja3 fingerprint so the connection goes straight through.

install:
pip install wsbypass

usage:
from wsbypass import connect

ws = connect("wss://target.com/ws", origin="https://target.com")
ws.send("40", 1)
data, _ = ws.recv()
print(data)
ws.close()
