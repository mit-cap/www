import getopt
import socket
import sys

def main(argv):
  sendstr = "hello from the thing"
  try:
    opts, args = getopt.getopt(argv, "s:", ["sendstr="])
    for opt, arg in opts:
      if opt in ("-s", "--sendstr"):
        sendstr = arg
  except getopt.GetoptError:
    pass  #noop

  #create an INET, STREAMing socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #now connect to the web server on port 80
  s.connect(('128.30.87.46', 1029))
  s.send(sendstr)
  #while 1:
  data = s.recv(1024)
  print data
  '''
    if not data:
      print "no data"
      break
  '''
  s.close

if __name__ == "__main__":
  main(sys.argv[1:])
