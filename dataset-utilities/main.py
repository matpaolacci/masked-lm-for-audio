import flacconverter as fc
import datasetanalyzer as da
from datasetanalyzer import InstrumentType as Instr
import os

if __name__ == "__main__":
    da.loadConfigPathsYaml(os.path.join(os.getcwd(),"dataset-utilities" , "configPaths.yaml"))
    da.buildDatasetZip({'Piano', 'Drums', 'Guitar', 'Bass'}, 0.20)
    #da.buildInstrumentsUsageFrequencyHistogram(da.SetType.TRAIN)