#!C:\Users\wanglw\AppData\Local\Programs\Python\Python36\python.exe
#coding=utf-8
import serial,time,csv
import tkinter as tk
import tkinter.font as tkFont
import struct

from cal_datas import write_datas, get_datas, read_datas
from crc16_mb import crc16

#vref = 3.3
#FS = 4095
#RL = 200e3
class App(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        
        chk_en = tk.IntVar()
        val_ad = tk.StringVar()
        val_cmd = tk.StringVar()
        val_op1 = tk.StringVar()
        val_op2 = tk.StringVar()

        val_0 = tk.StringVar()
        val_1 = tk.StringVar()
        val_2 = tk.StringVar()
        val_3 = tk.StringVar()
        val_4 = tk.StringVar()
        val_5 = tk.StringVar()
        val_6 = tk.StringVar()
        val_7 = tk.StringVar()
        val_8 = tk.StringVar()

        val_9 = tk.StringVar()
        val_10 = tk.StringVar()
        val_11 = tk.StringVar()
        val_12 = tk.StringVar()
        val_13 = tk.StringVar()
        val_14 = tk.StringVar()
        val_15 = tk.StringVar()
        val_16 = tk.StringVar()

        val_17 = tk.StringVar()
        val_18 = tk.StringVar()
        val_19 = tk.StringVar()
        val_20 = tk.StringVar()
        val_21 = tk.StringVar()
        val_22 = tk.StringVar()
        val_23 = tk.StringVar()
        val_24 = tk.StringVar()

        val_25 = tk.StringVar()
        val_26 = tk.StringVar()
        val_27 = tk.StringVar()
        val_28 = tk.StringVar()
        val_29 = tk.StringVar()
        val_30 = tk.StringVar()
        val_31 = tk.StringVar()

        vpc = tk.StringVar()
        vp = tk.StringVar()

        val_ser = tk.StringVar()
        val_src = tk.StringVar()
        val_des = tk.StringVar()
        v1 = tk.StringVar()
        v2 = tk.StringVar()
        v3 = tk.StringVar()
        def openMyPort(v1,v2,v3):
            sport = v1.get();
            sportn = int(v2.get())
            try:
                self.ser1 = serial.Serial(sport,sportn)
                v3.set('Open'+' '+sport+' '+'Sucess')
                #print('Open {} Sucess!'.format(sport))
                #print(self.ser1)
            except serial.serialutil.SerialException:
                v3.set('Cannot open'+' '+sport)
                #print('Cannot open {}'.format(sport))

        def closeMyPort(v3):
            try:
                self.ser1.close()
                sport = v1.get()
                v3.set(sport+' '+'Closed')
            except:
                v3.set('Port Not Open')

        def sampleDatas(chk_en,\
                val_0,val_1,val_2,vsl_3,val_4,val_5,val_6,val_7,val_8,\
		    val_9,val_10,val_11,val_12,val_13,val_14,val_15,val_16,\
		    val_17,val_18,val_19,val_20,val_21,val_22,val_23,val_24,\
		    val_25,val_26,val_27,val_28,val_29,val_30,val_31,\
                       val_ad,val_cmd,val_ser):

            rsens = read_datas(self.ser1,val_ser,val_des,val_ad,val_cmd,chk_en)
            if len(rsens)==384:
                val_0.set(rsens[0:12])
                val_1.set(rsens[12:24])
                val_2.set(rsens[24:36])
                val_3.set(rsens[36:48])
                val_4.set(rsens[48:60])
                val_5.set(rsens[60:72])
                val_6.set(rsens[72:84])
                val_7.set(rsens[84:96])
                val_8.set(rsens[96:108])
                val_9.set(rsens[108:120])
                val_10.set(rsens[120:132])
                val_11.set(rsens[132:144])
                val_12.set(rsens[144:156])
                val_13.set(rsens[156:168])
                val_14.set(rsens[168:180])
                val_15.set(rsens[180:192])

                val_16.set(rsens[192:204])
                val_17.set(rsens[204:216])
                val_18.set(rsens[216:228])
                val_19.set(rsens[228:240])
                val_20.set(rsens[240:252])
                val_21.set(rsens[252:264])
                val_22.set(rsens[264:276])
                val_23.set(rsens[276:288])
                val_24.set(rsens[288:300])
                val_25.set(rsens[300:312])
                val_26.set(rsens[312:324])
                val_27.set(rsens[324:336])
                val_28.set(rsens[336:348])
                val_29.set(rsens[348:360])
                val_30.set(rsens[360:372])
                val_31.set(rsens[372:384])

        helv24 = tkFont.Font(family='Helvetica',size=18,weight='bold')
        helv16 = tkFont.Font(family='Helvetica',size=16,weight='bold')
        #self.addrLabel = tk.Label(self,fg='#00f',bg='#0f0',width=64,font=helv16,\
        #        text='32 CH Datas Monitor System')
        #self.addrLabel.grid(row=0,column=0,columnspan=64)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='MBAddr:')
        self.addrLabel.grid(row=1,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_ad,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=1,column=8,columnspan=32)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CMD:')
        self.addrLabel.grid(row=1,column=40,columnspan=8)
        #self.addrEntry = tk.Entry(self,textvariable=val_cmd,bg='white',fg='red',width=8,font=helv24)
        #self.addrEntry.grid(row=1,column=24,columnspan=8)
        optionListcmd = ('03','04','10')
        val_cmd.set(optionListcmd[1])
        self.addroption = tk.OptionMenu(self,val_cmd,*optionListcmd)
        self.addroption.grid(row=1,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='PORT:')
        self.addrLabel.grid(row=2,column=0,columnspan=8)

        optionListc =('COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10','COM11',\
                'COM12','COM13','COM14','COM15','COM16','COM17','COM18','COM19','COM20','COM21','COM22')
        vpc.set(optionListc[2])
        self.addoption = tk.OptionMenu(self,vpc,*optionListc)
        self.addoption.grid(row=2,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='BautRate:')
        self.addrLabel.grid(row=2,column=40,columnspan=8)
        #self.OptionMenu(row=1,column=56,columnspan=8)

        optionList = ('4800','9600','19200','38400','57600','115200','230400')
        vp.set(optionList[6])
        self.addoption = tk.OptionMenu(self,vp,*optionList)
        self.addoption.grid(row=2,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH0:')
        self.addrLabel.grid(row=10,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_0,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=10,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH16:')
        self.addrLabel.grid(row=10,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_16,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=10,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH1:')
        self.addrLabel.grid(row=11,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_1,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=11,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH17:')
        self.addrLabel.grid(row=11,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_17,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=11,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH2:')
        self.addrLabel.grid(row=12,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_2,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=12,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH18:')
        self.addrLabel.grid(row=12,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_18,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=12,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH3:')
        self.addrLabel.grid(row=13,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_3,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=13,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH19:')
        self.addrLabel.grid(row=13,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_19,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=13,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH4:')
        self.addrLabel.grid(row=14,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_4,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=14,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH20:')
        self.addrLabel.grid(row=14,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_20,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=14,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH5:')
        self.addrLabel.grid(row=15,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_5,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=15,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH21:')
        self.addrLabel.grid(row=15,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_21,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=15,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH6:')
        self.addrLabel.grid(row=16,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_6,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=16,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH22:')
        self.addrLabel.grid(row=16,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_22,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=16,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH7:')
        self.addrLabel.grid(row=17,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_7,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=17,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH23:')
        self.addrLabel.grid(row=17,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_23,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=17,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH8:')
        self.addrLabel.grid(row=18,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_8,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=18,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH24:')
        self.addrLabel.grid(row=18,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_24,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=18,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH9:')
        self.addrLabel.grid(row=19,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_9,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=19,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH25:')
        self.addrLabel.grid(row=19,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_25,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=19,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH10:')
        self.addrLabel.grid(row=20,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_10,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=20,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH26:')
        self.addrLabel.grid(row=20,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_26,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=20,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH11:')
        self.addrLabel.grid(row=21,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_11,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=21,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH27:')
        self.addrLabel.grid(row=21,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_27,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=21,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH12:')
        self.addrLabel.grid(row=22,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_12,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=22,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH28:')
        self.addrLabel.grid(row=22,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_28,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=22,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH13:')
        self.addrLabel.grid(row=23,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_13,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=23,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH29:')
        self.addrLabel.grid(row=23,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_29,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=23,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH14:')
        self.addrLabel.grid(row=24,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_14,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=24,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH30:')
        self.addrLabel.grid(row=24,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_30,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=24,column=48,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH15:')
        self.addrLabel.grid(row=25,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_15,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=25,column=8,columnspan=32)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH31:')
        self.addrLabel.grid(row=25,column=40,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_31,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=25,column=48,columnspan=32)

        self.genButton = tk.Button(self,text='Read',font=helv24,width=8,command=lambda :\
                sampleDatas(chk_en,val_0,val_1,val_2,val_3,val_4,val_5,val_6,val_7,val_8,\
		        val_9,val_10,val_11,val_12,val_13,val_14,val_15,val_16,\
		        val_17,val_18,val_19,val_20,val_21,val_22,val_23,val_24,\
		        val_25,val_26,val_27,val_28,val_29,val_30,val_31,\
                val_ad,val_cmd,val_ser))
        self.genButton.grid(row=62,column=0)

        self.addcheck = tk.Checkbutton(self,onvalue=1,offvalue=0,text='WrToFile',variable=chk_en)
        self.addcheck.grid(row=62,column=8,columnspan=8)

        self.addrEntry = tk.Entry(self,textvariable=val_des,bg='white',fg='red',width=20,font=helv24)
        self.addrEntry.grid(row=62,column=16)

        self.genButton = tk.Button(self,text='OpenPort',font=helv24,width=8,command=lambda \
                                   :openMyPort(vpc,vp,val_ser))
        self.genButton.grid(row=62,column=40)
        self.addrEntry = tk.Entry(self,textvariable=val_ser,bg='white',fg='red',width=32,font=helv24)
        self.addrEntry.grid(row=62,column=48,columnspan=24)

        self.genButton = tk.Button(self,text='Write',font=helv24,width=8,command=lambda \
                                   :write_datas(self.ser1,val_ad))
        self.genButton.grid(row=63,column=0)
        self.genButton = tk.Button(self,text='GetDatas',font=helv24,width=8,command=lambda \
                                   :get_datas(val_src,val_0,val_1,val_2,val_3,val_4,val_5,val_6,\
                                   val_7,val_8,val_9,val_10,val_11,val_12,val_13,val_14,val_15,\
                                   val_16,val_17,val_18,val_19,val_20,val_21,val_22,val_23,val_24,\
                                   val_25,val_26,val_27,val_28,val_29,val_30,val_31))
        self.genButton.grid(row=63,column=8)
        self.addrEntry = tk.Entry(self,textvariable=val_src,bg='white',fg='red',width=20,font=helv24)
        self.addrEntry.grid(row=63,column=16)
        self.genButton = tk.Button(self,text='ClosePort',font=helv24,width=8,command=lambda \
                                   :closeMyPort(val_ser))
        self.genButton.grid(row=63,column=40)

app1 = App()
app1.master.title('GasModuleCalibration-20190126')
app1.mainloop()

