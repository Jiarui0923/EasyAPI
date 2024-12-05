from ._get_pdb import get_pdb as get_pdb_
from ..types import PDB, PDBID, PDBSource
from easyapi import register, cache

@register(required_resources={'cpu':1, 'cuda':0})
@cache(disable=True)
def get_pdb(pdb_id: PDBID['The PDB ID or UniProt ID.'],
            source: PDBSource['(Ignore for 4 chars PDB ID) The PDB fetch source for UniProt.'] = 'alphafold2-v4',
            resources = {}) -> dict[
                PDB['pdb': 'The fetched PDB file.']
            ]:
    _pdb = get_pdb_(pdb_id=pdb_id, source=source)
    return dict(pdb=_pdb)