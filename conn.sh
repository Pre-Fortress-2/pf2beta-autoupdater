!#/bin/bash
ip=($(jq -r '.SERVER_IP' config.json))
port=($(jq -r '.PORT' config.json))
pw=($(jq -r '.SERVER_PW' config.json))

echo "connecting to ${ip[@]}"

./rcon-cli --host ${ip[@]} --password ${pw[@]} --port ${port[@]} say "(ATTENTION)"
sleep 2s
./rcon-cli --host ${ip[@]} --password ${pw[@]} --port ${port[@]} say "Critical Server Update."
sleep 1s
./rcon-cli --host ${ip[@]} --password ${pw[@]} --port ${port[@]} say "Server will restart in 10 seconds."
sleep 7s
./rcon-cli --host ${ip[@]} --password ${pw[@]} --port ${port[@]} say "3..."
sleep 1s
./rcon-cli --host ${ip[@]} --password ${pw[@]} --port ${port[@]} say "2..."
sleep 1s
./rcon-cli --host ${ip[@]} --password ${pw[@]} --port ${port[@]} say "1..."
sleep 2s
./rcon-cli --host ${ip[@]} --password ${pw[@]} --port ${port[@]} kickall "Server is updating"
