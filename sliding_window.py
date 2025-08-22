class Sliding_window:
    def fixed_size(self, arr: list, k: int, t: int) -> int:
        if len(arr) < k:
            return None
        
        window_sum = sum(arr[:k])
        count = 0
        mean_sum = window_sum / k
        if mean_sum >= t:
            count += 1

        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i-k]
            mean_sum = window_sum / k
            if mean_sum >= t:
                count += 1

        return count

arr = [2, 1, 5, 1, 3, 2, 8, 9]
k = 3
T = 3
s = Sliding_window()
print(s.fixed_size(arr, k, T))

