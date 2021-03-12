from modules.experiment import ComplexityExperiment
from modules.closestPointsDNQ import ClosestPoints as cp1
from modules.cp3 import ClosestPoints as cp2

'''
This test generates results for alogirthm specified
'''
def Main():
    experiment = ComplexityExperiment(cp1, 1000, 4, 10, "data.csv")
    experiment.run()
    experiment2 = ComplexityExperiment(cp2, 1000, 4, 10, "data2.csv")
    experiment2.run()

if __name__ == "__main__":
    Main()
