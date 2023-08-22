# Metabolomics_Data_Analysis
This repo covers my studies  and work about metabolomics data analysis

Metabolomics is the comprehensive study of the metabolome, which refers to the complete set of small-molecule metabolites (such as metabolic intermediates, hormones, and other signaling molecules) found within a biological sample. This field is a subset of systems biology and is analogous to genomics, transcriptomics, and proteomics, which study the genome, transcriptome, and proteome, respectively.

## A brief overview of metabolomics data

1. **Types of Metabolites**: Metabolites can be broadly categorized into primary and secondary metabolites. Primary metabolites are directly involved in growth, development, and reproduction, while secondary metabolites are often involved in ecological interactions, such as defense against herbivores or pathogens.

2. **Techniques for Data Acquisition**:
   - **Mass Spectrometry (MS)**: This is one of the most commonly used techniques in metabolomics. It can be used to identify and quantify metabolites in a sample.
   - **Nuclear Magnetic Resonance (NMR) Spectroscopy**: Another common technique, NMR provides information about the structure and quantity of metabolites.
   - **Chromatography**: Techniques like gas chromatography (GC) and liquid chromatography (LC) are used to separate complex mixtures of metabolites before they are analyzed by MS or NMR.

3. **Data Analysis**:
   - **Preprocessing**: This step involves noise reduction, baseline correction, alignment, and normalization of the raw data.
   - **Identification of Metabolites**: Using databases and spectral libraries, the detected signals are matched to known metabolites.
   - **Quantification**: The concentration of each metabolite is determined.
   - **Statistical Analysis**: Techniques like principal component analysis (PCA) or partial least squares-discriminant analysis (PLS-DA) are used to identify patterns and differences between samples.
   - **Pathway Analysis**: This step involves mapping the identified and quantified metabolites onto known metabolic pathways to understand the biological context.

4. **Applications**:
   - **Biomarker Discovery**: Identifying metabolites that can act as indicators for diseases or other physiological states.
   - **Drug Development**: Understanding the metabolic response to drugs and identifying potential side effects.
   - **Functional Genomics**: Linking genes to their metabolic functions.
   - **Nutrition and Agriculture**: Studying the effects of diet on metabolism or improving crop quality and resistance.

5. **Challenges**:
   - **Complexity**: The metabolome is highly dynamic and can vary based on factors like age, diet, environment, and health status.
   - **Sensitivity**: Detecting low-abundance metabolites can be challenging.
   - **Annotation**: Many detected metabolites remain unidentified due to the lack of comprehensive reference databases.

6. **Databases and Tools**: There are several databases and software tools available for metabolomics data analysis. Examples include METLIN, HMDB (Human Metabolome Database), and MassBank. Software tools like XCMS, MetaboAnalyst, and MZmine are commonly used for data processing and analysis.

In summary, metabolomics offers a snapshot of the physiological state of an organism by analyzing its metabolites. The data generated can provide insights into various biological processes, disease states, and responses to environmental changes.

## Databases 

There are several databases that have been developed to store, organize, and provide access to metabolomics data. 

**A list of some of the most widely used metabolomics databases:**

