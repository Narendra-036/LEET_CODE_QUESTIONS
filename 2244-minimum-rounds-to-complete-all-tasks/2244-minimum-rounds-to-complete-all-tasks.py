class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        task_map = Counter(tasks)
        # print(task_map)
        rounds = 0
        for count in task_map.values():
            if count == 1:
                return -1
            rounds += count // 3 + min(1, count % 3)

        return rounds