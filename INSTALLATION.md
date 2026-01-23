# 📦 Installation Guide

Complete step-by-step installation instructions for the Vulnerability Scanner Dashboard.

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Windows Installation](#windows-installation)
3. [Linux/Mac Installation](#linuxmac-installation)
4. [Troubleshooting](#troubleshooting)
5. [Running the Application](#running-the-application)

---

## System Requirements

### Minimum Requirements
- **OS**: Windows 10/11, Linux (Ubuntu 20.04+), macOS 10.15+
- **Python**: 3.8 or higher
- **RAM**: 2 GB minimum (4 GB recommended)
- **Disk Space**: 500 MB free space
- **Browser**: Chrome, Firefox, Edge, or Safari (latest versions)

### Required Software
- Python 3.8+ ([Download](https://www.python.org/downloads/))
- Git ([Download](https://git-scm.com/downloads))
- pip (comes with Python)

---

## Windows Installation

### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **IMPORTANT**: Check "Add Python to PATH"
4. Click "Install Now"
5. Verify installation:
```cmd
python --version
pip --version
```

### Step 2: Install Git

1. Download Git from [git-scm.com](https://git-scm.com/downloads)
2. Run the installer with default settings
3. Verify:
```cmd
git --version
```

### Step 3: Clone Repository

```cmd
cd Desktop
git clone https://github.com/nainaisrat/vuln-scanner-dashboard.git
cd vuln-scanner-dashboard
```

### Step 4: Create Virtual Environment (Optional but Recommended)

```cmd
python -m venv venv
venv\Scripts\activate
```

### Step 5: Install Dependencies

```cmd
pip install -r requirements.txt
```

### Step 6: Run Application

```cmd
python app.py
```

Visit: `http://localhost:5000`

---

## Linux/Mac Installation

### Step 1: Install Python 3.8+

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip git
```

**macOS (using Homebrew):**
```bash
brew install python3 git
```

Verify:
```bash
python3 --version
pip3 --version
git --version
```

### Step 2: Clone Repository

```bash
cd ~
git clone https://github.com/nainaisrat/vuln-scanner-dashboard.git
cd vuln-scanner-dashboard
```

### Step 3: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run Application

```bash
python app.py
```

Visit: `http://localhost:5000`

---

## Troubleshooting

### Common Issues

#### 1. "Python not found" or "Command not found"

**Windows:**
- Reinstall Python and check "Add to PATH"
- Restart Command Prompt

**Linux/Mac:**
- Use `python3` instead of `python`
- Use `pip3` instead of `pip`

#### 2. "Permission denied" errors

**Linux/Mac:**
```bash
sudo chmod +x app.py
```

#### 3. "Module not found" errors

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. Port 5000 already in use

Edit `app.py` and change:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Changed to 8080
```

#### 5. Database errors

Delete the database and restart:
```bash
rm instance/vulnerabilities.db
python app.py
```

### Getting Help

If you encounter issues not listed here:

1. Check [GitHub Issues](https://github.com/nainaisrat/vuln-scanner-dashboard/issues)
2. Create a new issue with:
   - Your OS and Python version
   - Full error message
   - Steps you've tried

---

## Running the Application

### Development Mode

```bash
python app.py
```

Access at: `http://localhost:5000`

### Production Mode (Not Recommended for Production Use)

This is a demonstration project. For actual production:

1. Use a production WSGI server (Gunicorn, uWSGI)
2. Set up proper database (PostgreSQL, MySQL)
3. Configure reverse proxy (Nginx, Apache)
4. Enable HTTPS
5. Implement authentication

### Stopping the Application

Press `Ctrl+C` in the terminal

---

## Next Steps

After successful installation:

1. ✅ Read the [README.md](README.md)
2. ✅ Review the [Usage Guide](#)
3. ✅ Start scanning (with permission!)
4. ✅ Export your first PDF report

---

**Need more help?** Contact: isratnaina1995@gmail.com
