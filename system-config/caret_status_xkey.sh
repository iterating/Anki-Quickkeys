#!/bin/bash

for pid in $(pidof -x caret_status_xkey.sh); do
    if [ $pid != $$ ]; then
        echo "[$(date)] : caret_status_xkey.sh : Process is already running with PID $pid"
        exit 1
    fi
done

mkdir -p /tmp/ankinate/xkeysnail
echo "0" > /tmp/ankinate/caret

millitime=`date +%s%3N`
echo "$millitime" > /tmp/ankinate/millitime

IBUSADD=$(cat ~/.config/ibus/bus/`ls ~/.config/ibus/bus -1rt | tail -n1` | awk -F'IBUS_ADDRESS=' '{print $2}' | xargs)
dbus-monitor --address $IBUSADD "path='/org/freedesktop/IBus/Panel',interface='org.freedesktop.IBus.Panel',member='FocusOut'" 2> /dev/null | grep --line-buffered -o -P '(?<=object path \"/org/freedesktop/IBus/InputContext_).*(?=[\"])' |
while read ln
do
	newtime=`date +%s%3N`
	difftime=$(( newtime - millitime ))
	millitime="$newtime"
	echo "$millitime" > /tmp/ankinate/millitime
	appname=$(xprop -id `xprop -root | grep "_NET_ACTIVE_WINDOW(WINDOW)" | awk '{print $5}'` | grep "WM_CLASS(STRING)" | awk '{print substr($4,2,length($4)-2)}')
	if [ "${ln}" == "1" ]; then
		appname=$(xprop -id `xprop -root | grep "_NET_ACTIVE_WINDOW(WINDOW)" | awk '{print $5}'` | grep "WM_CLASS(STRING)" | awk '{print substr($4,2,length($4)-2)}')
		if [ "${appname}" == "Firefox" ]; then
			# echo "ff ww"
			printf 'ff ww %s\n' "1" > /tmp/ankinate/caret
		elif [ "${appname}" == "Chromium" ] || [ "${appname}" == "Chromium-browser" ] || [ "${appname}" == "Google-chrome" ] || [ "${appname}" == "Epiphany" ]; then
			# echo "chrome ww"
			printf 'chrome ww %s\n' "1" > /tmp/ankinate/caret
		else
			echo "reset" > /tmp/ankinate/caret
		fi
	else
		if [ "${appname}" == "Firefox" ]; then
			# echo "ff nw"
			printf 'ff nw\n' > /tmp/ankinate/caret
		elif [ "${appname}" == "Chromium" ] || [ "${appname}" == "Chromium-browser" ] || [ "${appname}" == "Google-chrome" ] || [ "${appname}" == "Epiphany" ]; then
			# echo "chrome nw"
			printf 'chrome nw\n' > /tmp/ankinate/caret
		else
			echo "reset" > /tmp/ankinate/caret
		fi
	fi

done&

while (true);do
	sleep 0.2
	appname2=$(xprop -id `xprop -root | grep "_NET_ACTIVE_WINDOW(WINDOW)" | awk '{print $5}'` | grep "WM_CLASS(STRING)" | awk '{print substr($4,2,length($4)-2)}')
	check=$(cat /tmp/ankinate/caret)
	millitime=$(cat /tmp/ankinate/millitime)
	newtime=`date +%s%3N`
	difftime=$(( newtime - millitime ))
	if (( $difftime > 200 )); then
		if [ "${check}" == "ff nw" ] && [ "${lastcheck}" != 1 ]; then
			echo "firefox no wordwise"
			# Sets new config
			perl -pi -e "s/[^\n]\s{3}(K.*)(# Chrome-nw)/    # \$1\$2/g;s/[^\n]\s{3}#\s(K.*)(# Firefox-nw)/    \$1\$2/g;s/[^\n]\s{3}(K.*)(# Beginning of Line)/    # \$1\$2/g;s/[^\n]\s{3}(K.*)(# End of Line)/    # \$1\$2/g" /tmp/ankinate/xkeysnail/ankinate-multikey.py 2>/dev/null
			lastcheck=1
			ww=0
		elif [ "${check}" == "chrome nw" ] && [ "${lastcheck}" != 2 ]; then
			echo "chrome no wordwise"
			# Sets new config
			perl -pi -e "s/[^\n]\s{3}(K.*)(# Firefox-nw)/    # \$1\$2/g;s/[^\n]\s{3}(K.*)(# Beginning of Line)/    # \$1\$2/g;s/[^\n]\s{3}(K.*)(# End of Line)/    # \$1\$2/g;s/[^\n]\s{3}#\s(K.*)(# Chrome-nw)/    \$1\$2/g" /tmp/ankinate/xkeysnail/ankinate-multikey.py 2>/dev/null
			lastcheck=2
			ww=0
		elif ([ "${check}" != "chrome nw" ] && [ "${check}" != "ff nw" ] && [ "${lastcheck}" != 3 ]) || ([ "${appname2}" != "Firefox" ] && [ "${appname2}" != "Chromium" ] && [ "${appname2}" != "Chromium-browser" ] && [ "${appname2}" != "Google-chrome" ] && [ "${appname2}" != "Epiphany" ] && [ "${check}" == "reset" ] && [ "${lastcheck}" != 3 ]); then
			echo "wordwise"
			# Sets original config
			perl -pi -e "s/[^\n]\s{3}(K.*)(# Firefox-nw)/    # \$1\$2/g;s/[^\n]\s{3}#\s(K.*)(# Beginning of Line)/    \$1\$2/g;s/[^\n]\s{3}#\s(K.*)(# End of Line)/    \$1\$2/g;s/[^\n]\s{3}(K.*)(# Chrome-nw)/    # \$1\$2/g" /tmp/ankinate/xkeysnail/ankinate-multikey.py 2>/dev/null
			# cp /home/ryan/.config/ankinate/ankinate-multikey.py /tmp/ankinate/xkeysnail/ankinate-multikey.py
			lastcheck=3
		fi
	fi
done
