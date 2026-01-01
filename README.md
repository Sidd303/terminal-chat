
# Terminal Chat Application 🖥️💬

A simple **terminal-based chat application** built using **Python sockets**, allowing users to chat with each other through the command line.

This project is being built step-by-step, starting from local communication and later expanding to global usage.

---

## 📁 Project Structure

terminal-chat/
│
├── server/
│   └── server.py        # Chat server
│
├── client/
│   └── client.py        # Chat client
│
├── app.py               # Entry / future controller (optional)
├── .gitignore
└── README.md

## 🚀 Features (Planned & Implemented)

- ✅ Terminal-based chat
- ✅ Client–server architecture
- ⏳ Real-time messaging (threading)
- ⏳ Multiple clients support
- ⏳ Usernames
- ⏳ Global access (via tunneling / hosting)
- ⏳ Optional encryption

---

## 🛠️ Requirements

- Python 3.8+
- Works on Linux / macOS / Windows

No external libraries required (uses Python standard library).

---

## ▶️ How to Run (Local)

### Start the Server
```bash
cd server
python server.py
````

### Start the Client

```bash
cd client
python client.py
```

Open multiple terminals to simulate multiple users.

---

## 🌍 Global Usage (Future Plan)

The server will later be exposed globally using:

* SSH tunneling
* Reverse proxy
* Or cloud hosting (without revealing private IP)

---

## 📌 Author

* **Name:** Sidd303
* **Email:** [sidd.laau@gmail.com](mailto:sidd.laau@gmail.com)

---

## 📄 License

This project is open-source and free to use for learning purposes.

