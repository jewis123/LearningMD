### 数据结构策略

1. 滑动窗口：可以用列表维护窗口，也可以用双指针维护窗口范围
3. 双指针（相向首尾指针，同向快慢指针）
5. 合并间隔 
6. 循环排序（从前到后将值和值对应的索引元素互换位置）
7. 广度优先搜索：队列
8. 深度优先搜索：栈
9. 双堆
10. [单调栈/队列](https://leetcode-cn.com/explore/learn/card/queue-stack/218/stack-last-in-first-out-data-structure/879/)：通过维护一个单调结构避免重复遍历，使得操作复杂度能维持在O(N)
11. K路合并：利用小根堆将多个有序数组合并成1个有序数组。py库：heapq.merge
11. 线段树：是一个完全二叉树，它在各个节点保存一条线段（数组中的一段子数组），主要用于高效解决连续区间的动态查询问题，每个操作的复杂度为O(lgN)
13. 并查集：主要解决动态连接性问题，查询点到点是否连通，合并两个连通的点

### 算法策略

1. 动态规划
2. 分治算法
3. 贪心算法
4. 回溯法
5. 

### 其他思想

1. 快速幂

2. 位操作：[异或](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/zhi-chu-xian-yi-ci-de-shu-xi-lie-wei-yun-suan-by-a/)

3. [摩尔投票法](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)： 符合条件+1，不符合条件-1，正负抵消

4. 对称遍历

   









