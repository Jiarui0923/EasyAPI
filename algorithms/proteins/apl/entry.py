id='apl'
name='(APL) Antigen Processing Likelihood'
description='Calculate APL by Sequence Entropy, B-Factor, SASA, and COREX.'
version='0.0.1'
references=[]
required_resources={'cpu':-1, 'cuda':0}
_types = {
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
    'sasa': dict(id='sasa',
                 meta='numarray',
                 name='SASA Values',
                 doc='SASA Values in Sorted Chain ID Order',
                 condition=None,
                 version='0.0.1'),
    'corex': dict(id='corex',
                  meta='numarray',
                  name='COREX (ln(kf)) Values',
                  doc='COREX Values in Sorted Chain ID Order',
                  condition=None,
                  version='0.0.1'),
    'bfactor': dict(id='bfactor',
                  meta='numarray',
                  name='B-Factor Values',
                  doc='B-Factor values in given PDB file atom orders',
                  condition=None,
                  version='0.0.1'),
    'entropy': dict(id='sequence-entropy',
                 meta='numarray',
                 name='Sequence Entropy Values',
                 doc='Sequence Entropy Values in Sorted Chain ID Order',
                 condition=None,
                 version='0.0.1'),
    'residue_likelihood': dict(id='apl-residue-likelihood',
                 meta='numarray',
                 name='Residue Likelihood',
                 doc='Residue Level Likelihood',
                 condition=None,
                 version='0.0.1'),
    'peptide_likelihood': dict(id='apl-peptide-likelihood',
                 meta='numarray',
                 name='Peptide Likelihood',
                 doc='Peptide Level Likelihood',
                 condition=None,
                 version='0.0.1'),
    'aggregate': dict(id='apl-aggregate',
                 meta='numarray',
                 name='Residue Level Aggregated Score',
                 doc='Residue Level Aggregated Score',
                 condition=None,
                 version='0.0.1'),
}
in_params={
    'entropy': dict(io_type=_types['entropy'],
                  default_value=None,
                  desc='The sequence entropy of the given sequence based on the alignments.'),
    'bfactor': dict(io_type=_types['bfactor'],
                    default_value=None,
                    desc='The B-Factor. The order is the same order as the PDB.'),
    'corex':  dict(io_type=_types['corex'],
                   default_value=None,
                   desc='The COREX values. The order is the same order as the PDB.'),
    'sasa':  dict(io_type=_types['sasa'],
                  default_value=None,
                  desc='The solvent accessible surface area.'),
    'mer_size': dict(io_type=_types['float>1'],
                   default_value=15,
                   desc='The size of each mer of the sequence.'),
    'hop': dict(io_type=_types['float>1'],
                   default_value=7,
                   desc='The size of each hop of mers.'),
    'flank_size': dict(io_type=_types['float>1'],
                   default_value=20,
                   desc='The flank size of APL.'),
    'loop_size': dict(io_type=_types['float>1'],
                   default_value=21,
                   desc='The loop size of APL.'),
    'w_entropy': dict(io_type=_types['float>0'],
                   default_value=0.3474973544973545,
                   desc='The weight for entropy.'),
    'w_bfactor': dict(io_type=_types['float>0'],
                   default_value=0.1643121693121693,
                   desc='The weight for B-factor.'),
    'w_corex': dict(io_type=_types['float>0'],
                   default_value=0.2651851851851852,
                   desc='The weight for COREX.'),
    'w_sasa': dict(io_type=_types['float>0'],
                   default_value=0.22300529100529098,
                   desc='The weight for SASA.'),
}
out_params={
    'residue_likelihood': dict(io_type=_types['residue_likelihood'],
                                default_value=None,
                                desc='Residue Level Likelihood.'),
    'peptide_likelihood': dict(io_type=_types['peptide_likelihood'],
                                default_value=None,
                                desc='Peptide Level Likelihood.'),
    'aggregate': dict(io_type=_types['aggregate'],
                                default_value=None,
                                desc='Residue Level Aggregated Score.'),
}

from apl import get_apl
def main(entropy, bfactor, corex, sasa,
        mer_size=15, hop=7, flank_size=20, loop_size=21,
        w_entropy=0.3474973544973545,
        w_bfactor=0.1643121693121693,
        w_corex=0.2651851851851852,
        w_sasa=0.22300529100529098,
        resources={}):
    residue_likelihood, peptide_likelihood, aggregate_zscores = get_apl(seq_entropy=entropy, bfactor=bfactor, corex=corex, sasa=sasa,
                                                                        mer_size=int(mer_size), hop=int(hop), flank_size=int(flank_size), loop_size=int(loop_size),
                                                                        w_seq_entropy=w_entropy, w_bfactor=w_bfactor, w_sasa=w_sasa, w_corex=w_corex)
    return dict(residue_likelihood=residue_likelihood, peptide_likelihood=peptide_likelihood, aggregate=aggregate_zscores)
