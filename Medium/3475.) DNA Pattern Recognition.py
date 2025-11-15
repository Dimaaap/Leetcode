import pandas as pd


def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    samples["has_start"] = samples["dna_sequence"].str.startswith("ATG").astype(int)
    samples["has_stop"] = samples["dna_sequence"].str.endswith(("TAA", "TAG", "TGA")).astype(int)
    samples["has_atat"] = samples["dna_sequence"].str.contains("ATAT").astype(int)
    samples["has_ggg"] = samples["dna_sequence"].str.contains("GGG").astype(int)
    return samples


data = [[1, 'ATGCTAGCTAGCTAA', 'Human'], [2, 'GGGTCAATCATC', 'Human'], [3, 'ATATATCGTAGCTA', 'Human'], [4, 'ATGGGGTCATCATAA', 'Mouse'], [5, 'TCAGTCAGTCAG', 'Mouse'], [6, 'ATATCGCGCTAG', 'Zebrafish'], [7, 'CGTATGCGTCGTA', 'Zebrafish']]

samples_df = pd.DataFrame(data, columns=['sample_id', 'dna_sequence', 'species'])
print(analyze_dna_patterns(samples_df))