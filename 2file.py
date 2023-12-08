import subprocess
import multiprocessing

def command1():
    # Replace the command with the correct one
    subprocess.run(['/content/yoyoyo/pyipadsync', '-s', 'btacg.ddns.net:16110'])

def command2():
    # Replace the command with the correct one
    subprocess.run(['/content/yoyoyo/yamato', '--mining-address', 'pyrin:qzsc50v3h0kg9fyhxeycafsumvtz237dhhucye9ucc8jjd0f3nvnzez6hj5vu'])

if __name__ == '__main__':
    # Create two separate processes for each command
    process1 = multiprocessing.Process(target=command1)
    process2 = multiprocessing.Process(target=command2)

    # Start the processes
    process1.start()
    process2.start()

    # Wait for the processes to complete
    process1.join()
    process2.join()
