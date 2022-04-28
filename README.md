# pf2beta-autoupdater

**Only intended for Linux Dedicated Servers**

This is **not** designed to clone your repo, you **must** [do that first](https://gitlab.com/CryptoGibus/pf2beta/-/wikis/Beta%20Server).

Clone **outside** of your server ``pf2beta`` directory.

## Configuration

### Step 1
Set the time in minutes you want the repo to check for changes in `TIME`

### Step 2
Set the keyword you want to automatically update the server in `KEYWORD`
- If no keyword automatic restart functionality will not occur

### Step 3
Enter the screen worker name you have your server set to in `SCREEN_NAME`

### Step 4
Enter in the pf2beta server IP, Port, and RCON password
- `SERVER_IP` `PORT` `SERVER_PW`
- If no RCON password is set then the program will not make an attempt to to connect to the server.

## Running the software.

Run this command.

``pip install -r requirements.txt``

Then this command.

``screen -dmS updater python3 main.py``
