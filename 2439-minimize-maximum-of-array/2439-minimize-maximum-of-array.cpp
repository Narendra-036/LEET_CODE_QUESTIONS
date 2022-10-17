class Solution {
public:
    int minimizeArrayValue(vector<int>& a) {
        int n = a.size();
        vector<long long> nums(n);
        for(int i=0; i<n; ++i) nums[i] = a[i];
        long long sum = 0;
        for(auto c: nums) sum+=c;
        long long l=ceil((double)sum/n), r=1e9+4, m;
        vector<long long> temp = nums;
        long long ans = 1e9;
        while(l<=r){
            // cout << l << ' ' << r <<endl;
            m = ceil(((double)l+r)/2);
            // cout << m << endl;
            for(int i=n-1; i>0; --i){
                if(temp[i]<=m) continue;
                long long diff = temp[i]-m;
                temp[i] = m;
                temp[i-1] += diff;
            }
            long long tans = *max_element(temp.begin(),temp.end());
            // cout << tans << endl;
            if(tans <= m) r = m-1;
            else l = m+1;
            ans = min(ans,tans);
            temp = nums;
        }
        return ans;
    }
};