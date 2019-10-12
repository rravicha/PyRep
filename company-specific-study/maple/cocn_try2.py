import time
import concurrent.futures

def workload(seconds):
	print(f"Starting {seconds}")
	time.sleep(seconds)
	print(f"Done {seconds}")

sec_list=list(range(6))

with concurrent.futures.ThreadPoolExecutor() as executor:
	