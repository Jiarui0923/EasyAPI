id='select-chain'
name='Select Chains from PDB File'
description='Select destinated chains from the given PDB file.'
version='0.0.1'
references=[]
required_resources={'cpu':1, 'cuda':0}
_types = {
    'pdb': dict(id='pdb',
                meta='string',
                name='PDB File',
                doc='The protein PDB file',
                condition=None,
                version='0.0.1'),
    'chain': dict(id='chain-ids',
                  meta='string',
                  name='PDB Chain IDs',
                  doc='The protein chain ids, seperate with `,`, no blank character.',
                  condition='[A-Za-z0-9]+(,[A-Za-z0-9]+)*',
                  version='0.0.1'),
}
in_params={
    'pdb':   _types['pdb'],
    'chain': _types['chain'],
}
out_params={
    'pdb':   _types['pdb'],
}

from select_chain import select_chain
def main(pdb, chain, resources={}):
    _pdb_data = select_chain(pdb=pdb, chain=chain)
    return dict(pdb=_pdb_data)
