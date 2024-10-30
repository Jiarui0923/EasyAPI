id='bfactor'
name='Get B-Factor'
description='Extract B-Factor from the given PDB file.'
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
    'record': dict(id='pdb-record',
                  meta='string',
                  name='PDB record',
                  doc='(ATOM|HETATM) PDB record names which could be ATOM or HETATM',
                  condition='(ATOM|HETATM)',
                  version='0.0.1'),
    'bfactor': dict(id='bfactor',
                  meta='numarray',
                  name='B-Factor Values',
                  doc='B-Factor values in given PDB file atom orders',
                  condition=None,
                  version='0.0.1')
}
in_params={
    'pdb':    dict(io_type=_types['pdb'],
                   default_value=None,
                   desc='The input PDB file.'),
    'record': dict(io_type=_types['record'],
                   default_value='ATOM',
                   desc='The PDB record for B-Factor extraction.'),
}
out_params={
    'bfactor': dict(io_type=_types['pdb'],
                    default_value=None,
                    desc='The B-Factor. The order is the same order as the PDB.'),
}

from bfactor import get_bfactor
def main(pdb, record, resources={}):
    _bfactor = get_bfactor(pdb=pdb, record=record)
    return dict(bfactor=_bfactor)
