# FastAPI Speech Translation API

Real-time multilingual speech translation with emotion preservation.

## Prerequisites

- Python 3.10+
- API keys: [Deepgram](https://console.deepgram.com/), [DeepL](https://www.deepl.com/pro-api), [ElevenLabs](https://elevenlabs.io/)

## Installation

1. **Create and activate virtual environment:**

   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # Windows PowerShell
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**

   ```bash
   Copy-Item .env.example .env  # Windows
   ```

   Edit `.env` and add your API keys:

   ```env
   DEEPGRAM_API_KEY="your-key-here"
   DEEPL_API_KEY="your-key-here"
   ELEVENLABS_API_KEY="your-key-here"
   ```

4. **Run the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

API will be available at: http://localhost:8000

## API Documentation

- Swagger UI: http://localhost:8000/docs

## Running with Frontend

**Terminal 1 - Backend:**

```bash
cd d:\My\fast-api-tmp
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

**Terminal 2 - Frontend:**

```bash
cd d:\My\fe-ai-text-and-speech
npm run dev
```

Access at: http://localhost:3000
