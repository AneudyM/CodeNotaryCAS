

LINE_HEADER = "Your assets will not be uploaded. They will be processed locally."


def parse(output_str):
    lines = dict()
    for line in output_str.splitlines():
        if line == LINE_HEADER or line == '':
            continue
        line = line.rstrip()
        line = line.replace('\t', '')
        line = line.split(':', maxsplit=1)
        lines[line[0]] = line[1]
    return lines

