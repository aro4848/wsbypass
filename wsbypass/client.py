from curl_cffi.requests import Session
from curl_cffi import CurlWsFlag

def connect(url, origin=None, headers=None, impersonate="chrome120"):
    h = dict(headers or {})
    if origin:
        h["Origin"] = origin
    sess = Session()
    sock = sess.ws_connect(url, headers=h, impersonate=impersonate)

    class Handle:
        pass

    h_obj = Handle()
    h_obj._s = sess
    h_obj._sock = sock
    h_obj.send = sock.send
    h_obj.recv = sock.recv
    h_obj.close = sock.close
    return h_obj
