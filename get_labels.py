import sys
import csv


input_file = 'train.data'
output_file = 'train_label.data'
label_dict = {}


def readfile(f):
	infile = open(f)
	reader = csv.reader(infile, delimiter=",")   
	reader.next()
	return reader

def get_labels():
	reader = readfile(input_file)
	for(user_id, sku, category, query, click_time, query_time) in reader:
		if sku in label_dict.keys():
			label_dict[sku] = label_dict[sku] + 1
		else:
			label_dict[sku] = 1
	writer = open(output_file,'w+')
	for i,j in label_dict.iteritems():
		print i, j
		writer.write(i+","+str(j)+'\n')
	writer.close()

get_labels()
