from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet import BIP44HDWallet
from hdwallet.utils import generate_mnemonic


class WebWallet:
    def __init__(self, strength, additional_paths=10) -> None:
        self._strength = strength
        self._defauls_path = "m/44'/60'/0'/0/0"
        self._additional_paths = [
            f"m/44'/60'/0'/0/{_}" for _ in range(additional_paths)
        ]
        self._bip44_hdwallet = self._set_get_bip44_hdwallet()

    @property
    def mnemonic(self):
        return self._bip44_hdwallet.mnemonic()

    @property
    def additional_paths(self):
        return self._additional_paths

    @property
    def private_key(self):
        return self._bip44_hdwallet.private_key()

    @property
    def address(self):
        return self._bip44_hdwallet.address()

    def _generate_mnemonic(self, strength: int) -> str:
        MNEMONIC: str = generate_mnemonic(language="english", strength=strength)
        return MNEMONIC

    def _set_get_bip44_hdwallet(self):
        bip44_hdwallet: object = BIP44HDWallet(cryptocurrency=EthereumMainnet)
        MNEMONIC: str = self._generate_mnemonic(self._strength)
        bip44_hdwallet.from_mnemonic(mnemonic=MNEMONIC, language="english")
        return bip44_hdwallet
