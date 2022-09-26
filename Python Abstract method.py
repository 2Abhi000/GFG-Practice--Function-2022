#Python Abstract method check anagram strings
from abc import ABC, abstractmethod
 
class Anangram(ABC):
 
    @abstractmethod
    def anagram(self):
        pass
class implements_anagram(Anangram):
    def anagram(self,s):
        st=s.split()
        s1=st[0]
        s2=st[1]
        if len(s1)==len(s2):
            print('ANAGRAM')
        else:
            print('NOT ANAGRAM')


st=input("Enter the string: ")   

imp=implements_anagram()
imp.anagram(st)
