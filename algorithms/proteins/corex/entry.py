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
    'pdb':         dict(io_type=_types['pdb'],
                        default_value=None,
                        desc='The input PDB file.'),
    'window_size': dict(io_type=_types['float>1'],
                        default_value=10,
                        desc='The protein folding unit size. Also, the number of partition schemes.'),
    'min_size':    dict(io_type=_types['float>1'],
                        default_value=4,
                        desc='The minumum protein folding unit size.'),
    'samples':     dict(io_type=_types['float>1'],
                        default_value=10000,
                        desc='(Ignore for exhaustive sampling) The sample number for each partition scheme. Total sample number=samples*window_size.'),
    'sampler':     dict(io_type=_types['corex-sampler'],
                        default_value='exhaustive',
                        desc='The COREX states sampler'),
    'threshold':   dict(io_type=_types['float>0'],
                        default_value=0.75,
                        desc='(Ignore for exhaustive sampling) The threshold for the sampler.'),
    'sconf_weight':  dict(io_type=_types['float>0'],
                          default_value=1.0,
                          desc='Entropy factor.'),
    'base_fraction': dict(io_type=_types['float>0'],
                          default_value=1.0,
                          desc='The base fraction used to sum all COREX (ln_kf) values.'),
    'probe_radius': dict(io_type=_types['float>1'],
                         default_value=1.4,
                         desc='The probe radius for SASA in A.'),
    'n_points':     dict(io_type=_types['float>1'],
                         default_value=1000,
                         desc='The number of test points in Shrake & Rupley algorithm for SASA.'),
}
out_params={
    'corex':  dict(io_type=_types['corex'],
                   default_value=None,
                   desc='The COREX values. The order is the same order as the PDB.'),
}

from corex import corex
def main(pdb, window_size, min_size, samples,
         sampler, threshold, sconf_weight,
         base_fraction, probe_radius, n_points,
         resources={}):
    corex_values = corex(pdb, window_size=int(window_size), min_size=int(min_size),
                         samples=int(samples), sampler=sampler, threshold=threshold,
                         sconf_weight=sconf_weight, base_fraction=base_fraction,
                         probe_radius=probe_radius, point_number=int(n_points),
                         worker_num=-1, gpu_num=-1)
    return dict(corex=corex_values)
