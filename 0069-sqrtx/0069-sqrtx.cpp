class Solution {
public:
    int mySqrt(int x) {
        // long int start =0;
        long int prev=0;
        // int mid=start+end/2;
        while(true)
        {
            if (prev*prev==x){return prev;}
            else if(prev*prev>x){return prev-1;}
            else{prev+=1;}
        }
    }
};