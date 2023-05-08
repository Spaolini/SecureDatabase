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
key = b'e\xaf\xc4n[\xcb\x8e\r\xae\x00\x11\xca\x91C\xf3\x8d'

# userin = (input("To get customer information, enter their ID number:"))


cursor = db.cursor(buffered=True)
cursor2 = db.cursor()

query = "select lastName from customers"
# query = "select firstName from customers"

cursor.execute(query)

# putting results into an array
outputarr = [lastName for [lastName] in cursor.fetchall()]
# outputarr = [firstName for [firstName] in cursor.fetchall()]
encryptarr = []
decryptarr = []


def encryption():
    cipher = AES.new(key, AES.MODE_EAX)
    data = x.encode('latin-1')
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
    print(plaintext.decode('latin-1'))


def query_decrypt():
    skim = (x[2:])
    new_ciphertext = skim.decode('unicode_escape').encode("raw_unicode_escape")
    # print(new_ciphertext)
    new_nonce = new_ciphertext[:16]
    cipher = AES.new(key, AES.MODE_EAX, nonce=new_nonce)
    plaintext = cipher.decrypt(new_ciphertext[16:-1])
    print(plaintext.decode('latin-1'))


for x in outputarr:
    query_decrypt()
    # cipher = AES.new(key, AES.MODE_EAX, nonce=nonce_sep)
    # plaintext = cipher.decrypt(x[16:])
    # print(plaintext.decode('latin-1'))

# insert_cipher = "insert into customers (enc_firstName) values ('testing')"
# cursor2.execute(insert_cipher)
# print("executed")
# for i in encryptarr:
#     print("array element:", x)
