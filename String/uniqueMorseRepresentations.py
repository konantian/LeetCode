#Source : https://leetcode.com/problems/count-and-say/
#Author : Yuan Wang
#Date   : 2018-07-04
'''
********************************************************************************** 
International Morse Code defines a standard encoding where each letter is mapped 
to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", 
"c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given 
below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.",
"---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse 
code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the 
concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation 
of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
**********************************************************************************/
'''

#Self solution, Time complexity:O(n) Space complexity:O(n)
def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    import string
    
    result=[]
    result=set(result)
    alphabet=list(string.ascii_lowercase)
    cod=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    Morse=dict(zip(alphabet,cod))
    count=0
    for x in words:
        content=""
        for i in x:
            if i in Morse.keys():
                content+=Morse[i]
        if content not in result:
            count+=1
            result.add(content)

    return count

words=["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(words))