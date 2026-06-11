from charm.toolbox.pairinggroup import pair


class Proxy:

    def __init__(self, group, pp):

        self.group = group
        self.pp = pp

    
    # ================================================================


    def parse_policy(self, payload):

        return payload['ciphertext'], payload['policy']
    

    # ====================================================================

    def re_encrypt(self, elg_pk, ct_elg, rk, abe_components):

        C1_elg = ct_elg['C1']
        C2_elg = ct_elg['C2']

        rk0 = rk['rk0']
        rk1 = rk['rk1']

        g_s = abe_components['g_s']

        term1 = pair(elg_pk, rk0)
        term2 = pair(C2_elg, rk1)

        C1_prime = C1_elg * term1 * term2

        C2_prime = g_s * C2_elg

        return {
            'C1_prime': C1_prime,
            'C2_prime': C2_prime,
            'C3_prime': abe_components['C3_prime'],
            'C4_prime': abe_components['C4_prime'],
            'policy': abe_components['policy']
        }
    
    