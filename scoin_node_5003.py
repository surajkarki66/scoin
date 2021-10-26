from flask import jsonify, request
from uuid import uuid4

from app import create_app
from blockchain.blockchain import Blockchain


app = create_app()


@app.route('/mine_block', methods=['GET'])
def mine_block():
    ''' Mining a new block '''
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(
        sender=node_address, receiver='Alex', amount=1)
    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'Congratulations!, you just mined a block!',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
        'transactions': block['transactions']
    }
    return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
    ''' Get current chain of block chain '''
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200


@app.route('/is_valid', methods=['GET'])
def is_valid():
    ''' Checking blockchain is valid or not '''
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good. The blockchain is valid.'}
    else:
        response = {
            'message': 'We have a problem. The blockchain is not valid.'}
    return jsonify(response), 200


@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    ''' Adding a new transaction to the Blockchain '''
    json = request.get_json()
    transaction_keys = ["sender", "reciever", "amount"]
    if not all(key in json for key in transaction_keys):
        return "Some elements of the transaction are missing", 400

    index = blockchain.add_transaction(
        json["sender"], json["reciever"], json["amount"])
    response = {
        'message': f'This transaction will be added to the Block {index}'}
    return jsonify(response), 201


@app.route('/connect_node', methods=['POST'])
def connect_node():
    ''' Connecting new nodes '''
    json = request.get_json()
    nodes = json.get('nodes')

    if nodes is None:
        return "No node", 400

    for node in nodes:
        blockchain.add_node(node)

    response = {
        'message': 'All the nodes are now connected. The Scoin Blockchain now contains the following nodes: ',
        'total_nodes': list(blockchain.nodes)}

    return jsonify(response), 201


@app.route('/replace_chain', methods=['GET'])
def replace_chain():
    ''' Replace the chain by longest chain if needed '''
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'The nodes had different chains so the chain was replaced by the longest one.',
                    'new_chain': blockchain.chain}
    else:
        response = {'message': 'All good. The chain is the largest one.',
                    'actual_chain': blockchain.chain}
    return jsonify(response), 200


if __name__ == '__main__':

    # Creating an address for the node on Port 5000
    node_address = str(uuid4()).replace("-", "")

    # Creating a Blockchain
    blockchain = Blockchain()

    # Running the app
    app.run(host='0.0.0.0', port='5003')
