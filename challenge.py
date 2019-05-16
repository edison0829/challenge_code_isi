import glob
import sys
import os
import timeit

class Files_reader(object):
    def __init__(self, path, output):
        self.directory = glob.glob(path+'/*.txt')
        self.map1 = {}
        self.map2 = {}
        self.w = output


    # reads all the P*.txt files into an index when it initializes.
    def reader(self):
        for file in self.directory:
            name = str(file).split('.')[0].split('/')[-1]
            text_file = open(file, "r")
            lines = text_file.read().split('\n')
            # if len(lines) != len(set(lines)):
            #     print ('error, duplicated string! found in ' + name)
            # if name == 'P6375_located at street address':
            #     count = Counter(lines)
            #     print (count.most_common(5))
            if 'P' in name:
                self.map1[name] = set(lines)
            if 'sample' in name:
                self.map2[name] = set(lines)
        print ('all files finished reading!')
        return self.map1, self.map2

    # Retrun the results for each of the sample*.txt files.
    def find_property(self):
        for key2,value2 in self.map2.items():
            start = timeit.default_timer()
            res = []
            for key1,value1 in self.map1.items():
                res.append((key1,len(value1 & value2)))
            res = sorted(res,key=lambda x:x[1],reverse=True)
            with open(self.w + "/" + key2 + "_output.txt", 'w') as outfile:
                outfile.write('\n'.join([str(i) for i in res]))
            outfile.close()
            stop = timeit.default_timer()
            print('Time: ', stop - start, key2)
        print('all examples finished!')


inp = sys.argv[1]
outp = sys.argv[2]
if not os.path.exists(outp):
    os.makedirs(outp)
r = Files_reader(inp,outp)
r.reader()
r.find_property()

# print (res)
