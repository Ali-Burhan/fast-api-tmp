# 🛠️ Installation Guide# 🛠️ Installation Guide



Complete installation instructions for the FastAPI Speech Translation API.Complete installation instructions for the FastAPI Speech Translation API.



> **Quick Start:** If you just want to get started quickly, run `./setup.sh` (Linux/Mac) or `setup.bat` (Windows)> **Quick Start:** If you just want to get started quickly, run `./setup.sh` (Linux/Mac) or `setup.bat` (Windows)



------



## Table of Contents## Table of Contents



1. [Prerequisites](#prerequisites)1. [Prerequisites](#prerequisites)

2. [Automated Installation](#automated-installation)2. [Automated Installation](#automated-installation)

3. [Manual Installation](#manual-installation)3. [Manual Installation](#manual-installation)

4. [Configuration](#configuration)4. [Configuration](#configuration)

5. [Running the Application](#running-the-application)5. [Running the Application](#running-the-application)

6. [Verification](#verification)6. [Verification](#verification)

7. [Troubleshooting](#troubleshooting)7. [Troubleshooting](#troubleshooting)



------



## Prerequisites## Prerequisites



### Required### Required



1. **Python 3.13+** - [Installation instructions below](#installing-python-313)1. **Python 3.13+** - [Installation instructions below](#installing-python-313)

2. **Redis server** - For caching audio data2. **Redis server** - For caching audio data

3. **FFmpeg** - For audio format conversion3. **FFmpeg** - For audio format conversion

   - Ubuntu/Debian: `sudo apt-get install ffmpeg`   - Ubuntu/Debian: `sudo apt-get install ffmpeg`

   - macOS: `brew install ffmpeg`   - macOS: `brew install ffmpeg`

   - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html)   - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

4. **MediaInfo** - For audio file metadata4. **MediaInfo** - For audio file metadata

   - Ubuntu/Debian: `sudo apt-get install mediainfo`   - Ubuntu/Debian: `sudo apt-get install mediainfo`

   - macOS: `brew install media-info`   - macOS: `brew install media-info`

   - Windows: `choco install mediainfo`   - Windows: `choco install mediainfo`

5. **API Keys:**5. **API Keys:**

   - [Deepgram](https://console.deepgram.com/) - Speech-to-Text   - [Deepgram](https://console.deepgram.com/) - Speech-to-Text

   - [DeepL](https://www.deepl.com/pro-api) - Translation   - [DeepL](https://www.deepl.com/pro-api) - Translation

   - [ElevenLabs](https://elevenlabs.io/) - Text-to-Speech   - [ElevenLabs](https://elevenlabs.io/) - Text-to-Speech



### Installing Python 3.13### Installing Python 3.13



**Using pyenv (Recommended):****Using pyenv (Recommended):**

```bash```bash

# Install pyenv# Install pyenv

curl https://pyenv.run | bashcurl https://pyenv.run | bash



# Install Python 3.13# Install Python 3.13

pyenv install 3.13.0pyenv install 3.13.0

pyenv global 3.13.0pyenv global 3.13.0

``````

> See [PYENV_GUIDE.md](PYENV_GUIDE.md) for detailed pyenv instructions> See [PYENV_GUIDE.md](PYENV_GUIDE.md) for detailed pyenv instructions



**macOS:****macOS:**

```bash```bash

brew install python@3.13brew install python@3.13

``````



**Ubuntu/Debian:****Ubuntu/Debian:**

```bash```bash

sudo apt updatesudo apt update

sudo apt install python3.13 python3.13-venv python3.13-devsudo apt install python3.13 python3.13-venv python3.13-dev

``````



**Windows:****Windows:**

- Download from [python.org](https://www.python.org/downloads/)- Download from [python.org](https://www.python.org/downloads/)

- ⚠️ Check "Add Python to PATH" during installation- ⚠️ Check "Add Python to PATH" during installation



### Installing Redis### Installing Redis



Redis is required for caching audio data during processing.Redis is required for caching audio data during processing.



**macOS:****macOS:**

```bash```bash

brew install redisbrew install redis

brew services start redisbrew services start redis

``````



**Ubuntu/Debian:****Ubuntu/Debian:**

```bash```bash

sudo apt-get install redis-serversudo apt-get install redis-server

sudo service redis-server startsudo service redis-server start

``````



**Windows:****Windows:**

- Download from [GitHub Releases](https://github.com/microsoftarchive/redis/releases)- Download from [GitHub Releases](https://github.com/microsoftarchive/redis/releases)

- Or use WSL (Windows Subsystem for Linux)- Or use WSL (Windows Subsystem for Linux)



**Verify Redis:****Verify Redis:**

```bash```bash

redis-cli pingredis-cli ping

# Should return: PONG# Should return: PONG

``````



------



## Automated Installation## Automated Installation



### Linux/macOS### Linux/macOS



> **Note:** The script automatically detects and supports pyenv. See [PYENV_GUIDE.md](PYENV_GUIDE.md) if you encounter issues.> **Note:** The script automatically detects and supports pyenv. See [PYENV_GUIDE.md](PYENV_GUIDE.md) if you encounter issues.



```bash```bash

./setup.sh./setup.sh

``````



The script will:The script will:

- ✅ Check for Python 3.13+- ✅ Check for Python 3.13+

- ✅ Initialize pyenv if present- ✅ Initialize pyenv if present

- ✅ Create virtual environment- ✅ Create virtual environment

- ✅ Install all dependencies- ✅ Install all dependencies

- ✅ Show next steps- ✅ Show next steps



### Windows### Windows



```cmd```cmd

setup.batsetup.bat

``````



Or double-click `setup.bat` in File Explorer.Or double-click `setup.bat` in File Explorer.



------



## Manual Installation## Manual Installation



### 1. Create Virtual Environment### 1. Create Virtual Environment



```bash```bash

# Linux/macOS# Linux/macOS

python3.13 -m venv venvpython3.13 -m venv venv

source venv/bin/activatesource venv/bin/activate



# Windows (Command Prompt)# Windows (Command Prompt)

python -m venv venvpython -m venv venv

venv\Scripts\activate.batvenv\Scripts\activate.bat



# Windows (PowerShell)# Windows (PowerShell)

python -m venv venvpython -m venv venv

venv\Scripts\Activate.ps1venv\Scripts\Activate.ps1

``````



### 2. Install Dependencies### 2. Install Dependencies



```bash```bash

pip install --upgrade pippip install --upgrade pip

pip install -r requirements.txtpip install -r requirements.txt

``````



------



## Configuration## Configuration



### 1. Create Environment File### 1. Create Environment File



```bash```bash

# Linux/macOS# Linux/macOS

cp .env.example .envcp .env.example .env



# Windows# Windows

copy .env.example .envcopy .env.example .env

``````



### 2. Edit `.env` File### 2. Edit `.env` File



Add your API keys:Add your API keys:



```env```env

# API Keys (Required)# API Keys (Required)

DEEPGRAM_API_KEY=your_deepgram_api_key_hereDEEPGRAM_API_KEY=your_deepgram_api_key_here

DEEPL_API_KEY=your_deepl_api_key_hereDEEPL_API_KEY=your_deepl_api_key_here

ELEVENLABS_API_KEY=your_elevenlabs_api_key_hereELEVENLABS_API_KEY=your_elevenlabs_api_key_here



# Redis Configuration# Redis Configuration

REDIS_HOST=localhostREDIS_HOST=localhost

REDIS_PORT=6379REDIS_PORT=6379

REDIS_DB=0

REDIS_PASSWORD=""# Logging

REDIS_CACHE_TTL=3600LOG_LEVEL=INFO

DEBUG=False

# Audio Processing```

MAX_AUDIO_SIZE_MB=25

---

# Logging

LOG_LEVEL=INFO## Running the Application

DEBUG=False

```### Development Mode



---```bash

# Activate virtual environment first

## Running the Application# Linux/macOS: source venv/bin/activate

# Windows: venv\Scripts\activate

### Development Mode

uvicorn app.main:app --reload

```bash```

# Activate virtual environment first

# Linux/macOS: source venv/bin/activate**Access:** http://localhost:8000

# Windows: venv\Scripts\activate

### Production Mode

uvicorn app.main:app --reload

``````bash

uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4

**Access:** http://localhost:8000```



### Production Mode### Production Deployment



```bash**Using systemd (Linux):**

uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4

```Create `/etc/systemd/system/emotion-ai.service`:



### Production Deployment```ini

[Unit]

**Using systemd (Linux):**Description=FastAPI Speech Translation API

After=network.target

Create `/etc/systemd/system/emotion-ai.service`:

[Service]

```iniType=simple

[Unit]User=www-data

Description=FastAPI Speech Translation APIWorkingDirectory=/opt/emotion-ai

After=network.targetEnvironment="PATH=/opt/emotion-ai/venv/bin"

ExecStart=/opt/emotion-ai/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000

[Service]Restart=always

Type=simple

User=www-data[Install]

WorkingDirectory=/opt/emotion-aiWantedBy=multi-user.target

Environment="PATH=/opt/emotion-ai/venv/bin"```

ExecStart=/opt/emotion-ai/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000

Restart=alwaysEnable and start:

```bash

[Install]sudo systemctl enable emotion-ai

WantedBy=multi-user.targetsudo systemctl start emotion-ai

``````



Enable and start:---

```bash

sudo systemctl enable emotion-ai## Verification

sudo systemctl start emotion-ai

```### 1. Check API Health



---```bash

curl http://localhost:8000/health

## Verification```



### 1. Check API Health**Expected:**

```json

```bash{

curl http://localhost:8000/health  "status": "healthy",

```  "redis": "connected"

}

**Expected:**```

```json

{### 2. View API Documentation

  "status": "healthy",

  "redis": "connected"- **Swagger UI**: http://localhost:8000/docs

}- **ReDoc**: http://localhost:8000/redoc

```

### 3. Test the API

### 2. View API Documentation

```bash

- **Swagger UI**: http://localhost:8000/docscurl -X POST "http://localhost:8000/api/process-audio" \

- **ReDoc**: http://localhost:8000/redoc  -F "audio=@your_audio.wav" \

  -o response.json

### 3. Test the API```



```bash---

curl -X POST "http://localhost:8000/api/process-audio" \

  -F "audio=@your_audio.wav" \## Troubleshooting

  -o response.json

```### pyenv Issues



---**Error:** `pyenv: python3.13: command not found`



## Troubleshooting**Solution:**

```bash

### pyenv Issues# Initialize pyenv

export PYENV_ROOT="$HOME/.pyenv"

**Error:** `pyenv: python3.13: command not found`export PATH="$PYENV_ROOT/bin:$PATH"

eval "$(pyenv init --path)"

**Solution:**eval "$(pyenv init -)"

```bash

# Initialize pyenv# Set version

export PYENV_ROOT="$HOME/.pyenv"pyenv local 3.13.0

export PATH="$PYENV_ROOT/bin:$PATH"

eval "$(pyenv init --path)"# Run setup again

eval "$(pyenv init -)"./setup.sh

```

# Set version

pyenv local 3.13.0> See [PYENV_GUIDE.md](PYENV_GUIDE.md) for complete pyenv documentation



# Run setup again### Python Not Found

./setup.sh

```**Error:** `Python 3.13 or higher is required but not found!`



> See [PYENV_GUIDE.md](PYENV_GUIDE.md) for complete pyenv documentation**Solutions:**

- Install with pyenv: `pyenv install 3.13.0 && pyenv global 3.13.0`

### Python Not Found- Install from [python.org](https://www.python.org/downloads/)

- Ensure Python is in PATH (Windows)

**Error:** `Python 3.13 or higher is required but not found!`

### Redis Connection Failed

**Solutions:**

- Install with pyenv: `pyenv install 3.13.0 && pyenv global 3.13.0`**Error:** `Connection to Redis failed`

- Install from [python.org](https://www.python.org/downloads/)

- Ensure Python is in PATH (Windows)**Solutions:**

1. Check if running: `redis-cli ping`

### Redis Connection Failed2. Start Redis:

   - macOS: `brew services start redis`

**Error:** `Connection to Redis failed`   - Linux: `sudo service redis-server start`

   - Windows: Run `redis-server.exe`

**Solutions:**

1. Check if running: `redis-cli ping`### Permission Denied (setup.sh)

2. Start Redis:

   - macOS: `brew services start redis`**Error:** `Permission denied: './setup.sh'`

   - Linux: `sudo service redis-server start`

   - Windows: Run `redis-server.exe`**Solution:**

```bash

### FFmpeg or MediaInfo Not Foundchmod +x setup.sh

./setup.sh

**Error:** `FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'````



**Solutions:**### Virtual Environment Issues

- Ubuntu/Debian: `sudo apt-get install ffmpeg mediainfo`

- macOS: `brew install ffmpeg media-info`**Solution:**

- Windows: Download and install from respective websites```bash

# Remove and recreate

### Permission Denied (setup.sh)rm -rf venv

python3.13 -m venv venv

**Error:** `Permission denied: './setup.sh'`source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt

**Solution:**```

```bash

chmod +x setup.sh### OpenSmile Installation Failed

./setup.sh

```**Note:** OpenSmile is optional. The API will use mock emotion detection if unavailable.



### Virtual Environment Issues**For full functionality:**

- macOS: `xcode-select --install`

**Solution:**- Linux: `sudo apt-get install build-essential`

```bash- Windows: Install Visual Studio Build Tools

# Remove and recreate

rm -rf venv### Invalid API Keys

python3.13 -m venv venv

source venv/bin/activate  # or venv\Scripts\activate on Windows**Solutions:**

pip install -r requirements.txt- Verify keys in `.env` (no extra spaces or quotes)

```- Check API quotas and remaining credits

- Ensure keys are active in respective dashboards

### OpenSmile Installation Failed

---

**Note:** OpenSmile is optional. The API will use mock emotion detection if unavailable.

## Additional Resources

**For full functionality:**

- macOS: `xcode-select --install`- **[README.md](README.md)** - Project overview and quick reference

- Linux: `sudo apt-get install build-essential`- **[API_REFERENCE.md](API_REFERENCE.md)** - Complete API documentation  

- Windows: Install Visual Studio Build Tools- **[PYENV_GUIDE.md](PYENV_GUIDE.md)** - Python version management

- **[Postman Collection](postman_collection.json)** - API testing

### Invalid API Keys

---

**Solutions:**

- Verify keys in `.env` (no extra spaces or quotes)## Need Help?

- Check API quotas and remaining credits

- Ensure keys are active in respective dashboards1. Check logs for error messages

2. Verify all prerequisites are installed

---3. Ensure API keys are correctly configured

4. Test Redis: `redis-cli ping`

## Additional Resources5. Check Python version: `python --version`



- **[README.md](README.md)** - Project overview and quick referenceFor API service documentation:

- **[API_REFERENCE.md](API_REFERENCE.md)** - Complete API documentation  - [Deepgram Docs](https://developers.deepgram.com/)

- **[PYENV_GUIDE.md](PYENV_GUIDE.md)** - Python version management- [DeepL API Docs](https://www.deepl.com/docs-api)

- **[Postman Collection](postman_collection.json)** - API testing- [ElevenLabs Docs](https://docs.elevenlabs.io/)



---

## Need Help?

1. Check logs for error messages
2. Verify all prerequisites are installed
3. Ensure API keys are correctly configured
4. Test Redis: `redis-cli ping`
5. Test FFmpeg: `ffmpeg -version`
6. Test MediaInfo: `mediainfo --version`
7. Check Python version: `python --version`

For API service documentation:
- [Deepgram Docs](https://developers.deepgram.com/)
- [DeepL API Docs](https://www.deepl.com/docs-api)
- [ElevenLabs Docs](https://docs.elevenlabs.io/)
