import pandas as pd
import pickle

class GPKDataset:
    def __init__(self, array_of_dicts):
        self.dataframe = pd.DataFrame(array_of_dicts)

    def save(self, output_path):
        if output_path.endswith('.json'):
            self.dataframe.to_json(output_path, orient='records', indent=4)
        elif output_path.endswith('.csv'):
            self.dataframe.to_csv(output_path, index=False)
        elif output_path.endswith('.pickle'):
            with open(output_path, 'wb') as f:
                pickle.dump(self.dataframe, f)
        else:
            raise ValueError(f"Unsupported file format for: {output_path}. Try one of these: json, csv, or pickle.")