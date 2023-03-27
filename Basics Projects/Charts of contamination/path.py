import csv

def read_csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = (','))
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header,row)
            dictionary = dict(iterable) #other method {key: value for key, value in iterable}
            data.append(dictionary)
        return data


if __name__ == '__main__': 
    data = read_csv('Digital Portfolio/Project_2.py/data_p.csv')
    #Note: Especify the path of the file
    print(data)