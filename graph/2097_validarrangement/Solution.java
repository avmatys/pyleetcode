class Solution {

    private Map<Integer, Deque<Integer>> graph;

    private List<Integer> euler(int start) {
        Stack<Integer> stack = new Stack<>();
        List<Integer> result = new ArrayList<>();
        stack.push(start);
        while (!stack.empty()) {
            int node = stack.peek();
            if (this.graph.getOrDefault(node, new ArrayDeque<>()).isEmpty()) {
                result.add(node);
                stack.pop(); // Visited all related nodes
            } else {
                int next = this.graph.get(node).pop();
                stack.push(next);
            }
        }
        return result;
    }

    public int[][] validArrangement(int[][] pairs) {
        // Build a graph
        this.graph = new HashMap<>();
        Map<Integer, Integer> degree = new HashMap<>();
        for(int[] edge: pairs) {
            int start = edge[0], end = edge[1];
            this.graph.computeIfAbsent(start, t -> new ArrayDeque<>()).addLast(end);
            degree.put(start, degree.getOrDefault(start, 0) + 1); // out edge
            degree.put(end, degree.getOrDefault(end, 0) - 1); // in edge
        }
        // Find a start node
        int start = pairs[0][0];
        for(int node: degree.keySet()) {
            if (degree.get(node) == 1) {
                start = node;
                break;
            }
        }
        // Get the traverse
        List<Integer> traverse = this.euler(start);
        Collections.reverse(traverse);
        int[][] result = new int[traverse.size() - 1][2];
        for(int i = traverse.size() - 2; i >= 0; i--) {
            result[i] = new int[] {traverse.get(i), traverse.get(i + 1)};
        }   
        return result;
    }
}
