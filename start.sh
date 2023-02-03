if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Hydra-sjz/Hyd-Autofilter.git /Hyd-Autofilter
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Hyd-Autofilter
fi
cd /Hyd-Autofilter
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
