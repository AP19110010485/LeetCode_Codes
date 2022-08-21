class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        qm_number = 0
        n = len(target)
        m = len(stamp)
        order = [] # the reversed order
        target_list = list(target)
        while qm_number < n: # Stamp until all the characters in target_list is '?'.
            qm_added = 0
            for i in range(n - m + 1): # i stands for the position to start stamping. Stamping cannot happen outside
                valid = True
                temp_added = 0
                for j in range(m): # Check if stamp[j] == target_list[i + j] or target_list[i + j] == '?'
                    if stamp[j] == target_list[i + j]:
                        temp_added += 1
                    elif target_list[i + j] == '?':
                        continue
                    else: # Invalid position to stamp
                        valid = False
                        break
                if valid and temp_added > 0:
                    qm_added += temp_added
                    order.append(i)
                    # Change the target_list
                    for k in range(m):
                        target_list[i + k] = '?'       
            if qm_added == 0:
                # Nothing happened in this scan, then it's impossible.
                return []
            else:
                qm_number += qm_added
        order.reverse()
        return order