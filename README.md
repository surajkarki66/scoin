# scoin

## To run it locally
```bash
  $ pip install -r "requirements.txt"
```

Run different nodes
```bash
  $ python scoin_node_5001.py
  $ python scoin_node_5002.py
  $ python scoin_node_5003.py
```

 
 Now all apis are live.
 
 ## Endpoints
 
 ##### 1) To mine a block in a blockchain from node1(port:5001):
 GET Request on:  `http://localhost:5001/mine_block`
 
 ##### 2) To get full blockchain from node1(port:5001)
 GET Request on:  `http://localhost:5001/get_chain`
 
 ##### 3) To check if the chain is valid or not from node1(port:5001)
 GET Request on:  `http://localhost:5001/is_valid`
 
 ##### 4) To connect all different nodes from node1(port:5001)
 POST Request on:  `http://localhost:5001/connect_node`
 - JSON payload: ```bash
      {
          "nodes": [
            "http://127.0.0.1:5001",
            "http://127.0.0.1:5002",
            "http://127.0.0.1:5003"
          ]
       }
 ```

 ##### 5) To replace the chain by longest chain if needed from node1(port:5001)
 GET Request on:  `http://localhost:5001/replace_chain`
 
 ##### 6) To add a new transaction to the Blockchain from node1(port:5001)
 POST Request on:  `http://localhost:5001/add_transaction`
 - JSON payload: ```bash
      {
          "sender":"Alex" ,
          "reciever": "Michael",
          "amount": 10
       }
 ```
 
 
