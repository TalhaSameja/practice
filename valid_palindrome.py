# def removeWhiteSpacesAndCovertToLowerCase(string:str):
#     withoutWhiteSpace = string.replace(" ","")
#     convertToLowerCase = withoutWhiteSpace.lower()
#     return convertToLowerCase
    
# print(removeWhiteSpacesAndCovertToLowerCase("Hello World"))
# s = "A man, a plan, a canal: Panama"
# newstr = ""
# for i in s:
#     if i.isalnum():
#         newstr += i.lower()
# if newstr == newstr[::-1]:
#    print('True')        
class ValidPalindrome:
    def isPalindrome(self, s:str):
        l,r = 0, len(s)-1
        
        while l<r:
            while l<r and not self.isalnum(s[l]):
                l += 1
            while l<r and not self.isalnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isalnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z')or
         ord('a') <= ord(c) <= ord('z')or
         ord('0') <= ord(c) <= ord('9'))
        
s = "A man, a plan, a canal: Panama"
string = ValidPalindrome()
print(string.isPalindrome(s))
