import os
import pandas as pd
import matplotlib.pyplot as plt


def aggregate_data(folder_path):
    """
    Aggregate all the data from the folder into a dictionary
    :param folder_path: path to the folder containing all the data
    :return: a dictionary with metabolite_id as key and a dataframe as value
    """
    all_data = {}
    for filename in os.listdir(folder_path):
        print(f"Processing {filename}")
        if filename.endswith(".tsv"):
            metabolite_id = filename.split('_')[0]
            data = pd.read_csv(os.path.join(folder_path, filename), sep='\t', header=None, names=['m/z', 'intensity'])
            all_data[metabolite_id] = data
        print(f"Finished processing {filename}")
    return all_data


def plot_spectrum(data, metabolite_id):
    """
    Plot the spectrum for a given metabolite
    :param data: a dataframe containing the spectrum data
    :param metabolite_id: the metabolite id
    :return: None
    """
    plt.figure(figsize=(10, 6))
    plt.stem(data['m/z'], data['intensity'], use_line_collection=True)
    plt.title(f"Spectrum for {metabolite_id}")
    plt.xlabel("m/z")
    plt.ylabel("Intensity")
    plt.show()



def find_high_intensity_peaks(data, threshold=500):
    """
    Find the peaks with intensity higher than the threshold
    :param data: a dataframe containing the spectrum data
    :param threshold: the threshold for the intensity
    :return: a dataframe containing the peaks with intensity higher than the threshold
    """
    return data[data['intensity'] > threshold]


def main():
    folder_path = "/Users/ozsari/Documents/Metabolomics_Data_Analysis/data/hmdb_experimental_msms_peak_lists"  
    all_data = aggregate_data(folder_path)
    
    for metabolite_id, data in all_data.items():
        print(f"Processing data for {metabolite_id}")
        
        # Visualization
        plot_spectrum(data, metabolite_id)
        
        # Basic Data Analysis
        high_intensity_peaks = find_high_intensity_peaks(data)
        print(f"High intensity peaks for {metabolite_id}:\n", high_intensity_peaks)
        
        

if __name__ == "__main__":
    main()


