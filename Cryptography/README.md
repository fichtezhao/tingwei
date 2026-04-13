If you're preparing for a Singapore CTF (like those run by National University of Singapore or GovTech Singapore), you don’t need “academic cryptography” — you need practical attack skills + Python automation.

Here’s a focused, hands-on tutorial roadmap with Python examples tailored for CTF crypto challenges.

🧠 1. Core CTF Crypto Concepts (What You MUST Know)

Most CTF crypto problems fall into these buckets:

🔑 Classical Ciphers
Caesar / ROT
Vigenère
Substitution
🔐 Encoding / Obfuscation
Base64, Base32
Hex, binary
XOR
🧮 Modern Crypto (CTF-style weaknesses)
RSA (small primes, bad padding)
AES (ECB mode patterns)
Hashes (MD5 collisions, brute force)
🐍 2. Python Setup

Install useful libraries:

pip install pycryptodome pwntools sympy
🔓 3. Basic Tools You’ll Use Everywhere
(1) Base64 Decode
import base64

cipher = "SGVsbG8gQ1RGIQ=="
print(base64.b64decode(cipher).decode())
(2) XOR Attack (VERY COMMON)
def xor(data, key):
    return bytes([b ^ key for b in data])

cipher = bytes.fromhex("1a0f1c")
for k in range(256):
    result = xor(cipher, k)
    if b"flag" in result:
        print(k, result)

👉 Used in MANY beginner/intermediate CTFs.

(3) Frequency Analysis (Breaking Substitution)
from collections import Counter

text = "GSRH RH Z HVXIVG"
print(Counter(text))
🧠 4. RSA Attacks (VERY IMPORTANT)

Most Singapore CTF crypto challenges include RSA.

📌 Case 1: Small n (Factorable)
from sympy import factorint

n = 3233
factors = factorint(n)
print(factors)
📌 Case 2: Recover Private Key

d≡e−1(modϕ(n))
d≡e
−1
(modϕ(n))

from Crypto.Util.number import inverse

p = 61
q = 53
n = p * q
phi = (p-1)*(q-1)
e = 17

d = inverse(e, phi)
print(d)
📌 Case 3: Decrypt Cipher
c = 2790
m = pow(c, d, n)
print(m)
🔐 5. AES Weakness (ECB Mode)
Detect ECB via repeated blocks:
from Crypto.Cipher import AES

def detect_ecb(ciphertext):
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    return len(blocks) != len(set(blocks))

👉 If blocks repeat → ECB → vulnerable.

🔑 6. Hash Cracking (Dictionary Attack)
import hashlib

target = "5d41402abc4b2a76b9719d911017c592"

wordlist = ["hello", "password", "flag"]

for word in wordlist:
    if hashlib.md5(word.encode()).hexdigest() == target:
        print("Found:", word)
⚔️ 7. Real CTF Workflow

When you see a challenge:

Step 1: Identify type
Looks random? → encoding or XOR
Numbers? → RSA
Long hex? → AES / hash
Step 2: Try quick wins
Base64 decode
XOR brute force
Strings search (strings tool)
Step 3: Automate with Python
Never solve manually
Write scripts fast
🧰 8. Must-Know Tools for Singapore CTFs
CyberChef → quick decoding
pwntools → scripting
Wireshark → if crypto + network
John the Ripper → hashes
🧪 9. Practice Platforms

To match Singapore-level difficulty:

CTFtime
Hack The Box
picoCTF
🚀 10. Pro Tips (This matters a LOT)
Learn to recognize patterns quickly
Build your own Python snippet library
Don’t overthink — most CTF crypto is intentionally broken
Practice RSA attacks heavily (they show up ALL the time
