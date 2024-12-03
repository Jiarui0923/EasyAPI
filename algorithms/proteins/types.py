from easyapi.annotations import String
from easyapi.annotations import NumArray
from easyapi.annotations import Number
from easyapi.annotations import NumberGreateThan1
from easyapi.annotations import PositiveNumber

class Sequence(String):
    id        = 'protein-seq'
    name      = 'Protein Amio Acid Sequence'
    doc       = 'The protein amio acid sequence'
    condition = '[ACDEFGHIKLMNPQRSTVWY?]+'
    
class FASTA(String):
    id        = 'fasta'
    name      = 'FASTA Sequence'
    doc       = 'The FASTA sequence file'
    
class Entropy(NumArray):
    id        = 'sequence-entropy'
    name      = 'Sequence Entropy Values'
    doc       = 'Sequence Entropy Values in Sorted Chain ID Order'

class PDB(String):
    id        = 'pdb'
    name      = 'PDB File'
    doc       = 'The protein PDB file.'
    
class Chain(String):
    id        = 'chain-ids'
    name      = 'PDB Chain IDs'
    doc       = 'The protein chain ids, seperate with `,`, no blank character.'
    condition = '[A-Za-z0-9]+(,[A-Za-z0-9]+)*'
    
class SASA(NumArray):
    id        = 'sasa'
    name      = 'SASA Values'
    doc       = 'SASA Values in Sorted Chain ID Order.'
    
class SASAlgorithm(String):
    id        = 'sasa-algorithm'
    name      = 'SASA Algorithm'
    doc       = '(ShrakeRupley|LeeRichards) The SASA Algorithm that could be ShrakeRupley or LeeRichards.'
    condition = '(ShrakeRupley|LeeRichards)'