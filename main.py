import git
import valve.rcon
import json
import sys
import subprocess
import time
import platform

def pullRepo(localRepo):
    o = localRepo.remotes.origin
    try:
        print("Attempting to pull")
        o.pull()
        print("Success")
    except Exception as e:
        print("Unable to pull repo, please make this user has the proper credentials.")
        print(e)
    
def restartServer(server, port, password, screen, localRepo):
    
    server_address = (server, int(port))
    # try:
    #     with valve.rcon.RCON(server_address, password) as rcon:
    #         print(rcon('say (ATTENTION)'))
    #         time.sleep(2)
    #         print(rcon('say "Critical Server Update."'))
    #         time.sleep(1)
    #         print(rcon('say "Server will restart in 10 seconds."'))
    #         time.sleep(7)
    #         print(rcon('say "3..."'))
    #         time.sleep(1)
    #         print(rcon('say "2..."'))
    #         time.sleep(1)
    #         print(rcon('say "1..."'))
    #         time.sleep(2)
    #         print(rcon('kickall "Server is updating"'))
    # except Exception as e:
    #     print(e)
        
    if platform.system().lower() == "windows":
        try:
            print(subprocess.call(f"screen -X -S {screen} quit"))
            pullRepo(localRepo)
            print(subprocess.call(f"screen -dmS {screen} ./run.sh"))
        except Exception as e:
            print("Unable restart server, check users perms")
            print(e)
    if platform.system().lower() == "windows":
        print("Please relaunch your server.")
        
def parseCommit(config):

    server = config["SERVER_IP"]
    port = config["PORT"]
    password = config["SERVER_PW"]
    key = config["KEYWORD"]
    screen = config["SCREEN_NAME"]
    
    localRepo = git.Repo("../pf2beta")
    main = localRepo.head.reference
    gitmsg = main.commit.message
    
    print("Checking out " + str(main))
    
    print(str(gitmsg))    
     
    if key.lower() in gitmsg.lower():
        print("Critical server update detected")
        restartServer(server, port, password, screen, localRepo)
    else:
        print(f"Keyword \'{key}\' not found\n")
        pullRepo(localRepo)

def main():
    try:
        with open('config.json') as json_file:
            config = json.load(json_file)

    except Exception as e:
        print("Unable to open config.json - Please check it is in the root directory")
        print(e)
        sys.exit(1)
        
    while True:
        parseCommit(config)
        time.sleep(float(config["TIME"])*60)
               
main()