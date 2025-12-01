# 🛠️ Setup Guide# 🛠️ Installation Guide# 🛠️ Installation Guide



Complete installation instructions for the FastAPI Speech Translation API.



> **Quick Start:** Run `./setup.sh` (Linux/Mac) or `setup.bat` (Windows) for automated setup.Complete installation instructions for the FastAPI Speech Translation API.Complete installation instructions for the FastAPI Speech Translation API.



---



## Table of Contents> **Quick Start:** If you just want to get started quickly, run `./setup.sh` (Linux/Mac) or `setup.bat` (Windows)> **Quick Start:** If you just want to get started quickly, run `./setup.sh` (Linux/Mac) or `setup.bat` (Windows)



1. [Prerequisites](#prerequisites)

2. [Automated Installation](#automated-installation)

3. [Manual Installation](#manual-installation)------

4. [Configuration](#configuration)

5. [Running the Application](#running-the-application)

6. [Verification](#verification)

7. [Troubleshooting](#troubleshooting)## Table of Contents## Table of Contents



---



## Prerequisites1. [Prerequisites](#prerequisites)1. [Prerequisites](#prerequisites)



### Required2. [Automated Installation](#automated-installation)2. [Automated Installation](#automated-installation)



1. **Python 3.13+** - [Installation instructions below](#installing-python-313)3. [Manual Installation](#manual-installation)3. [Manual Installation](#manual-installation)

2. **Redis server** - For caching audio data

3. **FFmpeg** - For audio format conversion4. [Configuration](#configuration)4. [Configuration](#configuration)

   - Ubuntu/Debian: `sudo apt-get install ffmpeg`

   - macOS: `brew install ffmpeg`5. [Running the Application](#running-the-application)5. [Running the Application](#running-the-application)

   - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

4. **MediaInfo** - For audio file metadata6. [Verification](#verification)6. [Verification](#verification)

   - Ubuntu/Debian: `sudo apt-get install mediainfo`

   - macOS: `brew install media-info`7. [Troubleshooting](#troubleshooting)7. [Troubleshooting](#troubleshooting)

   - Windows: `choco install mediainfo`

5. **API Keys:**

   - [Deepgram](https://console.deepgram.com/) - Speech-to-Text

   - [DeepL](https://www.deepl.com/pro-api) - Translation------

   - [ElevenLabs](https://elevenlabs.io/) - Text-to-Speech



### Installing Python 3.13

## Prerequisites## Prerequisites

**Using pyenv (Recommended):**

```bash

# Install pyenv

curl https://pyenv.run | bash### Required### Required



# Install Python 3.13

pyenv install 3.13.9

pyenv global 3.13.91. **Python 3.13+** - [Installation instructions below](#installing-python-313)1. **Python 3.13+** - [Installation instructions below](#installing-python-313)

```

2. **Redis server** - For caching audio data2. **Redis server** - For caching audio data

> See [PYENV_GUIDE.md](PYENV_GUIDE.md) for detailed pyenv instructions

3. **FFmpeg** - For audio format conversion3. **FFmpeg** - For audio format conversion

**macOS:**

```bash   - Ubuntu/Debian: `sudo apt-get install ffmpeg`   - Ubuntu/Debian: `sudo apt-get install ffmpeg`

brew install python@3.13

```   - macOS: `brew install ffmpeg`   - macOS: `brew install ffmpeg`



**Ubuntu/Debian:**   - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html)   - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

```bash

sudo apt update4. **MediaInfo** - For audio file metadata4. **MediaInfo** - For audio file metadata

sudo apt install python3.13 python3.13-venv python3.13-dev

```   - Ubuntu/Debian: `sudo apt-get install mediainfo`   - Ubuntu/Debian: `sudo apt-get install mediainfo`



**Windows:**   - macOS: `brew install media-info`   - macOS: `brew install media-info`

- Download from [python.org](https://www.python.org/downloads/)

- ⚠️ Check "Add Python to PATH" during installation   - Windows: `choco install mediainfo`   - Windows: `choco install mediainfo`



### Installing Redis5. **API Keys:**5. **API Keys:**



Redis is required for caching audio data during processing.   - [Deepgram](https://console.deepgram.com/) - Speech-to-Text   - [Deepgram](https://console.deepgram.com/) - Speech-to-Text



**macOS:**   - [DeepL](https://www.deepl.com/pro-api) - Translation   - [DeepL](https://www.deepl.com/pro-api) - Translation

```bash

brew install redis   - [ElevenLabs](https://elevenlabs.io/) - Text-to-Speech   - [ElevenLabs](https://elevenlabs.io/) - Text-to-Speech

brew services start redis

```



**Ubuntu/Debian:**### Installing Python 3.13### Installing Python 3.13

```bash

sudo apt-get install redis-server

sudo service redis-server start

```**Using pyenv (Recommended):****Using pyenv (Recommended):**



**Windows:**```bash```bash

- Download from [GitHub Releases](https://github.com/microsoftarchive/redis/releases)

- Or use WSL (Windows Subsystem for Linux)# Install pyenv# Install pyenv



**Verify Redis:**curl https://pyenv.run | bashcurl https://pyenv.run | bash

```bash

redis-cli ping

# Should return: PONG

```# Install Python 3.13# Install Python 3.13



---pyenv install 3.13.0pyenv install 3.13.0



## Automated Installationpyenv global 3.13.0pyenv global 3.13.0



### Linux/macOS``````



> **Note:** The script automatically detects and supports pyenv. See [PYENV_GUIDE.md](PYENV_GUIDE.md) if you encounter issues.> See [PYENV_GUIDE.md](PYENV_GUIDE.md) for detailed pyenv instructions> See [PYENV_GUIDE.md](PYENV_GUIDE.md) for detailed pyenv instructions



```bash

# Make script executable

chmod +x setup.sh**macOS:****macOS:**



# Run setup```bash```bash

./setup.sh

```brew install python@3.13brew install python@3.13



**What the script does:**``````

1. ✅ Checks Python 3.13+ is installed

2. ✅ Creates virtual environment

3. ✅ Installs Python dependencies

4. ✅ Creates `.env` from template**Ubuntu/Debian:****Ubuntu/Debian:**

5. ✅ Verifies Redis connection

6. ✅ Checks FFmpeg and MediaInfo```bash```bash

7. ✅ Tests the installation

sudo apt updatesudo apt update

### Windows

sudo apt install python3.13 python3.13-venv python3.13-devsudo apt install python3.13 python3.13-venv python3.13-dev

```cmd

setup.bat``````

```



**What the script does:**

1. ✅ Checks Python 3.13+ is installed**Windows:****Windows:**

2. ✅ Creates virtual environment

3. ✅ Installs Python dependencies- Download from [python.org](https://www.python.org/downloads/)- Download from [python.org](https://www.python.org/downloads/)

4. ✅ Creates `.env` from template

5. ✅ Prompts for Redis setup- ⚠️ Check "Add Python to PATH" during installation- ⚠️ Check "Add Python to PATH" during installation



---



## Manual Installation### Installing Redis### Installing Redis



### Step 1: Clone Repository



```bashRedis is required for caching audio data during processing.Redis is required for caching audio data during processing.

git clone <repository-url>

cd fast-api-tmp

```

**macOS:****macOS:**

### Step 2: Create Virtual Environment

```bash```bash

**Linux/macOS:**

```bashbrew install redisbrew install redis

python3.13 -m venv venv

source venv/bin/activatebrew services start redisbrew services start redis

```

``````

**Windows:**

```cmd

python -m venv venv

venv\Scripts\activate**Ubuntu/Debian:****Ubuntu/Debian:**

```

```bash```bash

### Step 3: Install Dependencies

sudo apt-get install redis-serversudo apt-get install redis-server

```bash

pip install --upgrade pipsudo service redis-server startsudo service redis-server start

pip install -r requirements.txt

`````````



### Step 4: Install System Dependencies



**Linux (Ubuntu/Debian):****Windows:****Windows:**

```bash

sudo apt-get update- Download from [GitHub Releases](https://github.com/microsoftarchive/redis/releases)- Download from [GitHub Releases](https://github.com/microsoftarchive/redis/releases)

sudo apt-get install ffmpeg mediainfo redis-server

sudo service redis-server start- Or use WSL (Windows Subsystem for Linux)- Or use WSL (Windows Subsystem for Linux)

```



**macOS:**

```bash**Verify Redis:****Verify Redis:**

brew install ffmpeg media-info redis

brew services start redis```bash```bash

```

redis-cli pingredis-cli ping

**Windows:**

- FFmpeg: Download from [ffmpeg.org](https://ffmpeg.org/download.html)# Should return: PONG# Should return: PONG

- MediaInfo: `choco install mediainfo` or download from [mediaarea.net](https://mediaarea.net/en/MediaInfo)

- Redis: Use WSL or download from [GitHub](https://github.com/microsoftarchive/redis/releases)``````



---



## Configuration------



### Step 1: Create Environment File



```bash## Automated Installation## Automated Installation

# Linux/macOS

cp .env.example .env



# Windows### Linux/macOS### Linux/macOS

copy .env.example .env

```



### Step 2: Add API Keys> **Note:** The script automatically detects and supports pyenv. See [PYENV_GUIDE.md](PYENV_GUIDE.md) if you encounter issues.> **Note:** The script automatically detects and supports pyenv. See [PYENV_GUIDE.md](PYENV_GUIDE.md) if you encounter issues.



Edit `.env` file and add your API keys:



```env```bash```bash

# Required API Keys

DEEPGRAM_API_KEY=your_deepgram_key_here./setup.sh./setup.sh

DEEPL_API_KEY=your_deepl_key_here

ELEVENLABS_API_KEY=your_elevenlabs_key_here``````



# Redis Configuration

REDIS_HOST=localhost

REDIS_PORT=6379The script will:The script will:

REDIS_DB=0

REDIS_PASSWORD=- ✅ Check for Python 3.13+- ✅ Check for Python 3.13+

REDIS_CACHE_TTL=3600

- ✅ Initialize pyenv if present- ✅ Initialize pyenv if present

# Audio Processing

MAX_AUDIO_SIZE_MB=25- ✅ Create virtual environment- ✅ Create virtual environment



# Logging- ✅ Install all dependencies- ✅ Install all dependencies

LOG_LEVEL=INFO

DEBUG=False- ✅ Show next steps- ✅ Show next steps

```



### Step 3: Get API Keys

### Windows### Windows

1. **Deepgram** (Speech-to-Text)

   - Sign up: https://console.deepgram.com/

   - Create API key in dashboard

   - Free tier: 45,000 minutes```cmd```cmd



2. **DeepL** (Translation)setup.batsetup.bat

   - Sign up: https://www.deepl.com/pro-api

   - Get API key from account``````

   - Free tier: 500,000 characters/month



3. **ElevenLabs** (Text-to-Speech)

   - Sign up: https://elevenlabs.io/Or double-click `setup.bat` in File Explorer.Or double-click `setup.bat` in File Explorer.

   - Get API key from profile

   - Free tier: 10,000 characters/month



---------



## Running the Application



### Development Mode## Manual Installation## Manual Installation



```bash

# Activate virtual environment first

source venv/bin/activate  # Linux/macOS### 1. Create Virtual Environment### 1. Create Virtual Environment

# venv\Scripts\activate    # Windows



# Run with auto-reload

uvicorn app.main:app --reload```bash```bash

```

# Linux/macOS# Linux/macOS

**Access the API:**

- API: http://localhost:8000python3.13 -m venv venvpython3.13 -m venv venv

- Swagger UI: http://localhost:8000/docs

- ReDoc: http://localhost:8000/redocsource venv/bin/activatesource venv/bin/activate



### Production Mode



```bash# Windows (Command Prompt)# Windows (Command Prompt)

# Run without auto-reload

uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4python -m venv venvpython -m venv venv

```

venv\Scripts\activate.batvenv\Scripts\activate.bat

### Background Service (Linux)



Create `/etc/systemd/system/emotion-ai.service`:

# Windows (PowerShell)# Windows (PowerShell)

```ini

[Unit]python -m venv venvpython -m venv venv

Description=FastAPI Speech Translation API

After=network.target redis.servicevenv\Scripts\Activate.ps1venv\Scripts\Activate.ps1



[Service]``````

Type=simple

User=your-username

WorkingDirectory=/path/to/fast-api-tmp

Environment="PATH=/path/to/fast-api-tmp/venv/bin"### 2. Install Dependencies### 2. Install Dependencies

ExecStart=/path/to/fast-api-tmp/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000

Restart=always



[Install]```bash```bash

WantedBy=multi-user.target

```pip install --upgrade pippip install --upgrade pip



Enable and start:pip install -r requirements.txtpip install -r requirements.txt

```bash

sudo systemctl daemon-reload``````

sudo systemctl enable emotion-ai

sudo systemctl start emotion-ai

sudo systemctl status emotion-ai

```------



---



## Verification## Configuration## Configuration



### Test Health Endpoint



```bash### 1. Create Environment File### 1. Create Environment File

curl http://localhost:8000/health

```



**Expected response:**```bash```bash

```json

{# Linux/macOS# Linux/macOS

  "status": "healthy"

}cp .env.example .envcp .env.example .env

```



### Test Audio Processing

# Windows# Windows

```bash

# Create test audio or use your owncopy .env.example .envcopy .env.example .env

curl -X POST "http://localhost:8000/api/process-audio" \

  -F "audio=@test_audio.wav" \``````

  -F "target_language=es" \

  -o response.json



# Check response### 2. Edit `.env` File### 2. Edit `.env` File

cat response.json

```



### Verify ServicesAdd your API keys:Add your API keys:



**Python Version:**

```bash

python --version```env```env

# Should show: Python 3.13.x

```# API Keys (Required)# API Keys (Required)



**Redis:**DEEPGRAM_API_KEY=your_deepgram_api_key_hereDEEPGRAM_API_KEY=your_deepgram_api_key_here

```bash

redis-cli pingDEEPL_API_KEY=your_deepl_api_key_hereDEEPL_API_KEY=your_deepl_api_key_here

# Should return: PONG

```ELEVENLABS_API_KEY=your_elevenlabs_api_key_hereELEVENLABS_API_KEY=your_elevenlabs_api_key_here



**FFmpeg:**

```bash

ffmpeg -version# Redis Configuration# Redis Configuration

# Should show FFmpeg version info

```REDIS_HOST=localhostREDIS_HOST=localhost



**MediaInfo:**REDIS_PORT=6379REDIS_PORT=6379

```bash

mediainfo --versionREDIS_DB=0

# Should show MediaInfo version

```REDIS_PASSWORD=""# Logging



---REDIS_CACHE_TTL=3600LOG_LEVEL=INFO



## TroubleshootingDEBUG=False



### Python Version Issues# Audio Processing```



**Problem:** `python: command not found` or wrong versionMAX_AUDIO_SIZE_MB=25



**Solution:**---

```bash

# Use python3.13 explicitly# Logging

python3.13 --version

LOG_LEVEL=INFO## Running the Application

# Or set up pyenv (recommended)

# See PYENV_GUIDE.md for detailed instructionsDEBUG=False

```

```### Development Mode

### Redis Connection Failed



**Problem:** `ConnectionError: Error 111 connecting to localhost:6379`

---```bash

**Solution:**

```bash# Activate virtual environment first

# Check if Redis is running

redis-cli ping## Running the Application# Linux/macOS: source venv/bin/activate



# Start Redis if not running# Windows: venv\Scripts\activate

# Linux

sudo service redis-server start### Development Mode



# macOSuvicorn app.main:app --reload

brew services start redis

```bash```

# Check Redis logs

# Linux: /var/log/redis/redis-server.log# Activate virtual environment first

# macOS: /usr/local/var/log/redis.log

```# Linux/macOS: source venv/bin/activate**Access:** http://localhost:8000



### FFmpeg Not Found# Windows: venv\Scripts\activate



**Problem:** `FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'`### Production Mode



**Solution:**uvicorn app.main:app --reload

```bash

# Install FFmpeg``````bash

# Ubuntu/Debian

sudo apt-get install ffmpeguvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4



# macOS**Access:** http://localhost:8000```

brew install ffmpeg



# Verify installation

which ffmpeg### Production Mode### Production Deployment

ffmpeg -version

```



### MediaInfo Not Found```bash**Using systemd (Linux):**



**Problem:** `FileNotFoundError: mediainfo cannot be found`uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4



**Solution:**```Create `/etc/systemd/system/emotion-ai.service`:

```bash

# Install MediaInfo

# Ubuntu/Debian

sudo apt-get install mediainfo### Production Deployment```ini



# macOS[Unit]

brew install media-info

**Using systemd (Linux):**Description=FastAPI Speech Translation API

# Verify installation

which mediainfoAfter=network.target

mediainfo --version

```Create `/etc/systemd/system/emotion-ai.service`:



### Permission Denied on setup.sh[Service]



**Problem:** `Permission denied: ./setup.sh````iniType=simple



**Solution:**[Unit]User=www-data

```bash

chmod +x setup.shDescription=FastAPI Speech Translation APIWorkingDirectory=/opt/emotion-ai

./setup.sh

```After=network.targetEnvironment="PATH=/opt/emotion-ai/venv/bin"



### Virtual Environment IssuesExecStart=/opt/emotion-ai/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000



**Problem:** Cannot create or activate virtual environment[Service]Restart=always



**Solution:**Type=simple

```bash

# Remove and recreateUser=www-data[Install]

rm -rf venv

python3.13 -m venv venvWorkingDirectory=/opt/emotion-aiWantedBy=multi-user.target

source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txtEnvironment="PATH=/opt/emotion-ai/venv/bin"```

```

ExecStart=/opt/emotion-ai/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000

### OpenSmile Installation Failed

Restart=alwaysEnable and start:

**Note:** OpenSmile is optional. The API will use mock emotion detection if unavailable.

```bash

**For full functionality:**

- macOS: `xcode-select --install`[Install]sudo systemctl enable emotion-ai

- Linux: `sudo apt-get install build-essential`

- Windows: Install Visual Studio Build ToolsWantedBy=multi-user.targetsudo systemctl start emotion-ai



### Invalid API Keys``````



**Solutions:**

- Verify keys in `.env` (no extra spaces or quotes)

- Check API quotas and remaining creditsEnable and start:---

- Ensure keys are active in respective dashboards

```bash

---

sudo systemctl enable emotion-ai## Verification

## Additional Resources

sudo systemctl start emotion-ai

- **[README.md](README.md)** - Project overview and quick reference

- **[API_REFERENCE.md](API_REFERENCE.md)** - Complete API documentation  ```### 1. Check API Health

- **[PYENV_GUIDE.md](PYENV_GUIDE.md)** - Python version management

- **[Postman Collection](postman_collection.json)** - API testing



------```bash



## Need Help?curl http://localhost:8000/health



1. Check logs for error messages## Verification```

2. Verify all prerequisites are installed

3. Ensure API keys are correctly configured

4. Test Redis: `redis-cli ping`

5. Test FFmpeg: `ffmpeg -version`### 1. Check API Health**Expected:**

6. Test MediaInfo: `mediainfo --version`

7. Check Python version: `python --version````json



For API service documentation:```bash{

- [Deepgram Docs](https://developers.deepgram.com/)

- [DeepL API Docs](https://www.deepl.com/docs-api)curl http://localhost:8000/health  "status": "healthy",

- [ElevenLabs Docs](https://docs.elevenlabs.io/)

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
