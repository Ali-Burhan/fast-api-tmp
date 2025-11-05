# 🚀 Quick Start Guide

Get the Speech Translation API running in under 5 minutes!

## Prerequisites Checklist

- [ ] Python 3.10+ installed
- [ ] Redis running (Docker recommended)
- [ ] API keys ready:
  - [ ] Deepgram API key
  - [ ] DeepL API key
  - [ ] ElevenLabs API key

---

## Option 1: Docker (Recommended) 🐳

### Step 1: Get API Keys

```bash
# Add your API keys to .env file
cat > .env << EOF
DEEPGRAM_API_KEY=your_deepgram_key
DEEPL_API_KEY=your_deepl_key
ELEVENLABS_API_KEY=your_elevenlabs_key
EOF
```

### Step 2: Start with Docker Compose

```bash
# Start everything (API + Redis)
docker-compose up -d

# Check logs
docker-compose logs -f api

# Test the API
curl http://localhost:8000/health
```

### Step 3: Stop

```bash
docker-compose down
```

---

## Option 2: Local Development 💻

### Step 1: Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### Step 2: Start Redis

```bash
# Using Docker (easiest)
docker run -d -p 6379:6379 redis:alpine

# OR install Redis locally:
# Mac: brew install redis && brew services start redis
# Ubuntu: sudo apt install redis-server && sudo service redis-server start
# Windows: Download from https://redis.io/docs/getting-started/installation/
```

### Step 3: Configure Environment

```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your API keys
# Required: DEEPGRAM_API_KEY, DEEPL_API_KEY, ELEVENLABS_API_KEY
```

### Step 4: Run the API

```bash
# Development mode (with auto-reload)
uvicorn app.main:app --reload

# Production mode
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## 🧪 Test the API

### 1. Check Health

```bash
curl http://localhost:8000/health
```

**Expected:** `{"status":"healthy","redis":"connected"}`

### 2. View API Documentation

Open in browser: http://localhost:8000/docs

### 3. Process Sample Audio

```bash
# Download a sample audio (or use your own)
curl -o sample.wav "https://www2.cs.uic.edu/~i101/SoundFiles/gettysburg.wav"

# Process it
curl -X POST "http://localhost:8000/api/process-audio" \
  -F "audio=@sample.wav" \
  | jq .
```

### 4. Test Individual Services

**Transcribe:**
```bash
curl -X POST "http://localhost:8000/api/speech-to-text/transcribe" \
  -F "audio=@sample.wav" | jq .
```

**Detect Emotion:**
```bash
curl -X POST "http://localhost:8000/api/emotion/detect" \
  -F "audio=@sample.wav" | jq .
```

**Translate:**
```bash
curl -X POST "http://localhost:8000/api/translation/translate" \
  -H "Content-Type: application/json" \
  -d '{"text":"Hello world","source_lang":"en"}' | jq .
```

---

## 📝 Common Issues

### Issue: "Connection to Redis failed"

**Solution:**
```bash
# Check if Redis is running
redis-cli ping

# Start Redis
docker run -d -p 6379:6379 redis:alpine
```

### Issue: "Module 'opensmile' not found"

**Solution:**
```bash
# OpenSmile is optional - API will use mock emotion detection
# To install it:
pip install opensmile
```

### Issue: "Invalid API key"

**Solution:**
- Double-check API keys in `.env`
- Ensure no extra spaces or quotes
- Verify keys are active in respective dashboards

### Issue: "Port 8000 already in use"

**Solution:**
```bash
# Use a different port
uvicorn app.main:app --port 8001

# Or find and kill the process using port 8000
# Mac/Linux:
lsof -ti:8000 | xargs kill -9
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

---

## 🎯 Next Steps

1. **Test Different Audio Files**: Try various languages and emotions
2. **Explore API Docs**: http://localhost:8000/docs
3. **Import Postman Collection**: Use `postman_collection.json`
4. **Read Full Documentation**: See `README.md`
5. **Check cURL Examples**: See `CURL_EXAMPLES.md`

---

## 📊 Performance Tips

- Use MP3 or WAV for best results
- Keep audio files under 25MB
- Use Redis caching to speed up processing
- Set `DEBUG=False` in production

---

## 🆘 Get Help

- Check logs: `docker-compose logs api` (Docker) or terminal output (local)
- Visit API docs: http://localhost:8000/docs
- Review error messages in API responses
- Ensure all API keys are valid and have sufficient credits

---

**Ready to go!** 🎉

Now process your first audio file:

```bash
curl -X POST "http://localhost:8000/api/process-audio" \
  -F "audio=@your_audio.wav" \
  -o result.json

# View results
cat result.json | jq .

# Extract and play audio
cat result.json | jq -r '.audio_base64' | base64 -d > output.mp3
```


