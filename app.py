from flask import Flask, request, jsonify, render_template, redirect, url_for

import hashlib
import json

app = Flask(__name__)
PORT = 5000 
peers = set()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []

      
        initial_transactions = []
        dummy_block = {
            'index': 1,
          
            'transactions': initial_transactions,
            'proof': 0,
            'previous_hash': '0'
        }

      
        proof = self.proof_of_work(dummy_block)
        self.transactions = initial_transactions
        self.create_block(proof=proof, previous_hash='0')

    def create_block(self, proof, previous_hash):
      

        block = {
            'index': len(self.chain) + 1,
            
            'transactions': self.transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.transactions = []
        block['hash'] = self.hash(block)
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, block_data):
        proof = 0
       
        index = block_data['index']
        transactions = block_data['transactions']
        previous_hash = block_data['previous_hash']

        while True:
            block_candidate = {
                'index': index,
               
                'transactions': transactions,
                'proof': proof,
                'previous_hash': previous_hash
            }
            guess_hash = self.hash(block_candidate)
            if guess_hash[:4] == '0000':
                return proof
            proof += 1

    def hash(self, block):
        block_copy = block.copy()
        block_copy.pop('hash', None)
        return hashlib.sha256(json.dumps(block_copy, sort_keys=True).encode()).hexdigest()

    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({'sender': sender, 'receiver': receiver, 'amount': amount})
        return self.get_previous_block()['index'] + 1

    def is_chain_valid(self, chain):
        prev = chain[0]
        for i in range(1, len(chain)):
            current = chain[i]
            if current['previous_hash'] != self.hash(prev):
                return False
            prev = current
        return True

blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html', chain=blockchain.chain, peers=list(peers))

@app.route('/mine', methods=['POST'])
def mine():
    previous_block = blockchain.get_previous_block()
    block_data = {
        'index': previous_block['index'] + 1,
        'transactions': blockchain.transactions,
        'previous_hash': previous_block['hash']
    }
    proof = blockchain.proof_of_work(block_data)
    blockchain.create_block(proof, previous_block['hash'])
    return redirect(url_for('index'))

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    sender = request.form['sender']
    receiver = request.form['receiver']
    amount = request.form['amount']
    blockchain.add_transaction(sender, receiver, amount)
    return redirect(url_for('index'))

@app.route('/register_node', methods=['POST'])
def register_node():
    node_url = request.form['node']
    peers.add(node_url)
    return redirect(url_for('index'))

@app.route('/consensus', methods=['POST'])
def consensus():
    from urllib import request as urlrequest
    global blockchain
    max_chain = blockchain.chain
    for node in peers:
        try:
            response = urlrequest.urlopen(f"{node}/chain")
            data = json.loads(response.read().decode())
            if len(data['chain']) > len(max_chain) and blockchain.is_chain_valid(data['chain']):
                max_chain = data['chain']
        except:
            continue
    blockchain.chain = max_chain
    return redirect(url_for('index'))

@app.route('/chain')
def get_chain():
    return jsonify({'chain': blockchain.chain, 'length': len(blockchain.chain)})

@app.route('/nodes')
def get_nodes():
    return jsonify({'nodes': list(peers)})

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    app.run(port=port)
