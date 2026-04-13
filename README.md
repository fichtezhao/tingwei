
Here’s a clear, practical tutorial on cryptography using Python, starting from basics and moving to real-world usage. I’ll keep it hands-on so you can actually use this in projects.

🔐 1. What is Cryptography?

Cryptography is about:

Confidentiality → keep data secret
Integrity → ensure data isn’t altered
Authentication → verify identity

Two main types:

Symmetric encryption (same key)
Asymmetric encryption (public + private key)
🧰 2. Setup (Python Library)

Use the widely trusted library:

pip install cryptography
🔑 3. Symmetric Encryption (Fernet – Easiest Start)

Fernet is high-level, safe, and beginner-friendly.

Generate a key
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
Encrypt data
f = Fernet(key)

message = b"Secret message"
encrypted = f.encrypt(message)

print(encrypted)
Decrypt data
decrypted = f.decrypt(encrypted)
print(decrypted.decode())

✔ Uses AES under the hood
✔ Handles IV + padding automatically

🔐 4. Hashing (Passwords, Integrity)

Hashing is one-way (can’t decrypt).

Example with SHA-256
import hashlib

password = "my_secure_password"
hash_value = hashlib.sha256(password.encode()).hexdigest()

print(hash_value)
Verify password
input_password = "my_secure_password"

if hashlib.sha256(input_password.encode()).hexdigest() == hash_value:
    print("Match")

👉 In real apps, use bcrypt instead (more secure against brute force)

🔑 5. Asymmetric Encryption (Public/Private Key)

Used in:

HTTPS
Digital signatures
Secure key exchange
Generate RSA keys
from cryptography.hazmat.primitives.asymmetric import rsa

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()
Encrypt with public key
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

message = b"Hello secure world"

encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
Decrypt with private key
decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(decrypted.decode())
✍️ 6. Digital Signatures (Authentication)
Sign data
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
Verify signature
public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

✔ Ensures message is authentic and unchanged

🔐 7. Best Practices (IMPORTANT)
❌ Don’t implement crypto from scratch
✅ Use trusted libraries like cryptography
✅ Use Fernet for most app-level encryption
✅ Use bcrypt / argon2 for passwords
✅ Store keys securely (env vars, vaults)
❌ Never hardcode keys in code
🚀 8. Real-World Use Cases
Secure API tokens
Encrypting local files
Password storage
HTTPS (TLS uses these concepts)
Blockchain & digital signatures
