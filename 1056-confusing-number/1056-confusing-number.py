class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid = {2,3,5,7,4}
        string = [num for num in str(n)]
        valid = {'0': '0', '1':'1', '6': '9', '8':'8', '9':'6'}
        new_num = []
        
        for digits in string:
            if int(digits) in invalid:
                return False
            else:
                new_num.append(valid[digits])
                
        if new_num[::-1] == string:
            return False
        
        return True
            
        