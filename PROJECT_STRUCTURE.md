# 📁 Project Structure

Complete overview of the Speech Translation API codebase.

```
fast-api-tmp/
│
├── app/                                    # Main application package
│   ├── __init__.py
│   ├── main.py                            # FastAPI app & orchestration logic
│   │
│   ├── core/                              # Core infrastructure
│   │   ├── __init__.py
│   │   ├── config.py                      # Configuration & environment settings
│   │   ├── redis_client.py                # Redis caching client
│   │   └── utils.py                       # Utility functions
│   │
│   └── modules/                           # Feature modules (modular monolith)
│       ├── __init__.py
│       │
│       ├── speech_to_text/                # Deepgram integration
│       │   ├── __init__.py
│       │   ├── service.py                 # Transcription service
│       │   └── router.py                  # API endpoints
│       │
│       ├── emotion_detection/             # OpenSmile integration
│       │   ├── __init__.py
│       │   ├── service.py                 # Emotion detection service
│       │   └── router.py                  # API endpoints
│       │
│       ├── translation/                   # DeepL integration
│       │   ├── __init__.py
│       │   ├── service.py                 # Translation service
│       │   └── router.py                  # API endpoints
│       │
│       └── text_to_speech/                # ElevenLabs integration
│           ├── __init__.py
│           ├── service.py                 # TTS service
│           └── router.py                  # API endpoints
│
├── tests/                                 # Unit tests
│   ├── conftest.py                        # Pytest configuration & fixtures
│   ├── test_main.py                       # Main API endpoint tests
│   ├── test_services.py                   # Service layer tests
│   └── test_utils.py                      # Utility function tests
│
├── requirements.txt                       # Python dependencies
├── .env.example                           # Example environment variables
├── .gitignore                             # Git ignore rules
├── .dockerignore                          # Docker ignore rules
│
├── Dockerfile                             # Docker image definition
├── docker-compose.yml                     # Multi-container setup (API + Redis)
│
├── README.md                              # Main documentation
├── QUICKSTART.md                          # Quick start guide
├── CURL_EXAMPLES.md                       # cURL command examples
├── PROJECT_STRUCTURE.md                   # This file
├── postman_collection.json                # Postman API collection
│
├── pytest.ini                             # Pytest configuration
├── mypy.ini                               # Type checking configuration
├── alembic.ini                            # Database migrations (optional)
│
├── CHANGELOG.md                           # Version history
├── CONTRIBUTING.md                        # Contribution guidelines
├── LICENSE                                # License information
└── Makefile                               # Build automation (optional)
```

---

## 📦 Module Breakdown

### **Core (`app/core/`)**

**Purpose**: Application-wide infrastructure and utilities.

| File | Purpose |
|------|---------|
| `config.py` | Environment configuration using Pydantic Settings |
| `redis_client.py` | Async Redis client for caching audio files |
| `utils.py` | Helper functions (validation, key generation, emotion mapping) |

---

### **Modules (`app/modules/`)**

**Architecture**: Modular Monolith - each module is self-contained with service + router.

#### 1. **Speech-to-Text** (`speech_to_text/`)

- **Service**: Deepgram API integration for transcription
- **Features**: 
  - Auto language detection (English/Spanish)
  - Smart formatting and punctuation
  - Async processing

#### 2. **Emotion Detection** (`emotion_detection/`)

- **Service**: OpenSmile feature extraction
- **Features**:
  - Extract pitch, energy, speaking rate
  - Classify emotions (happy, sad, angry, neutral, surprised)
  - Fallback mock detection if OpenSmile unavailable

#### 3. **Translation** (`translation/`)

- **Service**: DeepL API integration
- **Features**:
  - High-quality translation (EN ↔ ES)
  - Auto-detect target language
  - Language code normalization

#### 4. **Text-to-Speech** (`text_to_speech/`)

- **Service**: ElevenLabs API integration
- **Features**:
  - Emotional speech synthesis
  - Voice settings based on emotion
  - Multilingual support

---

## 🔄 Request Flow

