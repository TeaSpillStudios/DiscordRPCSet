import argparse, json 

#static void UpdatePresence()
#{
#    DiscordRichPresence discordPresence;
#    memset(&discordPresence, 0, sizeof(discordPresence));
#    discordPresence.state = "main.nelua";
#    discordPresence.details = "Project: TeaEngine";
#    discordPresence.largeImageKey = "floppydisc1024";
#    discordPresence.largeImageText = "NeoVim";
#    Discord_UpdatePresence(&discordPresence);
#}

parser = argparse.ArgumentParser()

parser.add_argument('-s', '--state', default='Idling', dest='state', help='Set state', type=str)
parser.add_argument('-p', '--project', default='None', dest='project', help='Set project', type=str)
parser.add_argument('-f', '--file', default='None', dest='file', help='Set file name', type=str)

args = parser.parse_args()

#data = {'rpc': 
#    [
#        {'status': [args.state]},
#        {'project': [args.project]},
#        {'file': [args.file]},
#    ]
#}

data = {
    'status': args.state,
    'project': args.project,
    'file': args.file
}

jsonData = json.dumps(data)

jsonFile = open("/tmp/nvimrpc.json", "w")
jsonFile.write(jsonData)
jsonFile.close()

print(f'State: {args.state}\nProject: {args.project}\nFile: {args.file}')

print(f'\n{jsonData}')
