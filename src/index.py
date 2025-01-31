import mmap
import os
import sys
import time

def extract_logs(log_file, date):
    output_dir = "../output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/output_1{date}.txt"

    with open(log_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            if line[:10] == date:
                outfile.write(line)



def find_first_occurrence(filename, target_date):
    with open(filename, "r") as f:
        mmapped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        
        file_size = os.fstat(f.fileno()).st_size
        low, high = 0, file_size

        while low < high:
            mid = (low + high) // 2
            
            mmapped_file.seek(mid)
            mmapped_file.readline()
            
            position = mmapped_file.tell()
            line = mmapped_file.readline().decode('utf-8', errors='ignore')
            
            if not line:
                break

            log_date = line[:10] 
            
            if log_date < target_date:
                low = position 
            else:
                high = mid
            
        return low

def copy_logs_from_position(filename, output_filename, start_position):
    with open(filename, "r") as src, open(output_filename, "w") as dest:
        src.seek(start_position)
        while chunk := src.read(1024 * 1024):
            dest.write(chunk)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please run command in following fashion: python index.py YYYY-MM-DD")
        sys.exit(1)

    log_file = 'logs_2024.log'
    search_date = sys.argv[1]

    start = time.time()
    extract_logs(log_file, search_date)
    end = time.time()
    print(f"Task done using normal reading line by line in {str(end-start)}s")

    start = time.time()
    # Searching for the first log entry on "search_date"
    position = find_first_occurrence(log_file, search_date)
    # copying logs from first position of date to "output"
    output_file = f"../output/output_2{search_date}.txt"
    copy_logs_from_position(log_file, output_file, position)
    end = time.time()
    print(f"Task Completed using binary search in {str(end-start)}s")