1. **HMDB (Human Metabolome Database)**: This is a comprehensive resource for human metabolites. It provides detailed information about metabolites, including their structures, biochemistry, and biological roles.The link for the website is as follows: [https://hmdb.ca/](https://hmdb.ca/)

2. **METLIN**: A metabolite and tandem mass spectrometry database, METLIN provides information on thousands of metabolites and supports identification efforts in metabolomics. Website: https://metlin.scripps.edu/ 

3. **MassBank**: This is a public repository for mass spectra, which can be used for the identification of metabolites based on their spectral data. Website: https://massbank.eu/MassBank/

4. **LipidMaps**: As the name suggests, this database focuses on lipids. It provides structures, nomenclature, and other relevant information about lipids. Website: https://www.lipidmaps.org/

5. **GNPS (Global Natural Products Social Molecular Networking)**: This is a platform for collaborative molecular discovery and provides a public data repository for mass spectrometry data. Website: https://gnps.ucsd.edu/ProteoSAFe/static/gnps-splash.jsp 

6. **MetaboLights**: Hosted by the European Bioinformatics Institute (EBI), MetaboLights is a database for metabolomics experiments and derived information. It's a comprehensive resource that includes experimental data, metadata, and analytical results. Website: https://www.ebi.ac.uk/metabolights/

7. **MoNA (MassBank of North America)**: This is a free and open repository of mass spectral data, which is particularly useful for natural products research. Website: https://mona.fiehnlab.ucdavis.edu/

8. **BioMagResBank (BMRB)**: This is a repository for data from NMR spectroscopy on proteins, peptides, nucleic acids, and other biomolecules. While not exclusively for metabolomics, it's a valuable resource for NMR-based metabolomics studies. Website: https://bmrb.io/

9. **KNApSAcK**: A comprehensive species-metabolite relationship database, useful for researchers studying plant metabolomics. website: http://www.knapsackfamily.com/KNApSAcK/

10. **Metabolomics Workbench**: This platform provides a suite of tools and databases to facilitate metabolomics research. It includes data from various metabolomics studies, reference compounds, and more. Website: https://www.metabolomicsworkbench.org/

11. **Golm Metabolome Database (GMD)**: This database provides mass spectra, metabolite profiles, and related information, primarily for plant metabolomics. Website: http://gmd.mpimp-golm.mpg.de/

12. **MMCD (Madison Metabolomics Consortium Database)**: It contains data on metabolites, including their NMR and MS spectra. Website: http://english.qibebt.cas.cn/ic/ji/medison/201406/t20140605_122189.html

When using these databases, it's essential to be aware of the type of data they contain (e.g., spectral data, metabolite structures, experimental data) and the organisms or biological contexts they cover. This will help in selecting the most appropriate database for a specific research question or analysis.

## Metabolomics Data

Metabolomics data can be quite complex due to the vast number of metabolites present in biological samples and the various techniques used to detect them. 

**A general overview of what metabolomics data might look like:**

1. **Raw Data**:
   - **Mass Spectrometry (MS)**: Raw data from MS experiments typically consist of mass-to-charge ratios (m/z) plotted against intensity. In tandem MS (MS/MS), you'll also see fragmentation patterns of selected ions.
   - **Nuclear Magnetic Resonance (NMR) Spectroscopy**: Raw NMR data are presented as spectra where chemical shifts (usually in ppm) are plotted against intensity. Peaks in the spectra correspond to specific nuclei in the metabolites.

2. **Processed Data**:
   - **Peak Lists**: After processing raw data, you'll often have a list of detected peaks with their corresponding m/z values (for MS) or chemical shifts (for NMR), and their intensities.
   - **Metabolite Identification**: Peaks are matched to known metabolites using databases. This results in a list of identified metabolites and their quantities in the sample.
   - **Matrix Format**: For multivariate analysis, data are often organized into a matrix where rows represent samples, columns represent detected metabolites, and the cell values represent the quantity or intensity of each metabolite in each sample.

3. **Metadata**:
   - Information about the samples, such as the source (e.g., human plasma, plant tissue), conditions (e.g., disease state, treatment), and any other relevant experimental details.

4. **Annotation**:
   - Once metabolites are identified, they can be annotated with additional information, such as their pathways, biological roles, and chemical properties.

5. **Visualization**:
   - **Heatmaps**: Used to visualize the relative levels of metabolites across multiple samples.
   - **Chromatograms (for MS data)**: Plots showing the intensity of detected ions as a function of retention time.
   - **Spectra (for NMR data)**: Plots showing the intensity of detected signals as a function of chemical shift.
   - **Metabolic Pathway Maps**: Visual representations of metabolic pathways with highlighted metabolites that have been detected or show significant changes.

6. **Statistical Outputs**:
   - Results from statistical analyses, such as p-values, fold changes, and scores from multivariate analyses (e.g., PCA or PLS-DA scores).

In practice, the appearance of metabolomics data will depend on the software and tools used for data acquisition, processing, and analysis. However, the above gives a general sense of the types of data and visualizations you might encounter in metabolomics research.


## Processing raw MS-based metabolomics data
Processing raw metabolomics data obtained from mass spectrometry (MS) is a crucial step to transform the complex datasets into a format suitable for downstream analysis and biological interpretation.

**A general workflow for processing raw MS-based metabolomics data:**

1. **Data Conversion**:
   - Convert vendor-specific raw data files into open formats like mzXML or mzML. Tools like ProteoWizard's MSConvert can be used for this purpose.

2. **Peak Detection**:
   - Identify peaks in the MS data. This involves distinguishing genuine metabolite signals from noise.
   - Each peak corresponds to an ionized metabolite, and its height or area represents its abundance.

3. **Baseline Correction**:
   - Remove the background signal to enhance the genuine peaks. This step helps in improving the accuracy of peak detection and quantification.

4. **Peak Alignment**:
   - When analyzing multiple samples, it's essential to ensure that the same metabolite is aligned across all samples. This step compensates for minor variations in retention times across different runs.
   - Tools like XCMS and MZmine are popular for peak detection and alignment.

5. **De-isotoping**:
   - MS data often contain isotopic peaks, which are signals from heavier isotopes of the elements in the metabolites (e.g., C-13 instead of the more common C-12). 
   - De-isotoping involves identifying and removing these redundant peaks to retain only the monoisotopic peak for each metabolite.

6. **Gap Filling**:
   - Sometimes, a metabolite might not be detected in a particular sample due to its low concentration. Gap filling involves estimating or imputing these missing values.

7. **Normalization**:
   - To account for variations in sample concentration or instrument sensitivity, data are normalized. Common methods include total ion current (TIC) normalization, probabilistic quotient normalization (PQN), or normalization to internal standards.

8. **Metabolite Identification**:
   - Match the detected m/z values and, if available, MS/MS fragmentation patterns to known metabolites in databases like METLIN, MassBank, or HMDB.
   - This step can be challenging due to the vast number of possible metabolites and isomers, and not all detected features will be confidently identified.

9. **Quantification**:
   - Determine the concentration or relative abundance of each identified metabolite. This can be done using the peak area or peak height.

10. **Quality Control**:
   - It's essential to include quality control (QC) samples in the experiment, which are analyzed throughout the run.
   - QC samples help in assessing the stability, reproducibility, and overall quality of the data. Any systematic drifts or anomalies can be detected and corrected.

11. **Batch Effect Correction** (if necessary):
   - If samples were run in multiple batches, there might be batch-specific variations. These need to be identified and corrected to ensure that the observed differences are due to the experimental conditions and not technical artifacts.

12. **Data Transformation and Scaling**:
   - Before statistical analysis, data might be log-transformed, auto-scaled (mean-centered and divided by the standard deviation), or Pareto-scaled (mean-centered and divided by the square root of the standard deviation).

Once these processing steps are completed, the data are ready for downstream statistical analysis, such as univariate or multivariate analysis, to identify significant metabolites or patterns related to the experimental conditions.



<p>
    <center>
        <img src="assets/workflow.png" alt>
        <em>Workflow for metabolomics data analysis </em> [1]
    </center>
</p>

## References
[1] Chen Y, Li EM, Xu LY. Guide to Metabolomics Analysis: A Bioinformatics Workflow. Metabolites. 2022 Apr 15;12(4):357. doi: 10.3390/metabo12040357. PMID: 35448542; PMCID: PMC9032224. 