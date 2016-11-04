#CLVS logs Integration to Zeus

We were provided with 5 files with different log formats. Following are the file name and regular expression used to describe their pattern

1. boot_log
   >Regular Expression : 

>1. *Sep 27 07:29:57.517: %SPANTREE-5-EXTENDED_SYSID: Extended SysId enabled for type vlanCannot Get the number of ports in MAC notification

>2. GigabitEthernet0/1/4 is down, line protocol is down \n
  Hardware is A900-IMA8T1Z, address is c8f9.f98d.1f0d (bia c8f9.f98d.1f0d)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full Duplex, 1000Mbps, link type is auto, media type is RJ45
  output flow-control is unsupported, input flow-control is on
  Carrier delay is 5 sec
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
     
3. .Sep 27 09:32:30.514: MST[0]:-TX> Gi0/1/2  BPDU Prot:0 Vers:3 Type:2

4. interface GigabitEthernet0/1/2
   no ip address
   negotiation auto
   service instance 10 ethernet
   encapsulation dot1q 100
   rewrite ingress tag pop 1 symmetric
   bridge-domain 10
   
5. PID Runtime(ms)     Invoked      uSecs   5Sec   1Min   5Min TTY Process 
   1           4          12        333  0.00%  0.00%  0.00%   0 Chunk Manager    
   2          56        1522         36  0.00%  0.00%  0.00%   0 Load Meter
   
   
