# SVM categorizer

SVM machine pre-trained with limited data. This was mainly written to explore the possibility of using this kind of model to categorize paragraphs of text, cutting down on time used for manual review.
If needed, users can change the contents of parse() to suit their categorization needs.

## Technologies
Created with:
* Python 3.10

You will need matplotlib and numpy downloaded to run this program.

### Launch

Change parse() such that the word categorization fits your needs.
First run parse_text() with the data that you will train the model with. The data must be a txt file with all paragraphs seperated by empty lines. 
The coordinates for your data will appear in a new parsed.txt file. Encode it into x and y, line 74. 

```
x = np.array([0.2,0.0434783,0.33333,0.0652174,0.1111111,0,0.1666667,-0.0909091,0,-0.25,0.0294118,0.04])
y = np.array([0.1,0.0434783,-0.33333,0,0,0.22222,-0.375,-0.136364,-0.25,0.125,-0.323529,-0.08])
```

You will have to tell the program which points are in the same category, on line 78. Note that there are only two categories due to the use of a linear kernel.

Afterwards, you can use the console as-is to generate categories for new input. The console accepts command line input of txt files to be processed. I have labels 'SKIP' and 'DO' for my purposes, which can be changed on line 69-70. The labels will be written in order into parsed_results.txt files in your directory.

#### Sources

Thanks to Milecia McGregor for her model-fitting tutorial (https://www.freecodecamp.org/news/svm-machine-learning-tutorial-what-is-the-support-vector-machine-algorithm-explained-with-code-examples/).

