class Solution {
    private static int maxSumRec( int [] a, int l, int r) {
        // base
        if (l == r) {
            return a[l];
        }

        int totalMax = -99999999;
        int center = (l + r) / 2;

        // left
        totalMax = Math.max(totalMax, maxSumRec(a, l, center));

        // right
        totalMax = Math.max(totalMax, maxSumRec(a, center + 1, r));

        // across
        int maxLeft = -99999999;
        int leftTotal = 0;
        for (int i = center; i >= l; i--) {
            leftTotal += a[i];
            maxLeft = Math.max(maxLeft, leftTotal);
        }

        int maxRight = -99999999;
        int rightTotal = 0;
        for (int i = center + 1; i <= r; i++) {
            rightTotal += a[i];
            maxRight = Math.max(maxRight, rightTotal);
        }

        return Math.max(totalMax, maxLeft + maxRight);

    }

    public int maxSubArray(int[] nums) {
        return maxSumRec (nums, 0, nums.length - 1);
    }
}
