testSetup=$(cat <<-ENDimport unittest

class Test$($1)(unittest.TestCase):

    def test_$projectName(self):
        self.assertEqual(5, 6)
END
)

directory=$1
mkdir $directory
cd $directory
mkdir tests
touch tests/__init__.py
printf "%s" "$testSetup" > "tests/test_$($1).py"
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install sniffer macfsevents
sniffer
