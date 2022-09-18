#todo add extra info for enabling service
# idea file also need updated premonitions

SERVICE_PATH=/etc/systemd/system
# todo make these args?
GAME=factorio
startOnBoot=y
# idea should this be an arg
GAME_FLAGS="--start-server /opt/$GAME/saves/{save_file}.zip --server-settings /opt/$GAME/data/server-settings.json"

{
echo '[Unit]'
echo 'Description=Factorio Headless Server'
echo ''
echo '[Service]'
echo 'Type=simple'
echo "User=$USER"
echo "ExecStart=/opt/$GAME/bin/x64/$GAME $GAME_FLAGS"
} > $SERVICE_PATH/$GAME.service

# idea it might just be better to have a enable and start/stop script



if [ "Y" = "$startOnBoot" ]; then
  systemctl enable factorio.service
else
  echo "to start server manually use 'systemctl start factorio.service'"
fi;

echo "Press Any key to complete.."
read -r