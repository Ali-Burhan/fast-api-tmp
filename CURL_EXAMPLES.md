# cURL Examples for Speech Translation API

## Complete Audio Processing Pipeline

### Process English Audio → Spanish Translation

```bash
curl -X POST "http://localhost:8000/api/process-audio" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "audio=@english_audio.wav" \
  | jq .
```

### Process Spanish Audio → English Translation

```bash
curl -X POST "http://localhost:8000/api/process-audio" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "audio=@spanish_audio.mp3" \
  | jq .
```

### Save Translated Audio to File

```bash
# Get the response
response=$(curl -X POST "http://localhost:8000/api/process-audio" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "audio=@input.wav")

# Extract base64 audio and save
echo "$response" | jq -r '.audio_base64' | base64 -d > output.mp3
```

---

## Individual Module Endpoints

### 1. Speech-to-Text

#### Transcribe English Audio

```bash
curl -X POST "http://localhost:8000/api/speech-to-text/transcribe" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "audio=@english.wav" \
  | jq .
```

**Expected Response:**
```json
{
  "language": "English",
  "language_code": "en",
  "text": "Hello, how are you today?"
}
```

#### Transcribe Spanish Audio

```bash
curl -X POST "http://localhost:8000/api/speech-to-text/transcribe" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "audio=@spanish.mp3" \
  | jq .
```

---

### 2. Emotion Detection

#### Detect Emotion from Audio

```bash
curl -X POST "http://localhost:8000/api/emotion/detect" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "audio=@sample.wav" \
  | jq .
```

**Expected Response:**
```json
{
  "emotion": "happy",
  "attributes": {
    "pitch_mean": 0.65,
    "energy": 0.72,
    "speaking_rate": 0.55
  }
}
```

---

### 3. Translation

#### English to Spanish

```bash
curl -X POST "http://localhost:8000/api/translation/translate" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello, how are you?",
    "source_lang": "en",
    "target_lang": "es"
  }' \
  | jq .
```

**Expected Response:**
```json
{
  "translated_text": "Hola, ¿cómo estás?",
  "source_language": "en",
  "target_language": "es"
}
```

#### Spanish to English

```bash
curl -X POST "http://localhost:8000/api/translation/translate" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Buenos días, ¿cómo está?",
    "source_lang": "es",
    "target_lang": "en"
  }' \
  | jq .
```

#### Auto-detect Target Language

```bash
curl -X POST "http://localhost:8000/api/translation/translate" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Good morning",
    "source_lang": "en"
  }' \
  | jq .
```

---

### 4. Text-to-Speech

#### Generate Happy Speech

```bash
curl -X POST "http://localhost:8000/api/text-to-speech/generate" \
  -H "accept: audio/mpeg" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "¡Hola! ¿Cómo estás?",
    "emotion": "happy",
    "emotion_attributes": {
      "pitch_mean": 0.7,
      "energy": 0.8,
      "speaking_rate": 0.6
    },
    "language_code": "es"
  }' \
  --output happy_speech.mp3
```

#### Generate Sad Speech

```bash
curl -X POST "http://localhost:8000/api/text-to-speech/generate" \
  -H "accept: audio/mpeg" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "I am feeling down today",
    "emotion": "sad",
    "emotion_attributes": {
      "pitch_mean": 0.3,
      "energy": 0.4,
      "speaking_rate": 0.5
    },
    "language_code": "en"
  }' \
  --output sad_speech.mp3
```

#### Generate Neutral Speech

```bash
curl -X POST "http://localhost:8000/api/text-to-speech/generate" \
  -H "accept: audio/mpeg" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "This is a neutral statement",
    "emotion": "neutral",
    "language_code": "en"
  }' \
  --output neutral_speech.mp3
```

#### Get Available Voices

```bash
curl -X GET "http://localhost:8000/api/text-to-speech/voices" \
  -H "accept: application/json" \
  | jq .
```

---

## Health and Status Checks

### Check API Health

```bash
curl -X GET "http://localhost:8000/health" \
  -H "accept: application/json" \
  | jq .
```

### Get API Info

```bash
curl -X GET "http://localhost:8000/" \
  -H "accept: application/json" \
  | jq .
```

---

## Advanced Examples

### Process Audio with Error Handling

```bash
#!/bin/bash

audio_file="input.wav"
output_file="output.mp3"

# Check if audio file exists
if [ ! -f "$audio_file" ]; then
  echo "Error: Audio file not found"
  exit 1
fi

# Process audio
response=$(curl -s -X POST "http://localhost:8000/api/process-audio" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "audio=@$audio_file")

# Check for errors
if echo "$response" | jq -e '.detail' > /dev/null 2>&1; then
  echo "Error: $(echo "$response" | jq -r '.detail')"
  exit 1
fi

# Extract and save audio
echo "$response" | jq -r '.audio_base64' | base64 -d > "$output_file"

# Display results
echo "Processing complete!"
echo "Original: $(echo "$response" | jq -r '.original_text')"
echo "Translated: $(echo "$response" | jq -r '.translated_text')"
echo "Emotion: $(echo "$response" | jq -r '.emotion')"
echo "Audio saved to: $output_file"
```

### Batch Process Multiple Audio Files

```bash
#!/bin/bash

# Process all WAV files in a directory
for audio in audio_samples/*.wav; do
  echo "Processing: $audio"
  
  filename=$(basename "$audio" .wav)
  output="output_${filename}.mp3"
  
  response=$(curl -s -X POST "http://localhost:8000/api/process-audio" \
    -H "accept: application/json" \
    -H "Content-Type: multipart/form-data" \
    -F "audio=@$audio")
  
  echo "$response" | jq -r '.audio_base64' | base64 -d > "$output"
  
  echo "✓ Saved: $output"
done
```

### Test with Timing

```bash
# Measure processing time
time curl -X POST "http://localhost:8000/api/process-audio" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "audio=@sample.wav" \
  -o result.json
```

---

## Testing Different Audio Formats

```bash
# MP3
curl -X POST "http://localhost:8000/api/process-audio" \
  -F "audio=@audio.mp3" | jq .

# WAV
curl -X POST "http://localhost:8000/api/process-audio" \
  -F "audio=@audio.wav" | jq .

# M4A
curl -X POST "http://localhost:8000/api/process-audio" \
  -F "audio=@audio.m4a" | jq .

# FLAC
curl -X POST "http://localhost:8000/api/process-audio" \
  -F "audio=@audio.flac" | jq .

# OGG
curl -X POST "http://localhost:8000/api/process-audio" \
  -F "audio=@audio.ogg" | jq .
```

---

## Notes

- All examples assume the API is running at `http://localhost:8000`
- Add `-v` flag for verbose output: `curl -v ...`
- Add `-s` flag for silent mode (no progress bar): `curl -s ...`
- Use `jq` for pretty JSON formatting (install: `brew install jq` or `apt-get install jq`)
- For Windows PowerShell, use `Invoke-RestMethod` instead of `curl`

## Windows PowerShell Examples

### Process Audio (PowerShell)

```powershell
$response = Invoke-RestMethod -Uri "http://localhost:8000/api/process-audio" `
  -Method Post `
  -Form @{ audio = Get-Item -Path "audio.wav" }

# Display results
$response | ConvertTo-Json -Depth 5

# Save audio
[System.Convert]::FromBase64String($response.audio_base64) | 
  Set-Content -Path "output.mp3" -Encoding Byte
```


