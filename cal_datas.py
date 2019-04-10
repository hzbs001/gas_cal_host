#!C:\Users\wanglw\AppData\Local\Programs\Python\Python36\python.exe
#coding=utf-8
import time,csv,struct
from crc16_mb import crc16
len1ch = 12
len1ch_byte = 42

datas = []
regdatas = []

def write_datas(ser1,val_ad):
    pos = 192
    reg16num = 120

    cmd = 0x10
    crc = crc16()
    try:
        addr = int(val_ad.get(),16)
    except ValueError:
        addr = 0x58

    startreg = 0
    startregh = ((startreg+pos)>>8)&0xFF
    startregl = (startreg+pos)&0xFF
    reg16numh = (reg16num>>8)&0xFF
    reg16numl = reg16num&0xFF
    mb_datas = datas[0:240]
    mb_datas.insert(0,reg16numl*2)
    mb_datas.insert(0,reg16numl)
    mb_datas.insert(0,reg16numh)
    mb_datas.insert(0,startregl)
    mb_datas.insert(0,startregh)
    mb_datas.insert(0,cmd)
    mb_datas.insert(0,addr)

    myinputL = crc.createarray(mb_datas)
    print(myinputL)
    myinput = bytes(myinputL)
    ser1.write(myinput)
    time.sleep(0.03)
    ser1.flush()
    time.sleep(0.02)

    startreg = 120 
    startregh = ((startreg+pos)>>8)&0xFF
    startregl = (startreg+pos)&0xFF
    reg16numh = (reg16num>>8)&0xFF
    reg16numl = reg16num&0xFF
    mb_datas = datas[240:480]
    mb_datas.insert(0,reg16numl*2)
    mb_datas.insert(0,reg16numl)
    mb_datas.insert(0,reg16numh)
    mb_datas.insert(0,startregl)
    mb_datas.insert(0,startregh)
    mb_datas.insert(0,cmd)
    mb_datas.insert(0,addr)

    myinputL = crc.createarray(mb_datas)
    myinput = bytes(myinputL)
    ser1.write(myinput)
    time.sleep(0.03)
    ser1.flush()
    time.sleep(0.02)

    startreg = 360
    startregh = ((startreg+pos)>>8)&0xFF
    startregl = (startreg+pos)&0xFF
    reg16numh = (reg16num>>8)&0xFF
    reg16numl = reg16num&0xFF
    mb_datas = datas[480:720]
    mb_datas.insert(0,reg16numl*2)
    mb_datas.insert(0,reg16numl)
    mb_datas.insert(0,reg16numh)
    mb_datas.insert(0,startregl)
    mb_datas.insert(0,startregh)
    mb_datas.insert(0,cmd)
    mb_datas.insert(0,addr)

    myinputL = crc.createarray(mb_datas)
    myinput = bytes(myinputL)
    ser1.write(myinput)
    time.sleep(0.03)
    ser1.flush()
    time.sleep(0.02)

    startreg = 480
    startregh = ((startreg+pos)>>8)&0xFF
    startregl = (startreg+pos)&0xFF
    reg16numh = (reg16num>>8)&0xFF
    reg16numl = reg16num&0xFF
    mb_datas = datas[720:960]
    mb_datas.insert(0,reg16numl*2)
    mb_datas.insert(0,reg16numl)
    mb_datas.insert(0,reg16numh)
    mb_datas.insert(0,startregl)
    mb_datas.insert(0,startregh)
    mb_datas.insert(0,cmd)
    mb_datas.insert(0,addr)

    myinputL = crc.createarray(mb_datas)
    myinput = bytes(myinputL)
    ser1.write(myinput)
    time.sleep(0.03)
    ser1.flush()
    time.sleep(0.02)
    
