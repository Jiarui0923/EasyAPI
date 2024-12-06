from ._apl import get_apl
from ..types import Entropy, BFactor, COREX, SASA
from ..types import PeptideLikelihood, ResidueLikelihood, APLAggregate
from ..types import PositiveNumber, NumberGreateThan1, Number
from easyapi import register, cache

@register(required_resources={'cpu':1, 'cuda':0})
@cache(disable=True)
def apl(sequence_entropy: Entropy['The sequence entropy of the given sequence based on the alignments.'],
        bfactor: BFactor['The B-Factor. The order is the same order as the PDB.'],
        corex: COREX['The COREX values. The order is the same order as the PDB.'],
        sasa: SASA['The solvent accessible surface area.'],
        mer_size: NumberGreateThan1['The size of each mer of the sequence.'] = 15,
        hop: NumberGreateThan1['The size of each hop of mers.'] = 7,
        flank_size: NumberGreateThan1['The flank size of APL.'] = 20,
        loop_size: NumberGreateThan1['The loop size of APL.'] = 21,
        w_entropy: Number['The weight for entropy.'] = 0.3474973544973545,
        w_bfactor: Number['The weight for B-factor.'] = 0.1643121693121693,
        w_corex: Number['The weight for COREX.'] = 0.2651851851851852,
        w_sasa: Number['The weight for SASA.'] =0.22300529100529098,
        resources = {}) -> dict[
            ResidueLikelihood['residue_likelihood', 'Residue Level Likelihood.'],
            PeptideLikelihood['peptide_likelihood', 'Peptide Level Likelihood.'],
            APLAggregate['apl_aggregate', 'Residue Level Aggregated Score.']
        ]:
    '''(APL) Antigen Processing Likelihood
    Calculate APL by Sequence Entropy, B-Factor, SASA, and COREX.
    '''
    residue_likelihood, peptide_likelihood, aggregate_zscores = get_apl(seq_entropy=sequence_entropy, bfactor=bfactor, corex=corex, sasa=sasa,
                                                                        mer_size=int(mer_size), hop=int(hop), flank_size=int(flank_size), loop_size=int(loop_size),
                                                                        w_seq_entropy=w_entropy, w_bfactor=w_bfactor, w_sasa=w_sasa, w_corex=w_corex)
    return dict(residue_likelihood=residue_likelihood, peptide_likelihood=peptide_likelihood, apl_aggregate=aggregate_zscores)
