class Solution {

    private List<String> euler(Map<String, Queue<String>> graph, String start) {
        List<String> path = new LinkedList<>();
        Stack<String> stack = new Stack<>();
        stack.push(start);
        while(!stack.isEmpty()){
            String node = stack.peek();
            if (graph.getOrDefault(node, new PriorityQueue<>()).isEmpty()) {
                path.add(0, node); // Add to the beginning
                stack.pop();
            } else {
                stack.push(graph.get(node).poll());
            }
        }
        return path;
    }

    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, Queue<String>> graph = new HashMap<>();
        for(List<String> pair: tickets) {
            String start = pair.get(0), end = pair.get(1);
            graph.computeIfAbsent(start, t -> new PriorityQueue<>()).offer(end);
        }
        List<String> result = this.euler(graph, "JFK");
        return result;
    }
}
