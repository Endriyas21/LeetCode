class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> store = new HashMap<>();
        for(int num : nums){
            store.put(num, store.getOrDefault(num, 0)+1);
        }
        PriorityQueue<Map.Entry<Integer,Integer>> maxHeap = new PriorityQueue<>(Collections.reverseOrder(Map.Entry.comparingByValue()));
        maxHeap.addAll(store.entrySet());
        int[] temp = new int[k];
        int index = 0;
        while (k > 0){
            temp[index++] = maxHeap.poll().getKey();
            k--;
        }
        return temp;
    }
}