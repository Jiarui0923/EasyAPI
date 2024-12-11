from ..types import Entropy, BFactor, COREX, SASA
from ..types import ResidueLikelihood, APLAggregate
from ..types import APLTable
from easyapi import register, cache

import json
import numpy as np

def zscore(x):
    x = np.array(x)
    z = (x - np.mean(x)) / np.std(x)
    return z.tolist()

@register(required_resources={'cpu':1, 'cuda':0})
@cache(disable=True)
def apl_aggregate(sequence_entropy: Entropy['The sequence entropy of the given sequence based on the alignments.'],
        bfactor: BFactor['The B-Factor. The order is the same order as the PDB.'],
        corex: COREX['The COREX values. The order is the same order as the PDB.'],
        sasa: SASA['The solvent accessible surface area.'],
        apl_aggregate: APLAggregate['The size of each mer of the sequence.'],
        residue_likelihood: ResidueLikelihood['The size of each hop of mers.'],
        resources = {}) -> dict[
            APLTable['apl_table', 'Combined APL and its components values.'],
        ]:
    '''APL Result Aggregator
    Aggregate BFactor, SASA, COREX, Sequenc Entropy, and APL together to be an intigrated table.
    '''
    data = {
        'B-Factor': zscore(bfactor),
        'SASA': zscore(sasa),
        'COREX': zscore(corex),
        'Sequence Entropy': zscore(sequence_entropy),
        'Aggregate': zscore(apl_aggregate),
        'APL': zscore(residue_likelihood),
    }
    data = json.dumps(data, indent=2)
    return dict(apl_table=data)
