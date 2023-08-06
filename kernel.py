import time
import sys
def init():
    print("""  
                                  ______ 
                                 |____  |
  _ __ _____   _____ _ __ ___  ___   / / 
 | '__/ _ \ \ / / _ \ '__/ __|/ _ \ / /  
 | | |  __/\ V /  __/ |  \__ \  __// /   
 |_|  \___| \_/ \___|_|  |___/\___/_/    
   reverse7 kernel. GlassOS 3.0
                                          """)
    import shell
    import kernel



def clock():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Current time is " + current_time)

def shutdown():
    print("Shutting down...")
    sys.exit()
# for compiling (with pyinstaller), only compile the kernel