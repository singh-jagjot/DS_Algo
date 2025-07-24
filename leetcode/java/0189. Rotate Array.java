🧠 Core Insight
When you reverse the whole array, the elements that need to go to the front (the last k elements) end up at the front,
but in reverse order. The remaining elements are also in reverse order, so you fix that by reversing each part again.

🧠 Why It Works — Conceptual Summary
The idea is that rotating an array is just rearranging two parts:
The last k elements → move to the front
The first n−k elements → shift to the right

So, the reverse steps simulate this partitioning and repositioning:
Full reverse puts both parts in the opposite order
Partial reverses correct the local order of each part

class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;
        reverse(nums, 0, n-1);
        reverse(nums, 0, k-1);
        reverse(nums, k, n-1);

    }

    void reverse(int[] arr, int i, int j) {
        while (i<j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j]=temp;
            i++;
            j--;
        }
    }
}

// This one is complicated to understand but essentially it builds on the idea of placing each element in its original position
// while keeping track of the element originally in that position. Basically, at every step, we place an element in its
// rightful position and keep track of the element already there or the one being overwritten in an additional variable.
// We can't do this in one linear pass and the idea here is based on cyclic-dependencies between elements.

public void rotate(int[] nums, int k) {
    int n = nums.length;
    k = k % n;  // Important when k > n
    int count = 0;  // To count how many elements have been moved

    for (int start = 0; count < n; start++) {
        int current = start;
        int prev = nums[start];

        do {
            int next = (current + k) % n;

            // Swap
            int temp = nums[next];
            nums[next] = prev;
            prev = temp;

            current = next;
            count++;

        } while (start != current);  // Until cycle closes
    }
}