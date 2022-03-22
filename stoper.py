import time
def time_convert(sekundy):
  minuty = sekundy // 60
  sekundy = sekundy % 60
  godziny = minuty // 60
  minuty = minuty % 60
  print("czas = {0}:{1}:{2}".format(int(godziny),int(minuty),sekundy))
input("kliknij enter by zacząć")
start_time = time.time()
input("kilknij enter by zakończyć")
end_time = time.time()
time_lapsed = end_time - start_time

