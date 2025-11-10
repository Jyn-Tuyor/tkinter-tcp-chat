# 💬 Tkinter TCP Chat App

A simple **TCP-based chat application** built with **Python** and **Tkinter**.  
It allows multiple clients to connect to a server and exchange messages in real time through sockets.

---

## 🚀 Features

- 🖥️ GUI built with **Tkinter**
- 🌐 Real-time **TCP socket communication**
- 👥 Supports **multiple clients**
- 🔔 Server broadcasts messages to all connected users
- 🧵 Uses **threads** for handling multiple connections
- 💬 Simple, clean chat interface

---

## 🧩 Project Structure

```
📁 tcp-chat-app
├── server.py        # Handles incoming connections and broadcasts messages
├── client.py        # Tkinter GUI for sending/receiving messages
└── README.md        # project documentation
```

---

## ⚙️ How It Works

1. **Server**  
   - Waits for incoming connections.  
   - Receives messages from clients and broadcasts them to everyone.

2. **Client (Tkinter GUI)**  
   - Connects to the server using sockets.  
   - Displays received messages in a chat window.  
   - Sends user input back to the server.

---

## 🧠 Tech Stack

- **Python 3.x**
- **Tkinter** (for GUI)
- **socket** (for TCP networking)
- **threading** (for handling multiple clients)

---

## 🛠️ Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/tkinter-tcp-chat.git
cd tkinter-tcp-chat
```

### 2️⃣ Run the Server
```bash
python server.py
```

---

## 🔐 Notes

- All clients must be on the **same network** (for local testing use `localhost`).
- Default port: `7878` (you can change it in the code).
- Designed for learning purposes — not production-grade security.

---

## 🌟 Future Improvements

- 🔒 Add message encryption (e.g., using `ssl`)
- 👤 Add usernames and login system
- 🕹️ Add emoji or file sharing support
- ☁️ Deploy server online for remote access

---

## ...

Built for learning **network programming** and **GUI design** with Python.  
Feel free to fork, improve, and contribute!
