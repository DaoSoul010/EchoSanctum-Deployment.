import os
import zipfile

# Directory structure for the bundle
base_dir = "/mnt/data/EchoSanctumEngine"
os.makedirs(base_dir, exist_ok=True)


os.makedirs(base_dir, exist_ok=True)

# File contents
handler_script = '''\
import os
import sys
import subprocess
from datetime import datetime

LOGFILE = "echo_log.txt"

def log(message):
    with open(LOGFILE, "a") as f:
        f.write(f"[{datetime.now()}] {message}\\n")

def write_file(filename, content):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        log(f"Wrote to {filename}")
        return f"✅ File saved: {filename}"
    except Exception as e:
        log(f"Error writing file: {e}")
        return f"❌ Error: {str(e)}"

def git_commit_push(msg):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", msg], check=True)
        subprocess.run(["git", "push"], check=True)
        log("Changes pushed to GitHub")
        return "🚀 Changes committed and pushed."
    except subprocess.CalledProcessError as e:
        log(f"Git error: {e}")
        return f"❌ Git error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python humanport_handler.py <filename> <content>")
        sys.exit(1)

    filename = sys.argv[1]
    content = sys.argv[2]
    result = write_file(filename, content)
    print(result)
'''

readme_content = '''\
# EchoSanctum HumanPort Handler

This script lets your local AI agent (e.g., KoboldAI or LM Studio) write files directly to your machine and push to GitHub using simple commands.

## Usage

Run this script in background or on-demand:

```bash
python humanport_handler.py myscript.py "print('Hello world')"

 subprocess.run(["git", "commit", "-m", msg], check=True)
        subprocess.run(["git", "push"], check=True)
        log("🚀 Git push successful.")
        return True
    except subprocess.CalledProcessError as e:
        log(f"❌ Git push failed: {e}")
        return False

# Sample usage (can be deleted after test)
if __name__ == "__main__":
    success = write_file("example.txt", "EchoSanctum lives.")
    if success:
        git_commit_push("Added example.txt from EchoDeploymentHandler")

