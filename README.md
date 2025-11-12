# 4.Execution_of_NetworkCommands
## AIM :Use of Network commands in Real Time environment
## Software : Command Prompt And Network Protocol Analyzer
## Procedure: To do this EXPERIMENT- follows these steps:
<BR>
In this EXPERIMENT- students have to understand basic networking commands e.g cpdump, netstat, ifconfig, nslookup ,traceroute and also Capture ping and traceroute PDUs using a network protocol analyzer 
<BR>
All commands related to Network configuration which includes how to switch to privilege mode
<BR>
and normal mode and how to configure router interface and how to save this configuration to
<BR>
flash memory or permanent memory.
<BR>
This commands includes
<BR>
• Configuring the Router commands
<BR>
• General Commands to configure network
<BR>
• Privileged Mode commands of a router 
<BR>
• Router Processes & Statistics
<BR>
• IP Commands
<BR>
• Other IP Commands e.g. show ip route etc.
<BR>

## Program
## client.py
```
import socket
from pythonping import ping
s=socket.socket() 
s.bind(('localhost', 8000))
s.listen(5)
c, addr = s.accept()
while True:
	hostname = c.recv(1024).decode()
	try:
		c.send(str(ping(hostname, verbose=False)).encode())
	except KeyError:
		c.send("Not Found".encode())

```
## server.py
```
import socket
s = socket.socket()
s.connect(('localhost', 8000))
while True:
	ip = input("Enter the website you want to ping ")
	s.send(ip.encode())
	print(s.recv(1024).decode())

```

## Output
![alt text](image.png)
#### netstat
![WhatsApp Image 2025-11-12 at 10 51 17_9adf2139](https://github.com/user-attachments/assets/bc26058b-3803-4fa4-be3e-9551433aa561)
#### ipconfig
![WhatsApp Image 2025-11-12 at 10 51 18_043ddb6b](https://github.com/user-attachments/assets/778e4e60-caeb-419f-8be0-34c17baa26da)
#### ping 
![WhatsApp Image 2025-11-12 at 10 51 18_427e3bcc](https://github.com/user-attachments/assets/440caac2-9ac3-49d7-b550-38bfa0bf09c8)
#### tracert
![WhatsApp Image 2025-11-12 at 10 51 18_ffc4e964](https://github.com/user-attachments/assets/237d8729-22b2-4b24-a47e-32f13f516e2a)
#### nslookup
![WhatsApp Image 2025-11-12 at 10 51 18_d7aa23e7](https://github.com/user-attachments/assets/16be49ab-e507-401c-a298-75ea272745b8)
#### getmac
![WhatsApp Image 2025-11-12 at 10 51 18_b9fccfea](https://github.com/user-attachments/assets/ce8925d2-a043-4678-8c81-cd97ab6c7a37)
#### hostname 
![WhatsApp Image 2025-11-12 at 10 51 18_593860b9](https://github.com/user-attachments/assets/36d956a1-5e28-4295-8e14-1d40939392b5)
#### nbtstat
![WhatsApp Image 2025-11-12 at 10 51 17_8d8e6344](https://github.com/user-attachments/assets/482ccd4e-163c-417a-a339-d11b53829525)
#### arp
![WhatsApp Image 2025-11-12 at 10 51 19_e461a66f](https://github.com/user-attachments/assets/41103afe-4c64-47fb-be7c-462e4bf98abf)
#### systeminfo
![WhatsApp Image 2025-11-12 at 10 51 18_097c3052](https://github.com/user-attachments/assets/5d400e33-42d9-4a81-a09a-f4ce1c107535)




## Result
Thus Execution of Network commands Performed 
