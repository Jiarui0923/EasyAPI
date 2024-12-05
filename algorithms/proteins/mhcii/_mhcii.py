import requests
import pandas as pd
import io


def iedb_mhcii(sequence, mer_size=15, hop = 7, method='recommended',
               alleles=["HLA-DRB1*03:01", "HLA-DRB1*07:01", "HLA-DRB1*15:01", "HLA-DRB3*01:01", "HLA-DRB3*02:02", "HLA-DRB4*01:01", "HLA-DRB5*01:01"]):

    peptides = []
    for i in range(0, len(sequence) - mer_size + 1, hop):
        peptide = sequence[i:i + mer_size]
        peptides.append(peptide)

    fasta_sequences = "\n".join([f">peptide{i+1}\n{peptides[i]}" for i in range(len(peptides))])

    url = "http://tools-cluster-interface.iedb.org/tools_api/mhcii/"
    data = {
        "method": method,
        "sequence_text": fasta_sequences,
        "allele": ','.join(alleles)
    }

    response = requests.post(url, data=data)

    if response.status_code != 200: raise ConnectionError(f"{response.text}")

    mhcii_res = pd.read_csv(io.StringIO(response.text), sep='\t')
    if 'peptide' not in mhcii_res.columns:
        raise ValueError("Expected 'peptide' column not found in response.")

    pivot_df = mhcii_res.pivot(index='peptide', columns='allele', values='rank')
    pivot_df = pivot_df.fillna(0)
    pivot_df = pivot_df.reset_index()

    pivot_df.rename(columns={'peptide': 'Peptide'}, inplace=True)

    peptides_df_ = None
    for p in peptides:
        if p in pivot_df['Peptide'].values:
            if peptides_df_ is None: peptides_df_ = pivot_df[pivot_df['Peptide'] == p]
            else: peptides_df_ = pd.concat([peptides_df_, pivot_df[pivot_df['Peptide'] == p]])
    return peptides_df_.reset_index(drop=True)

def get_mhcii(sequence, mer_size=15, hop = 7, method='recommended',
               alleles=["HLA-DRB1*03:01"]):
    _mhcii_data = iedb_mhcii(sequence=sequence, mer_size=mer_size, hop=hop,
                             alleles=alleles)
    return _mhcii_data.to_json(index=False)