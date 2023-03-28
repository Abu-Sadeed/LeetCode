import java.util.Stack;

/*
 * @lc app=leetcode id=155 lang=java
 *
 * [155] Min Stack
 */

// @lc code=start
class MinStack {

    Stack<Integer> my_stack = new Stack<>();
    Stack<Integer> min_stack = new Stack<>();

    public MinStack() {

    }

    public void push(int val) {
        if (min_stack.isEmpty() || val <= min_stack.peek()) {
            min_stack.push(val);
        }
        my_stack.push(val);
    }

    public void pop() {
        if (my_stack.peek().equals(min_stack.peek())) {
            min_stack.pop();
        }
        my_stack.pop();
    }

    public int top() {
        return my_stack.peek();
    }

    public int getMin() {
        return min_stack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
// @lc code=end
