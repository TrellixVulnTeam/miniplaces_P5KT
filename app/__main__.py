import argparse
import logging
logging.basicConfig(level=logging.INFO)

import numpy as np
np.random.seed(234421)

from app.download import download_data
from app.train import train_model

def get_args():
    parser = argparse.ArgumentParser(description='Miniplaces project to classify images')
    parser.add_argument('--download', help='Download dataset', action='store_true')
    parser.add_argument('--train', help='Train tiles', action='store_true')
    parser.add_argument('--force', help='Force an action', action='store_true')
    parser.add_argument('--model_type', help='The model to train with', type=str, default='basic_model')
    parser.add_argument('--model_file', help='The h5 model file to input/output.', type=str)
    parser.add_argument('--batch_size', help='The batch size to train on.', type=int, default=100)
    parser.add_argument('--epochs', help='The batch size to train on.', type=int, default=500)
    args = parser.parse_args()
    if not args.model_file:
        args.model_file = 'models/{}.h5'.format(args.model_type)
    return args

def main():
    args = get_args()
    if args.download:
        download_data(force=args.force)
    elif args.train:
        train_model(args)

if __name__ == '__main__':
    main()
