rm /etc/resolv.conf
echo nameserver 10.10.10.78 > /etc/resolv.conf
ifconfig eth0 down
ifconfig eth0 up
ifconfig eth0 10.10.77.116 netmask 255.255.0.0
route add -net 192.168.1.0/24 gw 10.10.10.69
ping -v files.sec660.org
