#!/bin/env python
import sys, signal
import http.server
import socketserver

# Reading portnumber from command line
if sys.argv[1:]:
  port = int(sys.argv[1])
else:
  port = 8080

# Note ForkingTCPServer does not work on Windows as the os.fork() 
# function is not available on that OS. Instead we must use the 
# subprocess server to handle multiple requests
server = socketserver.ThreadingTCPServer(('',port), http.server.SimpleHTTPRequestHandler )

#Ensures that Ctrl-C cleanly kills all spawned threads
server.daemon_threads = True  
#Quicker rebinding
server.allow_reuse_address = True  

# A custom signal handle to allow us to Ctrl-C out of the process
def signal_handler(signal, frame):
    print( 'Exiting http server (Ctrl+C pressed)')
    try:
      if( server ):
        server.server_close()
    finally:
      sys.exit(0)

# Install the keyboard interrupt handler
signal.signal(signal.SIGINT, signal_handler)

# Now loop forever
try:
  while True:
    print('loop')
    sys.stdout.flush()
    server.serve_forever()

    print('loop2')
except KeyboardInterrupt:
  pass

server.server_close()