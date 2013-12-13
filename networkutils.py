import struct
class NetworkManager(object):
  def __init__(self, s, delimiter="\n"): # the constructor takes in a socket object
    self.s = s
    self.delimiter = delimiter

  def recv_line(self): # reads exactly one line from the socket. line delimiter can be \n or \r\n. Wait till delimiter if its not available immediately
    message_line = ''
    while True:
        c = self.s.recv(1)
        message_line = message_line + c
        if c == self.delimiter :
            break
    return message_line

  def recv_strict(self,length):# takes in an argument as an integer "length" and reads exactly "length" bytes from the socket and returns it. If "length" bytes are not available, wait till they arrive.
    message_strict = ''
    while True:
        c = self.s.recv(1)
        message_strict = message_strict + c
        if len(message_strict) == length:
            break
    return message_strict
 
  def send_integer(self,integer): # send a 4 byte integer out through the socket
    integer = struct.pack("<I",integer)
    self.s.send(integer)

  def recv_integer(self): # receive a 4 byte integer from the socket
    received_message = self.recv_strict(4)
    received = struct.unpack("<I",received_message)[0]
    return received
