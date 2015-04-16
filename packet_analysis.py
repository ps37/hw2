import xml.etree.ElementTree as ET
import sys

infile = sys.argv[1]
tree = ET.parse(infile)
root = tree.getroot()

#each child = each packet
"""child[0] = packet number
child[1] = time
child[2] = source
child[3] = destination
child[4] = protocol
child[5] = length
child[6] = info"""

wifi_packets = 0
DNS_packets = 0 
HTTP_packets = 0 
TCP_packets = 0
UDP_packets = 0
QUIC_packets = 0
total_bytes = 0
retransmitted_packets = 0
my_traffic = 0 

for child in root:
    if child.tag == 'structure':
        i = 1
    else:
        total_bytes = total_bytes + int(child[5].text)
        if child[4].text == "802.11":
            wifi_packets += 1
        elif child[4].text == "DNS":
            DNS_packets += 1
        elif child[4].text == "TCP" or child[4].text == "TLSv1" or child[4].text == "TLSv1.2":
            TCP_packets += 1
        elif child[4].text == "QUIC":
            QUIC_packets += 1
        elif child[2].text == "172.25.34.58" or child[3].text == "172.25.34.58":
            my_traffic += 1 
        elif child[4].text == "HTTP" or child[4].text == "HTTPS":
            HTTP_packets += 1
        # check for retransmitted packets
        info = child[6].text
        if type(info) ==  str:
            parsed_info = info.split(" ")
            for element in parsed_info:
                if element == 'Retransmission]':
                    retransmitted_packets += 1
                    break

bytes_per_sec = float(total_bytes) / float(child[1].text)
avg_mbits_per_sec = float(bytes_per_sec * 8) / 1000000

print "total packets are: " + child[0].text
print "wifi packets are: " + str(wifi_packets)
print "DNS packets are: " + str(DNS_packets)
print "TCP packets are: " + str(TCP_packets)
print "HTTP packets are: " + str(HTTP_packets)
print "UDP packets are: " + str(DNS_packets + QUIC_packets)
print "total bytes are: " + str(total_bytes)
print "Retransmitted packets are: " + str(retransmitted_packets)
print "total real time of capture: " + child[1].text
print
print "the % of HTTP traffic is: " +  str((float(HTTP_packets) / float(child[0].text)) * 100 )
print "the % of TCP traffic is: " +  str((float(TCP_packets) / float(child[0].text)) * 100 )
print "the % of WIFI traffic is: " +  str((float(wifi_packets) / float(child[0].text)) * 100 )
print "the % of DNS traffic is: " +  str((float(DNS_packets) / float(child[0].text)) * 100 )
print "the % of UDP traffic is: " +  str((float(DNS_packets + QUIC_packets) / float(child[0].text)) * 100 )
#print "the % of traffic to my machine is: " + str((float(my_traffic) / float(child[0].text)) * 100 )
print "the % of retransmitted packets is: " + str((float(retransmitted_packets) / float(child[0].text)) * 100 )
print "the avg mega bits per second are: " + str(avg_mbits_per_sec)
