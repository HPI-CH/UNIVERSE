# Wearable EEG, PPG, and EDA Dataset curated under Mental Workload and Stress in Controlled and Uncontrolled Environments
## About
The repository provides the platform to create the dataset and how to use the dataset with the example of preprocessing, feature extraction, and machine learning pipeline as follows:
- Psychopy: A Python toolbox showing the data collection protocol to reproduce or extend the dataset in the controlled setup.
- Preprocessing: A pipeline to preprocess the dataset. This is the first step in loading the data from the repository.
- Features: A repository to create machine learning features from the preprocessing steps with different window sizes.
- Machine learning: A practical machine learning pipeline with example algorithms utilizing the above features to guide the researchers.
## Setup
Clone repository
git clone https://github.com/HPI-CH/UNIVERSE.git
cd UNIVERSE

Create virtual environment with Python version 3.7 (for example using Conda)
conda create --name name_of_your_choice python=3.7
conda activate name_of_your_choice

Install requirements
pip install -r requirements.txt

Download the data using the [link here](10.5281/zenodo.10371068)
