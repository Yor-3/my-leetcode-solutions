class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()
        left, right = 0, min(len(tasks), len(workers))

        def can_assign(k):
            if k == 0:
                return True
            used_pills = 0
            avail = workers[-k:]  # Take the k strongest workers
            tasks_subset = tasks[:k]  # Take the k easiest tasks
            
            # We'll process tasks from hardest to easiest
            for t in reversed(tasks_subset):
                if not avail:
                    return False
                # Try to assign without pill first
                if avail[-1] >= t:
                    avail.pop()
                else:
                    # Need to use a pill - find first worker that can do it with pill
                    found = False
                    for i in range(len(avail)):
                        if avail[i] + strength >= t:
                            found = True
                            avail.pop(i)
                            used_pills += 1
                            break
                    if not found or used_pills > pills:
                        return False
            return True

        while left < right:
            mid = (left + right + 1) // 2
            if can_assign(mid):
                left = mid
            else:
                right = mid - 1

        return left