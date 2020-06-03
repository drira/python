import time
valeur = time.time ()

def stopWatch(value):
    '''From seconds to Days;Hours:Minutes;Seconds'''

    valueD = (((value/365)/24)/60)
    Days = int (valueD)

    valueH = (valueD-Days)*365
    Hours = int(valueH)

    valueM = (valueH - Hours)*24
    Minutes = int(valueM)

    valueS = (valueM - Minutes)*60
    Seconds = int(valueS)


    print (Days,";",Hours,":",Minutes,";",Seconds)




start = time.time() # What in other posts is described is

end = time.time()         
stopWatch(end-start) #Use then my code