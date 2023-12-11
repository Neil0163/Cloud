Traceroute allows you to see the route that a specific ping takes from one client to another 

traceroute google.com < this for example will trace the route from the client terminal to google server>

you can then use taceroute mapper that will display the specific route the oing has taken. 

traceroute -p 2 google.com
traceroute to google.com (172.217.16.238), 64 hops max, 52 byte packets
 1  192.168.5.1 (192.168.5.1)  9.271 ms  12.457 ms  4.348 ms
 2  192.168.1.254 (192.168.1.254)  11.351 ms  5.164 ms  4.804 ms

 here in the above the -q followed by a number speeds up traceroute process by reducing the number of probes.

 traceroute -r reverses the route from which the trace is conducted.

 ************HOW DOES IT ACUTALLY WORK*************

 Traceroute works by sending out a series of interent control message protocol ICMP echo request packets with varying time to live (TTL) values

***************TTL******************

 TTL stands for time to live and is a value in the IP header of a packet. It represents the maximum number of hops (routers) that a packet
 can pass through before being discarded. 

 *************TIME EXCEEDED REPLY*************

 A time exceeded reply is a ICMP message sent by a router when the TTL of a packet expires, it is used by traceroute to determine the route 
 takewn by packets.