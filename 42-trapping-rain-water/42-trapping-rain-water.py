class Solution:
    def trap(self, height: List[int]) -> int:
        """
        [0,1,0,2,1,0,1,3,2,1, 2, 1]
         0 1 2 3 4 5 6 7 8 9 10 11
                         ^
        total_water = 6
        prev_highest_point = 2
        water_to_add = min(prev_highest_point, nextHighest) - height[i]
        nextHighestPoint = {
            # index -> nextHighestPointValue
            0: 1,
            1: 2,
            2: 2
            3: 3,
            4: 3,
            5: 3,
            6: 3,
            7: None,
            8: 2,
            9: 2,
            10: None,
            11: None,
        }
        curr_sum = min(height[lo], height[hi]) * (hi - lo)
        """
        # index -> next highest point value
        nextHighest = {}
        for i in range(len(height) -1, -1, -1):
            if i == len(height) -1:
                nextHighest[i] = None
                continue
            # if next highest is not None
            if nextHighest[i+1]:
                # if the next number's highest num is greater
                # than our current number, keep it as the next highest
                if nextHighest[i+1] >= height[i]:
                    nextHighest[i] = nextHighest[i+1]
                # otherwise our current number has no next greater num
                else:
                    nextHighest[i] = None
            # otherwise set next highest to the next number
            # in the array if it is greater than our current num
            elif height[i] <= height[i+1]:
                nextHighest[i] = height[i+1]
            else:
                nextHighest[i] = None

        total_water = 0
        prev_highest_point = 0
        for i in range(len(height)):
            if nextHighest[i]:
                water_to_add = min(prev_highest_point, nextHighest[i]) - height[i]
                if water_to_add > 0:
                    total_water += water_to_add
            prev_highest_point = max(prev_highest_point, height[i])
        return total_water
        """
        [0,1,0,2,1,0,1,3,2,1, 2, 1]
         0 1 2 3 4 5 6 7 8 9 10 11
         ^
        total_water = 0
        prev_highest_point = 0
        water_to_add = min(prev_highest_point, nextHighest) - height[i]
        nextHighest: {11: None, 10: None, 9: 2, 8: 2, 7: None, 6: 3, 5: 3, 4: 3, 3: 3, 2: 3, 1: 3, 0: 3}
        """
        