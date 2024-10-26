id='sasa'
name='(SASA) Solvent Accessible Surface Area'
description='Calculate the solvent accessible surface area for the given protein. The results will be an array concatenated by the order of sorted(chains)'
version='0.0.1'
references=[]
required_resources={'cpu':-1, 'cuda':0}
_types = {
    'pdb': dict(id='pdb',
                meta='string',
                name='PDB File',
                doc='The protein PDB file',
                condition=None,
                version='0.0.1'),
    'algorithm': dict(id='sasa-algorithm',
                meta='string',
                name='SASA Algorithm',
                doc='(ShrakeRupley|LeeRichards) The SASA Algorithm that could be ShrakeRupley or LeeRichards.',
                condition='(ShrakeRupley|LeeRichards)',
                version='0.0.1'),
    'float>1': dict(id='float-greater-than-1',
                meta='number',
                name='float>1',
                doc='The float number that is greater than 1.',
                condition={'min':1},
                version='0.0.1'),
    'sasa': dict(id='sasa',
                 meta='numarray',
                 name='SASA Values',
                 doc='SASA Values in Sorted Chain ID Order',
                 condition=None,
                 version='0.0.1')
}
in_params={
    'pdb':   _types['pdb'],
    'algorithm': _types['algorithm'],
    'probe_radius': _types['float>1'],
    'n_points': _types['float>1'],
    'n_slices': _types['float>1'],
}
out_params={
    'sasa':  _types['sasa'],
}

from sasa import sasa
def main(pdb, algorithm, probe_radius, n_points, n_slices, resources={}):
    sasa_values = sasa(pdb,
                       algorithm=algorithm,
                       probe_radius=probe_radius,
                       n_points=int(n_points),
                       n_slices=int(n_slices),
                       worker_num=1)
    return dict(sasa=sasa_values)
