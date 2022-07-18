var kClosest = function(points, k) {
    return quickSelect(points, k)
};

var quickSelect = function(points, k) {
    let left = 0, right = points.length - 1
    let pivotIndex = points.length
    while (pivotIndex !== k) {
        // Repeatedly partition the array
        // while narrowing in on the kth element
        pivotIndex = partition(points, left, right)
        if (pivotIndex < k) {
            left = pivotIndex
        } else {
            right = pivotIndex - 1
        }
    }
    
    // Return the first k elements of the partially sorted array
    return points.slice(0, k)
};

var partition = function(points, left, right) {
    let pivot = choosePivot(points, left, right)
    let pivotDist = squaredDistance(pivot)
    while (left < right) {
        // Iterate through the range and swap elements to make sure
        // that all points closer than the pivot are to the left
        if (squaredDistance(points[left]) >= pivotDist) {
           [points[left], points[right]] = [points[right], points[left]]
            right--
        } else {
            left++
        }
    }
    
    // Ensure the left pointer is just past the end of
    // the left range then return it as the new pivotIndex
    if (squaredDistance(points[left]) < pivotDist)
        left++
    return left
};

// Choose a pivot element of the array
const choosePivot = (points, left, right) => points[left + ((right - left) >> 1)]

// Calculate and return the squared Euclidean distance
const squaredDistance = ([x,y]) => x ** 2 + y ** 2