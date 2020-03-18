# __name__ == '__main__ is required for all multiprocessing module usage
# each example below has its own name == main, but all are commented out except
# the example in use as they only one name == main can run concurrently

import os
import time
import logging
from multiprocessing import Process, Lock, Value, Pool, Queue, current_process
from multiprocessing import log_to_stderr, get_logger

#-------------------------------------------------------------------------------------
# Example 1, square 4 numbers and print out process id's (in no particular order)
#-------------------------------------------------------------------------------------
def square(num):
	result = num * num
    
    #will get the os process id of current running process using os.getpid()
	#this number is some random amount and does not necessarily signify anything
    #process_id = os.getpid()
	#print(f'Process ID: {process_id}')
	
	#for a more understandaple process id, current_process() method can be used
	#to get the name of the process objects
	process_name = current_process().name
	print(f'Process Name: {process_name}')
	
	print(f'The number {num} square is: {result}')
	
#Example 1 __name__ == '__main__'
'''
if __name__ == '__main__':
	processes = []
	numbers = [1,2,3,4]   

	#In the case below (processes may not be in order, must use lock for that)
	#This is ok for my Yahoo Stock History data pull
	for num in numbers:
		#Processes are spawned by creating a Process object and calling its
		#start() method
		process = Process(target = square, args = (num,))
		processes.append(process)
		process.start()
'''

#----------------------------------------------------------------------------------
# Example 2 (creates a large range of numbers and processes)
# and joins them so they run in order and also artificially slows 
# things down using time.sleep() so that task manager will register them
#----------------------------------------------------------------------------------
def square2(numbers):
	for num in numbers:
		time.sleep(0.5)
		result = num * num
		print(f'The number {num} square is: {result}')
	
if __name__ == '__main__':
	processes = []
	numbers = range(100)   

	#Creates 50 processes
	for i in range(50):
		process = Process(target = square2, args = (numbers,))
		processes.append(process)
		process.start()
	
	#this joins the processes
	for process in processes:
		process.join()
	
	print('Multiprocessing Complete')


#-----------------------------------------------------------------------------------------------
# Example 3 Locks
#-----------------------------------------------------------------------------------------------
#ex 3a funcs
def add_500_noMulti(total):
	for i in range(100):
		time.sleep(0.01)
		total += 5
	return(total)
	
def sub_500_noMulti(total):
	for i in range(100):
		time.sleep(0.01)
		total -= 5
	return(total)

#ex 3b funcs
def add_500_noLock(total):
	for i in range(100):
		time.sleep(0.01)
		total.value += 5
	
def sub_500_noLock(total):
	for i in range(100):
		time.sleep(0.01)
		total.value -= 5
		
#ex 3c funcs		
def add_500_lock(total, lock):
	for i in range(100):
		time.sleep(0.01)
		lock.acquire()
		total.value += 5
		lock.release()
	
def sub_500_lock(total, lock):
	for i in range(100):
		time.sleep(0.01)
		lock.acquire()
		total.value -= 5
		lock.release()


# Locks enforce limits on access to a resource in an environment where there are 
# many threads of executions (or running processes)

#ex 3a: basic no multiprocessing example
'''
if __name__ == '__main__':
	total = 500
	print(f'start amount : {total}')
	total = add_500_noMulti(total)
	print(f'add 500 = {total}')
	total = sub_500_noMulti(total)
	print(f'subtract 500 = {total}')
'''
	
#ex 2: Uses Shared value resource created using
#multiprocessing package Value() method
#note that due to no locks, this does not always return 500
#like it should
'''
if __name__ == '__main__':
	total = Value('i', 500)
	add_process = Process(target=add_500_noLock, args=(total,))
	sub_process = Process(target=sub_500_noLock, args=(total,))
	add_process.start()
	sub_process.start()
	add_process.join()
	sub_process.join()
	print(total.value)
'''
	
#ex 3: Utilizes locks in order to ensure calculations are
#performed in order
'''
if __name__ == '__main__':
	total = Value('i', 500) #shared resource value object
	lock = Lock()
	
	#This uses logging package in order to display program info 
	#on the cmd line
	log_to_stderr() #prints out all logging info to terminal as code is run
	logger = get_logger()
	logger.setLevel(logging.INFO) #set types of logs to return (DEBUG,INFO, etc.)
	
	add_process = Process(target=add_500_lock, args=(total, lock))
	sub_process = Process(target=sub_500_lock, args=(total, lock))
	
	add_process.start()
	sub_process.start()
	
	add_process.join()
	sub_process.join()
	
	print(total.value)
'''

#-----------------------------------------------------------------------------------------------
# Ex 4 Pool
#-----------------------------------------------------------------------------------------------
# Pool objects are asynchronus groups of processes (called workers) that run simultaneously
def sum_square(numbers):
	s = 0
	for i in range(numbers):
		s += i * i
	return(s)

def sum_square_with_mp(numbers):
	start = time.time()
	p = Pool() #automatically uses all cores on machine, can set explicitly with Pool(6)
	#print(os.cpu_count()) # counts number of cores on pc
	
	#takes the sum_square function and numbers iterable and maps each element appropriately 
	#based on number of processors on computer
	result = p.map(sum_square, numbers)
	p.close()
	p.join()	
	
	end = time.time() - start
	print(f'Processing {len(numbers)} numbers took {end} time using multiprocessing')

def sum_square_no_mp(numbers):
	start = time.time()
	result = []
	
	for i in numbers:
		result.append(sum_square(i))
		
	end = time.time() - start
	print(f'Processing {len(numbers)} numbers took {end} time using serial processing')
'''	
if __name__ == '__main__':
	numbers = range(10000)
	sum_square_with_mp(numbers) #multiprocessing is faster with larger numbers val
	sum_square_no_mp(numbers)   #regular processing is faster with smaller numbers val 
'''
	
#-----------------------------------------------------------------------------------------------
# Ex 5 Queue
#-----------------------------------------------------------------------------------------------
def squareit(numbers, queue):
	for i in numbers:
		queue.put(i * i)
		
def cubeit(numbers, queue):
	for i in numbers:
		queue.put(i * i * i)

'''
if __name__ == '__main__':

	numbers = range(5)
	queue = Queue()
	
	square_process = Process(target = squareit, args = (numbers, queue))
	cube_process = Process(target = cubeit, args = (numbers, queue))
	
	square_process.start()
	cube_process.start()
	
	#join ensures all processes completed before proceeding with program
	square_process.join()
	cube_process.join()
	
	#access the queue and gets its contents until empty
	#note that queue elements may not be in order, however, the contents of
	#the queue are writing their results correctly becuase the processes are sharing
	#the same queue resource
	while not queue.empty():
		print(queue.get())
'''