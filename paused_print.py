import time
#Just print a single char and wait for a few milliseconds .. like old conesole interfaces
def printD(msg):
  words = list(msg)  # ['I', 'need', 'practice']
  for word in words:
    print(word, end ="",flush=True)
    time.sleep(0.05)