from wallet import *
from cipher_utils import *

if __name__ == "__main__":
    print("\nNATIVE WALLET\n")

    wallet = WebWallet(strength=128)

    native_address = wallet.address
    native_mnemonic = wallet.mnemonic
    native_private_key = wallet.private_key

    print(native_address)
    print(native_mnemonic)
    print(native_private_key)

    print("\nENCRYPTED WALLET\n")

    encrypted_pk = Encryptor(shift=1).simple_encrypt(native_private_key)
    print(encrypted_pk)

    print("\nDECRYPTED WALLET\n")

    decrypted_pk = Decryptor(shift=1).simple_decrypt(encrypted_pk)
    print(decrypted_pk)
