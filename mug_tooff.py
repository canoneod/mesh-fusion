import pymeshlab as pl
import argparse
import os

source_path = "/mnt/c/Users/Kim/Desktop/ShapeNetCore.v2/03797390"
output_path = ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_id', type=str, default="", help="get model id from txt file")
    name = parser.parse_args().model_id
    path = os.path.join(source_path, name, "model")
    mesh = pl.MeshSet.load_new_mesh(path)
    mesh.save_current_mesh(os.path.join())

    # if file path does not exist, save 