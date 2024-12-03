from ..types import Sequence, Fasta, Entropy
from easyapi import register, cache
from .seq_entropy import get_entropy

@register(required_resources={'cpu':1, 'cuda':0})
@cache(disable=True)
def seq_entropy(sequence: Sequence['The protein amio acid sequence. The order is the same order as the PDB.'],
                alignment: Fasta['The BLAST outpus in FASTA format for the given sequence.'],
                resources = {}) -> dict[
                    Entropy['sequence_entropy', 'The sequence entropy of the given sequence based on the alignments.']
                ]:
    """Sequence Entropy
    Compute sequence entropy for the given sequence and BLAST outputs.
    """
    _entropy = get_entropy(sequence=sequence, alignment=alignment)
    return dict(sequence_entropy=_entropy)