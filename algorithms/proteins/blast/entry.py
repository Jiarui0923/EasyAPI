id='blast'
name='BLAST Protein Sequence'
description='BLAST a provided protein sequence and return a FASTA formatted result.'
version='0.0.1'
references=[]
required_resources={'cpu':1, 'cuda':0}
_types = {
    'protein_seq': dict(id='protein-seq',
                  meta='string',
                  name='Protein Amio Acid Sequence',
                  doc='The protein amio acid sequence',
                  condition='[ACDEFGHIKLMNPQRSTVWY?]+',
                  version='0.0.1'),
    'algorithm':dict(id='blast-algorithm',
                meta='string',
                name='BLAST Algorithm',
                doc='The BLAST algorithm which could be `blastp` or `blastx`',
                condition='(blastp|blastx)',
                version='0.0.1'),
    'database': dict(id='blast-database',
                meta='string',
                name='BLAST Databases',
                doc='The BLAST database could be `uniref50`',
                condition='(uniref50)',
                version='0.0.1'),
    'fasta': dict(id='fasta',
                  meta='string',
                  name='FASTA Sequence',
                  doc='The FASTA sequence file',
                  condition=None,
                  version='0.0.1'),
    'matrix': dict(id='blast-matrix',
                meta='string',
                name='BLAST Matrix',
                doc=' Different matrices can affect the sensitivity for detecting homologous sequences.',
                condition='(BLOSUM45|BLOSUM50|BLOSUM62|BLOSUM80|BLOSUM90|PAM30|PAM70|PAM250)',
                version='0.0.1'),
    'float>0': dict(id='float-greater-than-0',
                meta='number',
                name='float>0',
                doc='The float number that is greater than 0.',
                condition={'min':0},
                version='0.0.1'),
    'float>1': dict(id='float-greater-than-1',
                meta='number',
                name='float>1',
                doc='The float number that is greater than 1.',
                condition={'min':1},
                version='0.0.1'),
}
in_params={
    'sequence': dict(io_type=_types['protein_seq'],
                     default_value=None,
                     desc='The protein amio acid sequence. The order is the same order as the PDB.'),
    'algorithm': dict(io_type=_types['algorithm'],
                     default_value='blastp',
                     desc='The BLAST algorithm which could be `blastp` or `blastx`'),
    'db': dict(io_type=_types['database'],
               default_value='uniref50',
               desc='The BLAST database could be `uniref50`'),
    'expect_value': dict(io_type=_types['float>0'],
                         default_value=10,
                         desc='The expect threshold sets the maximum e-value threshold for hits to be reported. Lower values make the search more stringent.'),
    'word_size': dict(io_type=_types['float>0'],
                      default_value=3,
                      desc='This is the size of initial words or seed matches used in the search. Smaller values increase sensitivity but can slow down the search.'),
    'max_target_seqs': dict(io_type=_types['float>1'],
                       default_value=500,
                       desc='Specifies the maximum number of aligned sequences to return. Increasing this will yield more hits.'),
    'matrix': dict(io_type=_types['matrix'],
                   default_value='BLOSUM62',
                   desc='Different matrices can affect the sensitivity for detecting homologous sequences.'),
}
out_params={
    'blast': dict(io_type=_types['fasta'],
                  default_value=None,
                  desc='The BLAST outpus in FASTA format.'),
}

from blast import blast_fasta
import os
def main(sequence, algorithm='blastp', db='uniref50',
         expect_value=10, word_size=3, max_target_seqs=500,
         matrix='BLOSUM62', resources={}):
    _seq = blast_fasta(sequence=sequence, algorithm=algorithm, db=db,
                       num_worker=os.cpu_count(), expect_value=expect_value,
                       word_size=int(word_size), max_target_seqs=int(max_target_seqs),
                       matrix=matrix)
    return dict(blast=_seq)
