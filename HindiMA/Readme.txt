This folder contains the distribution of Hindi Morphology Analyser developed at CFILT, IITB.

The folder conains 
	1) HindiMA.jar - Jar distibution of MA
	2) HindiLinguisticResources - Data resources used for Morphology Analysis
	3) Doc - Javadoc for HindiMA.jar

How to use:

1) update the "Path" field in "HindiLinguisticResources/hindiConfig" file. This variable should point to the location of HindiLinguisticResources directory.

2) Morph Analyser may be called from command line by 

java -jar HindiMA.jar <path/to/hindiConfig>/hindiConfig <word to be analysed>   >   analysis.txt

OR

1) Put HindiMA.jar in your classpath
2) Intialise a variable of HindiAnalyser class with the path of the configFile (hindiConfig) 
3) call function <HindiAnalyser>.analyse(word) to analyse word

