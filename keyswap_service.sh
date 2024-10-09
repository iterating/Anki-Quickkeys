#!/bin/bash

systemctl --user stop keyswap >/dev/null 2>&1
systemctl --user disable keyswap >/dev/null 2>&1
systemctl --user stop keyswap.timer >/dev/null 2>&1
systemctl --user disable keyswap.timer >/dev/null 2>&1
mkdir -p ~/.config/systemd/user
mkdir -p ~/.config/autostart
cp ./system-config/keyswap.service ~/.config/systemd/user/keyswap.service
cp ./system-config/ankinate.desktop ~/.config/autostart/ankinate.desktop
cp ./system-config/keyswap.timer ~/.config/systemd/user/keyswap.timer
cp ./ankikeys/binary/ankikeys ~/.config/ankinate/ankikeys
cp ./system-config/xactive.sh ~/.config/ankinate/xactive.sh
cp ./system-config/caret_status.sh ~/.config/ankinate/caret_status.sh
cp ./system-config/cleanup.sh ~/.config/ankinate/cleanup.sh
cp ./system-config/.firefox-nw ~/.config/ankinate/.firefox-nw
sed -i "s/{username}/`whoami`/g" ~/.config/systemd/user/keyswap.service
sed -i "s/{displayid}/`echo "$DISPLAY"`/g" ~/.config/systemd/user/keyswap.service
# if [ "${#DISPLAY}" -gt 2 ]
# 	then
sed -i "s/#Environment/Environment/g" ~/.config/systemd/user/keyswap.service
# fi
systemctl --user daemon-reload
sed -i "s/ExecStart=/ExecStart=${swapcmd}/g" ~/.config/systemd/user/keyswap.service
systemctl --user enable keyswap.timer
systemctl --user start keyswap
