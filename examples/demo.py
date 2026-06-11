from lightsabre.utils.policy import setup_group, normalize_attr
from lightsabre.core.kgc import KGC
from lightsabre.core.owner import DataOwner
from lightsabre.core.proxy import Proxy
from lightsabre.core.user import ThirdParty
from charm.toolbox.pairinggroup import GT


def main():

    print("\n================================")
    print("Light-SABRE Demo")
    print("==================================")


    # ===================================================

    # SETUP

    # ===================================================


    group = setup_group()
    kgc = KGC(group)

    
    pp, msk, elg_pk, elg_sk = kgc.setup()

    # ===========================================================

    # Encryption

    # ===========================================================


    owner = DataOwner(group, pp, elg_pk)

    M = group.random(GT)

    policy = "(ADMIN AND HR) OR MANAGER"

    payload = owner.encrypt(M, policy)

    # ===========================================================

    # Proxy

    # ===========================================================

    proxy = Proxy(group, pp)

    ct_elg, parsed_policy = proxy.parse_policy(payload)

    # ===========================================================

    # Re-encryption

    # ===========================================================


    rk, rk_secret, abe_components = kgc.generate_re_encryption_key(parsed_policy)


    ct_abe = proxy.re_encrypt(elg_pk, ct_elg, rk, abe_components)


    # ===========================================================

    # User Keys

    # ===========================================================


    user_attrs = ['ADMIN', 'HR', 'MANAGER']
    #user_attrs = ['ADMIN']
    #user_attrs = ['MANAGER']



    sk_abe = kgc.generate_user_key(user_attrs, rk_secret)

    # ===========================================================

    # Decryption

    # ===========================================================

    user = ThirdParty(group, pp)

    recovered = user.decrypt(ct_abe, sk_abe, user_attrs)


    # ===========================================================

    # Verification

    # ===========================================================

    print(f"Original: {M}")

    print(f"Recovered: {recovered}")

    if recovered == M:
        print("SUCCESS")
    else:
        print("FAILURE")
    


if __name__ == "__main__":
    main()
