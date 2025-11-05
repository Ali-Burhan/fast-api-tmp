# Python 3.13 Installation Guide

## Quick Fix for Python 3.13 Compatibility

The requirements.txt has been updated for Python 3.13 compatibility. Here's how to install:

### Step 1: Upgrade pip and build tools first

```powershell
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools wheel
```

### Step 2: Install dependencies

```powershell
pip install -r requirements.txt
```

### Step 3: If you still get errors with numpy

If numpy still fails, install it separately first:

```powershell
pip install numpy>=1.26.0
pip install -r requirements.txt
```

### Alternative: Install core dependencies first

```powershell
# Install build tools
pip install setuptools wheel

# Install numpy and pandas first (they're dependencies for opensmile)
pip install numpy>=1.26.0 pandas>=2.2.0

# Then install the rest
pip install -r requirements.txt
```

## What Changed

- **numpy**: Updated from `1.24.3` to `>=1.26.0` (Python 3.13 compatible)
- **pandas**: Updated from `2.0.3` to `>=2.2.0` (Python 3.13 compatible)
- **FastAPI**: Updated to `0.115.0` (latest stable)
- **Pydantic**: Updated to `2.9.2` (v2 syntax)
- **All other packages**: Updated to latest Python 3.13 compatible versions
- **Added**: `setuptools` and `wheel` for building

## Verification

After installation, verify everything works:

```powershell
python -c "import fastapi; import numpy; import pandas; print('All imports successful!')"
```

## Troubleshooting

### Issue: "Cannot import 'setuptools.build_meta'"

**Solution:**
```powershell
pip install --upgrade setuptools wheel
```

### Issue: numpy still failing

**Solution:** Try installing from conda-forge or use a pre-built wheel:
```powershell
pip install --only-binary :all: numpy
pip install --only-binary :all: pandas
```

### Issue: opensmile installation fails

**Solution:** OpenSmile is optional - the API will use mock emotion detection if it fails:
```powershell
# Skip opensmile for now
pip install -r requirements.txt --ignore-installed opensmile
```