def get_datas(val_src,val_0,val_1,val_2,val_3,val_4,val_5,val_6,val_7,\
        val_8,val_9,val_10,val_11,val_12,val_13,val_14,val_15,val_16,\
        val_17,val_18,val_19,val_20,val_21,val_22,val_23,val_24,val_25,\
        val_26,val_27,val_28,val_29,val_30,val_31):
    filename = val_src.get()
    if filename=='':
        filename = 'input'
    filename = filename + '.csv'
    try:
        csvFile = open(filename,'r')
    except FileNotFoundError:
        pass
    reader = csv.reader(csvFile)
    i = 0
    datas[:] = []
    regdatas[:] = []
    for row in reader:
        #Ignore first row
        if i==0:
            pass
        elif i<33:
            if i==1:
                val_0.set(row)
            elif i==2:
                val_1.set(row)
            elif i==3:
                val_2.set(row)
            elif i==4:
                val_3.set(row)
            elif i==5:
                val_4.set(row)
            elif i==6:
                val_5.set(row)
            elif i==7:
                val_6.set(row)
            elif i==8:
                val_7.set(row)
            elif i==9:
                val_8.set(row)
            elif i==10:
                val_9.set(row)
            elif i==11:
                val_10.set(row)
            elif i==12:
                val_11.set(row)
            elif i==13:
                val_12.set(row)
            elif i==14:
                val_13.set(row)
            elif i==15:
                val_14.set(row)
            elif i==16:
                val_15.set(row)
            elif i==17:
                val_16.set(row)
            elif i==18:
                val_17.set(row)
            elif i==19:
                val_18.set(row)
            elif i==20:
                val_19.set(row)
            elif i==21:
                val_20.set(row)
            elif i==22:
                val_21.set(row)
            elif i==23:
                val_22.set(row)
            elif i==24:
                val_23.set(row)
            elif i==25:
                val_24.set(row)
            elif i==26:
                val_25.set(row)
            elif i==27:
                val_26.set(row)
            elif i==28:
                val_27.set(row)
            elif i==29:
                val_28.set(row)
            elif i==30:
                val_29.set(row)
            elif i==31:
                val_30.set(row)
            elif i==32:
                val_31.set(row)
            j = 0
            regdatas.append(0x0F0F)
            datas.append(0x0F)
            datas.append(0x0F)
            for cln in row:
                if (j==0)or(j==1):
                    ttt = int(cln)
                    regdatas.append(ttt)
                    datas.append((ttt>>8)&0xFF)
                    datas.append(ttt&0xFF)
                else:
                    res1 = struct.pack('f',float(cln))
                    regdatas.append(res1[3]*256+res1[2])
                    regdatas.append(res1[1]*256+res1[0])
                    datas.append(res1[3])
                    datas.append(res1[2])
                    datas.append(res1[1])
                    datas.append(res1[0])
                j = j+1
        i = i+1

    print(datas)
    print(len(datas))
    return datas

