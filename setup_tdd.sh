directory=$1
mkdir $directory
cd $directory
mkdir tests
touch tests/__init__.py
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install sniffer macfsevents
sniffer
