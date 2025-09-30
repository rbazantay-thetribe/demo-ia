## Virtual environment (venv)

Follow these steps to create and activate a Python virtual environment and install dependencies.

### Prerequisites
- Python 3.10 or newer installed
- `pip` available

### Create the environment (Linux/macOS)
```bash
python3 -m venv .venv
```

### Activate the environment (Linux/macOS)
```bash
source .venv/bin/activate
```

### Upgrade pip (recommended)
```bash
python -m pip install --upgrade pip
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Deactivate when you are done
```bash
deactivate
```

### Windows (PowerShell) equivalents
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
deactivate
```


