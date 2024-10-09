#!/bin/bash
if [ -f {homedir}/.config/systemd/user/keyswap.timer ]; then
	systemctl --user stop keyswap.timer >/dev/null 2>&1
	systemctl --user disable keyswap.timer >/dev/null 2>&1
fi
if [ -f {homedir}/.config/systemd/user/keyswap.service ]; then
	systemctl --user stop keyswap >/dev/null 2>&1
	systemctl --user disable keyswap >/dev/null 2>&1
fi

# export DISPLAY={displayid};/usr/bin/xhost +SI:localuser:root
mkdir -p /tmp/ankikeys/xkeysnail
cp {homedir}/.config/ankikeys/ankikeys-multikey.py /tmp/ankikeys/xkeysnail/ankikeys-multikey.py
