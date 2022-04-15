import git
import json
import sys
import subprocess
import time
def main():
    try:
        with open('config.json') as json_file:
            config = json.load(json_file)

    except Exception as e:
        print("unable to open config.json - please check it is in the root directory")
        print(e)
        sys.exit(1)
        
    while True:
        parseCommit(config)
        time.sleep(int(config["TIMEINMINUTES"])*60)
    
def pullRepo(remoteRepo):
    localRepo = git.Repo("../pf2beta")
    o = localRepo.remotes.origin
    
    r = remoteRepo.remotes.origin
    try:
        o.pull()
    except Exception as e:
        print("unable to pull from local repo, using remote credentials instead")
        print(e)
        try: 
            r.pull()
        except Exception as re:
            print("unable to pull from remote repo, maybe you forgot to enter the write styling for the repo?")
            print(re)
            sys.exit(1)
    
def restartServer():
    subprocess.call(['sh', './conn.sh'])
    
        
        
def parseCommit(config):
    
    user = config["USER"]
    token = config["TOKEN"]
    url = config["REPO"]
    key = config["KEYWORD"]
    
    repoURL = f"https://{user}:{token}@{url}"
    print("Checking out " + url)
    
    remoteRepo = git.Repo("../pf2beta")
    main = remoteRepo.head.reference
    gitmsg = main.commit.message
    
    print(str(gitmsg))
    pullRepo(remoteRepo)
    if gitmsg.lower() == key.lower():
        print("Critical server update detected")
        restartServer()
        
main()