import pandas as pd
import pickle

class GPKDataset:
    def __init__(self, array_of_dicts):
        self.array_of_dicts = array_of_dicts #no dataframes

    def save(self, output_path):
        dataframe = pd.DataFrame(self.array_of_dicts)
        if output_path.endswith('.json'):
            dataframe.to_json(output_path, orient='records', indent=4)
        elif output_path.endswith('.csv'):
            dataframe.to_csv(output_path, index=False)
        elif output_path.endswith('.pickle'):
            with open(output_path, 'wb') as f:
                pickle.dump(dataframe, f)
        else:
            raise ValueError(f"Unsupported file format for: {output_path}. Try one of these: json, csv, or pickle.")