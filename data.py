from __future__ import print_function

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

            data.append({
                'age': age,
                'employer': emp,
                'education': edu,
                'marital': mar,
                'job': job,
                'ethnicity': eth,
                'sex': sex,
                'hours': hrs,
                'nationality': nat,
                'income': inc
            })
        return data