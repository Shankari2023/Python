import argparse

def get_input_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--id', type=str, required=False)
    args = parser.parse_args()
    return (args.__dict__)
