class Solution:
    def average(self, salary: List[int]) -> float:
        s=min(salary)
        a=max(salary)
        salary=set(salary)
        salary.remove(s)
        salary.remove(a)
        return sum(salary)/len(salary)