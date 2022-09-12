from pypresence import Presence
from os import path
import time, json

clientId = "1018290419492192317"

RPC = Presence(clientId)

RPC.connect()

hasUpdated = False

val = 10 

jsonStr = '{"status": "Idling", "project": "None", "file": "None"}'

jsonFile = open("/tmp/nvimrpc.json", "w")
jsonFile.write(jsonStr)
jsonFile.close()

while True:
    oTime = path.getctime("/tmp/nvimrpc.json")
    time.sleep(1)
    nTime = path.getctime("/tmp/nvimrpc.json")

    if oTime != nTime:
        hasUpdated = False 

    print(hasUpdated)

    if not hasUpdated:
        with open("/tmp/nvimrpc.json", "r") as statusJSON:
            jsonData = json.load(statusJSON)

            print(jsonData['status'])

            if jsonData['status'] == "Idling":
                RPC.update(state="Idling", large_image="floppydisc1024")
            else:
                RPC.update(details="Editing project: " + jsonData['project'], state="Editing file: " + jsonData['file'], large_image="floppydisc1024")

        val += 1
        hasUpdated = True

        statusJSON.close()
