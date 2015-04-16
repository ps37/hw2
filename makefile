cmd:
	python packet_analysis.py ws_wireless.xml > ws_wireless_op.txt
	python packet_analysis.py tcpdump_wireless.xml > tcpdump_wireless_op.txt
	python packet_analysis.py dumpcap_wireless.xml > dumpcap_wireless_op.txt
	python packet_analysis.py ws_wired.xml > ws_wired_op.txt
	python packet_analysis.py tcpdump_wired.xml > tcpdump_wired_op.txt
	python packet_analysis.py dumpcap_wired.xml > dumpcap_wired_op.txt
	
clear:
	rm -rf *~ ws_wireless_op.txt tcpdump_wireless_op.txt dumpcap_wireless_op.txt
	rm -rf *~ ws_wired_op.txt tcpdump_wired_op.txt dumpcap_wired_op.txt