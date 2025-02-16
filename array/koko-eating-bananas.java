class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        // Helper function to calculate the total hours needed to eat all bananas at speed k
        int calculateHours(int[] piles, int k) {
            int hours = 0;
            for (int pile : piles) {
                // Calculate the hours needed for the current pile and add it to the total hours
                // (pile + k - 1) / k is equivalent to Math.ceil(pile / k)
                hours += (pile + k - 1) / k;
            }
            return hours;
        }

        // Binary search to find the minimum eating speed
        int left = 1; // Minimum possible speed
        int right = Arrays.stream(piles).max().getAsInt(); // Maximum possible speed
        int result = right;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int hours = calculateHours(piles, mid);

            if (hours <= h) {
                result = mid; // Update result to the current mid
                right = mid - 1; // Try a smaller speed
            } else {
                left = mid + 1; // Try a larger speed
            }
        }

        return result;
    }
}