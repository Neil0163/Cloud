*******FInding an ip adress to an domian**********

; nslookup example.org
# This is the address of our resolver, not of example.org
Server:    192.168.6.1
Address:   192.168.6.1#53 # Port 53 is the port for DNS

# Below is the address of example.org
Non-authoritative answer:
Name:	example.org
Address: 93.184.216.34


************Using dig to find out more***********

That's good. But what if we wanted to take a closer look at the DNS records associated with example.org, say for example if we needed to debug a problem. For this we can use dig.

dig allows us to query the DNS records associated with a particular domain. There are a number of possible record types. One important one is an A record, which dictates one or more IP addresses for the domain.

# Get 'A' records for 'example.org'
; dig example.org A

; <<>> DiG 9.10.6 <<>> example.org A
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 48269
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;example.org.	              IN    A

;; ANSWER SECTION:
example.org.        28521   IN    A    93.184.216.34

;; Query time: 78 msec
;; SERVER: 192.168.8.1#53(192.168.8.1)
;; WHEN: Sat Dec 03 13:12:19 GMT 2022
;; MSG SIZE  rcvd: 45
You can see the IP address against the single A record in the ANSWER SECTION.

You'll notice in the nslookup output there was a line saying 'Non-authoritative answer'. This means that our DNS server (in this case, my local router) isn't the authoritative source for information about example.org. It's just repeating what it has heard from another source, assuming that it is correct.

However, what if it recently changed? We might want to go straight to the authoritative nameserver for that domain. For that, we need to know what it is, and for this, we can look at the NS record.

; dig example.org NS
; <<>> DiG 9.10.6 <<>> example.org NS
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 4583
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 5

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;example.org.	                 IN    NS

;; ANSWER SECTION:
example.org.           3052    IN    NS      a.iana-servers.net.
example.org.           3052    IN    NS      b.iana-servers.net.

;; ADDITIONAL SECTION:
a.iana-servers.net.    1626    IN    A       199.43.135.53
b.iana-servers.net.    139275  IN    A       199.43.133.53
a.iana-servers.net.    1626    IN    AAAA    2001:500:8f::53
b.iana-servers.net.    139275  IN    AAAA    2001:500:8d::53

;; Query time: 94 msec
;; SERVER: 192.168.8.1#53(192.168.8.1)
;; WHEN: Sat Dec 03 13:16:38 GMT 2022
;; MSG SIZE  rcvd: 176
Here, dig has told us that the nameservers for example.org are a.iana-servers.net and b.iana-servers.net (there are two for redundancy). It has also helpfully provided their IP addresses in an ADDITIONAL SECTION beneath.

Let's use nslookup to look up example.org directly from a.iana-servers.net.

# To specify a DNS server to use, we pass it as the second argument
; nslookup example.org a.iana-servers.net
Server:   a.iana-servers.net
Address:  199.43.135.53#53

Name:    example.org
Address: 93.184.216.34
Note that we now don't have that 'Non-authoritative answer' line, because we're now asking the main authority for that domain name.

