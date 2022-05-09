#!/usr/bin/env python3
"""Testing platform for Python3. ## testing the multi desktop output
    working.
"""
from pythonosc.udp_client import SimpleUDPClient

play        = "Els Miserables".upper()
range_start = 1  # first array value
range_end   = 48  # last array value
scene_start = 1  # first scene value before start playing
scene_end   = 49 # last scene value


serverlist = [["mad1", "127.0.0.1", 8010]
             ,["mad2", "192.168.88.246", 8030]
             ]

print("\n{}\n".format(play))
input("INICIO. Presiona INTRO para INICIAR la función...")
for mad,servername,serverport in serverlist:
    client = SimpleUDPClient(servername, serverport)  # Create client
    client.send_message("/cues/Bank-1/columns/start_by_number", scene_start)   # go to first column

for scene in range(range_start,range_end):
    input('Presiona INTRO para ir a la escena: {}...'.format(scene))
    for mad,servername,serverport in serverlist:
    	# set up OSC desktop
        client = SimpleUDPClient(servername, serverport)  # Create client
        # send client command
        client.send_message("/cues/Bank-1/columns/start_next", 1)   # Send int message

input("FINAL. Presiona INTRO para ir a la escena FINAL...")
for mad,servername,serverport in serverlist:
    client = SimpleUDPClient(servername, serverport)  # Create client
    client.send_message("/cues/Bank-1/columns/start_by_number", scene_end)   # go to first column

print("\n{}\nBuen trabajo. ¡¡FINALIZADO!!".format(play))
