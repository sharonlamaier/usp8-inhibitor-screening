import pandas as pd
from rdkit.Chem import MolFromSmiles, rdFingerprintGenerator

def load_data(file):
    df = pd.read_csv(file)
    return df

def rdfp_gen(df):
    rdkitfpgen = rdFingerprintGenerator.GetRDKitFPGenerator(fpSize=2048)
    molecule = [MolFromSmiles(i) for i in df['SMILES']]
    rdkitfp = [(rdkitfpgen.GetFingerprint(mol)) for mol in molecule]
    tup = [tuple(i) for i in rdkitfp]
    rdfp_list = [list(i) for i in tup]
    rdfp_df = pd.DataFrame(rdfp_list)
    return rdfp_df