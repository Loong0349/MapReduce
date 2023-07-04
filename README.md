# MapReduce

This is a MapReduce assignment implemented on AWS EC2.

The dataset used is "headline.csv" downloaded from https://www.kaggle.com/datasets/therohk/examine-the-examiner.
The dataset comprises approximately 3.08 million article headlines authored by around 21,000 individuals over a six-year period at http://www.examiner.com/.

The "preprocess.py" code is used for data preprocessing, including tasks like removing stop words and performing lemmatization.
The preprocessed data is saved in the "processed_headline" folder.

"WordCount.java," "WCMapper.java," and "WCReducer.java" contain the driver, mapper, and reducer codes respectively, used for counting word frequencies.
The results of the word count analysis are saved in the "mapred_results" folder.

"others.py" is a Python code that performs a similar word frequency count using a non-MapReduce algorithm.
The results of this Python code are saved in the "python_results" folder.

The "analysis.py" file is used to analyze word frequencies and generate a word cloud based on those frequencies.
The word cloud images are saved in the "cloudimg" folder.
