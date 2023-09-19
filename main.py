import hashlib

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Create a SHA-256 hash of the block's data and previous hash
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        sha.update(self.previous_hash.encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Create the first block in the blockchain (Genesis Block)
        return Block("Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(data, previous_block.hash)
        self.chain.append(new_block)

# Create a Blockchain instance
blockchain = Blockchain()

# Add some blocks to the blockchain
blockchain.add_block("First Block")
blockchain.add_block("Second Block")
blockchain.add_block("Third Block")
blockchain.add_block("Fourth Block")

# Print the contents of the blockchain
print("Blockchain:")
for block in blockchain.chain:
    print('Data:', block.data)
    print('Previous Hash:', block.previous_hash)
    print('Hash:', block.hash)
    print()
