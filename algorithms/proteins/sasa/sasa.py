import freesasa
from io import StringIO
from Bio.PDB import PDBParser
from uuid import uuid4
def sasa(pdb:str,
         algorithm:str='ShrakeRupley',
         probe_radius:float=1.4,
         n_points:int=1000,
         n_slices:int=20,
         worker_num:int=1):
    pdb_io = StringIO(pdb)
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(str(uuid4()), pdb_io)
    structure = freesasa.structureFromBioPDB(structure)
    sasa_params = freesasa.Parameters({
        'algorithm'    : algorithm, 
        'probe-radius' : probe_radius, 
        'n-points'     : n_points,
        'n-slices'     : n_slices, 
        'n-threads'    : worker_num,
    })
    sasa_values = freesasa.calc(structure, sasa_params).residueAreas()
    sasa_data = {}
    for chain_id, chain_data in sasa_values.items():
        res_data = [item.relativeTotal for item in chain_data.values()]
        sasa_data[chain_id] = res_data
    sasa_values_list = []
    for key in sorted(sasa_data): sasa_values_list += sasa_data[key]
    return sasa_values_list