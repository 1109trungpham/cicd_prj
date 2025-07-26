mkdir cicd_prj
cd cicd_prj
python3.11 -m venv venv
source venv/bin/activate
pip install pytest

mkdir source
mkdir test

echo "def add(a, b): return a + b" > source/utils.py
touch source/__init__.py  (biến source/ thành một package Python chuẩn)

echo "from source.utils import add
def test_add():
    assert add(2, 3) == 5" > test/test_utils.py

echo "venv
.env
.DS_Store" > .gitignore

pip freeze > requirements.txt


