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

# keys for each column
fn_key = b'e\xaf\xc4n[\xcb\x8e\r\xae\x00\x11\xca\x91C\xf3\x8d'
ln_key = b'e\x08\xa8Z\xbb\xe3\x89\x0b\x95\xf0\x9d\xb2a2\xd2m'
addr_key = b'\xd9\x01$}`\xa3\xb4\xd6s\xee\x023|\xe0\xda\x8b'
SSN_key = b'\x9dR\x120_\x158\xa4\xd3\xa5\xa0\x0c\xcbi\xeb\xbe'
dob_key = b'\xe0`\xf0\xf2\x90\xf3\x86 c\x9d}\xad\x80}\xfa\xfa'
pass_key = b'=\xbf\xa3\x97\x05NxW\xcb\x8f\xa3\xc4\xf0m\xd4^'
num_key = b'\xa5\xc12H\x11r\xeb`\x7f\xfb\x04F\xa0\xda\xea+'

# getKey = bytes(
#     input("Please provide authentication key:").encode().decode('unicode_escape').encode("raw_unicode_escape"))

cursor = db.cursor(prepared=True)

# keys for each column in the customers table
fns_query = """select firstName from customers where custID=%s"""
lns_query = """select lastName from customers where custID=%s"""
ssns_query = """select SSN from customers where custID=%s"""
addrs_query = """select address from customers where custID=%s"""
fn_query = """select firstName from customers"""
ln_query = """select lastName from customers"""
ssn_query = """select SSN from customers"""
addr_query = """select address from customers"""

# initializing empty arrays
encryptarr = []
decryptarr = []
inputarray = []


def encryption():
    cipher = AES.new(dob_key, AES.MODE_EAX)  # creating new instance of the cipher
    data = x.encode('latin-1')  # encodes using latin-1
    nonce = cipher.nonce  # new random value created from the cipher
    tempcipher = cipher.encrypt(data)  # This is where the encryption is done
    global ciphertext
    ciphertext = nonce + tempcipher  # nonce value is attached to the ciphertext, creating complete ciphertext
    print("ciphertext: ", ciphertext)
    encryptarr.append(ciphertext)


def decryption():
    nonce_sep = ciphertext[:16]  # separate nonce value from ciphertext
    cipher = AES.new(dob_key, AES.MODE_EAX, nonce=nonce_sep)  # new instance of cipher
    plaintext = cipher.decrypt(ciphertext[16:])  # decryption of plaintext
    print(plaintext.decode('latin-1'))


def query_decrypt():
    skim = (x[2:])  # formatting
    new_ciphertext = skim.decode('unicode_escape').encode("raw_unicode_escape")  # formatting
    # same steps as decryption function
    new_nonce = new_ciphertext[:16]
    cipher = AES.new(getKey, AES.MODE_EAX, nonce=new_nonce)
    plaintext = cipher.decrypt(new_ciphertext[16:-1])
    print(plaintext.decode('latin-1'))


query = "select DOB from employees"

# encryption example
# cursor.execute(query)
# result = cursor.fetchall()
# outputarr = [row[0] for row in result]
# for x in outputarr:
#     encryption()
#     decryption()


# Menu for column decryption
# getnum = int((input(
#     " enter 1 for first name \n enter 2 for last name \n enter 3 for address \n enter 4 for SSN \n enter 5 for first "
#     "name by custID search \n enter 6 for last "
#     "name by custID search \n enter 7 for address "
#     "by custID search \n enter 8 for SSN "
#     "by custID search \n enter number: ")))
# if getnum == 1:
#     cursor.execute(fn_query)
#     result = cursor.fetchall()
#     outputarr = [row[0] for row in result]
#     for x in outputarr:
#         query_decrypt()
# elif getnum == 2:
#     cursor.execute(ln_query)
#     result = cursor.fetchall()
#     outputarr = [row[0] for row in result]
#     for x in outputarr:
#         query_decrypt()
# elif getnum == 3:
#     cursor.execute(addr_query)
#     result = cursor.fetchall()
#     outputarr = [row[0] for row in result]
#     for x in outputarr:
#         query_decrypt()
# elif getnum == 4:
#     cursor.execute(ssn_query)
#     result = cursor.fetchall()
#     outputarr = [row[0] for row in result]
#     for x in outputarr:
#         query_decrypt()
# elif getnum == 5:
#     getcustID = input("To get customer information, enter their ID number:")
#     userin = (getcustID,)
#     cursor.execute(fns_query, userin)
#     result = cursor.fetchall()
#     outputarr = [row[0] for row in result]
#     for x in outputarr:
#         query_decrypt()
# elif getnum == 6:
#     getcustID = input("To get customer information, enter their ID number:")
#     userin = (getcustID,)
#     cursor.execute(lns_query, userin)
#     result = cursor.fetchall()
#     outputarr = [row[0] for row in result]
#     for x in outputarr:
#         query_decrypt()
# elif getnum == 7:
#     getcustID = input("To get customer information, enter their ID number:")
#     userin = (getcustID,)
#     cursor.execute(addrs_query, userin)
#     result = cursor.fetchall()
#     outputarr = [row[0] for row in result]
#     for x in outputarr:
#         query_decrypt()
#
# elif getnum == 8:
#     getcustID = input("To get customer information, enter their ID number:")
#     userin = (getcustID,)
#     cursor.execute(ssns_query, userin)
#     result = cursor.fetchall()
#     outputarr = [row[0] for row in result]
#     for x in outputarr:
#         query_decrypt()
