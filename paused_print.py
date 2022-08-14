import time
#Just print a single char and wait for a few milliseconds .. like old conesole interfaces
def console(msg):
  words = list(msg)  # ['I', 'need', 'practice']
  for word in words:
    print(word.upper(), end ="",flush=True)
    time.sleep(0.02)
