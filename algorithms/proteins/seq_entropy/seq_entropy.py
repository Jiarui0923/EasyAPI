import numpy as np
import tempfile
import random
import string

import warnings
warnings.filterwarnings('ignore')
from Bio.Align.Applications import ClustalOmegaCommandline
from Bio import AlignIO

def entropy_calc(alignment):
    unmasked_array = np.array(alignment, 'S1')
    AA_list = [b'G', b'A', b'V', b'L', b'I',
               b'M', b'F', b'W', b'P',
               b'S', b'T', b'C', b'Y',
               b'N', b'Q', b'D', b'E',
               b'K', b'R', b'H', b'-']

    new_array = unmasked_array
    correctionfactor = 0
    for ind in range(0, unmasked_array.shape[1]):
        if unmasked_array[-1][ind] == b'-':
            new_array = np.delete(new_array, (ind-correctionfactor), 1)
            correctionfactor += 1        
    entropies = []
    for column in new_array.T:
        AA_count_dict = dict.fromkeys(AA_list, 0)
        sumentropies = []
        for residue in column:
            for key in AA_count_dict:
                if key == residue: AA_count_dict[key] += 1
        for key in AA_count_dict:
            frequency = AA_count_dict[key]/new_array.shape[0]
            if frequency != 0.0:
                singentropy = frequency*float(np.log(frequency))
                sumentropies.append(singentropy)
        sumentropy = -(sum(sumentropies))
        entropies.append(sumentropy)
    return entropies


# ===========================================================
# Author: Jai Bansal
# Created Date: 2024-11-01
# Update: Jai Bansal
# Updated Date: 2024-11-22
# Updated Comment: Changed hyperparameters
# Description: Calculates sequence entropy and extracts B-Factors
# ===========================================================
def get_entropy(sequence, alignment):
    """
    Run a computation to calculate the solvent-accessible surface area (SASA) for a molecular structure from a PDB file and extracts the bFactors

    Parameters
    ----------
        pdb_path: str
            Path to the PDB file containing the molecular structure to be analyzed.

        algorithm: str, [optional, default: 'Shrake-Rupley']
            The algorithm to use for calculating the solvent-accessible surface area. Common choices are 'Shrake-Rupley' and 'Lee-Richards'.

        probe_radius: float, [optional, default: 1.4]
            The radius of the solvent probe, usually representing the size of a water molecule. Default is 1.4 Å.

        n_points: int, [optional, default: 100]
            Number of points used for sampling the surface. Higher values improve accuracy but increase computational cost.

        n_slices: int, [optional, default: 20]
            Number of slices used for sampling in cylindrical coordinates. This parameter affects the resolution of the SASA calculation.

        n_threads: int, [optional, default: 1]
            Number of threads to use for parallel computation. Increasing this value can speed up calculations by using multiple cores.
        
    Returns
    -------
     PDBfile, calculated entropies, extracted bFactors, asa results
        
    """
    with tempfile.NamedTemporaryFile(delete=True) as in_file:
        with tempfile.NamedTemporaryFile(delete=True) as out_file:
            with tempfile.NamedTemporaryFile(delete=True) as query_file:
                in_file.write(alignment.encode())
                in_file.flush()
                query_file.write(f'>{random.sample(string.ascii_letters, 16)}\n{sequence}\n'.encode())
                query_file.flush()
                clustalomega_cline = ClustalOmegaCommandline(infile=in_file.name, outfile=out_file.name,
                                                            outfmt='fasta', force=True,
                                                            profile1 = query_file.name, dealign = True,
                                                            seqtype = "Protein")
                clustalomega_cline()
                alignment = AlignIO.read(out_file.name, 'fasta')
                entropies = entropy_calc(alignment)
                return entropies