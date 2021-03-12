import time
import random

class ComplexityExperiment:

    current = 0
    data = []
    testData = []
    def __init__(self, algorithm, maxTests, average, seed):
        self.maxTests = maxTests
        random.seed(seed)
        self.average = average
        self.algorithm = algorithm
        pass

    def generate_data(self, length):
        self.testData = []
        for i in range(0, length + 100):
            self.testData.append([1, random.random()])
        pass

    def run(self):
        for i in range(0,self.maxTests):
            self.generate_data(i)
            total = 0
            for j in range(self.average):
                start_time = time.time()
                self.algorithm(self.testData)
                end_time = time.time()
                total = end_time - start_time
            self.data.append(total/self.average)
            self.progressBar()
        for i in self.data:
            print(i)
        print("Experiment Complete", end='\t')
    def progressBar(self):
        self.current += 1
        barLength = 100
        percentage = int(self.current / self.maxTests * 100)
        arrow = '-' * int(percentage/100 * barLength - 1) + '>'
        spaces = ' ' * (barLength - len(arrow))
        print('Progress: [%s%s] %d %%' % (arrow, spaces, percentage), end='\r')

