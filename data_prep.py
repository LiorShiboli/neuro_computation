import numpy as np
import pandas as pd
import os
import json
def load_and_filter_data(dirname: str) -> list[np.array]:
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
                    arr = json.loads(line)
                    if isinstance(arr, list):
                        img = np.array(arr)
                        #filter images with incorrect or not enough info
                        if img.size != 101 or ((img[1:] == -1) | (img[1:] == 1)).sum() != 100 or img[1:].sum() < -97 or img[1:].sum() >97 :
                            print("Error in: ", file)
                        else:
                            data.append(img)
                except:
                    print("Error in: ", file)

    print(len(data), " images loaded as data")

    return data
def main():
    Data = np.array(load_and_filter_data("noisy_data"))
    Coloums = np.arange(len(Data[0]))
    df = pd.DataFrame(Data,columns=Coloums)
    df.to_csv("preproceesed_noisy_data")

if __name__ == "__main__":
    main()