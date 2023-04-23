import mysql.connector
from Crypto.Cipher import AES
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from secrets import token_bytes

# database connection
db = mysql.connector.connect(
    host="pi.cs.oswego.edu",
    user="spaolini",
    password="isc329",
    database="21F_spaolini"
)
# key = b'e\xaf\xc4n[\xcb\x8e\r\xae\x00\x11\xca\x91C\xf3\x8d'

userin = (input("To get customer information, enter their ID number:"),)

try:
    if userin:
        key = input("enter authentication key:").encode().decode('unicode_escape').encode("raw_unicode_escape")

except UnicodeDecodeError:
    key = input("incorrect key,please try again:").encode().decode('unicode_escape').encode("raw_unicode_escape")

cursor = db.cursor()

# value = "select convert (bytes using utf8) from customers where custID=1029"

query = "select firstName from customers where custID=%s"

cursor.execute(query, userin)

# putting results into an array

outputarr = [firstName for [firstName] in cursor.fetchall()]
encryptarr = []
decryptarr = []


def encryption():
    cipher = AES.new(key, AES.MODE_EAX)
    data = x.encode()
    nonce = cipher.nonce
    # print(nonce)
    tempcipher = cipher.encrypt(data)
    global ciphertext
    ciphertext = nonce + tempcipher
    # print("temp",tempcipher)
    print(ciphertext)
    encryptarr.append(ciphertext)


def decryption():
    nonce_sep = ciphertext[:16]
    # print(nonce_sep)
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce_sep)
    plaintext = cipher.decrypt(ciphertext[16:])
    # decryptarr.append(plaintext.decode())
    # print(type(plaintext))


def query_decrypt():
    skim = bytes(x[2:])
    new_ciphertext = skim.decode('unicode_escape').encode("raw_unicode_escape")
    new_nonce = new_ciphertext[:16]
    cipher = AES.new(key, AES.MODE_EAX, nonce=new_nonce)
    plaintext = cipher.decrypt(new_ciphertext[16:])
    print(plaintext)


for x in outputarr:
    query_decrypt()
