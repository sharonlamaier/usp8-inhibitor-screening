# USP8 Inhibitor Screening
<img src="https://github.com/sharonlamaier/usp8-inhibitor-screening/blob/main/TOC.png" width=50% height=50%>

## Overview 
This repository is created based on the following manuscript titled "Accelerating primary screening of USP8 inhibitors from drug repurposing databases with tree-based machine learning".
The repository includes the best performing model from the manuscript that can be used for the USP8 inhibitory activity classification of compounds, as well as a main python script that can be used to run the classification simply via CLI.   

The training data for the models is obtained from the primary high throughput screening data for USP8 inhibitors provided by the Buhrlage group (https://pubchem.ncbi.nlm.nih.gov/bioassay/1645853). 

The repository also includes test datasets used in the manuscript, which can be used to validate the reproducibility of our results, as well as a sample test dataset of diverse compounds obtained from the COCONUT database.

## Environment
The conda environment that can be used to reproduce results from the manuscript is provided by the yaml file (````environment.yml````).

## Steps to use the pre-trained model for USP8 inhibitory activity classification from SMILES
1. Clone this repository: <br>
   ````git clone https://github.com/sharonlamaier/usp8-inhibitor-screening.git```` <br>
   ````cd usp8-inhibitor-screening````
3. Create and activate the conda environment: <br>
   ````conda env create -f environment.yml```` <br>
   ````conda activate usp8````
4. Run the code specifying the model, dataset, and activity threshold: <br>
   ````python main.py --data data/smiles_colombo.csv --model models/xgb_rdkit_nounder_bigtrain.pkl --threshold 0.01 --o output.txt````
5. Prediction scores and predicted activities can be accessed from ````output.txt````.

## Directory structure
- ````main.py````: Python script to run the model's classification via CLI.
- ````data/````: Includes datasets with SMILES of compounds for classification. 
   - Colombo et al. (2010) (Top 10 compounds with lowest IC<sub>50</sub>): ````smiles_colombo.csv````
   - Tian et al. (2024) (Top 10 compounds with lowest IC<sub>50</sub>):  ````smiles_tian.csv````
   - Waltrich-Augusto (2025) (11 compounds): ````smiles_waltrichaugusto.csv````
   - COCONUT (SMILES of 1000 diverse compounds obtained by RDKit LazyBitVectorPick MaxMinPicker): ````smiles_coconut.csv````
- ````models/````: Includes pre-trained models.
  - XGBoost model trained with the combined HTS training and validation datasets: ````xgb_rdkit_nounder_bigtrain.pkl```` 
- ````src/````: Includes python scripts required for fingerprint generation and applying the classification model.
   - For loading the dataset and generation of RDKit fingerprints: ````data-utils.py```` 
   - For loading the model and generating prediction scores and activity based on user-defined threshold (default: 0.01): ````model-utils.py````