def read_datas(ser1,val_ser,val_des,val_ad,val_cmd,chk_en):
    itemp = 0
    rsens = []
    crc = crc16()
    try:
        addr = int(val_ad.get(),16)
    except ValueError:
        addr = 0x58
    cmd = int(val_cmd.get(),16)

    regstart = 0x0000
    regnum = 0x0054
    regstarth = (regstart>>8) & 0xFF
    regstartl = regstart & 0xFF
    regnumh = (regnum>>8) & 0xFF
    regnuml = regnum & 0xFF
    for j in range(0,8):
        regstart = j*84
        regstarth = (regstart>>8) & 0xFF
        regstartl = regstart & 0xFF
        regnumh = (regnum>>8) & 0xFF
        regnuml = regnum & 0xFF

        myinputL = []
        myinputL.append(addr)
        myinputL.append(cmd)
        myinputL.append(regstarth)
        myinputL.append(regstartl)
        myinputL.append(regnumh)
        myinputL.append(regnuml)
        myinputL = crc.createarray(myinputL)
        myinput = bytes(myinputL)

        ser1.write(myinput)
        time.sleep(0.03)
        ser1.flush()
        time.sleep(0.03)
        count = ser1.inWaiting()
        data = ser1.read(count)

        if crc.calcrc(data):
            flag = 1
            for i in range(0,4):
                #VOC datas ieee754 float
                voc = [data[i*len1ch_byte+6],data[i*len1ch_byte+5],data[i*len1ch_byte+4],data[i*len1ch_byte+3]]
                tmp = struct.unpack('f',bytes(voc))
                tmp = '%.2f'%tmp
                rsens.append(tmp)
                #Temp datas ieee754 float
                temp = [data[i*len1ch_byte+10],data[i*len1ch_byte+9],data[i*len1ch_byte+8],data[i*len1ch_byte+7]]
                tmp = struct.unpack('f',bytes(temp))
                tmp = '%.2f'%tmp
                rsens.append(tmp)
                #Humi datas ieee754 float
                humi = [data[i*len1ch_byte+14],data[i*len1ch_byte+13],data[i*len1ch_byte+12],data[i*len1ch_byte+11]]
                tmp = struct.unpack('f',bytes(humi))
                tmp = '%.2f'%tmp
                rsens.append(tmp)
                #Rs real time(kOhm)
                rsens.append(str(data[i*len1ch_byte+15]*256+data[i*len1ch_byte+16]))
                #Rstd(kOhm)
                rsens.append( str(data[i*len1ch_byte+17]*256+data[i*len1ch_byte+18]))
                #RL(kOhm)
                rsens.append( str(data[i*len1ch_byte+19]*256+data[i*len1ch_byte+20]))
                #sensity cofficient s1x^s0
                s1 = [data[i*len1ch_byte+24],data[i*len1ch_byte+23],data[i*len1ch_byte+22],data[i*len1ch_byte+21]]
                tmp = struct.unpack('f',bytes(s1))
                tmp = '%.2f'%tmp
                rsens.append(tmp)
                #sensity cofficient s1x^s0
                s0 = [data[i*len1ch_byte+28],data[i*len1ch_byte+27],data[i*len1ch_byte+26],data[i*len1ch_byte+25]]
                tmp = struct.unpack('f',bytes(s0))
                tmp = '%.2f'%tmp
                rsens.append(tmp)
                #Temperature cofficient tc1*t+t0
                tc1 = [data[i*len1ch_byte+32],data[i*len1ch_byte+31],data[i*len1ch_byte+30],data[i*len1ch_byte+29]]
                tmp = struct.unpack('f',bytes(tc1))
                tmp = '%.2f'%tmp
                rsens.append(tmp)
                #Temperature cofficient tc1*t+t0
                tc0 = [data[i*len1ch_byte+36],data[i*len1ch_byte+35],data[i*len1ch_byte+34],data[i*len1ch_byte+33]]
                tmp = struct.unpack('f',bytes(tc0))
                tmp = '%.2f'%tmp
                rsens.append(tmp)
                #humidity cofficient hc1*t+h0
                hc1 = [data[i*len1ch_byte+40],data[i*len1ch_byte+39],data[i*len1ch_byte+38],data[i*len1ch_byte+37]]
                tmp = struct.unpack('f',bytes(hc1))
                tmp = '%.2f'%tmp
                rsens.append(tmp)
                #humidity cofficient hc1*t+h0
                hc0 = [data[i*len1ch_byte+44],data[i*len1ch_byte+43],data[i*len1ch_byte+42],data[i*len1ch_byte+41]]
                tmp = struct.unpack('f',bytes(hc0))
                tmp = '%.2f'%tmp
                rsens.append(tmp)

            val_ser.set('%d Bytes Received'%data[2])
        else:
            flag = 0

    if(chk_en.get()==1)and(flag==1):
        filename = val_des.get()
        if filename=='':
            filename = 'dout'
        filename = filename + '.csv'
        #csvFile = open('dout.csv','a')
        try:
            csvFile = open(filename,'a')
        except FileNotFoundError:
            csvFile = open(filename,'w')
        writer = csv.writer(csvFile)
        writer.writerow(['VOC','Temp','Humi','Rsr','Rstd','RL','S1','S0','TC1','TC0','HC1','HC0'])
        for k in range(0,32):
            writer.writerow(rsens[12*k:12*(k+1)])

        mytime = time.strftime('%Y-%m-%d-%H:%M:%S',\
                time.localtime(time.time()))
        fp=open('data.txt','a+')
        fp.write(mytime+'\n')
        for i in range(0,len1ch):
            #fp.write('%.4f\t'%rsens[i])
            fp.write(rsens[i])
        fp.write('\nEnd of Sample\n\n')
        fp.close()
    return rsens

