from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Define the function to perform AES encryption
def aes_encrypt(plain_text, key):
	# Generate a random initialization vector (IV)
	iv = get_random_bytes(AES.block_size)
	# Create a new AES cipher object with the key and IV in CBC mode
	cipher = AES.new(key, AES.MODE_CBC, iv)
	# Pad the plain text to ensure it's a multiple of the block size
	padded_text = pad(plain_text.encode(), AES.block_size)
	# Encrypt the padded text
	cipher_text = cipher.encrypt(padded_text)
	return iv + cipher_text

# Define the function to perform AES decryption
def aes_decrypt(cipher_text, key):
	# Extract the IV from the beginning of the cipher text
	iv = cipher_text[:AES.block_size]
	# Create a new AES cipher object with the same key and IV in CBC mode
	cipher = AES.new(key, AES.MODE_CBC, iv)
	# Decrypt the cipher text (excluding the IV)
	decrypted_padded_text = cipher.decrypt(cipher_text[AES.block_size:])
	# Unpad the decrypted text to retrieve the original message
	decrypted_text = unpad(decrypted_padded_text, AES.block_size)
	return decrypted_text.decode()

# Define a 16-byte (128-bit) key for AES
key = b'This is a key123'  # Note: This key must be either 16, 24, or 32 bytes long

# Define the plain text to be encrypted
plain_text = "Hello, welcome to the world of cryptography!"

# Encrypt the plain text using the key
cipher_text = aes_encrypt(plain_text, key)
print(f"Encrypted text (in bytes): {cipher_text}")

# Decrypt the cipher text using the key
decrypted_text = aes_decrypt(cipher_text, key)
print(f"Decrypted text: {decrypted_text}")