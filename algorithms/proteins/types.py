from easyapi.annotations import String
from easyapi.annotations import NumArray
from easyapi.annotations import Number
from easyapi.annotations import NumberGreateThan1
from easyapi.annotations import PositiveNumber
from easyapi.annotations import JSONString

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
    
class PDBID(String):
    id        = 'pdbid'
    name      = 'PDB ID'
    doc       = 'The PDB ID, which can be 4 chars for RCSB or 6 chars for UniProt.'
    condition = '[A-Za-z0-9]{4}|[A-Za-z0-9]{6}'
    
class PDBSource(String):
    id        = 'pdb_source'
    name      = 'PDB Source'
    doc       = '(alphafold2-v3|alphafold2-v4) The PDB fetch source which could be alphafold2-v3 or alphafold2-v4'
    condition = 'alphafold2-v3|alphafold2-v4'
    
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
    
class Alleles(String):
    id        = 'alleles'
    name      = 'The Alleles Marks'
    doc       = 'The alleles marks seperate by `,`. The avaliable options are from iedb.org.'
    version   = '0.0.1'
    
class MHCIIMethods(String):
    id        = 'mhcii-methods'
    name      = 'The IEDB MHC-II Methods'
    doc       = 'The IEDB MHC-II prediction methods.'
    condition = '(recommended|ann|consensus|netmhccons|netmhcpan|netmhcstabpan|pickpocket|smm|smmpmbec)',
    version   = '0.0.1'
    
class MHCII(JSONString):
    id        = 'mhcii'
    name      = 'IEDB MHCII Predictions'
    doc       = 'A JSON file for MHCII prediction results.'
    version   = '0.0.1'
    
class COREXSampler(String):
    id        = 'corex-sampler'
    name      = 'COREX Sampler'
    doc       = '(exhaustive|montecarlo|adaptive) The COREX micro-states sampler, which could be exhaustive enumerate, Monte Carlo, or Adaptibe Monte Carlo sampler.'
    condition = '(exhaustive|montecarlo|adaptive)'
    version   = '0.0.1'
    
class COREX(NumArray):
    id        = 'corex'
    name      = 'COREX (ln(kf)) Values'
    doc       = 'COREX Values in Sorted Chain ID Order'
    version   = '0.0.1'