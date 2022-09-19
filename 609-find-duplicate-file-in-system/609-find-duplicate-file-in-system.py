class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mp=defaultdict(list);
        
        for path in paths:
            split_path=path.split(" ");
            root_path=split_path[0];
            for i in range(1,len(split_path)):
                j=0;
                while(j<len(split_path[i]) and split_path[i][j]!='('):
                    j+=1;
                file_name=split_path[i][:j];
                file_content=split_path[i][j:len(split_path[i])-1];
                mp[file_content].append(root_path+"/"+file_name);
        ans=[];
        for x,y in mp.items():
            if(len(y)==1):
                continue;
            ans.append(y);
        
        return ans