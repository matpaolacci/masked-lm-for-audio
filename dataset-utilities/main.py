import datasetanalyzer as da, os

if __name__ == "__main__":
    da.loadConfigPathsYaml(os.path.join(os.getcwd(), "configPaths.yaml"))
    # buildDatasetZip({'Piano', 'Drums', 'Guitar', 'Bass'}, 0.20)
    da.buildInstrumentsUsageFrequencyHistogram(da.SetType.TRAIN)