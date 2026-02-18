<img width="734" height="241" alt="Untitled-11" src="https://github.com/user-attachments/assets/b84698b2-05cf-4abd-97c2-e34bd231cdd1" />

# <p align="center"> RYHA FRAMEWORK </p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0--GOD-red?style=for-the-badge&logo=ghostery" alt="Version">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Android%20%7C%20iOS-blue?style=for-the-badge&logo=apple" alt="Platforms">
  <img src="https://img.shields.io/badge/Status-Undetected-green?style=for-the-badge&logo=checkmarx" alt="Status">
</p>

---

## ⚡ Overview
**RYHA** is an elite, modular Research Framework designed for high-end security testing. It features a "Ghost Core" that stays invisible and "Gadgets" (Modules) that find hidden data.

> [!WARNING]  
> **FOR RESEARCH ONLY.** This tool is for learning how to defend systems. Never use it for bad things!

---

## 🧱 The "Secret Base" Setup
Before we start, make sure your folders look like this:

📂 **RYHA-Framework/**
┣ 📂 **core/** — 🧠 The Brains (engine.py, loader.py, __init__.py)  
┣ 📂 **modules/** — 💎 The Gadgets (harvester.py, network.py, __init__.py)  
┗ 📂 **dashboard/** — 🕹️ The Control Room (server.py)  

---

## 🚀 How to Use (Step-by-Step)

### 1️⃣ Step 1: Get the Ingredients
Open your terminal (the black box) and type this:

pip install flask requests pyinstaller pillow

This gets all the tools the computer needs to understand RYHA.


2️⃣ Step 2: Set the "Home Address"
 * Open core/engine.py.
 * Look for YOUR_SERVER_IP.
 * Change it to your own IP address so the agent knows where to send the loot.


3️⃣ Step 3: Start the Control Room
To see your agents live, you must run the server:
python dashboard/server.py

Go to http://localhost:5000 in your browser to see your Dashboard!


4️⃣ Step 4: Make the "Ghost"
Turn your code into a real file that runs anywhere:
pyinstaller --onefile --noconsole --name ryha_agent core/engine.py

Look inside the dist/ folder for ryha_agent.exe. This is your invisible agent.


5️⃣ Step 5: The "Boom" Delivery 💥
Hide your ryha_agent.exe inside a normal picture using a joiner.
 * When someone opens the "picture," RYHA wakes up in the background and stays there forever (Lifetime Access).
📱 Mobile Powers
 * Android: Run the same files inside Termux or wrap them in an .apk.
 * Apple: Use Pythonista to run the modules on iOS.


📊 Features
| Icon | Feature | Role |
|---|---|---|
| 🛡️ | Anti-VM | If a researcher tries to catch RYHA, it vanishes! |
| ⚓ | Persistence | Even if the PC restarts, RYHA stays alive. |
| 💎 | Harvester | Finds AWS keys, Discord tokens, and SSH keys. |
📜 
<p align="center">
:P
</p>

-----
<div align="center">

### 🌟 If you found this useful, please star the repo! 🌟

**Made with Coded by the SAYO**

*Hack the Planet* 🌐🔓

</div>

---


---

<div align="center">

**Remember**: There's nothing can't be exposed in that world and there's no privacy at all. So, be safe be updated.

© 2025 RYHA. All rights reserved.

</div>
