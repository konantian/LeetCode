'''
Source : https://oj.leetcode.com/problems/plus-one/
Author : Yuan Wang
Date   : 2018-05-28

/********************************************************************************** 
* 
* Given a non-negative number represented as an array of digits, plus one to the number.
* 
* The digits are stored such that the most significant digit is at the head of the list.
*               
**********************************************************************************/
'''


#convert the list to an integer and plus this inter by one
#then convert it back to string and list it to get a new list
#time complexity O(n), space complexity O(n)
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits=[str(i) for i in digits]
    number="".join(digits)
    number=int(number)
    number+=1
    number=str(number)
    
    digits=[int(i) for i in number]
    
    return digits

def plusOneB(digits):
    d = [str(x) for x in digits]
    num = int(''.join(d)) + 1
    
    return list(map(int, str(num)))

#iterate the list from the end, detect if any digit is 9
#if it is 9, make it to 0 and add by 1 at the digit before it
#if initial number is 9, we need add a 1 at the front of the list
def plusOneC(digits):

    for i in range(len(digits)-1,-1,-1):
        if digits[i] < 9:
            digits[i]+=1
            return digits
        else:
            digits[i] = 0

    digits.insert(0,1)
    return digits

digits=[9]
print(plusOneC(digits))