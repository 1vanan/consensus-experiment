import csv

header1 = ['consensus-res']

csv_file_name = 'resources/cnf_3_orgs-majority/consensus-base-experiment.csv'


def write_stats(total_num, probability, writer_func):
    for i in range(1, total_num + 1):
        if i % (probability + 1) == 0:
            writer_func.writerow([0])
        else:
            writer_func.writerow([1])


with open(csv_file_name, 'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter=',')

    # write the header
    writer.writerow(header1)

    write_stats(100, 99, writer)

    header2 = ['consensus-modified']
