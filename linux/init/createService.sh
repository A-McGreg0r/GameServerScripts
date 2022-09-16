#todo add extra info for enabling service
#file also need updated premions

SERVICE_PATH=/etc/systemd/system
GAME=factorio
GAME_FLAGS="--start-server /opt/factorio/saves/{save_file}.zip --server-settings /opt/factorio/data/server-settings.json"

{
echo '[Unit]'
echo 'Description=Factorio Headless Server'
echo ''
echo '[Service]'
echo 'Type=simple'
echo "User=$USER"
echo "ExecStart=/opt/$GAME/bin/x64/$GAME $GAME_FLAGS"
} > $SERVICE_PATH/$GAME.service


while [ "Y" != "$startOnBoot" ] && [ "N" != "$startOnBoot" ];
do
   echo -n  "Start on boot?: [Y/N] "
   read -r startOnBoot
done


if [ "Y" = "$startOnBoot" ]; then
  systemctl enable factorio.service
else
  echo "to start server manually use 'systemctl start factorio.service'"
fi;

echo "Press Any key to complete.."
read -r