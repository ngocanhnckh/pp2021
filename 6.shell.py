import subprocess

cmd = ""
while(True):
    cmd=input("unfriendly@shell:/>")
    if (cmd=="exit"):
        break
    subprocess.run(cmd,check=True)