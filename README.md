# Automated Conversation Maker


### What is Automated Conversation Maker?
As the name suggest this project tries to implement virtual agents who can communicate on there own. The communication is very basic which is introductory communication when two new people meet. The data used for carrying out the communication is extracted from facebbok using Facebook graph search API.		 

### Installation and Setup

#### 1) Install NLTK		
Install the Stanford NLTK. The NLTK and installation guidlines can be found at http://www.nltk.org/install.html		

#### 2) Download Stanford Dependancy Parser
Download stanford dependancy parser from link below		
http://nlp.stanford.edu/software/lex-parser.shtml		

After downloading stanford dependancy parser follow the steps below		
1) Locate the src folder in the repository		 
2) On line number 12 there is a following code		

command = r'java -mx1200m -cp "Path_to/stanford-parser.jar:" edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "typedDependencies" <path to>/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz ' + input_file_name +' > '+output_file_name 
#### 3) 

