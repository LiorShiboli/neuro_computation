import os
import numpy as np
import pandas as pd
def load_data(dirname: str) -> list[np.array]:
    data = []

    files = [os.path.join(dirname, file) for file in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, file))]

    print("Loading", len(files), "files as data")

    for file in files:
        try:
            with open(file) as f:
                content = f.read()
        except:
            print("Error in: ", file)
            continue

        content = content.replace("(", "[").replace(")", "]")

        for line in content.split('\n'):
            if ('[' in line) and (']' in line):
                try:
                    
                    if isinstance(arr, list):
                        img = np.array(arr)
                        if img.size != 101 or ((img[1:] == -1) | (img[1:] == 1)).sum() != 100:
                            print("Error in: ", file)
                        else:
                            data.append(img)
                except:
                    print("Error in: ", file)

    print(len(data), " images loaded as data")

    return data