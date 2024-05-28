#!/usr/bin/env python3
import csv
import sys
import io

def do_compare(source, target):
    diff = []

    with open(source, 'r') as src, open(target, 'r') as tgt:
        src_reader = csv.reader(src)
        tgt_reader = csv.reader(tgt)
        
        header = []

        for row_num, (src_row, tgt_row) in enumerate(zip(src_reader, tgt_reader), start=1):
            if row_num == 1:
                header = tgt_row
                continue

            if src_row != tgt_row:
                diff.append([row_num] + tgt_row)

    return (header, diff)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python compare.py source.csv target.csv")
        sys.exit(1)

    source = sys.argv[1]
    target = sys.argv[2]

    (header, diff) = do_compare(source, target)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['#'] + header)
    writer.writerows(diff)

    output.seek(0)
    print(output.getvalue())
