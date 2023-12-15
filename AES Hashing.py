from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

def aes_encrypt(text, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(text.encode('utf-8'))
    return b64encode(nonce + tag + ciphertext).decode('utf-8')

def aes_decrypt(encrypted_text, key):
    data = b64decode(encrypted_text.encode('utf-8'))
    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_text = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted_text.decode('utf-8')

# Example usage
input_text = "Sensitive Information"
encryption_key = get_random_bytes(16)  # 128-bit key for AES-128
encrypted_result = aes_encrypt(input_text, encryption_key)
decrypted_result = aes_decrypt(encrypted_result, encryption_key)

print(f'Original Text: {input_text}')
print(f'Encrypted Text: {encrypted_result}')
print(f'Decrypted Text: {decrypted_result}')
