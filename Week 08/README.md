# Information
Hard Deadline: 	Mon 1 Jun 2015 7:00 AM PDT  
Duration: Untimed  
Attempts: 100  

# Question 1
(True/False) It is impossible to compress a signal without compromising its integrity.

**[-]** True  
**[-]** False  


# Question 2
Signal compression is achieved due to the reduction in which of the following forms of redundancy? Check all that apply.

**[-]** Temporal redundancy in signals  
**[-]** Perceptual redundancy in signals (i.e., the presence of perceptually irrelevant information in signals)  
**[-]** Coding redundancy (i.e., the inefficient use of bits in representing signals)  
**[-]** Spatial redundancy in signals  
**[-]** Spectral redundancy in signals  


# Question 3
It is given that a discrete memoryless source (DMS) has alphabet S={a,b,c} with associated probabilities p(a)=0.2, p(b)=0.5 and p(c)=0.3. If the first two symbols emitted by the source are a and c, what is the probability of having a b emitted by the source as the third symbol?

**[-]** 0.2  
**[-]** 0.5  
**[-]** 0.7  
**[-]** 1  


# Question 4
Given a discrete memoryless source (DMS) with alphabet S={a,b,c} and associated probabilities p(a)=0.2, p(b)=0.5 and p(c)=0.3, what is the entropy of this source in unit of bits? Enter the answer to 3 decimal points.

**[-]** ?


# Question 5
For a DMS with alphabet {a,b,c,d} and associated probabilities p(a)=0.6, p(b)=0.3, p(c)=0.08, and p(d)=0.02, we want to design a Huffman code. In this design, when the two symbols with the lowest probabilities are combined to form a new symbol, 0 is assigned to the symbol of the two with higher probability. For example, in the initial stage, the two symbols with the lowest probabilities are c with p(c)=0.08 and d with p(d)=0.02. When c and d are combined, 0 is assigned to c, and 1 is assigned to d. When the encoding is complete, which of the following is the codeword assigned to c?

**[-]** 0  
**[-]** 01  
**[-]** 111  
**[-]** 110  


# Question 6
Assume a DMS with alphabet {a,b,c} and associated probabilities p(a)=0.5, p(b)=0.3, and p(c)=0.2. A sequence of length 4 is encoded using arithmetic coding, and the encoded number (the tag) is equal to 0.386. In the encoding process, the following limits are used FX(1)=0.5, FX(2)=0.8, and FX(3)=1. Based on this information, which of the following is the encoded 4-symbol sequence

**[-]** abca  
**[-]** abcb  
**[-]** baca  
**[-]** bbac  


# Question 7
In this problem, you will write a MATLAB program to compute the entropy of a given gray-scale image. Follow the instructions below to finish this problem.

(1) Download the input image from [here](https://d396qusza40orc.cloudfront.net/digital/images/week8_quizzes/Cameraman256.bmp). The input is a gray-scale image with pixel values in the range [0,255]. Treat the pixel intensities in this image as symbols emitted from a DMS.

(2) Build a probability model (i.e., an alphabet with associated probabilities) corresponding to this input image. Specifically, this alphabet consists of symbols {0,1,2,⋯,255}. In order to find the probabilities associated with each symbol, you will need to scan over all the pixels in this image, and for each pixel, adjust the probability associated with that pixel's intensity value accordingly, or in other words find the histogram of the image. Make sure you normalize the probability model correctly such that each probability is a real-valued number in [0,1].

(3) Compute the entropy using the formula that you have learned in class. Enter the result below to at least 2 decimal points.

**[-]** ?