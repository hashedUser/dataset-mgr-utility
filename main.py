# importing required libraries
import os
import sys
import logging
import warnings
import argparse
import kagglehub

def main():
    parser = argparse.ArgumentParser(description="Dataset Manager Utility")
    parser.add_argument(
        "-kaggle",
        metavar="DATASET_HANDLE",
        help="Download dataset from kaggle using the handle 'owner/dataset'.",
        type=str
    )

    args = parser.parse_args()

    if args.kaggle:
        dataset_handle = args.kaggle
        print(f"Downloading Kaggle dataset: {dataset_handle}")

        try:
            path = kagglehub.dataset_download(dataset_handle)
            print(f"Dataset downloaded to: {path}")
        except Exception as e:
            print(f"Error while downloading: {e}")

    else:
        print("No data source specified. Please use -kaggle <dataset_handle>.")

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    main()