# Devops-7 Assignment-2 Setup Guide

This guide provides step-by-step instructions to set up and run the `driver.sh` and `functions.py` scripts located in the `Assignment-2` directory of the `Devops-7` GitHub repository.

## Prerequisites

Before you begin, ensure that you have the following installed on your Windows machine:

1. **Python 3**
2. **Git Bash**

---

## Setup Instructions

### 1. Install Python 3

Python is required to run the `functions.py` script.

- **Download Python:**
  - Visit the [official Python website](https://www.python.org/downloads/windows/).
  - Download the latest Python 3 installer for Windows.

- **Install Python:**
  - Run the downloaded installer.
  - **Important:** During installation, **check the box** that says **"Add Python to PATH"**. This ensures Python is accessible from the command line.

- **Verify Installation:**
  - Open **Command Prompt** or **PowerShell**.
  - Run the following command:
    ```bash
    python --version
    ```
    You should see an output like:
    ```
    Python 3.x.x
    ```

### 2. Install Git Bash

Git Bash provides a Unix-like terminal on Windows, allowing you to run Bash scripts.

- **Download Git Bash:**
  - Visit the [Git for Windows](https://git-scm.com/download/win) download page.
  - Download the installer.

- **Install Git Bash:**
  - Run the installer.
  - Follow the installation prompts, accepting the default settings unless you have specific preferences.

### 3. Clone the Repository

Clone the `Devops-7` repository to your local machine.

- **Open Git Bash:**
  - Right-click on your desktop or desired folder.
  - Select **"Git Bash Here"**.

- **Clone the Repository:**
  ```bash
  git clone https://github.com/yashkumar3066/Devops-7.git
  ```

### 4. Navigate to Assignment-2 Directory

Change your directory to the `Assignment-2` folder within the cloned repository.

```bash
cd Devops-7/Assignment-2
```

### 5. Make the Bash Script Executable

Ensure that the `driver.sh` script has execute permissions.

```bash
chmod +x driver.sh
```

### 6. Run the Bash Script

Execute the `driver.sh` script to run all Python functions sequentially.

```bash
./driver.sh
```

---

## Troubleshooting

- **Python Not Found:**
  - Ensure Python is installed and added to your PATH.
  - Reopen Git Bash after installation to refresh environment variables.

- **Permission Denied Error:**
  - Re-run the `chmod +x driver.sh` command to set execute permissions.
  - Ensure you are in the correct directory (`Assignment-2`).

- **Script Errors:**
  - Verify that `functions.py` has no syntax errors.
  - Ensure all required Python modules are installed. If `functions.py` uses external libraries, install them using `pip`:
    ```bash
    pip install module-name
    ```

- **Git Clone Issues:**
  - Ensure you have the correct repository URL.
  - Verify your internet connection.

---
