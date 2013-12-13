from networkutils import NetworkManager
from socket import create_connection
 
# First create a socket to connect to the server
def get_socket(HOST, PORT):
  return create_connection((HOST, PORT))
 
def main():
# Create a socket
  s = get_socket("10.30.56.113", 1234)
# Create an object of NetworkManager class, pass in the socket object
  nm = NetworkManager(s)
# We can then receive a line from the network as :-
#  data = nm.recv_line()
#  print data
#  data = nm.recv_integer()
#  print data
  
  
main()
