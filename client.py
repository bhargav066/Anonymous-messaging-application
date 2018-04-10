import torify
import socket
import urllib.request
import os
if os.name=="nt":
    port=9150
else:
    port=9050
torify.set_tor_proxy("127.0.0.1", port)
torify.disable_tor_check()
torify.use_tor_proxy()
def torr(address):
    try:
        a=[]
        req = urllib.request.Request("http://"+address)
        res = urllib.request.urlopen(req, timeout=socket._GLOBAL_DEFAULT_TIMEOUT)
        received_msg = res.read().decode("utf-8")
        a.append(received_msg)
        a.append(0)
        return a
    except Exception as e:
        print("\ruser is offline",end="")
        return ["null",0]
    except KeyboardInterrupt:
        return [0,1]
        
