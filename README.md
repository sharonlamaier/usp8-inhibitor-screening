# USP8 Inhibitor Screening
1. Clone this repository: <br>
   ````git clone https://github.com/sharonlamaier/usp8-inhibitor-screening.git```` <br>
   ````cd usp8-inhibitor-screening````
3. Create and activate the conda environment: <br>
   ````conda env create -f environment.yml```` <br>
   ````conda activate usp8````
4. Run the code specifying the model, dataset, and activity threshold: <br>
   ````python main.py --data data/smiles_colombo.csv --model models/xgb_rdkit_nounder_bigtrain.pkl --threshold 0.01 --o output.txt````
