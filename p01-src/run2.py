from modules.experiment import ComplexityExperiment
from modules.closestPointsDNQ import ClosestPoints
def Main():
    experiment = ComplexityExperiment(ClosestPoints, 1000, 3, 10)
    experiment.run()

if __name__ == "__main__":
    Main()
