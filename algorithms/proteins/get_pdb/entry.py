id='get-pdb'
name='Get PDB file'
description='Get PDB file by PDB ID.'
version='0.0.1'
references=[]
required_resources={'cpu':1, 'cuda':0}
_types = {
    'pdbid': dict(id='pdbid',
                  meta='string',
                  name='PDB ID',
                  doc='The PDB ID, which can be 4 chars for RCSB or 6 chars for UniProt.',
                  condition='[A-Za-z0-9]{4}|[A-Za-z0-9]{6}',
                  version='0.0.1'),
    'source': dict(id='source',
                  meta='string',
                  name='The PDB Source',
                  doc='(alphafold2-v3|alphafold2-v4) The PDB fetch source which could be alphafold2-v3 or alphafold2-v4',
                  condition='alphafold2-v3|alphafold2-v4',
                  version='0.0.1'),
    'pdb': dict(id='pdb',
                meta='string',
                name='PDB File',
                doc='The protein PDB file',
                condition=None,
                version='0.0.1'),
}
in_params={
    'pdb_id': dict(io_type=_types['pdbid'],
                   default_value=None,
                   desc='The PDB ID or UniProt ID.'),
    'source': dict(io_type=_types['source'],
                   default_value='alphafold2-v4',
                   desc='(Ignore for 4 chars PDB ID) The PDB fetch source for UniProt.'),
}
out_params={
    'pdb':    dict(io_type=_types['pdb'],
                   default_value=None,
                   desc='The fetched PDB file.'),
}

from get_pdb import get_pdb
def main(pdb_id, source, resources={}):
    _pdb = get_pdb(pdb_id=pdb_id, source=source)
    return dict(pdb=_pdb)
