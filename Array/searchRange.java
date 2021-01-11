public int[] searchRange(int[] nums, int target) {
    int[] targetRange = {-1, -1};

    // find the index of the leftmost appearance of `target`.
    for (int i = 0; i < nums.length; i++) {
        if (nums[i] == target) {
            targetRange[0] = i;
            break;
        }
    }

    // if the last loop did not find any index, then there is no valid range
    // and we return [-1, -1].
    if (targetRange[0] == -1) {
        return targetRange;
    }

    // find the index of the rightmost appearance of `target` (by reverse
    // iteration). it is guaranteed to appear.
    for (int j = nums.length-1; j >= 0; j--) {
        if (nums[j] == target) {
            targetRange[1] = j;
            break;
        }
    }

    return targetRange;
}