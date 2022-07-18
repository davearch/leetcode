class Solution {

    /**
     * @param Integer[][] $points
     * @param Integer $k
     * @return Integer[][]
     */
    function kClosest($points, $K) {
        $distanceArray = [];
        
        foreach($points as $key => $value) {
            $distanceArray[$key] = (pow($value[0],2) + pow($value[1], 2)); 
        }
        asort($distanceArray);
        $distanceArray = array_slice($distanceArray, 0, $K, true);
        $resultArray = [];
        
        foreach ($distanceArray as $key => $value) {
            $resultArray[] = $points[$key];
        }
        
        return $resultArray;
        
    }
}