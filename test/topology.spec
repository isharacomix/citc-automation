

vm oob-mgmt-server netq-1.4.0 2 10 40
vm leaf01 cumulus-vx-3.7.2 1 2 2
vm leaf02 cumulus-vx-3.7.2 1 2 2
vm leaf03 cumulus-vx-3.7.2 1 2 2
vm leaf04 cumulus-vx-3.7.2 1 2 2
vm spine01 cumulus-vx-3.7.2 1 2 2
vm spine02 cumulus-vx-3.7.2 1 2 2
vm exit01 cumulus-vx-3.7.2 1 2 2
vm server01 ubuntu-16.04 2 4 4
vm server02 ubuntu-16.04 2 4 4
vm server03 ubuntu-16.04 2 4 4
vm server04 ubuntu-16.04 2 4 4
vm internet cumulus-vx-3.7.2 1 2 2
vm edge01 ubuntu-16.04 2 4 4

network oob-mgmt-server eth0 10.255.0.1 255.255.0.0 public
service oob-mgmt-server ssh eth0 22 TCP public
service oob-mgmt-server http eth0 80 TCP public
service oob-mgmt-server https eth0 443 TCP public
service oob-mgmt-server http2 eth0 1337 TCP public
service oob-mgmt-server grafana eth0 3000 TCP public
service oob-mgmt-server netqgui eth0 5000 TCP public
service oob-mgmt-server novnc eth0 6080 TCP public
service oob-mgmt-server netq eth0 9000 TCP public
service oob-mgmt-server mesos eth0 5050 TCP public
service oob-mgmt-server marathon eth0 8080 TCP public
service oob-mgmt-server mesosapp eth0 8088 TCP public

network oob-mgmt-server eth1 192.168.0.254 255.255.0.0
network leaf01 eth0 192.168.0.11 255.255.0.0
network leaf02 eth0 192.168.0.12 255.255.0.0
network leaf03 eth0 192.168.0.13 255.255.0.0
network leaf04 eth0 192.168.0.14 255.255.0.0
network spine01 eth0 192.168.0.21 255.255.0.0
network spine02 eth0 192.168.0.22 255.255.0.0
network server01 eth0 192.168.0.31 255.255.0.0
network server02 eth0 192.168.0.32 255.255.0.0
network server03 eth0 192.168.0.33 255.255.0.0
network server04 eth0 192.168.0.34 255.255.0.0
network exit01 eth0 192.168.0.41 255.255.0.0
network edge01 eth0 192.168.0.42 255.255.0.0
network internet eth0 192.168.0.43 255.255.0.0


autoconfig oob-mgmt-server

connect  leaf01 swp51   spine01 swp1
connect  leaf02 swp51   spine01 swp2
connect  leaf03 swp51   spine01 swp3
connect  leaf04 swp51   spine01 swp4
connect  leaf01 swp52   spine02 swp1
connect  leaf02 swp52   spine02 swp2
connect  leaf03 swp52   spine02 swp3
connect  leaf04 swp52   spine02 swp4

connect  server01 eth1   leaf01 swp1
connect  server01 eth2   leaf01 swp2
connect  server02 eth1   leaf02 swp1
connect  server02 eth2   leaf02 swp2
connect  server03 eth1   leaf03 swp1
connect  server03 eth2   leaf03 swp2
connect  server04 eth1   leaf04 swp1
connect  server04 eth2   leaf04 swp2

connect  exit01 swp51   spine01 swp30
connect  exit01 swp52   spine02 swp30

connect  internet swp1   exit01 swp44
connect  internet swp2   exit01 swp45

connect  edge01 eth1   exit01 swp1
connect  edge01 eth2   exit01 swp2
