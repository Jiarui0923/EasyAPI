from ..types import Sequence, Alleles, NumberGreateThan1, MHCIIMethods, MHCII
from easyapi import register, cache
from _mhcii import get_mhcii

@register(required_resources={'cpu':1, 'cuda':0})
@cache(disable=True)
def mhcii(sequence: Sequence['The sequence for MHCII search.'],
         alleles: Alleles['The alleles for this sequence, seperate by `,`.'] = "HLA-DRB1*03:01",
         mer_size: NumberGreateThan1['The size of each mer of the sequence.'] = 15,
         hop: NumberGreateThan1['The size of each mer of the sequence.'] = 7,
         method: NumberGreateThan1['The method used to compute MHC-II binding.'] = 'recommended',
         resources={}) -> dict[
             MHCII['mhcii', 'The MHC-II binding outputs from IEDB following JSON formats']
         ]:
    '''Get MHC-II Binding Prediction
    Use IEDB to predict the MHC-II binding.
    '''
    alleles = [allel for allel in alleles.split(',') if len(allel) > 0]
    _mhcii = get_mhcii(sequence=sequence, mer_size=int(mer_size),
                       hop=int(hop), method=method,
                       alleles=alleles)
    return dict(mhcii=_mhcii)