import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 get_features_iris.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("..", "..", "data", "stage1", "train.csv")
os.makedirs(os.path.join("..", "..", "data", "stage1"), exist_ok=True)

def process_data(fd_in, fd_out):
    fd_in.readline()
    for line in fd_in:
        line = line.rstrip('\n').split(',')
        target = line[-1]
        pental_length_cm = line[-2]
        pental_width_cm = line[-3]
        fd_out.write("{},{},{},\n".format(target, pental_length_cm, pental_width_cm))

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)
