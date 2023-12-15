import hashlib

def md5_hash(input_text):
    md5_hasher = hashlib.md5()
    md5_hasher.update(input_text.encode('utf-8'))
    return md5_hasher.hexdigest()

# Example usage
input_text = "Hello, World!"
hashed_result = md5_hash(input_text)
print(f'MD5 Hash: {hashed_result}')
