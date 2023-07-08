# Simple encryptor for private keys

The script is the simplest encryptor / decryptor for private keys.

## Setup

1. Download script
2. Install python
3. Open the folder with the script in any convenient IDE or terminal
4. Create a virtual environment
   
```bash
python -m venv .venv
```

5. Activate the virtual environment (on Windows)
```bash
source .venv/Scripts/activate
```

5. Activate the virtual environment (on Linux/Mac) 
```bash
source .venv/bin/activate
```

6. Install dependencies
```bash
pip install -r requirements.txt
```
7. Start
```bash
python main.py
```

## Litle FAQ

Here is a demo example. It is highly discouraged to use this entire code in your scripts, as the Caesar cipher is easily susceptible to brute-force attacks.