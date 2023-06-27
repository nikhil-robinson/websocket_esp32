from websocket_server import WebsocketServer
import socket

# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
    if len(message) > 200:
        message = message[:200]+'..'
        print("Client(%d) said: %s" % (client['id'], message))
        


def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

PORT=4455
IP = get_my_ip()
try:
    server = WebsocketServer(host= IP,port = PORT)
    if server:
        print(f"Server started on ws://{IP}:{PORT}")
        server.set_fn_new_client(new_client)
        server.set_fn_client_left(client_left)
        server.set_fn_message_received(message_received)
        server.run_forever()
except Exception as e:
      print("Failed {e}")

while True:
     server.send_message_to_all("hello esp32")
