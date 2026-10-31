import json
import os
import torch

def main():

    data = {
        # "train_pkl": "./data_PKL/cartoon_elephant_train.pkl",
        # "valid_pkl": "./data_PKL/cartoon_elephant_valid.pkl",
        # "output_path": './jobs/net_cartoon_elephant/',
        "train_pkl": "./data_PKL/dfaust_template_10_train.pkl",
        "valid_pkl": "./data_PKL/dfaust_template_10_train.pkl",
        "output_path": './jobs/dfaust_template_10/',
        "epochs": 700, 
        "lr": 2e-3, 
        "device": 'cuda' if torch.cuda.is_available() else 'cpu',
        "Din": 6,
        "Dout": 32,
        "h_initNet": [32,32],
        "h_edgeNet": [32,32],
        "h_vertexNet": [32,32],
        "numSubd": 2,
    }

    # create directory
    if not os.path.exists(data['output_path']):
        os.mkdir(data['output_path'])

    # write hyper parameters into a json file
    with open(data['output_path'] + 'hyperparameters.json', 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    main()