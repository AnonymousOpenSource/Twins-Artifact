# -*-coding:utf-8-*-
import time
from pathlib import Path
import pickle
import torch
from tqdm import tqdm
import os
from Tokenizer.InstructionTokenizer import InstructionTokenizer
from GIN import extract_all_graph
from torch_geometric.data import Data
from BlockEmbedding.asmRoberta import asmRobertaModel
from utils.DataLoaders import DataCollatorForSimilarBlocks
from DeepGNN import Net, MyData
from torch.nn import functional as F
from KMA.km_matcher import KMMatcher
import argparse
from matchlib import match




def main():
    parser = argparse.ArgumentParser(
        description='Compare two binaries.')
    parser.add_argument('--file1', type=str, default="example/clang/findutils/O0/find",
                        help='Input File 1')
    parser.add_argument('--file2', type=str, default="example/obfuscation/findutils/fla/find_stripped",
                        help='Input File 2')
    args = parser.parse_args()
    file1 = args.file1
    file2 = args.file2

    match(file1, file2)

if __name__ == '__main__':
    main()
