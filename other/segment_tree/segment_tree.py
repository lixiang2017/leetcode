'''
segment tree 根节点从0开始
原始数组为nums，下标使用start, end, mid等；
segment tree下标均使用含有*node*的，比如node, left_node, right_node。以免混淆。


学习来自B站UP主：正月点灯笼。将其CPP版本改成Python3。

推测：
线段树所使用的数组长度至少是原始数组的四倍。（三倍不够用）
'''


def build_tree(nums, tree, node, start, end):
	print('start, end: ', start, end)
	print('node: ', node)
	if start == end:
		tree[node] = nums[start]
		return

	mid = (start + end) // 2
	left_node = 2 * node + 1
	right_node = 2 * node + 2
	build_tree(nums, tree, left_node, start, mid)
	build_tree(nums, tree, right_node, mid + 1, end)
	tree[node] = tree[left_node] + tree[right_node]
	print('set tree node value, tree[{}] = [{}]'.format(node, tree[node]))


# update nums[idx] = value
def update_tree(nums, tree, node, start, end, idx, value):
	if start == end:
		nums[idx] = value
		tree[node] = value
		return

	mid = (start + end) // 2
	left_node = 2 * node + 1
	right_node = 2 * node + 2
	if start <= idx <= mid:
		update_tree(nums, tree, left_node, start, mid, idx, value)
	else:
		update_tree(nums, tree, right_node, mid + 1, end, idx, value)
	tree[node] = tree[left_node] + tree[right_node]


# query sum from L to R, [L, R]
def query_tree(nums, tree, node, start, end, L, R):
	#print('start, end: ', start, end)

	if end < L or start > R:
		return 0
	elif start == end:
		return tree[node]
	print('start, end: ', start, end)

	mid = (start + end) // 2
	left_node = 2 * node + 1
	right_node = 2 * node + 2
	sum_left  = query_tree(nums, tree, left_node, start, mid, L, R)
	sum_right = query_tree(nums, tree, right_node, mid + 1, end, L, R)
	return sum_left + sum_right


'''
这个版本才充分利用了区间和
'''
# query sum from L to R, [L, R]
def query_tree_v2(nums, tree, node, start, end, L, R):
	#print('start, end: ', start, end)

	if end < L or start > R:
		return 0
	elif L <= start and end <= R:
		return tree[node]
	elif start == end:
		return tree[node]
	print('start, end: ', start, end)

	mid = (start + end) // 2
	left_node = 2 * node + 1
	right_node = 2 * node + 2
	sum_left  = query_tree_v2(nums, tree, left_node, start, mid, L, R)
	sum_right = query_tree_v2(nums, tree, right_node, mid + 1, end, L, R)
	return sum_left + sum_right


def main():
	N = 10
	nums = list(range(N))
	tree = [-1] * (4 * N)
	# build tree
	start, end = 0, N - 1
	build_tree(nums, tree, 0, start, end)
	# print tree
	print('tree: ', tree)
	print('\n')

	# update tree
	print('-- update tree --------------')
	idx, value = 5, 505
	update_tree(nums, tree, 0, start, end, idx, value)
	# print tree
	print('tree: ', tree)
	print('\n')

	# query tree
	print('-- query tree v1 --------------')
	L, R = 2, 9
	s = query_tree(nums, tree, 0, start, end, L, R)
	print(f'sum between {L} and {R} is {s}')
	print('-- query tree v2 --------------')
	L, R = 2, 9
	s = query_tree_v2(nums, tree, 0, start, end, L, R)
	print(f'sum between {L} and {R} is {s}')


main()
