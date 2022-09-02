## Install

`PROJECT_DIR` is project root

```bash
mkdir ${PROJECT_DIR}
cd ${PROJECT_DIR}

sudo apt update -y
sudo apt install -y python3 python3-venv git

git clone http://185.208.77.246/inference/demo.git .
# git checkout develop

python3 -m venv venv
source venv/bin/activate
pip install -U pip wheel setuptools pytest
pip install -r requirements.txt
```

# Test

```bash
bin/test.sh

# OR
# source venv/bin/activate
# pytest
```

## Install package in other projects

```bash
pip install git+http://185.208.77.246/inference/demo.git
```

# User manual

```python
from lfdemo import get_users

df = get_users()
print(df)
```
