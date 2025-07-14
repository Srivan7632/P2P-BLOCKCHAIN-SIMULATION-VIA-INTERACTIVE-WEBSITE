Simple Blockchain Node with Flask and HTML UI

This project is a minimal blockchain prototype implemented using **Python Flask** and a styled **HTML/CSS** frontend.
It demonstrates:

- Transaction handling
- Proof-of-Work mining
- Node registration
- Consensus (longest valid chain)
- A responsive web interface to interact with all features

---

Features Implemented

- ✅ **Add Transactions** (Sender → Receiver → Amount)
- ✅ **Pending Transactions UI** (visually separates queued transactions)
- ✅ **Mine Block** (Proof of Work, hash starts with `0000`)
- ✅ **Block Status Tags** (`✓ Confirmed` badges for mined blocks)
- ✅ **Register Peer Nodes**
- ✅ **Consensus Algorithm** (adopts longest valid chain from peers)
- ✅ **Display Chain and Peers** with enhanced layout
- ✅ **Mobile-responsive layout & modern UI design**

---

## 📂 Files

| File                   | Description                                      |
| ---------------------- | ------------------------------------------------ |
| `app.py`               | Flask server with blockchain logic               |
| `templates/index.html` | Frontend UI with styled blocks and control panel |

---

## 🛠 How to Run

### 1. Setup Environment

Make sure Python 3.x is installed.

Install Flask:

```bash
pip install flask
```

### 2. Run the App

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 3. Run Additional Nodes

Open new terminals:

```bash
python app.py 5001
python app.py 5002
```

---

## 🔍 Example Use Case: Alice Sends to Bob

1. In **Add Transaction**:

   - Sender: `Alice`
   - Receiver: `Bob`
   - Amount: `50`
   - Click `Add Transaction`

2. Pending transaction appears in yellow under **Pending Transactions**.

3. Click `Mine` to create a block confirming the transaction.

4. The transaction moves to the chain, marked with a ✅ `Confirmed` badge.

5. Register another node with `http://localhost:5001` and click `Resolve Conflict` to sync.

---

## 🌐 Available Routes

| Route              | Method | Description           |
| ------------------ | ------ | --------------------- |
| `/`                | GET    | Web UI home           |
| `/mine`            | POST   | Mine new block        |
| `/add_transaction` | POST   | Add new transaction   |
| `/register_node`   | POST   | Register peer node    |
| `/consensus`       | POST   | Trigger consensus     |
| `/chain`           | GET    | Get full blockchain   |
| `/nodes`           | GET    | List registered peers |

---

Inspired By
Basic blockchain concepts from educational projects and tutorials, enhanced with a modern UI and real-time sync capability.

---

Notes

- This is a simplified implementation for learning and demonstration.
- Blocks are stored in memory, not persistent.
- No cryptographic signatures or real wallet logic.
- For the frontend application to work,need to store the index.html inside a templates folder

---

Next Steps

- Add timestamps and unique transaction IDs
- Implement wallet-like signing
- Add persistent DB or file storage
- Would make an mobile app interface
- Would make it even more interactive
  
