from charm.toolbox.pairinggroup import GT, pair
from charm.toolbox.secretutil import SecretUtil


class ThirdParty:

    def __init__(self, group, pp):

        self.group = group
        self.pp = pp

        self.util = SecretUtil(group, verbose=False)

    # ================================================================

    def decrypt(self, ct_abe, sk_abe, user_attrs):

        policy = ct_abe['policy']
        pruned = self.util.prune(policy, user_attrs)

        if not pruned:
            raise Exception("Policy not satisfied")
        
        coeffs = self.util.getCoefficients(policy)

        numerator = pair(
            ct_abe['C2_prime'],
            sk_abe['d0'] * sk_abe['d1']
        )

        denominator = self.group.init(GT, 1)

        for node in pruned:

            attr = node.getAttributeAndIndex()
            coeff = coeffs[attr]

            term1 = pair(
                ct_abe['C3_prime'][attr],
                sk_abe['d2'] * sk_abe['d3']
            )

            term2 = pair(
                ct_abe['C4_prime'][attr],
                sk_abe['hx_r'][attr] * sk_abe['hx_r_prime'][attr]
            )

            denominator*= (term1 * term2) ** coeff
        
        d = numerator / denominator

        return ct_abe['C1_prime'] / d

