import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 change_text_to_numeric.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage3", "train.csv")
os.makedirs(os.path.join("data", "stage3"), exist_ok=True)

def process_data(fd_in, fd_out):
    target = []
    p_length = []
    p_width = []

    for line in fd_in:
        line = line.rstrip('\n').split(',')
        target.append(line[0])
        p_length.append(line[1])
        p_width.append(line[2])

    for i in range(len(target)):
        if target[i] == 'setosa':
            target[i] = 1
        elif target[i] == 'versicolor':
            target[i] = 2
        else:
            target[i] = 0

    for targ, p_len, p_wid in zip(target, p_length, p_width):
        fd_out.write("{},{},{}\n".format(targ, p_len, p_wid))

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)
