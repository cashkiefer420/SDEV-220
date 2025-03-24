class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        low, mid, high = 0, 0, len(arr) - 1
        
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid], = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
                
def main():
    t = int(input().strip())
    ob = Solution()
    
    while t > 0:
        t -= 1
        arr = list(map(int, input().strip().split()))
        ob.sort012(arr)
    
        print(' '. join(map(str, arr)))
        print("~")
    
if __name__ == "__main__":
    main()