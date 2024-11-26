id='seq-entropy'
name='Sequence Entropy'
description='Compute sequence entropy for the given sequence and BLAST outputs.'
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
    'fasta': dict(id='fasta',
                  meta='string',
                  name='FASTA Sequence',
                  doc='The FASTA sequence file',
                  condition=None,
                  version='0.0.1'),
    'entropy': dict(id='sequence-entropy',
                 meta='numarray',
                 name='Sequence Entropy Values',
                 doc='Sequence Entropy Values in Sorted Chain ID Order',
                 condition=None,
                 version='0.0.1')
}
in_params={
    'sequence': dict(io_type=_types['protein_seq'],
                     default_value=None,
                     desc='The protein amio acid sequence. The order is the same order as the PDB.'),
    'alignment': dict(io_type=_types['fasta'],
                  default_value=None,
                  desc='The BLAST outpus in FASTA format for the given sequence.'),
}
out_params={
    'sequence_entropy': dict(io_type=_types['entropy'],
                  default_value=None,
                  desc='The sequence entropy of the given sequence based on the alignments.'),
}

from seq_entropy import get_entropy
def main(sequence, alignment, resources={}):
    _entropy = get_entropy(sequence=sequence, alignment=alignment)
    return dict(sequence_entropy=_entropy)
