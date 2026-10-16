import wsbypass

url = "wss://echo.websocket.org"

print("connecting to websocket...")
ws = wsbypass.connect(url)

print("sending test frame...")
ws.send("hello from wsbypass", 1)

data, _ = ws.recv()
print("received:", data.decode("utf-8", "ignore"))

ws.close()
