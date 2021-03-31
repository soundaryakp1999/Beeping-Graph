import winsound
import time
from sonipy.sonify import SonifyTool
import matplotlib.pyplot as plt
import threading
import time
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')

def beep(x_cor,y_cor):
  C4 = 261.6 # Hz
  frequency_args = {
    'frequency_min' : C4,
    'frequency_max' : C4*4
  }

  duration_args = {
    'time_total' : 10000, # ms
  }

  duration_scale = 1. / 2000. # x value / time (ms)



  Tone = SonifyTool(x_cor, y_cor,frequency_args = frequency_args,duration_args = duration_args,bliplength=0.5)
  Tone.play()
  Tone.save()
  time.sleep(2)
  winsound.PlaySound('tones/multitone.wav', winsound.SND_FILENAME)




def plot_point(x_cor,y_cor):
  plt.plot(x_cor, y_cor)
  plt.xlabel('x - axis')
  plt.ylabel('y - axis')
  plt.title('My  graph!')
  plt.show()



print("Enter total no. of terms followed by degree and coefficient separated by space on each new line")
n=int(input())
terms={}
x_cor=[]
y_cor=[]
for i in range (0,n):
    x, y = map(int, input().split(' '))
    terms[x]=y
for x in range(-15,15):
    x_cor.append(x)
    y=0
    for degree,coefficient in terms.items():
        temp=x**degree
        temp=temp*coefficient
        y=y+temp
    y_cor.append(y)

threading.Thread(target=plot_point,args=(x_cor,y_cor)).start()
threading.Thread(target=beep,args=(x_cor,y_cor)).start()

plot_point(x_cor,y_cor)

beep(x_cor,y_cor)

