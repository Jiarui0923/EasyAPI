id='corex'
name='(COREX) CORrelation with hydrogen EXchange protection factors'
description='An algorithm designed to compute comformational stability of a protein. The results will be an array concatenated by the order of sorted(chains)'
version='0.0.1'
references=[]
required_resources={'cpu':-1, 'cuda':-1}
_types = {
    'pdb': dict(id='pdb',
                meta='string',
                name='PDB File',
                doc='The protein PDB file',
                condition=None,
                version='0.0.1'),
    'float>1': dict(id='float-greater-than-1',
                meta='number',
                name='float>1',
                doc='The float number that is greater than 1.',
                condition={'min':1},
                version='0.0.1'),
    'float>0': dict(id='float-greater-than-0',
                meta='number',
                name='float>0',
                doc='The float number that is greater than 0.',
                condition={'min':0},
                version='0.0.1'),
    'corex-sampler': dict(id='corex-sampler',
                meta='string',
                name='COREX Sampler',
                doc='(exhaustive|montecarlo|adaptive) The COREX micro-states sampler, which could be exhaustive enumerate, Monte Carlo, or Adaptibe Monte Carlo sampler.',
                condition='(exhaustive|montecarlo|adaptive)',
                version='0.0.1'),
    'corex': dict(id='corex',
                  meta='numarray',
                  name='COREX (ln(kf)) Values',
                  doc='COREX Values in Sorted Chain ID Order',
                  condition=None,
                  version='0.0.1')
}
in_params={
    'pdb':   _types['pdb'],
    'window_size': _types['float>1'],
    'min_size': _types['float>1'],
    'samples': _types['float>1'],
    'sampler': _types['corex-sampler'],
    'threshold': _types['float>0'],
    'sconf_weight': _types['float>0'],
    'probe_radius': _types['float>1'],
    'n_points': _types['float>1'],
}
out_params={
    'corex':  _types['corex'],
}

from corex import corex
def main(pdb, window_size, min_size, samples,
         sampler, threshold, sconf_weight,
         base_fraction, probe_radius, n_points,
         resources={}):
    corex_values = corex(pdb, window_size=int(window_size), min_size=int(min_size),
                         samples=int(samples), sampler=sampler, threshold=threshold,
                         sconf_weight=sconf_weight, base_fraction=base_fraction,
                         probe_radius=probe_radius, point_number=n_points,
                         worker_num=-1, gpu_num=-1)
    return dict(corex=corex_values)
