### **Solutions Considered**  

1. **Line-by-Line Reading (Initial Approach)**  
   - I first attempted reading the log file **line by line** using Node.js's `readline` module.  
   - This method is memory efficient since it does not load the entire file into memory.  
   - However, it still requires scanning the entire file sequentially, which can be slow for large files.  

2. **Binary Search for Faster Access (Optimized Approach)**  
   - Since the logs are sorted by date, I considered using **binary search** to find the first occurrence of the target date.  
   - The idea was to jump to the correct position in the file instead of scanning everything.  
   - However, unlike an array, a file does not have direct indexing for lines, making binary search difficult.  

3. **Memory-Mapped File (`mmap`)**  
   - After researching, I found a method using `mmap`, which maps a portion of the file into memory for faster access.  
   - This approach theoretically allows seeking and reading data efficiently without loading the entire file.  
   - However, in practice, it performed worse than expected—likely due to disk I/O overhead and the complexity of handling newlines properly in a massive file.  

### **Final Solution Summary**  

After testing different approaches, I found that the **line-by-line reading method** performed the best in terms of both **efficiency** and **simplicity**. While binary search would be ideal in an indexed dataset, implementing it efficiently on a 1TB text file proved impractical. The `mmap` approach, despite being promising, did not offer significant improvements and, in some cases, performed worse.  

Thus, I chose the **line-by-line reading** approach while ensuring that:  
1. The script stops reading once it surpasses the target date (early termination).  
2. It writes only the relevant logs to an output file efficiently.  

### **Steps to Run**   

1. **Prepare the log file** (`logs_2024.log`) in the same directory as the script.  

2. **Run the script with the target date as an argument**:  
   ```sh
   python index.py 2024-12-01
   ```  

3. **Output logs will be saved to** `output_2024-12-01.txt`  

4. **Check execution time** printed in the console to verify performance.  