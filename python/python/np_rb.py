###############################################################
#
#   Synaccess Networks, Inc.  (www.synaccess-net.com)
#   Jan. 6th, 2013
#   Python Script Example 1  
#   for NP series. 
#   
################################################################

import socket 
import time 									
import sys 

def connect(ip_value, port_value):

	HOST = str(ip_value)			 			# The remote host IP address
	PORT = int(port_value)       				# The server port number
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, PORT))
	
	time.sleep(0.1) 							#use time.sleep to give delay and netBooter time to process
	
	sock.send('\r')								#send \r to start at beginning of line
	time.sleep(0.5)
	sock.send('help\r')							#help command for list of available control/status options
	time.sleep(0.5)								#delay between commands to allow NP unit to process
	
	sock.send('logout\r')						#send logout command to unit to gracefully close socket connection
	
	recv = sock.recv(2048)						#receive data from session
	print(recv)									#print data received
	
	time.sleep(0.1)
	
	sock.close()
	
	
  
def main():
	if len(sys.argv) !=5:
		print('\r\n')
		print('Example:> np_term.py -i 192.168.1.100 -p 23\r\n')
		print('          np_term.py -i Unit_IP_Addr  -p Telnet_port# \r\n')
		sys.exit(1)
	
	ip = sys.argv[1]							#For -i option in command line
	ip_value = sys.argv[2]						#IP address value entered
	port = sys.argv[3]							#For -p option in command line
	port_value = sys.argv[4]					#Port number entered
	if ip == '-i' and port == '-p':				#Check that the command line uses both -i and -p for valid connection
		connect(ip_value,port_value)			
	
		
if __name__ == '__main__':
	main()

	
