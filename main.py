import git
import valve.rcon
import json
import sys
import os
import time
import platform
import logging

REM_BRANCH = 'master'
logging.basicConfig(handlers=[logging.FileHandler(filename="updater.log", 
                                                  encoding='utf-8', mode='a+')],
                    format="[ %(asctime)s ] %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p",
                    level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
console.setFormatter(logging.Formatter("[ %(asctime)s ] %(message)s", "%m/%d/%Y %I:%M:%S %p"))
logging.getLogger('').addHandler(console)

def pullRepo(localRepo):
    o = localRepo.remotes.origin
    try:
        logging.warning("Attempting to pull")
        o.pull()
        logging.warning("Success")
    except Exception as e:
        logging.warning("Unable to pull repo, please make this user has the proper credentials.")
        print(e)
    
def restartServer(server, port, password, screen, localRepo):
    
    server_address = (server, int(port))
    if password != "":
        try:
            with valve.rcon.RCON(server_address, password) as rcon:
                print(rcon('say (ATTENTION)'))
                time.sleep(2)
                print(rcon('say "Critical Server Update."'))
                time.sleep(1)
                print(rcon('say "Server will restart in 10 seconds."'))
                time.sleep(7)
                print(rcon('say "3..."'))
                time.sleep(1)
                print(rcon('say "2..."'))
                time.sleep(1)
                print(rcon('say "1..."'))
                time.sleep(2)
                print(rcon('kickall "Server is updating"'))
        except Exception as e:
            print(e)
        
    if platform.system().lower() == "linux":
        try:
            os.system(f"screen -X -S {screen} quit")
            pullRepo(localRepo)
            os.system(f"screen -dmS {screen} ./run.sh")
        except Exception as e:
            logging.warning("Unable restart server, check users perms")
            print(e)
    if platform.system().lower() == "windows":
        logging.warning("Please relaunch your server.")
        
def parseCommit(config):

    server = config["SERVER_IP"]
    port = config["PORT"]
    password = config["SERVER_PW"]
    key = config["KEYWORD"]
    screen = config["SCREEN_NAME"]
    
    localRepo = git.Repo("../pf2beta")
    main = localRepo.head.reference
    gitmsg = main.commit.message
   
    logging.warning("Checking out " + str(main))
    logging.warning(str(gitmsg))    

    def pretty_diff(diff):
        for cht in diff.change_type:
            changes = list(diff.iter_change_type(cht))
            if len(changes) == 0:
                continue
            logging.warning("Changes type:", cht)
            for d in changes:
                print(d.b_path)
                if key in d.b_path:
                    return True

    while True:
        current_hash = localRepo.head.object.hexsha
        o = localRepo.remotes.origin
        o.fetch()
        changed = o.refs[REM_BRANCH].object.hexsha != current_hash
        if changed:
            diff = localRepo.head.commit.diff(o.refs[REM_BRANCH].object.hexsha)
            restart = pretty_diff(diff)
            if restart:
                logging.warning("Critical server update detected")
                restartServer(server, port, password, screen, localRepo)
                break
            else:
                logging.warning(f"Keyword \'{key}\' not found\n")
                pullRepo(localRepo)
                break
        else:
            logging.warning("No update detected")
            break

def main():
    try:
        with open('config.json') as json_file:
            config = json.load(json_file)

    except Exception as e:
        logging.warning("Unable to open config.json - Please check it is in the root directory")
        print(e)
        sys.exit(1)
        
    while True:
        parseCommit(config)
        time.sleep(float(config["TIME"])*60)
               
main()