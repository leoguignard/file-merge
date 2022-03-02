#!/usr/bin/env python
# Merge

from pathlib import Path
import argparse

def merge(inputs, output, default_v):
    """

    """
    if len(default_v)<len(inputs):
        default_v = [default_v[0]]*len(inputs)
    abs_p = []
    for p in inputs:
        p = Path(p)
        if not p.is_absolute():
            p = p.absolute()
        abs_p += [p]

    output = Path(output).absolute()
    if not output.parent.exists():
        Path.mkdir(output.parent)

    all_dicts = []
    for p in abs_p:
        append_d = {}
        with open(p, 'r') as f:
            lines = f.readlines()
        for l in lines:
            out = l.split()
            gene = out[0]
            to_append = out[1]
            append_d[gene] = to_append
        all_dicts.append(append_d)

    all_genes = set.union(*[set(d.keys()) for d in all_dicts])
    all_genes = sorted(all_genes)
    out_dict = {g:['0']*len(inputs) for g in all_genes}
    for g, val in out_dict.items():
        for i, d in enumerate(all_dicts):
            val[i] = d.get(g, default_v[i])

    with open(output, 'w') as f:
        for gene, val in out_dict.items():
            f.write(f'{gene}'+(',{}'*len(val)).format(*val)+'\n')
        f.close()
        print(f'Merged saved in folder "{output.parent}" under the name "{output.name}"')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge some files.')
    parser.add_argument('-i', '--inputs', type=str, nargs='+', required=True,
                        help='path to input files')
    parser.add_argument('-o', '--output', type=str, nargs=1, required=True,
                        help='path to output file (will create folder(s) if necessary)')
    parser.add_argument('-d', '--default-value', type=str, nargs='+', default='0',
                        help=('default value if not found'
                              '(either 1 value or as many as inputs)'))
    args = parser.parse_args()
    merge(args.inputs, args.output[0], args.default_value)
