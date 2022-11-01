import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 fill_na.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("..", "..", "data", "stage2", "train.csv")
os.makedirs(os.path.join("..", "..", "data", "stage2"), exist_ok=True)

def process_data(fd_in, fd_out):
    target = []
    p_length = []
    p_width = []

    for line in fd_in:
        line = line.rstrip('\n').split(',')
        target.append(line[0])
 
        if line[1]:
            p_length.append(float(line[1]))
        else:
            p_length.append(0)
 
        if line[2]:
            p_width.append(float(line[2]))
        else:
            p_width.append(0)


    s = sum(p_length)
    s1 = sum(p_width)

    for i in range(len(p_length)):
        if p_length[i] == 0:
            p_length[i] = round(s / len(p_length), 2)

    for i in range(len(p_width)):
        if p_width[i] == 0:
            p_width[i] = round(s1 / len(p_width), 2)

    for taeg, length, width in zip(target, p_length, p_width):
        fd_out.write("{},{},{}\n".format(taeg, length, width))


with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)
