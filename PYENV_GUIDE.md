# 🐍 pyenv Quick Reference

If you're using **pyenv** to manage Python versions, here's what you need to know:

---

## What is pyenv?

pyenv lets you easily switch between multiple versions of Python. It's useful when:
- Different projects require different Python versions
- You want to test code across Python versions
- You need a specific Python version without affecting system Python

---

## Installation

### Linux/macOS

```bash
# Install pyenv
curl https://pyenv.run | bash

# Add to shell configuration (~/.bashrc, ~/.zshrc, etc.)
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# Restart shell or source config
source ~/.bashrc  # or ~/.zshrc
```

### Windows

```powershell
# Install pyenv-win
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"
& "./install-pyenv-win.ps1"

# Restart terminal
```

---

## Common Commands

### Install Python Version

```bash
# List available versions
pyenv install --list

# Install Python 3.13.9
pyenv install 3.13.9

# Install latest 3.13.x
pyenv install 3.13

# Verify installation
pyenv versions
```

### Set Python Version

```bash
# Set global (default) version
pyenv global 3.13.9

# Set local version (current directory and subdirectories)
pyenv local 3.13.9

# Set shell session version (temporary)
pyenv shell 3.13.9

# Unset local version
pyenv local --unset
```

### Check Versions

```bash
# Show all installed versions
pyenv versions

# Show current active version
pyenv version

# Show where Python is coming from
which python
python --version
```

---

## Project Setup with pyenv

### For This Project

This project requires Python 3.13+. Here's how to set it up:

```bash
# 1. Install Python 3.13 (if not already installed)
pyenv install 3.13.9

# 2. Set it as the local version for this project
cd /path/to/fast-api-tmp
pyenv local 3.13.9

# 3. Verify
python --version
# Should show: Python 3.13.9

# 4. Run setup
./setup.sh
```

---

## Troubleshooting

### Issue: `pyenv: command not found`

**Solution:**
```bash
# Make sure pyenv is in PATH
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# Add these lines to ~/.bashrc or ~/.zshrc permanently
```

### Issue: `pyenv: version 'X.X.X' is not installed`

**Solution:**
```bash
# Install the required version
pyenv install 3.13.9

# Or check what you have
pyenv versions

# Set to an installed version
pyenv local 3.13.9  # Use an actual installed version
```

### Issue: Python version doesn't change

**Solution:**
```bash
# Check what's overriding
pyenv version

# Remove shell override
pyenv shell --unset

# Check for .python-version files in parent directories
find . -name ".python-version"

# Rehash pyenv shims
pyenv rehash
```

### Issue: `setup.sh` fails with pyenv

The `setup.sh` script automatically detects and uses pyenv. If you get errors:

```bash
# 1. Verify pyenv is working
pyenv versions

# 2. Install Python 3.13 if missing
pyenv install 3.13.9

# 3. Set local version
pyenv local 3.13.9

# 4. Run setup again
./setup.sh
```

---

## .python-version File

The `.python-version` file in the project root tells pyenv which Python version to use:

```bash
# View current setting
cat .python-version

# Create/update (usually done by setup.sh)
echo "3.13.9" > .python-version

# Or use pyenv command
pyenv local 3.13.9
```

**Note:** This file is gitignored to avoid forcing specific Python patch versions on all developers.

---

## Virtual Environments with pyenv

pyenv works great with virtual environments:

```bash
# pyenv sets the Python version
pyenv local 3.13.9

# Create venv with pyenv's Python
python -m venv venv

# Activate venv
source venv/bin/activate

# Now you're using Python 3.13.9 in a virtual environment
```

---

## Uninstalling Python Versions

```bash
# List installed versions
pyenv versions

# Uninstall a version
pyenv uninstall 3.11.0

# Verify
pyenv versions
```

---

## Additional Resources

- **pyenv GitHub**: https://github.com/pyenv/pyenv
- **pyenv-win**: https://github.com/pyenv-win/pyenv-win
- **Python.org**: https://www.python.org/downloads/

---

## Quick Reference Card

| Command | Description |
|---------|-------------|
| `pyenv install 3.13.9` | Install Python 3.13.9 |
| `pyenv versions` | List installed versions |
| `pyenv global 3.13.9` | Set global default |
| `pyenv local 3.13.9` | Set local project version |
| `pyenv version` | Show current version |
| `pyenv which python` | Show path to Python |
| `pyenv rehash` | Rehash shims |
| `pyenv uninstall 3.11.0` | Uninstall Python 3.11.0 |

---

**Back to:** [SETUP.md](SETUP.md) | [README.md](README.md)
