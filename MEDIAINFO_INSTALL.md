# MediaInfo Installation Guide

## Why MediaInfo is Needed

MediaInfo is required by `audiofile` (used by OpenSmile) to read MP3 files on Windows. Without it, you'll see this error:

```
FileNotFoundError: mediainfo cannot be found.
Please make sure it is installed.
```

## Installation

### Windows (Recommended: Chocolatey)

**Option 1: Using Chocolatey** (easiest)
```powershell
# Install Chocolatey first if you don't have it
# Visit: https://chocolatey.org/install

# Then install mediainfo
choco install mediainfo -y
```

**Option 2: Manual Installation**
1. Download from: https://mediaarea.net/en/MediaInfo/Download/Windows
2. Download the CLI version (Command Line Interface)
3. Install it
4. Add MediaInfo to your PATH:
   - Search for "Environment Variables" in Windows
   - Edit PATH variable
   - Add `C:\Program Files\MediaInfo` (or wherever you installed it)
5. Restart your terminal/PowerShell

**Option 3: Portable**
1. Download MediaInfo CLI from: https://mediaarea.net/en/MediaInfo/Download/Windows
2. Extract `mediainfo.exe` to a folder
3. Add that folder to your PATH

### Verification

After installation, verify it works:

```powershell
mediainfo --version
```

You should see something like:
```
MediaInfo Command line, 24.06
```

## Alternative: Use WAV Files

If you can't install MediaInfo, use WAV files instead of MP3:
- OpenSmile can read WAV files without MediaInfo
- Convert your MP3 to WAV using online tools or ffmpeg

## Linux/Mac

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install mediainfo
```

### macOS
```bash
brew install mediainfo
```

## Testing After Installation

Test with your audio file:

```powershell
# Restart your terminal first!
# Then restart the API server
uvicorn app.main:app --reload

# Test the endpoint
curl -X POST "http://localhost:8000/api/emotion/detect" `
  -F "audio=@scared-man-shouting-no.mp3"
```

## Still Having Issues?

If MediaInfo is installed but still not found:

1. **Restart your terminal/PowerShell** (PATH changes need restart)
2. **Restart your IDE** (VS Code, Cursor, etc.)
3. **Verify PATH**: Run `echo $env:PATH` (PowerShell) to see if MediaInfo folder is listed
4. **Try full path**: Find where `mediainfo.exe` is located and make sure that folder is in PATH

## Alternative: Skip Emotion Detection

If you can't install MediaInfo right now, the API will still work:
- Emotion detection will return "neutral" with default attributes
- All other features (STT, translation, TTS) will work normally

