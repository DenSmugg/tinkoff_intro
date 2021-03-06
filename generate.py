import argparse
import pickle
from model import Model
import random


def read_model(path='big_model.pickle'):
    with open(path, 'rb') as f:
        temp_model = pickle.load(f)
        return temp_model


parser = argparse.ArgumentParser()

parser.add_argument("--path",
                    help="path to model", default='big_model.pickle')
parser.add_argument("--prefix",
                    help="prefix", default='no prefix')

args = parser.parse_args()


model = read_model(path=args.path)

start_word = args.prefix.lower()
if args.prefix == 'no prefix':
    start_word = [*model.data][random.randint(0, len(model.data) - 1)]

text = start_word + ' '
for _ in range(40):
    nw_word = model.data[start_word][random.randint(0, min(len(model.data[start_word]) - 1, 4))]
    text += nw_word + ' '
    start_word = nw_word

text += '.'
print(text)