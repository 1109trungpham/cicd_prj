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

-================================================================================
-================================================================================

git init
git add .
git commit -m "init project"
git branch -M main
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin main

-================================================================================
-================================================================================

mkdir -p .github/workflows
touch .github/workflows/python-ci.yml
<!-- 
name: Python CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.11"

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: |
        PYTHONPATH=. pytest
-->

git add .github/workflows/python-ci.yml
git commit -m "add GitHub Actions CI"
git push

-================================================================================
-================================================================================

Vào repo của bạn trên GitHub
Click tab "Actions"
Bạn sẽ thấy workflow Python CI đang chạy
Nếu test pytest pass thì bạn sẽ thấy màu xanh ✅

-================================================================================
-================================================================================

git add .
git commit -m "Thêm ETL + workflow CD"
git push origin main