from hash import generateHash
import json
from time import time

# Cretae Block class

    # Define __init__ method with index, timestamp, transaction, previousHash parameters
    
        # Store index, transaction, timeStamp, previousHash in respective object variables
    
    
        # Calculate currentHash using the currentHash() method
    
    
    # Create currentHash() method
    
        # Create a variable blockString and store a string made by concatinating index, timestamp, previousHash and transaction 
        
        # Generating hash for blockString and return it
        
        
    
sender = "Mike"
receiver = "Sam"
sender = generateHash(sender)
receiver = generateHash(receiver)

transaction = { 
        "sender": sender, 
        "receiver": receiver, 
        "amount": 1000
    }

blockData = {
        'index': 1,
        'timestamp': time(),
        'transaction': transaction,
        'previousHash': "No Previous Hash Present. Since this is the first block.",
    }

# Use Block class and blockData to create a newBlock object.


# Display content fo the newBlock

