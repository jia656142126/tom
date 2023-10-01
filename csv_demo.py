import csv



# with open('data.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Name', 'Age', 'City'])
#     writer.writerow(['John', '25', 'New York'])
#     writer.writerow(['Emily', '30', 'London'])

# csvfile.close()


with open('data.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Sara', '35', 'Paris'])
    writer.writerow(['Michael', '42', 'Berlin'])

# 数据已追加到文件

csvfile.close()


with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t', quotechar="'", quoting=csv.QUOTE_ALL)
    for row in reader:
        print(row)
