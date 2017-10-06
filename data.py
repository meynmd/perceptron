from __future__ import print_function
import numpy as np

FEATURE_DIMENSIONS = (101, 7, 16, 7, 14, 5, 2, 101, 41, 2)

def read_examples(path):
    data = []
    with open(path, 'r') as fp:
        for i, line in enumerate(fp.readlines()):
            fields = line.split((', '))
            if len(fields) < 9:
                print('warning: data file line {} has unexpected format'.format(i))
                continue
            if len(fields) == 9:
                age, emp, edu, mar, job, eth, sex, hrs, nat = fields
                inc = None
            else:
                age, emp, edu, mar, job, eth, sex, hrs, nat, inc = fields
                inc = 1. if inc == '>50K' else -1.

            # data.append({
            #     'age': age,
            #     'employer': emp,
            #     'education': edu,
            #     'marital': mar,
            #     'job': job,
            #     'ethnicity': eth,
            #     'sex': sex,
            #     'hours': hrs,
            #     'nationality': nat,
            #     'income': inc
            # })

            data.append((int(age), emp, edu, mar, job, eth, sex, int(hrs), nat, inc))
        return data

def count_values(data):
    em, ed, ma, jo, et, se, na = {}, {}, {}, {}, {}, {}, {}
    for age, emp, edu, mar, job, eth, sex, hrs, nat, inc in data:
        em[emp] = True
        ed[edu] = True
        ma[mar] = True
        jo[job] = True
        et[eth] = True
        se[sex] = True
        na[nat] = True
    # ages 0-99, 100+; 0-99 hours, 100+
    return 101, len(em), len(ed), len(ma), len(jo), len(et), len(se), 101, len(na), 2

def preprocess(data_path):
        data = read_examples(data_path)
        processed = []
        for d in data:
            x = np.zeros(sum(FEATURE_DIMENSIONS))
            offset = 0
            for i, fd in enumerate(FEATURE_DIMENSIONS):
                x[offset + d[i]] = 1.
                offset += fd
            processed.append(x)
        return processed