```
Client Request
     ↓
FastAPI Router (main.py)
     ↓
/api/process-audio endpoint
     ↓
┌──────────────────────┐
│ 1. Cache audio       │ → Redis
└──────────────────────┘
     ↓
┌──────────────────────┐
│ 2. Speech-to-Text    │ → Deepgram API
│    (Transcribe)      │
└──────────────────────┘
     ↓
┌──────────────────────┐
│ 3. Emotion Detection │ → OpenSmile
│    (Analyze)         │
└──────────────────────┘
     ↓
┌──────────────────────┐
│ 4. Translation       │ → DeepL API
│    (Translate)       │
└──────────────────────┘
     ↓
┌──────────────────────┐
│ 5. Text-to-Speech    │ → ElevenLabs API
│    (Synthesize)      │
└──────────────────────┘
     ↓
┌──────────────────────┐
│ 6. Clear cache       │ → Redis
└──────────────────────┘
     ↓
JSON Response (with base64 audio)
     ↓
Client
```

---

## 🧩 Key Design Patterns

### 1. **Modular Monolith**
- Single deployable application
- Each module is independent and reusable
- Easy to extract into microservices later

### 2. **Async/Await**
- All I/O operations are async
- Non-blocking API calls
- Better performance under load

### 3. **Dependency Injection**
- Services are instantiated once
- Shared across requests
- Easy to mock for testing

### 4. **Configuration Management**
- Pydantic Settings for type-safe config
- Environment variable support
- Validation on startup

### 5. **Error Handling**
- Graceful degradation
- Detailed logging
- User-friendly error messages

---

## 🧪 Testing Structure

```
tests/
├── conftest.py           # Shared fixtures (Redis mock, sample data)
├── test_main.py          # Integration tests for main endpoint
├── test_services.py      # Unit tests for each service
└── test_utils.py         # Unit tests for utilities
```

**Coverage includes:**
- Health check endpoints
- Complete pipeline integration
- Individual service operations
- Utility functions
- Error handling

---

## 🔐 Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DEEPGRAM_API_KEY` | ✅ | - | Deepgram API key |
| `DEEPL_API_KEY` | ✅ | - | DeepL API key |
| `ELEVENLABS_API_KEY` | ✅ | - | ElevenLabs API key |
| `REDIS_HOST` | ❌ | localhost | Redis server host |
| `REDIS_PORT` | ❌ | 6379 | Redis server port |
| `LOG_LEVEL` | ❌ | INFO | Logging level |
| `DEBUG` | ❌ | False | Debug mode |

---

## 📊 Dependencies

### Core Framework
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `pydantic` - Data validation

### API Integrations
- `httpx` - Async HTTP client
- `opensmile` - Audio feature extraction

### Infrastructure
- `redis` - Caching layer
- `python-dotenv` - Environment management

### Development
- `pytest` - Testing framework
- `black` - Code formatter
- `mypy` - Type checker

---

## 🚀 Deployment Options

1. **Docker** (Recommended)
   ```bash
   docker-compose up -d
   ```

2. **Local Development**
   ```bash
   uvicorn app.main:app --reload
   ```

3. **Production**
   - Use Gunicorn with Uvicorn workers
   - Configure reverse proxy (nginx)
   - Set up monitoring and logging
   - Enable HTTPS/TLS

---

## 📈 Scalability Considerations

- **Horizontal Scaling**: Add more API instances behind load balancer
- **Redis Clustering**: For high availability
- **Rate Limiting**: Protect against abuse
- **Caching Strategy**: Optimize Redis TTL based on usage
- **Async Processing**: All I/O operations are non-blocking

---

## 🔧 Extending the Project

### Add New Language Support

1. Update language mappings in `translation/service.py`
2. Configure Deepgram language detection
3. Update voice selection in `text_to_speech/service.py`

### Add New Emotion

1. Update emotion classification in `emotion_detection/service.py`
2. Add voice settings mapping in `core/utils.py`
3. Update API documentation

### Add New Module

```bash
# Create module structure
mkdir -p app/modules/new_module
touch app/modules/new_module/__init__.py
touch app/modules/new_module/service.py
touch app/modules/new_module/router.py

# Register router in main.py
app.include_router(new_router, prefix="/api")
```

---

Built with ❤️ using FastAPI and modern Python async patterns.


