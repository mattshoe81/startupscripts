import os
import subprocess
from datetime import datetime


def execute(dir, cmd_string):
    cmds = command_string.split("&")

    for i in range(len(cmds)):
        atomic_cmd = f"cd {dir} & {cmds[i].strip()}"
        log(atomic_cmd)
        cmd = atomic_cmd.split(" ")
        log(subprocess.call(cmd, shell=True))


def log(message):
    file = open("./log.txt", "a")
    log_message = f"{datetime.now()}: {message}\n"
    file.write(log_message)
    print(log_message)


log("Running Startup Script: osu_git.py ")
directory = f"~\\Documents\\OSU\\sp2020"
path = os.path.expanduser(directory)
command_string = f"git pull origin master & git add --all & git commit -m \"ShutdownCommit\" & git push origin master"
execute(path, command_string)
log("\n\n\n")
