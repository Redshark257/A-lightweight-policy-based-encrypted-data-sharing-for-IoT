from charm.toolbox.pairinggroup import PairingGroup, G1, GT, ZR, pair
from charm.toolbox.secretutil import SecretUtil

def setup_group():
    return PairingGroup('SS512')

def normalize_attr(attr):
    return attr.upper().strip()