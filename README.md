# WARNING: THIS IS CURRENTLY ONLY USABLE ON LINUX! SORRY!

# pf2beta-autoupdater
auto updates your pf2beta server
This is **not** designed to clone your repo, you **must** [do that first](https://gitlab.com/CryptoGibus/pf2beta/-/wikis/Beta%20Server).

IF YOU ARE ON LINUX YOU MUST RUN THIS COMMAND
```
chmod +x conn.sh
```

place **outside** of your server pf2beta directory

*This program uses [`rcon-cli`](https://github.com/itzg/rcon-cli/releases/tag/1.6.0)*
```
curl -L https://github.com/itzg/rcon-cli/releases/download/1.6.0/rcon-cli_1.6.0_linux_amd64.tar.gz > rcon-cli_1.6.0_linux_amd64.tar.gz 
tar -xvzf rcon-cli_1.6.0_linux_amd64.tar.gz
```
- YOU MUST INSTALL THIS IN THE SAME DIRECTORY OF `pf2beta-autoupdater` I WILL NOT INCLUDE IT
    - There is a version for several different flavors of Linux and Windows

## Configuration

### Step 1
Please enter the name of your repo in `REPO` in this style
```
gitlab.com/username/reponame.git
```

### Step 2
Enter your gitlab username in `USER`

Be sure to generate and access token from your [gitlab](https://gitlab.com/-/profile/personal_access_tokens)
And put it in the `TOKEN` string in `config.json`

### Step 3
Set the time in minutes you want the repo to check for changes in `TIMEINMINUTES`

### Step 4
Set the keyword you want to automatically update the server in `KEYWORD`
- If no keyword automatic restart functionality will not occur
- If you want the server to restart after every update enter `upd1` in `KEYWORD`
  
### Step 5
Enter in the pf2beta server ip, port, and RCON password
- `SERVER_IP` `PORT` `SERVER_PW`
- If no RCON password is set this will just not work