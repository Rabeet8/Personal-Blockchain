import hashlib

# This line imports the hashlib module, which provides cryptographic hashing functions, including SHA-256, which you'll use to hash data.

# ---------------------------------------------------------------
# This is a function named hashGenerator that takes a data parameter.
# Inside the function, it calculates the SHA-256 hash of the data by encoding it as bytes and then converting the hash to its hexadecimal representation.
# The computed hash is returned.

def hashGenerator(data):
    result = hashlib.sha256(data.encode())  
    return result.hexdigest()
# ---------------------------------------------------------------

# This defines a Block class with a constructor (__init__) that initializes three attributes: data, hash, and prev_hash.
# Each block will store its data, its own hash, and the hash of the previous block in the chain.

class Block:
    def __init__(self, data, hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash
# ---------------------------------------------------------------

# This defines a Blockchain class with a constructor (__init__).
# Inside the constructor, it generates two initial hashes using the hashGenerator function. These hashes are for the "genesis" block, which is the first block in the blockchain.

class Blockchain:
    def __init__(self):
        hash_Last = hashGenerator('hello')
        hash_Start = hashGenerator("hello2")

        # Genesis Block
        genesis = Block("hello3", hash_Last, hash_Start)
        self.chain = [genesis]
# ---------------------------------------------------------------

# This creates the "genesis" block using the Block class and the two initial hashes.
# The self.chain attribute is initialized as a list containing only the genesis block, representing the blockchain's initial state.
  
    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(data + prev_hash)
        block = Block(data, hash, prev_hash)
        self.chain.append(block)

# ---------------------------------------------------------------


# Create a Blockchain instance
blc = Blockchain()

# Add some blocks to the blockchain
blc.add_block('1')
blc.add_block('2')
blc.add_block('3')
blc.add_block('4')
blc.add_block('5')


# Print the contents of the blockchain
for block in blc.chain:
    print(block.__dict__)
