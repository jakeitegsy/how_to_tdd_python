function testSetup {
    return @"
import unittest

class Test$($projectName.toUpper())(unittest.TestCase):

    def test_$projectName(self):
        self.assertEqual(5, 6)
"@
}

$projectName = $args[0]
mkdir $projectName
cd $projectName
mkdir tests
New-Item tests/__init__.py
$(testSetup) | Out-File $("tests/test_$($projectName).py") -Encoding UTF8
python -m venv .venv
.venv/scripts/activate
pip install -U pip
pip install sniffer pywin32
sniffer
