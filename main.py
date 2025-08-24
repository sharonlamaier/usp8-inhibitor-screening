import argparse
import pandas as pd
from src.data_utils import load_data, rdfp_gen
from src.model_utils import load_model, predict_proba, predict_activity

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True, help="Path to dataset")
    parser.add_argument("--model", type=str, required=True,
                        help="Specify name of model")
    parser.add_argument("--o", type=str, default="output.txt",
                        help="Specify name of output file")
    parser.add_argument("--threshold", type=float, default=0.01,
                        help="Threshold for activity")
    return parser.parse_args()

def main():
    args = parse_args()
    data = load_data(args.data)
    fp = rdfp_gen(data)
    model = load_model(args.model)
    predicted_prob = predict_proba(fp, model)
    predicted_activity = predict_activity(predicted_prob,args.threshold)
    output = args.o 
    #print(f'predicted probabilities: {predicted_prob}')
    #print(f'predicted activities: {predicted_activity}')
    df_predictions = pd.DataFrame({"pred_prob": predicted_prob, "pred_activity": predicted_activity})
    df = pd.concat([data[['SMILES']],df_predictions],axis=1)
    df.to_csv(output, sep=",", index=False)

if __name__ == "__main__":
    main()
