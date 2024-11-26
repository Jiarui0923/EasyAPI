id='get-seq'
name='Get Protein Sequence'
description='Extract the amio acid sequence of the given protein.'
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
    'protein_seq': dict(id='protein-seq',
                  meta='string',
                  name='Protein Amio Acid Sequence',
                  doc='The protein amio acid sequence',
                  condition='[ACDEFGHIKLMNPQRSTVWY?]+',
                  version='0.0.1'),
}
in_params={
    'pdb':    dict(io_type=_types['pdb'],
                   default_value=None,
                   desc='The input PDB file.'),
}
out_params={
    'sequence': dict(io_type=_types['protein_seq'],
                     default_value=None,
                     desc='The protein amio acid sequence. The order is the same order as the PDB.'),
}

from get_seq import get_seq
def main(pdb, resources={}):
    _seq = get_seq(pdb=pdb)
    return dict(sequence=_seq)
