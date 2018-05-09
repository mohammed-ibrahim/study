import sys
import csv

# info: one-time script to merge roots in csv and roots saved in google-keep study note.

# load the csv

core_contents = {}

def row_to_map(headers, row):
    content = {}

    for i in range(len(headers)):
        content[headers[i]] = row[i]

    return content

headers = None
with open("./core.csv", "rb") as read_handle:
    csv_reader = csv.reader(read_handle)

    for row in csv_reader:
        if headers is None:
            headers = list(row)
        else:
            root = row[0]
            core_contents[root] = row_to_map(headers, row)


# print(str(len(core_contents)))

extract_contents = {}


with open("./extract.csv", "rb") as read_handle:
    csv_reader = csv.reader(read_handle)
    extract_headers = None

    for row in csv_reader:
        if extract_headers is None:
            extract_headers = list(row)
        else:
            root = row[0].strip()
            extract_contents[root] = row_to_map(extract_headers, row)



# print(str(extract_contents))
# for key in extract_contents:
#     print("%s - %s" % (key, extract_contents[key]))



with open('/Users/ibrahim/Desktop/output.csv', "wb") as write_handle:
    writer = csv.DictWriter(write_handle, fieldnames=headers)

    matched = 0

    for core_key in core_contents:
        if core_key in extract_contents:
            core_contents[core_key]['meaning-v2'] = extract_contents[core_key]['meaning']
            matched = matched + 1

        for key in core_contents[core_key]:
            if key not in headers:
                print("%s key not found in headers" % key)

        writer.writerow(core_contents[core_key])

    print("Total matched: %d total missed: %d" % (matched, (len(extract_contents) - matched)))




missed_keys = [k for k in extract_contents if k not in core_contents]

for p in missed_keys:
    print("%s" % p)
