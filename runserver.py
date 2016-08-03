import psutil
import datetime
import sys

#inital method calls for cpu, memory, disks, and disk usage on main disk
cpu = psutil.cpu_times()
mem = psutil.virtual_memory()
disks = psutil.disk_partitions()
dusage = psutil.disk_usage('/')
io_counters = psutil.net_io_counters()
net_connections = psutil.net_connections()
net_speeds = psutil.net_if_stats()

#CPU stats
cpu_count = psutil.cpu_count()
cpu_count_logical_false = psutil.cpu_count(logical=False)
cpu_user = cpu[0]
cpu_system = cpu[2]
cpu_idle = cpu[3]

#memory stats
mem_used = float(mem[3])/1000000000
mem_total = float(mem[0])/1000000000
mem_percent = mem[2]
mem_available = float(mem[4])/1000000000

#Disk stats
disk_total = float(dusage[0])/1000000000
disk_used = float(dusage[1])/1000000000
disk_free = float(dusage[2])/1000000000
disk_percent = dusage[3]

#Net I/O stats
bytes_sent = io_counters[0]
bytes_recv = io_counters[1]
packets_sent = io_counters[2]
packets_recv = io_counters[3]
errin = io_counters[4]
errout = io_counters[5]

print("")
#Boot Time
print("-------------- Boot --------------")
print("Powered on since: " + datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
print("")
print("")

#CPU stats
print("-------------- CPU ---------------")
print("CPU Count: " + str(cpu_count))
print("")
print("---- CPU Times ----")
print("User: " + str(cpu_user) + "s")
print("System: " + str(cpu_system) + "s")
print("Idle: " + str(cpu_idle) + "s")
print("")
print("")

#RAM stats
print("-------------- RAM --------------")
print("Used/Total: " + "%.2f" % mem_used + "Gb / " + "%.2f" % mem_total + "Gb")
print("Percentage: " + "%.2f" % ((mem_used/mem_total)*100) + "%")
print("Available: " + "%.2f" % mem_available + "Gb")
print("")
print("")

#Disk stats
print("-------------- Disk Usage --------------")
print("Used/Total: " + "%.2f" % disk_used + "Gb / " + "%.2f" % disk_total + "Gb")
print("Percentage: " + str(disk_percent) + "%")
print("Available: " + "%.2f" % disk_free + "Gb")
print("")
print("")

#Net stats
print("-------------- Net --------------")
print("Bytes Sent: " + str(bytes_sent))
print("Bytes Received: " + str(bytes_recv))
print("Packets Sent: " + str(packets_sent))
print("Packets Received: " + str(packets_recv))
print("Errors In: " + str(errin))
print("Errors Out: " + str(errout))
print("")
