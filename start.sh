if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Hydrayt777/HyDrix-Tools-Bot-New.git /Hydrix
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Hydrix
fi
cd /Hydrix
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
