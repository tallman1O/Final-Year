TCP CLIENT-SERVER ON TWO MACHINES (MAC → UBUNTU)

GOAL:
Build a TCP server on Ubuntu and a TCP client on Mac, and make them communicate over LAN.

HARDWARE SETUP:
- Machine #1 (Ubuntu) — SERVER
- Machine #2 (MacBook) — CLIENT
- Ubuntu on Ethernet, Mac on Wi-Fi

RESULT:
Client sends “Hello from client!” and server responds “Hello from server!”

----------------------------------------------------
STEP 1: FIND UBUNTU IP
----------------------------------------------------
On Ubuntu:
    ip -4 addr show

Find the inet under the LAN interface, example:
    inet 172.19.1.208/21

This IP is used by the Mac to connect.

----------------------------------------------------
STEP 2: TEST CONNECTIVITY MAC → UBUNTU
----------------------------------------------------
On Mac:
    ping 172.19.1.208

Success = machines can talk over LAN.

----------------------------------------------------
STEP 3: CREATE AND COMPILE THE SERVER ON UBUNTU
----------------------------------------------------
Create file:
    nano server.c

Compile:
    gcc server.c -o server

Run server:
    ./server

Expected output:
    Server listening on port 8080...

----------------------------------------------------
STEP 4: CREATE AND COMPILE THE CLIENT ON MAC
----------------------------------------------------
Create file:
    nano client.c

Compile:
    gcc client.c -o client

Run client:
    ./client

----------------------------------------------------
STEP 5: EXPECTED BEHAVIOR
----------------------------------------------------
Ubuntu terminal prints:
    Client says: Hello from client!

Mac terminal prints:
    Server says: Hello from server!

----------------------------------------------------
HOW IT WORKS (LOW-LEVEL CONCEPTS)
----------------------------------------------------
Server side:
    socket()
    bind()
    listen()
    accept()
    recv()
    send()
    close()

Client side:
    socket()
    connect()
    send()
    recv()
    close()

----------------------------------------------------
NETWORK NOTES
----------------------------------------------------
- TCP over port 8080
- No firewall modifications required in your environment
- IPv4 used
- Endian conversion handled by htons() and inet_pton()

END OF FILE