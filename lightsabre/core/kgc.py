from charm.toolbox.pairinggroup import G1, GT, ZR, pair
from charm.toolbox.secretutil import SecretUtil


#from lightsabre.utils.policy import setup_group, normalize_attr

class KGC:

    def __init__(self, group):

        self.group = group
        self.util = SecretUtil(group, verbose=False)
        self.setup()

    
    # =====================================================

    def setup(self):

        g = self.group.random(G1)

        alpha = self.group.random(ZR)
        beta = self.group.random(ZR)
        gamma = self.group.random(ZR)

        e_gg_alpha = pair(g,g) ** alpha

        pp = {
            'g': g,
            'e_gg_alpha': e_gg_alpha,
            'g_alpha_beta': g** (alpha*beta)
        }

        msk = {
            'alpha': alpha,
            'beta': beta,
            'gamma': gamma,
            'g_alpha': g ** alpha,
            'g_beta': g ** beta
        }

        elg_pk = g ** (alpha * gamma)
        elg_sk = gamma

        self.pp = pp
        self.msk = msk

        return pp, msk, elg_pk, elg_sk
    
    # -------------------------------------------

    def generate_re_encryption_key(self, policy):

        policy = self.util.createPolicy(policy)
        g = self.pp['g']

        beta = self.msk['beta']
        gamma = self.msk['gamma']

        r = self.group.random(ZR)
        r_prime = self.group.random(ZR)
        s = self.group.random(ZR)

        r2 = r+r_prime

        rk0 = g ** (s * (gamma ** -1))
        rk1 = g ** (r2 * beta)

        shares = self.util.calculateSharesDict(s, policy)
        print(shares)

        C3_prime = {}
        C4_prime = {}

        for attr, lambda_i in shares.items():
            
            attr = self.util.strip_index(attr)
            attr = attr.strip().upper()
            h = self.group.hash(attr, G1)

            ri = self.group.random(ZR)
            print(attr)

            C3_prime[attr] = ((g**(beta*lambda_i)) * (h**(-ri)))
            C4_prime[attr] = g**ri

        rk = {
            'rk0': rk0,
            'rk1': rk1
        }

        rk_secret = {
            'r': r,
            'r_prime': r_prime
        }

        abe_components = {
            'g_s': g**s,
            'C3_prime': C3_prime,
            'C4_prime': C4_prime,
            'policy': policy
        }

        return rk, rk_secret, abe_components
    
    # =======================================================================

    def generate_user_key(self,attrs, rk_secret):

        g = self.pp['g']

        alpha = self.msk['alpha']
        beta = self.msk['beta']

        r = rk_secret['r']
        r_prime = rk_secret['r_prime']

        d0 = g**(alpha + r*beta)
        d1 = g**(r_prime*beta)
        d2 = g**r
        d3 = g**r_prime

        hx_r = {}
        hx_r_prime = {}

        for attr in attrs:

            attr = self.util.strip_index(attr)
            attr = attr.strip().upper()
            h = self.group.hash(attr, G1)

            hx_r[attr] = h**r
            hx_r_prime[attr] = h**r_prime

        return {
            'd0': d0,
            'd1': d1,
            'd2': d2,
            'd3': d3,
            'hx_r': hx_r,
            'hx_r_prime': hx_r_prime
        }
