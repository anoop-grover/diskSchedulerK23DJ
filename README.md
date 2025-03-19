
## **🖥️ Adaptive Disk Scheduling Visualizer**

A visual, interactive disk scheduling algorithm simulator built with Python and Tkinter.

## 📋 **Overview**

This application demonstrates various disk scheduling algorithms with an intuitive graphical interface. It provides real-time visualization of disk head movements and detailed performance metrics to help understand the efficiency of different scheduling strategies.
## ✨ **Features**

•	**Multiple Disk Scheduling Algorithms:**

o	First-Come-First-Serve (FCFS)  
o	Shortest Seek Time First (SSTF)  
o	SCAN  
o	C-SCAN  
o	LOOK  
o	C-LOOK  

•	**Interactive Request Management:**

o	Add disk requests with customizable parameters (Request Sequence, Initial Head Position)  
o	Delete or reset request entries  
o	Dynamic request queue visualization  

•	**Visual Representation:**

o	Graphical disk head movement visualization  
o	Real-time animation of seek operations  
o	Color-coded track movements for clarity  

•	**Comprehensive Performance Metrics:**

o	Total seek time  
o	Average seek time  
o	Seek sequence visualization  
o	Throughput analysis  
o	Efficiency comparison between algorithms


## **🚀 Installation & Setup**

**Prerequisites:**

•	Python 3.6+  
•	tkinter  
•	matplotlib

**Installation:**
1.Clone the repository:
    
    git clone https://github.com/your-repo/adaptiveDiskScheduler.git
    cd adaptiveDiskScheduler

2.Install the required packages:

    pip install -r requirements.txt
    
3.Run the application:

    python diskscheduler.py

## **🧙️ Usage**

1.	**Adding Requests:**

o	Enter the sequence of disk requests.  
o	Specify the initial head position.  
o	Click "Add Request" to include it in the queue.  

2.	**Selecting a Scheduling Algorithm:**

o	Choose from the dropdown menu (FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK).  
o	Click "Run Scheduler" to execute the selected algorithm.  
o	View the head movement visualization and performance metrics below.

3.	**Managing Requests:**
o	Select a request and click "Delete" to remove it.  
o	Click "Reset" to clear all requests.

## **🧬 Algorithms Explained**

•	**FCFS**: Requests are processed in the order they arrive.  
•	**SSTF**: Processes the request closest to the current head position.  
•	**SCAN**: Moves the disk head in one direction, serving requests, then reverses.  
•	**C-SCAN**: Like SCAN, but only serves requests in one pass before resetting.  
•	**LOOK**: Similar to SCAN but stops at the last request instead of going to the max/min track.  
•	**C-LOOK**: Like C-SCAN but stops at the last request before resetting.


## **📊 Performance Metrics**

•	**Total Seek Time**: Sum of all seek operations performed.  
•	**Average Seek Time**: Average movement required per request.  
•	**Throughput**: Number of requests completed per unit time.  
•	**Efficiency**: Comparison of different scheduling strategies.


## **📜 Note**

Currently, all code is contained in a single file. A proper code file structure will be implemented in upcoming updates.
## **📜 Future Enhancements**

•	Additional scheduling algorithms(F-SCAN, N-Step SCAN).  
•	Export functionality for metrics and charts.  
•	Enhanced animation of disk movements.  
•	Real-world workload simulation.

## **🤝 Contributing**

Contributions are welcome! Please feel free to submit a Pull Request.  


1.	Fork the project.
2.	Create your feature branch (git checkout -b feature/AmazingFeature).
3.	Commit your changes (git commit -m 'Add some AmazingFeature').
4.	Push to the branch (git push origin feature/AmazingFeature).
5.	Open a Pull Request.

## **📜 License**

This project is licensed under the MIT License - see the LICENSE file for details.
## **📞 Contact**

**Anoop Grover** - @anoop-grover

**Project Link** - https://github.com/anoop-grover/diskSchedulerK23DJ
