from biopandas.pdb import PandasPdb
import warnings

def get_bfactor(pdb, record='ATOM'):
    warnings.filterwarnings('ignore')
    _pdb_lines = str(pdb).splitlines(True)
    _pdb_df = PandasPdb()._construct_df(_pdb_lines)
    if record == 'ATOM': return _pdb_df['ATOM'].b_factor.to_list()
    elif record == 'HETATM': return  _pdb_df['HETATM'].b_factor.to_list()
    else: raise ValueError(f'{record} Not A Acceptable Record Name.')