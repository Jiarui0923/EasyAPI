id='mhcii'
name='Get MHC-II Binding Prediction'
description='Use IEDB to predict the MHC-II binding.'
version='0.0.1'
references=[]
required_resources={'cpu':1, 'cuda':0}
_types = {
    'json': dict(id='json',
                meta='string',
                name='JSON File',
                doc='The JSON format file',
                condition=None,
                version='0.0.1'),
    'protein_seq': dict(id='protein-seq',
                  meta='string',
                  name='Protein Amio Acid Sequence',
                  doc='The protein amio acid sequence',
                  condition='[ACDEFGHIKLMNPQRSTVWY?]+',
                  version='0.0.1'),
    'alleles': dict(id='alleles',
                  meta='string',
                  name='Protein Amio Acid Sequence',
                  doc='The protein amio acid sequence',
                  condition=None,
                  version='0.0.1'),
    'float>1': dict(id='float-greater-than-1',
                meta='number',
                name='float>1',
                doc='The float number that is greater than 1.',
                condition={'min':1},
                version='0.0.1'),
    'methods': dict(id='mhcii-methods',
                  meta='string',
                  name='The IEDB MHC-II Methods',
                  doc='The IEDB MHC-II prediction methods.',
                  condition='(recommended|ann|consensus|netmhccons|netmhcpan|netmhcstabpan|pickpocket|smm|smmpmbec)',
                  version='0.0.1'),
}
in_params={
    'sequence': dict(io_type=_types['protein_seq'],
                   default_value=None,
                   desc='The sequence for MHCII search.'),
    'alleles': dict(io_type=_types['alleles'],
                   default_value='HLA-DRB1*03:01',
                   desc='The alleles for this sequence, seperate by `,`.'),
    'mer_size': dict(io_type=_types['float>1'],
                   default_value=15,
                   desc='The size of each mer of the sequence.'),
    'hop': dict(io_type=_types['float>1'],
                   default_value=7,
                   desc='The size of each hop of mers.'),
    'method': dict(io_type=_types['methods'],
                   default_value='recommended',
                   desc='The method used to compute MHC-II binding.'),
    
}
out_params={
    'mhcii': dict(io_type=_types['json'],
                     default_value=None,
                     desc='The MHC-II binding outputs from IEDB following JSON formats'),
}

from mhcii import get_mhcii
def main(sequence, alleles="HLA-DRB1*03:01", mer_size=15,
         hop = 7, method='recommended', resources={}):
    alleles = [allel for allel in alleles.split(',') if len(allel) > 0]
    _mhcii = get_mhcii(sequence=sequence, mer_size=int(mer_size), hop=int(hop),
                       alleles=alleles)
    return dict(mhcii=_mhcii)
