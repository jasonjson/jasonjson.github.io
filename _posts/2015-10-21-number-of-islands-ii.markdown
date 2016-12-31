---
layout: post
title: Number of Islands II
date: 2015-10-21 03:03:07.000000000 -04:00
type: post
published: true
status: publish
categories:
- DFS Backtracking
- Matrix
tags:
- Hard
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469283843;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1949;}i:1;a:1:{s:2:"id";i:591;}i:2;a:1:{s:2:"id";i:1510;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    class UnionFind {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int find (int x) {
            if (!map.containsKey(x)) {
                map.put(x, x);
                return x;
            }
            int result = x;//compress path: add a loop to find() that links every node on the path to the root.
            while (result != map.get(result)) {
                result = map.get(result);
            }
            while (x != map.get(x)) {
                int temp = map.get(x);
                map.put(x, result);
                x = temp;
            }
            return x;
        }
    }
    public int convertToId(int x, int y, int m) {
        return x * m + y;//id must be x * col + y!!!! this is the only way to make it unique!!!
    }
    public List<integer> numIslands2(int n, int m, Point[] operators) {
        List<integer> result = new ArrayList<integer>();
        if (operators == null || operators.length == 0) return result;        
        int[] dx = {0, -1, 0, 1}, dy = {-1, 0, 1, 0};
        int[][] grid = new int[n][m];
        UnionFind uf = new UnionFind();
        int count = 0;
        for (Point p : operators) {
            count ++;
            int x = p.x, y = p.y;
            grid[x][y] = 1;
            int id = convertToId(x, y, m);
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && grid[nx][ny] == 1) {//dont forget this condition
                    int nid = convertToId(nx, ny, m);
                    int father = uf.find(id), nfather = uf.find(nid);
                    if (father != nfather) {
                        count --;
                        uf.map.put(father, nfather);
                    }
                }
            }
            result.add(count);
        }
        return result;
    }
}
</integer></integer></integer></pre>
<p>[/expand]</p>
