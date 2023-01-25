import heap

def schedule(array):
    heap.build_max_heap(array, len(array))

def get_next_task(array, heap_size):
	return heap.heap_extract_max(array, heap_size)

def increase_task_priority(array, i, key):
	heap.heap_increase_key(array, i, key)

def add_next_task(array, dict, key):
	heap.heap_insert(array, dict, key)

def get_all_tasks_sorted(array):
	heap.heap_sort(array, len(array))

def print_user_input():
	for x in user_input:
		print(x)

user_input = [	{'priority': 5, 'start_time': 10, 'duration': 20, 'type': 'audio', 'recorder': 'rec1'},
				{'priority': 3, 'start_time': 15, 'duration': 10, 'type': 'video', 'recorder': 'rec2'},
		 		{'priority': 1, 'start_time': 2,  'duration': 60, 'type': 'audio', 'recorder': 'rec3'},
		 		{'priority': 6, 'start_time': 13, 'duration': 33, 'type': 'audio', 'recorder': 'rec4'},
		 		{'priority': 2, 'start_time': 8, ' duration': 48, 'type': 'video', 'recorder': 'rec5'},
		 		{'priority': 4, 'start_time': 26, 'duration': 25, 'type': 'video', 'recorder': 'rec6'}]

#Schedule
schedule(user_input)

#Max element

#heap_size = len(user_input)
#local_max, local_heap_size = get_next_task(user_input, heap_size)
#print("")
#print(local_max)

#Increase task priority
i = 1
key = 12

increase_task_priority(user_input, i, key)

#Add next task
key = 55
dict = {'priority': 55, 'start_time': 55, 'duration': 55, 'type': 'video', 'recorder': 'rec7'}

add_next_task(user_input, dict, key)

#Sort tasks
get_all_tasks_sorted(user_input)

print_user_input()
