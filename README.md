# Wearable EEG, PPG, and EDA Dataset curated under Mental Workload conditions both in Controlled and Uncontrolled Environments
## About
The repository provides the platform to create the dataset and how to use the dataset with the example of preprocessing, feature extraction, and machine learning pipeline as follows:
### Psychopy: 
This platform is used to generate data in the controlled session. It is a Python toolbox which provides visual stimulation to elicit cognitive load of different levels. The data collection protocol can be used to reproduce or extend the dataset in the controlled setup.
### Data:
Download the data using the [link here](10.5281/zenodo.10371068)
### Setup:
- Clone repository
  
  `git clone https://github.com/HPI-CH/UNIVERSE.git`
  
   `cd UNIVERSE `  
- Create virtual environment with Python version 3.7 (for example using Conda)
  
  ` conda create --name name_of_your_choice python=3.7`
  ` conda activate name_of_your_choice`
  
- Install requirements
  
  `pip install -r requirements.txt`
  
### Data Loader:
Use `Data_Loader.ipynb` to load the **Raw**, **Synchronized**, and **Labeled** data.  Use the labeled data to perform preprocessing, feature extraction, and machine learning as described in the respective folders:
- Preprocessing: A pipeline used to preprocess the dataset. Among the various preprocessing methods performed in the state-of-the-art, the code shows an example of preprocessing steps performed on the dataset as a technical validation approach.  
- Features: 24 features were extracted from different modalities for 60-second windows as an example use case of the mentioned dataset.
- Machine learning: Using the features mentioned above, the Logistic Regression algorithm was applied to perform binary classification between high and low mental workload to provide sufficient proof of the technical validation of the dataset provided.
  
## Usage:
The **Raw** data can be used to perform different synchronization methods and for unsupervised learning algorithms. The **Labeled** data serves the purpose of using the data for deep learning models, among others. The **Preprocessed** data and features can be reused and extended to perform various algorithms. 
