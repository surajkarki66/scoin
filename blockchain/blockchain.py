import datetime
import hashlib
import json


class Blockchain:
    ''' Building a blockchain class '''

    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        ''' Creating a new block in the blockchain '''
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}

        self.chain.append(block)
        return block

    def get_previous_block(self):
        ''' Getting the previous block of the blockchain '''
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        ''' Giving a problem to the miners '''
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(str(
                new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()

            if hash_operation[:4] == '0000':
                check_proof = True

            else:
                new_proof += 1

        return new_proof

    def hash(self, block):
        ''' Making a hash of a block '''
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        ''' Cheking if a chain is valid or not '''
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(
                proof ** 2 - previous_proof ** 2).encode()).hexdigest()

            if hash_operation[:4] != '0000':
                return False

            previous_block = block
            block_index += 1

        return True
