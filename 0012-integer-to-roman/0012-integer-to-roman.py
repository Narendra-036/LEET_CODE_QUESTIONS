class Solution:
    def intToRoman(self, num: int) -> str:
      ans=''
      for i in range(1,5):
        
        if i==1:
          a=num//1000
          if a==0:
            continue
          ans=ans+(a*'M')
          num=num%1000
        elif i==2:
          
          a=num//100
          if a==0:
            continue
          if a<5:
            if a!=4:
              ans=ans+(a*'C')
            else:
              ans=ans+'CD'
          elif a==5:
            ans=ans+'D'
          elif a==9:
            ans=ans+'CM'
          elif a>5 and a<9:
            l=a%5
            ans=ans+'D'+l*'C'
          else:
            a+=1
          num=num%100
        elif i==3:
          a=num//10
          if a==0:
            continue
          if a<5:
            if a!=4:
              ans=ans+(a*'X')
            else:
              ans=ans+'XL'
          elif a>=5 and a<9:
            l=a%5
            ans=ans+'L'+(l*'X')
          else:
            ans=ans+'XC'
          num=num%10
        else:
          if num==0:
            continue
          if num<5:
            if num!=4:
              ans=ans+num*'I'
            else:
              ans=ans+'IV'
          elif num>=5 and num!=9:
              l=num%5
              ans=ans+'V'+l*'I'
          else:
              ans=ans+'IX'
              
      return ans
          
            