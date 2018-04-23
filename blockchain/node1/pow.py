import hashlib

def proof_of_work(prev_hash, num_leading_z = 5):
    nonce = None
    counter = 0
    leading_zeros = '0' * num_leading_z

    while not nonce:
        sha_protocol = hashlib.sha256()
        sha_protocol.update(
            str(prev_hash).encode('utf-8')+
            str(counter).encode('utf-8'))
        experimental_hash = sha_protocol.hexdigest()
        if str(experimental_hash[:num_leading_z]) == leading_zeros:
            nonce = counter
        else:
            counter += 1
    return nonce, num_leading_z
