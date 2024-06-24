import ubelt as ub
import json
from loguru import logger
import time

def wrap_osa(code:str):
    return f"osascript -e \'{code}\'"

def wrap_osa_list(code):
    output = "osascript "
    for line in code:
        output += f"-e '{line}' "
    return output


def switch_desktop(desk_num:int):
    mapping = {0:18, 1:19, 2:20, 3:21, 4:23}
    code = mapping[desk_num]#desk_num + 18
    os_script=f"tell application \"System Events\" to key code {code} using {{control down}}"
    os_script = wrap_osa(os_script)
    ub.cmd(os_script)

standard_programs = [
            "/Applications/Google Chrome.app",
            "/Applications/iTerm.app",
        ]
chrome_script = wrap_osa_list(["tell application \"Google Chrome\"", 
                               "make new window", 
                               "activate", 
                               "end tell",])



json_path = ub.Path("startup.json")
with json_path.open(mode='r') as f:
    config = json.load(f) 

if len(config['projects']) > 4:
    logger.error("Can't access more than 4 proj spaces, limit the # of projects")
    quit(-1)


switch_desktop(0)
initial_desktop_script = wrap_osa_list(["tell application \"Google Chrome\" to activate",
                                        "tell application \"iTerm\" to activate",
                                        "tell application \"iTerm2\"",
                                            "tell current window",
                                                "create tab with default profile",
                                            "end tell",
                                            "tell current session of current window",
                                                "write text \"sudo mactop\"",
                                            "end tell",
                                            "tell current window",
                                                "create tab with default profile",
                                            "end tell",
                                            "tell current session of current window",
                                                "write text \"spotify_player\"",
                                            "end tell",
                                            "tell current window",
                                                "create tab with default profile",
                                            "end tell",
                                        "end tell",
                                        ])
ub.cmd(initial_desktop_script)
time.sleep(5)

for pidx, project in enumerate(config['projects']):
    logger.debug(f"Desktop # {pidx+1}")
    switch_desktop(pidx+1)
    time.sleep(2)
    proj_name = project['name']
    logger.debug(f"project name {proj_name}")
    ub.cmd(chrome_script)
    time.sleep(2)
    dir_cmd = f"cd ~/kitware_projects/{proj_name}"
    iterm_script = wrap_osa_list([
        "tell application \"iTerm2\"",
        "create window with default profile",
            "tell current session of current window",
                f"write text \"{dir_cmd}\"",
            "end tell",
        "end tell"])
    ub.cmd(iterm_script)
    time.sleep(2)
    if 'extra_programs' in project.keys():
        for c in project['extra_programs']:
            ub.cmd(wrap_osa(c))
            time.sleep(2)



