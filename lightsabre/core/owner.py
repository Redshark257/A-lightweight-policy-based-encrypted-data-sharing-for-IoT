from charm.toolbox.pairinggroup import ZR

class DataOwner:

    def __init__(self, group, pp, elg_pk):

        self.group = group
        self.pp = pp
        self.elg_pk = elg_pk

    # =====================================================


    def encrypt(self, message_gt, policy):

        g = self.pp['g']
        e_gg_alpha = self.pp['e_gg_alpha']

        x = self.group.random(ZR)

        C1 = message_gt * (e_gg_alpha ** x)
        C2 = g ** x
        C3 = self.elg_pk ** x

        ct_elg = {
            'C1': C1,
            'C2': C2,
            'C3': C3
        }

        return {
            'ciphertext': ct_elg,
            'policy': policy
        }
    
    