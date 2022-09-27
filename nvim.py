import os, sys

cwd = os.getcwd()

if "GitHub" in cwd:
    cwd = cwd.split("/")[5]
else:
    cwd = "Unknown"

if len(sys.argv) < 2:
    os.system(f"python3 ~/bin/main.py -s Editting -f Buffer -p {cwd}")
    os.system(f"nvim")
else:
    os.system(f"python3 ~/bin/main.py -s Editting -f {sys.argv[1]} -p {cwd}")
    os.system(f"nvim {sys.argv[1]}")

os.system(f"python3 ~/bin/main.py -s Idling")
