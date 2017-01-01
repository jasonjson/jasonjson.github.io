---
layout: post
title: Clone Graph
date: 2015-10-21 13:25:04.000000000 -04:00
type: post
published: true
status: publish
categories:
- Graph
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465506870;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:434;}i:1;a:1:{s:2:"id";i:248;}i:2;a:1:{s:2:"id";i:591;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.</em></strong></p>
<p>[expand title="code1"]</p>
<pre>
public class Solution {
    HashMap<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        // write your code here
        if (node == null) return null;
        UndirectedGraphNode newNode = new UndirectedGraphNode(node.label);
        map.put(node, newNode);
        for (UndirectedGraphNode neighbor : node.neighbors) {
            if (!map.containsKey(neighbor)) {
                UndirectedGraphNode newNeighbor = cloneGraph(neighbor);
                map.put(neighbor, newNeighbor);
            }
            newNode.neighbors.add(map.get(neighbor));
        }
        return newNode;
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title="code2"]</p>
<pre>
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null) return null;        
        HashMap<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
        Queue<undirectedgraphnode> queue = new LinkedList<undirectedgraphnode>();        
        UndirectedGraphNode newNode = new UndirectedGraphNode(node.label);
        map.put(node, newNode);
        queue.add(node);//always add old node for cloning
        while (!queue.isEmpty()) {
            UndirectedGraphNode curr = queue.poll();
            UndirectedGraphNode newCurr = map.get(curr);
            for (UndirectedGraphNode neighbor : curr.neighbors) {
                if (map.containsKey(neighbor)) {
                    newCurr.neighbors.add(map.get(neighbor));
                } else {
                    UndirectedGraphNode newNeighbor = new UndirectedGraphNode(neighbor.label);
                    newCurr.neighbors.add(newNeighbor);
                    map.put(neighbor, newNeighbor);
                    queue.add(neighbor);//neighbor might have neighbors, push it to queue
                }
            }
        }
        return newNode;
    }
</undirectedgraphnode></undirectedgraphnode></pre>
<p>[/expand]</p>
