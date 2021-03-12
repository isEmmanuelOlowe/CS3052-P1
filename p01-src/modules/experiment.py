import time
import math
import random

class ComplexityExperiment:

    current = 0
    data = []
    testData = []
    def __init__(self, algorithm, maxTests, repeat, seed, fileName):
        self.maxTests = maxTests
        random.seed(seed)
        self.repeat = repeat
        self.algorithm = algorithm
        self.fileName = fileName
        pass

    def generate_data(self, length):
        self.testData = []
        for i in range(0, length + 100):
            self.testData.append([1, random.random()])
        pass

    def run(self):
        scaleFound = False
        self.scale = 0
        for i in range(0,self.maxTests):
            self.generate_data(i)
            minimum = 0
            first = True
            for j in range(self.repeat):
                start_time = time.time()
                self.algorithm(self.testData)
                end_time = time.time()
                if first == True:
                    first = False
                    minimum = end_time - start_time
                else:
                    minimum = min(minimum, end_time - start_time)
            self.data.append(minimum)
            if scaleFound != True:
                self.scale = minimum
                scaleFound = True
            self.progressBar()
        self.writeData()
        print("Experiment Complete", flush=True)
        
    def writeData(self):
        f = open(self.fileName, "w")
        for i in range(0, len(self.data)):
            f.write(str(i))
            f.write("," + str(self.data[i]))
            f.write("," + str(self.n2(i + 100) / self.n2(100) * self.scale))
            f.write("," + str(self.nlogn2(i + 100) / self.nlogn2(100) * self.scale))
            f.write("," + str(self.nlogn(i + 100) / self.nlogn(100) * self.scale) + "\n")
        f.close()

    def progressBar(self):
        self.current += 1
        barLength = 100
        percentage = int(self.current / self.maxTests * 100)
        arrow = '-' * int(percentage/100 * barLength - 1) + '>'
        spaces = ' ' * (barLength - len(arrow))
        print('Progress: [%s%s] %d %%' % (arrow, spaces, percentage), end='\r')

    # Generates n (log n) ^ 2 results
    def nlogn2(self, x):
        return x * math.log(x) ** 2

    # Generates n log n results
    def nlogn(self, x):
        return x * math.log(x)

    #function for generating n squared results
    def n2(self, x):
        return x ** 2
