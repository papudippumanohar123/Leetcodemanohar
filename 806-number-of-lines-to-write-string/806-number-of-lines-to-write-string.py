class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        su=0
        c=0
        for i in range(len(s)):
            su=su+widths[ord(s[i])-ord('a')]
            if su>100:
                su=widths[ord(s[i])-ord('a')]
                c=c+1
                
            
        
                
                
               
        return [c+1,su]
                
                
                
            
        