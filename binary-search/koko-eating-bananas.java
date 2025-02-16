class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        // Binary search to find the minimum eating speed
        int left = 1; // Minimum possible speed
        int right = Arrays.stream(piles).max().getAsInt(); // Maximum possible speed
        int minSpeed = right;

        while (left <= right) {
            int midSpeed = left + (right - left) / 2;
            int requiredHours = calculateTotalHours(piles, midSpeed);

            if (requiredHours <= h) {
                minSpeed = midSpeed; // Update minSpeed to the current midSpeed
                right = midSpeed - 1; // Try a smaller speed
            } else {
                left = midSpeed + 1; // Try a larger speed
            }
        }

        return minSpeed;
    }

    // Helper function to calculate the total hours needed to eat all bananas at speed k
    private int calculateTotalHours(int[] piles, int k) {
        int totalHours = 0;
        for (int pile : piles) {
            // Calculate the hours needed for the current pile and add it to the total hours
            // (pile + k - 1) / k is equivalent to Math.ceil(pile / k)
            totalHours += (pile + k - 1) / k;
        }
        return totalHours;
    }
}