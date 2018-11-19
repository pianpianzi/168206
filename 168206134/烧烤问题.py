import random
def sumtime(sump,apart=0,time1=10,time2=180,s=20):
    if apart==0:
        for i in range(sump):
            tim=time1*(int(i/s) )
            tim1=time2*(int((i+1)/8))*5
            print("吧台等待时间:" + str(tim)+"----"+str(i+1))
            if i==0:
                print("烧烤等待时间:" + str(180))
            if (i+1)%8==1 and (i+1)>1:
                tim2=tim1+3*60
                print("烧烤等待时间:" + str((tim2-tim)))
            if (i+1)%8==2 or(i+1)%8==3:
                tim2=tim1+6*60
                print("烧烤等待时间:" + str((tim2-tim)))
            if(i+1)%8==4:
                tim2=tim1+9*60
                print("烧烤等待时间:" + str((tim2-tim)))
            if (i+1)%8==5 or (i+1)%8==6:
                tim2=tim1+12*60
                print("烧烤等待时间:" + str((tim2-tim)))
            if (i+1)%8==7:
                tim2=tim1+15*60
                print("烧烤等待时间:" + str((tim2-tim)))
            if (i+1)%8==0:
                tim2=tim1
                print("烧烤等待时间:" + str((tim2-tim)))             
    if apart>1 and apart<180:
        for i in range(sump):
            #tim=time1*1
            tim1=time2*(int((i+1)/8))*5
            tim3=apart*i
            print("吧台等待时间:0"+"----"+str(i+1))
            if i==0:
                print("烧烤等待时间:" + str(180))
            if (i+1)%8==1 and (i+1)>1:
                tim2=tim1+3*60
                print("烧烤等待时间:" + str((tim2-tim3)))
            if (i+1)%8==2 or(i+1)%8==3:
                tim2=tim1+6*60
                print("烧烤等待时间:" + str((tim2-tim3)))
            if(i+1)%8==4:
                tim2=tim1+9*60
                print("烧烤等待时间:" + str((tim2-tim3)))
            if (i+1)%8==5 or(i+1)%8==6:
                tim2=tim1+12*60
                print("烧烤等待时间:" + str((tim2-tim3)))
            if (i+1)%8==7:
                tim2=tim1+15*60
                print("烧烤等待时间:" + str((tim2-tim3)))
            if (i+1)%8==0:
                tim2=tim1
                print("烧烤等待时间:" + str((tim2-tim3))) 
    if apart>=180:
            print("吧台等待时间:0")
            print("烧烤等待时间:0")


sump=50
apart=0
print(sumtime(sump,apart))
