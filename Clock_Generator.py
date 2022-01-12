import numpy as np
import scipy.signal as signal
import control
import matplotlib.pyplot as plt
import math as m
from PySide2.QtWidgets import QApplication, QWidget, QDesktopWidget , QVBoxLayout, QPushButton , QGroupBox, QGridLayout, QLineEdit,QMessageBox,QLabel
import sys
from PySide2.QtGui import QIcon, QFont, QIntValidator, QValidator, QDoubleValidator
from scipy import integrate
class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plotting Functions")
        self.setGeometry(400,400,800,550)
        self.setMinimumHeight(200)
        self.setMinimumWidth(200)
        self.setMaximumHeight(600)
        self.setMaximumWidth(800)
        self.i_pump_line_edit = QLineEdit()
        self.i_pump_line_edit.setPlaceholderText('Please Enter I_Pump Value')
        self.ko_line_edit = QLineEdit()
        self.ko_line_edit.setPlaceholderText('Please Enter Ko value')
        self.c1_line_edit = QLineEdit()
        self.c1_line_edit.setPlaceholderText('PLease Enter C1 Value')
        self.c2_line_edit = QLineEdit()
        self.c2_line_edit.setPlaceholderText('Please Enter C2 Value')
        self.R1_line_edit = QLineEdit()
        self.R1_line_edit.setPlaceholderText('Please Enter R1 Value')
        self.N_line_edit = QLineEdit()
        self.N_line_edit.setPlaceholderText('Please Enter N Value ')
        self.C3_line_edit=QLineEdit()
        self.C3_line_edit.setPlaceholderText('Please Enter C3 Value')
        self.R3_line_edit=QLineEdit()
        self.R3_line_edit.setPlaceholderText('Please Enter R3 Value')
        self.R_line_edit=QLineEdit()
        self.R_line_edit.setPlaceholderText('Please Enter Reference Divider Value')
        self.p_line_edit=QLineEdit()
        self.p_line_edit.setPlaceholderText('Please Enter Output Divider Value')
        self.fref_line_edit=QLineEdit()
        self.fref_line_edit.setPlaceholderText('Enter 50 MHz or 51.5625 MHz')
        self.icon()
        self.centering_window()
        self.layout()
        vbox=QVBoxLayout()
        vbox.addWidget(self.group_message)
        self.setLayout(vbox)
    def icon(self):
        window_icon=QIcon("icon.png")  # object for QICon
        self.setWindowIcon(window_icon)  # Passing the QICon object to setWindowIcon to display it when running the code
    def centering_window(self):
        center=self.frameGeometry()
        center_point=QDesktopWidget().availableGeometry().center()
        center.moveCenter(center_point)
        self.move(center.topLeft())
    def layout(self):
        self.group_message= QGroupBox("Please fill the following spaces")  # Object for GroupBox
        self.group_message.setFont(QFont("Decorative", 14))
        grid_layout=QGridLayout()  #object for QGrid Layout
        label_10 = QLabel('Fref')
        grid_layout.addWidget(label_10, 0, 0)
        grid_layout.addWidget(self.fref_line_edit, 0, 1)
        Label_1=QLabel('I_Pump')
        #Label_1.setStyleSheet('font: 16pt')
        #Label_1.setStyleSheet('background-color:#FED102')
        #grid_layout.addWidget(button1,0,0)  # Button1 is a widget which will be put in the 0 row and 0 column
        grid_layout.addWidget(Label_1,1,0)
        grid_layout.addWidget(self.i_pump_line_edit,1,1)
        Label_2=QLabel('Ko')
        grid_layout.addWidget(Label_2,2,0)
        grid_layout.addWidget(self.ko_line_edit, 2, 1)
        Label_3=QLabel('C1')
        grid_layout.addWidget(Label_3,3,0)
        grid_layout.addWidget(self.c1_line_edit,3,1)
        Label_4=QLabel('C2')
        grid_layout.addWidget(Label_4, 4, 0)
        grid_layout.addWidget(self.c2_line_edit, 4, 1)
        Label_5=QLabel('R1')
        grid_layout.addWidget(Label_5, 5, 0)
        grid_layout.addWidget(self.R1_line_edit, 5, 1)
        Label_6=QLabel('N')
        grid_layout.addWidget(Label_6, 6, 0)
        grid_layout.addWidget(self.N_line_edit, 6, 1)
        Label_7 = QLabel('C3')
        grid_layout.addWidget(Label_7, 7, 0)
        grid_layout.addWidget(self.C3_line_edit, 7, 1)
        Label_8 = QLabel('R3')
        grid_layout.addWidget(Label_8, 8, 0)
        grid_layout.addWidget(self.R3_line_edit, 8, 1)
        Label_9 = QLabel('Reference Divider')
        grid_layout.addWidget(Label_9, 9, 0)
        grid_layout.addWidget(self.R_line_edit, 9, 1)
        label = QLabel('Output_Divider')
        grid_layout.addWidget(label, 10, 0)
        grid_layout.addWidget(self.p_line_edit, 10, 1)
        button7 = QPushButton("Setting Values", self)
        button7.clicked.connect(self.setting_values)
        grid_layout.addWidget(button7,11,1)
        button7.setStyleSheet('background-color: #4267B2 ')
        button8 = QPushButton("Plot Open_Loop TF", self)
        button8.clicked.connect(self.Plotting_Open_Loop_TF)
        button8.setStyleSheet('background-color: yellow')
        grid_layout.addWidget(button8,12,0)
        button9 = QPushButton("Plot Closed_Loop TF", self)
        button9.clicked.connect(self.Plotting_Closed_Loop_TF)
        button9.setStyleSheet('background-color: #00bbee')
        grid_layout.addWidget(button9, 12 ,1)
        button10 = QPushButton("VCO Phase Noise TF", self)
        button10.clicked.connect(self.VCO_PhaseNoise_TF)
        #button10.setStyleSheet('background-color: #0be110')
        button10.setStyleSheet('background-color: yellow')
        #grid_layout.addWidget(button10, 7, 2)
        grid_layout.addWidget(button10, 13 , 0)
        button11 = QPushButton("Charge Pump Phase Noise TF", self)
        button11.clicked.connect(self.Charge_Pump_PhaseNoise_TF)
        #button11.setStyleSheet('background-color: #bb00ee')
        button11.setStyleSheet('background-color:#00bbee')
        #grid_layout.addWidget(button11, 8, 0)
        grid_layout.addWidget(button11, 13, 1)
        button12 = QPushButton("Loop Filter Phase Noise TF", self)
        button12.clicked.connect(self.LF_PhaseNoise_TF)
        #button12.setStyleSheet('background-color: #ffa500')
        button12.setStyleSheet('background-color: yellow')
        #grid_layout.addWidget(button12, 8, 1)
        grid_layout.addWidget(button12, 14, 0)
        button13 = QPushButton("Divider Phase Noise TF", self)
        button13.clicked.connect(self.Divider_PhaseNoisse_TF)
        #button13.setStyleSheet('background-color: #0080ff')
        button13.setStyleSheet('background-color:#00bbee')
        #grid_layout.addWidget(button13, 8, 2)
        grid_layout.addWidget(button13, 14, 1)
        button14=QPushButton('Plot Fourth Order OpenLoop TF',self)
        button14.clicked.connect(self.Plotting_Fourth_Order_Open_Loop_TF)
        grid_layout.addWidget(button14,15,0)
        button14.setStyleSheet('background-color: yellow')
        button15=QPushButton('Plot Fourth Order ClosedLoop TF',self)
        button15.clicked.connect(self.Plotting_Fourth_Order_Closed_Loop_TF)
        grid_layout.addWidget(button15,15,1)
        button15.setStyleSheet('background-color: #00bbee')
        button16 = QPushButton('Plot Fourth Order VCO Phase Noise TF', self)
        button16.clicked.connect(self.Plotting_Fourth_Order_VCO_Phase_Noise_TF)
        grid_layout.addWidget(button16, 16, 0)
        button16.setStyleSheet('background-color: yellow')
        button17=QPushButton('Plot Fourth Order Charge Pump Phase Noise TF',self)
        button17.clicked.connect(self.Plotting_Fourth_Order_Charge_Pump_Phase_Noise_TF)
        grid_layout.addWidget(button17,16,1)
        button17.setStyleSheet('background-color: #00bbee')
        button18=QPushButton('Plot Fourth Order LF Phase Noise TF',self)
        button18.clicked.connect(self.Plotting_Fourth_Order_LF_Phase_Noise_TF)
        grid_layout.addWidget(button18,17,0)
        button18.setStyleSheet('background-color: yellow')
        button19=QPushButton('Plot Fourth Order Divider PhaseNoise TF')
        button19.clicked.connect(self.Plotting_Fourth_Order_Divider_PhaseNoise_TF)
        grid_layout.addWidget(button19,17,1)
        button19.setStyleSheet('background-color: #00bbee')
        button20=QPushButton('Plot Output PhaseNoise Due TO VCO Phase Noise',self)
        button20.clicked.connect(self.Output_Phase_Noise_Due_To_VCO_Phase_Noise)
        #button20.clicked.connect(self.VCO_Noise)
        grid_layout.addWidget(button20,18,0)
        button20.setStyleSheet('background-color: yellow')
        button21=QPushButton('Plot Output PhaseNoise due to ChargePump Phase Noise',self)
        button21.clicked.connect(self.Output_Phase_Noise_Due_To_Charge_Pump_Phase_Noise)
        #button21.clicked.connect(self.Output_Charge_Pump_Phase_Noise)
        #button21.clicked.connect(self.Charge_Pump_Noise)
        grid_layout.addWidget(button21,18,1)
        button21.setStyleSheet('background-color: #00bbee')
        button22=QPushButton('Plot Output Phase Noise Due to Divider Phase Noise')
        button22.clicked.connect(self.Output_phase_Noise_Due_To_Feedback_Divider)
        #button22.clicked.connect(self.Output_Divider_Phase_Noise)
        button22.setStyleSheet('background-color: yellow')
        grid_layout.addWidget(button22,19,0)
        button23=QPushButton('Plot Output Phase Noise Due To Reference Noise')
        button23.clicked.connect(self.Output_Phase_Noise_Due_To_reference_Noise)
        #button23.clicked.connect(self.Reference_Noise)
        grid_layout.addWidget(button23,19,1)
        button23.setStyleSheet('background-color:#00bbee')
        button24=QPushButton('Plot Output_Phase_Noise_Due_To_MUX_Noise')
        button24.clicked.connect(self.Output_Phase_Noise_Due_To_MUX_Noise)
        #button24.clicked.connect(self.Reference_Divider_Phase_Noise)
        button24.setStyleSheet('background-color: yellow')
        grid_layout.addWidget(button24,20,0)
        button25=QPushButton('Plot Output Noise Due To LF Phase Noise')
        button25.clicked.connect(self.Output_Phase_Noise_Due_To_Loop_Filter_Phase_Noise)
        #button25.clicked.connect(self.Loop_Filter_Phase_Noise5)
        grid_layout.addWidget(button25,20,1)
        button25.setStyleSheet('background-color:#00bbee')
        button26=QPushButton('Plot Total Phase Noise')
        button26.clicked.connect(self.Total_Output_Phase_Noise)
        button26.setStyleSheet('background-color: yellow')
        grid_layout.addWidget(button26,21,0)
        button27=QPushButton('Plot Fourth Order Total Phase Noise')
        button27.clicked.connect(self.Total_Output_Phase_Noise_Fourth_Order)
        #button27.clicked.connect(self.Total_Phase_Noise_Fourth_Order)
        button27.setStyleSheet('background-color:#00bbee')
        grid_layout.addWidget(button27,21,1)
        #button23.clicked.connect(self.Output_Phase_Noise_Due_To_VCO_Phase_Noise)
        #button23.clicked.connect(self.VCO_Noise)
        self.group_message.setLayout(grid_layout)
    def setting_values(self):
        IPump = float(self.i_pump_line_edit.text())
        Ko = float(self.ko_line_edit.text())
        C1 = float(self.c1_line_edit.text())
        C2 = float(self.c2_line_edit.text())
        C3=float(self.C3_line_edit.text())
        R1 =float(self.R1_line_edit.text())
        R3=float(self.R3_line_edit.text())
        N = float(self.N_line_edit.text())
        R = float(self.R_line_edit.text())
        p= float(self.p_line_edit.text())
        fref=float(self.fref_line_edit.text())
    def I_Pump_Value(self):
        return float(self.i_pump_line_edit.text())
    def Ko_Value(self):
        return float(self.ko_line_edit.text())
    def C1_Value(self):
        return float(self.c1_line_edit.text())
    def C2_Value(self):
        return float(self.c2_line_edit.text())
    def C3_Value(self):
        return float(self.C3_line_edit.text())
    def R1_Value(self):
        return float(self.R1_line_edit.text())
    def R3_Value(self):
        return float(self.R3_line_edit.text())
    def N_Value(self):
        return float(self.N_line_edit.text())
    def Reference_Divider_Value(self):
        return float(self.R_line_edit.text())
    def Output_Divider_Value(self):
        return float(self.p_line_edit.text())
    def reference_frequency_value(self):
        return float(self.fref_line_edit.text())
    def frequency_axis(self):
        return range(1000,100000000,1000)
    def Calculating_K(self):
        return (GUI.I_Pump_Value() * GUI.Ko_Value()) / GUI.N_Value()
    def Calculating_Taw1(self):
        return GUI.C1_Value()*GUI.R1_Value()
    def Calculating_Taw2(self):
        return GUI.R1_Value()*GUI.C1_Value()*(GUI.C2_Value()/(GUI.C1_Value() +GUI.C2_Value()))
    def Calculating_Taw3(self):
        return GUI.R3_Value()*GUI.C3_Value()
    def Fout(self):
        global fout
        first_term=GUI.N_Value()
        second_term=GUI.Reference_Divider_Value()
        third_term=GUI.Output_Divider_Value()
        fout=((first_term*GUI.reference_frequency_value())/(second_term*third_term))
        return fout
    def Open_Loop_TF(self):
        num=np.array([GUI.R1_Value()*GUI.C1_Value()*GUI.Calculating_K(),GUI.Calculating_K()])
        den=np.array([GUI.Calculating_Taw2()*(GUI.C1_Value()+GUI.C2_Value()),(GUI.C1_Value()+GUI.C2_Value()),0,0])
        return control.tf(num,den)
    def Fourth_Order_Open_Loop_TF(self):
        num_6=np.array([GUI.Calculating_Taw1()*GUI.Calculating_K(),GUI.Calculating_K()])
        den_6=np.array([GUI.Calculating_Taw2()*GUI.Calculating_Taw3()*(GUI.C1_Value()+GUI.C2_Value()),((GUI.C3_Value()*(GUI.Calculating_Taw1())+(GUI.C1_Value()+GUI.C2_Value())*(GUI.Calculating_Taw2()+GUI.Calculating_Taw3()))),(GUI.C1_Value()+GUI.C2_Value()+GUI.C3_Value()),0,0])
        return control.tf(num_6,den_6)
    def Loop_Filter(self):
        num_7=np.array([GUI.Calculating_Taw1()*GUI.Calculating_Taw3(),(GUI.Calculating_Taw1()+GUI.Calculating_Taw3()),1])
        den_7=np.array([(GUI.C1_Value()+GUI.C2_Value())*GUI.Calculating_Taw2()*GUI.Calculating_Taw3(),(GUI.C3_Value()*GUI.Calculating_Taw1()+GUI.C1_Value()*GUI.Calculating_Taw3()+GUI.C2_Value()*GUI.Calculating_Taw3()+GUI.C1_Value()*GUI.Calculating_Taw2()+GUI.C2_Value()*GUI.Calculating_Taw2()),(GUI.C1_Value()+GUI.C2_Value())+GUI.C3_Value()*GUI.Calculating_Taw1(),0])
        return control.tf(num_7,den_7)
    def Closed_Loop_TF(self):
        num_1=np.array([GUI.N_Value()*GUI.Calculating_K()*GUI.Calculating_Taw1(),GUI.N_Value()*GUI.Calculating_K()])
        den_1=np.array([(GUI.C1_Value()+GUI.C2_Value())*GUI.Calculating_Taw2(),(GUI.C1_Value()+GUI.C2_Value()),GUI.Calculating_K()*GUI.Calculating_Taw1(),GUI.Calculating_K()])
        return control.tf(num_1,den_1)
    def Fourth_Order_Closed_Loop_TF(self):
        num_8=np.array([GUI.N_Value()*GUI.Calculating_K()*GUI.Calculating_Taw1(),GUI.N_Value()*GUI.Calculating_K()])
        den_8=np.array([GUI.Calculating_Taw2()*GUI.Calculating_Taw3()*(GUI.C1_Value()+GUI.C2_Value()),((GUI.C3_Value()*(GUI.Calculating_Taw1())+(GUI.C1_Value()+GUI.C2_Value())*(GUI.Calculating_Taw2()+GUI.Calculating_Taw3()))),(GUI.C1_Value()+GUI.C2_Value()+GUI.C3_Value()),GUI.Calculating_K()*GUI.Calculating_Taw1(),GUI.Calculating_K()])
        return control.tf(num_8,den_8)
    def VCO_Phase_Noise(self):
        num_2=np.array([(GUI.C1_Value()+GUI.C2_Value())*GUI.Calculating_Taw2(),(GUI.C1_Value()+GUI.C2_Value()),0,0])
        den_2=np.array([(GUI.C1_Value()+GUI.C2_Value())*GUI.Calculating_Taw2(),(GUI.C1_Value()+GUI.C2_Value()),GUI.Calculating_K()*GUI.Calculating_Taw1(),GUI.Calculating_K()])
        return control.tf(num_2,den_2)
    def Fourth_Order_VCO_Phase_Noise_TF(self):
        num_9=np.array([GUI.Calculating_Taw2()*GUI.Calculating_Taw3()*(GUI.C1_Value()+GUI.C2_Value()),((GUI.C3_Value()*(GUI.Calculating_Taw1())+(GUI.C1_Value()+GUI.C2_Value())*(GUI.Calculating_Taw2()+GUI.Calculating_Taw3()))),(GUI.C1_Value()+GUI.C2_Value()+GUI.C3_Value()),0,0])
        den_9=np.array([GUI.Calculating_Taw2()*GUI.Calculating_Taw3()*(GUI.C1_Value()+GUI.C2_Value()),((GUI.C3_Value()*(GUI.Calculating_Taw1())+(GUI.C1_Value()+GUI.C2_Value())*(GUI.Calculating_Taw2()+GUI.Calculating_Taw3()))),(GUI.C1_Value()+GUI.C2_Value()+GUI.C3_Value()),GUI.Calculating_K()*GUI.Calculating_Taw1(),GUI.Calculating_K()])
        return control.tf(num_9,den_9)
    def Charge_Pump_Phase_Noise(self):
        num_3 = np.array([GUI.N_Value()*GUI.Calculating_K()*GUI.Calculating_Taw1() * 2 * m.pi,GUI.N_Value() * GUI.Calculating_K() * 2 * m.pi])
        den_3 = np.array([(GUI.C1_Value()+GUI.C2_Value())*GUI.Calculating_Taw2() * GUI.I_Pump_Value(),(GUI.C1_Value()+GUI.C2_Value())* GUI.I_Pump_Value(),GUI.Calculating_K()*GUI.Calculating_Taw1() * GUI.I_Pump_Value(), GUI.Calculating_K() * GUI.I_Pump_Value()])
        return control.tf(num_3,den_3)
    def Fourth_Order_Charge_Pump_Phase_Noise(self):
        num_11=np.array([GUI.N_Value()*GUI.Calculating_K()*GUI.Calculating_Taw1()*m.pi*2,GUI.N_Value()*GUI.Calculating_K()*2*m.pi])
        den_11=np.array([GUI.I_Pump_Value()*GUI.Calculating_Taw2()*GUI.Calculating_Taw3()*(GUI.C1_Value()+GUI.C2_Value()),((GUI.C3_Value()*(GUI.Calculating_Taw1())+(GUI.C1_Value()+GUI.C2_Value())*(GUI.Calculating_Taw2()+GUI.Calculating_Taw3())))*GUI.I_Pump_Value(),(GUI.C1_Value()+GUI.C2_Value()+GUI.C3_Value())*GUI.I_Pump_Value(),GUI.Calculating_K()*GUI.Calculating_Taw1()*GUI.I_Pump_Value(),GUI.Calculating_K()*GUI.I_Pump_Value()])
        return control.tf(num_11,den_11)
    def Loop_Filter_Phase_Noise(self):
        num_4 = np.array([(GUI.C1_Value() + GUI.C2_Value()) * GUI.Calculating_Taw2() * (GUI.Ko_Value() * 2 * m.pi),(GUI.C1_Value() + GUI.C2_Value()) * (GUI.Ko_Value() * 2 * m.pi), 0])
        den_4 = np.array([(GUI.C1_Value() + GUI.C2_Value()) * GUI.Calculating_Taw2(), (GUI.C1_Value() + GUI.C2_Value()),GUI.Calculating_K() * GUI.Calculating_Taw1(), GUI.Calculating_K()])
        return control.tf(num_4,den_4)
    def Fourth_Order_Loop_Filter_Phase_Noise_TF(self):
        num_12=np.array([GUI.Ko_Value()*2*m.pi*GUI.Calculating_Taw2()*GUI.Calculating_Taw3()*(GUI.C1_Value()+GUI.C2_Value()),((GUI.C3_Value()*(GUI.Calculating_Taw1())+(GUI.C1_Value()+GUI.C2_Value())*(GUI.Calculating_Taw2()+GUI.Calculating_Taw3())))*GUI.Ko_Value()*2*m.pi,(GUI.C1_Value()+GUI.C2_Value()+GUI.C3_Value())*GUI.Ko_Value()*2*m.pi,0])
        den_12=np.array([GUI.Calculating_Taw2()*GUI.Calculating_Taw3()*(GUI.C1_Value()+GUI.C2_Value()),((GUI.C3_Value()*(GUI.Calculating_Taw1())+(GUI.C1_Value()+GUI.C2_Value())*(GUI.Calculating_Taw2()+GUI.Calculating_Taw3()))),(GUI.C1_Value()+GUI.C2_Value()+GUI.C3_Value()),GUI.Calculating_K()*GUI.Calculating_Taw1(),GUI.Calculating_K()])
        return control.tf(num_12,den_12)
    def Divider_Phase_Noise(self):
        num_5 = np.array([GUI.N_Value() * GUI.Calculating_K() * GUI.Calculating_Taw1(), GUI.N_Value() * GUI.Calculating_K()])
        den_5 = np.array([(GUI.C1_Value() + GUI.C2_Value()) * GUI.Calculating_Taw2(), (GUI.C1_Value() + GUI.C2_Value()),GUI.Calculating_K() * GUI.Calculating_Taw1(), GUI.Calculating_K()])
        return control.tf(num_5, den_5)
    def Fourth_Order_Divider_Phase_Noise_TF(self):
        num_13=np.array([GUI.N_Value()*GUI.Calculating_K()*GUI.Calculating_Taw1(),GUI.N_Value()*GUI.Calculating_K()])
        den_13=np.array([GUI.Calculating_Taw2()*GUI.Calculating_Taw3()*(GUI.C1_Value()+GUI.C2_Value()),((GUI.C3_Value()*(GUI.Calculating_Taw1())+(GUI.C1_Value()+GUI.C2_Value())*(GUI.Calculating_Taw2()+GUI.Calculating_Taw3()))),(GUI.C1_Value()+GUI.C2_Value()+GUI.C3_Value()),GUI.Calculating_K()*GUI.Calculating_Taw1(),GUI.Calculating_K()])
        return control.tf(num_13,den_13)
    def Plotting_Open_Loop_TF(self):
        j = []
        for k in GUI.frequency_axis():
            j.append(k * 2 * m.pi)
        (mag, phase_rad, w) = control.bode_plot(GUI.Open_Loop_TF(),GUI.frequency_axis(), dB=True, Hz=True, deg=True, margins=True)
        plt.show()
        plt.grid(which="both")
    def Plotting_Fourth_Order_Open_Loop_TF(self):
        (mag, phase_rad, w) = control.bode_plot(GUI.Open_Loop_TF(),GUI.frequency_axis(), dB=True, Hz=True, deg=True, margins=True)
        (mag, phase_rad, w) = control.bode_plot(GUI.Fourth_Order_Open_Loop_TF(), GUI.frequency_axis(), dB=True, Hz=True, deg=True,margins=True)
        plt.show()
        plt.grid(which="both")
    def Plotting_Closed_Loop_TF(self):
        j = []
        for k in GUI.frequency_axis():
            j.append(k * 2 * m.pi)
        (mag, phase_rad, w) = control.bode_plot(GUI.Closed_Loop_TF(),j, dB=True, Hz=True, deg=True,margins=True)
        plt.show()
        plt.grid(which="both")
    def Plotting_Fourth_Order_Closed_Loop_TF(self):
        #(mag, phase_rad, w) = control.bode_plot(GUI.Closed_Loop_TF(),GUI.frequency_axis(), dB=True, Hz=True, deg=True,margins=True)
        j=[]
        for k in GUI.frequency_axis():
            j.append(k*2*m.pi)
        (mag, phase_rad, w) = control.bode_plot(GUI.Fourth_Order_Closed_Loop_TF(),j, dB=True, Hz=True, deg=True,margins=True)
        plt.show()
        plt.grid(which="both")
    def VCO_PhaseNoise_TF(self):
        global array2
        array2=[]
        j=[]
        for k in GUI.frequency_axis():
            j.append(k*2*m.pi)
        (mag, phase_rad, w) = control.bode_plot(GUI.VCO_Phase_Noise(),j, dB=True, Hz=True,deg=True, margins=True)
        for i in mag:
            array2.append(control.mag2db(i))
        plt.show()
        plt.grid(which="both")
    def Plotting_Fourth_Order_VCO_Phase_Noise_TF(self):
        global array3
        array3 = []
        j = []
        for k in GUI.frequency_axis():
            j.append(k * 2 * m.pi)
        #( mag, phase_rad, w) = control.bode_plot(GUI.VCO_Phase_Noise(),GUI.frequency_axis(), dB=True, Hz=True,deg=True, margins=True)
        ( mag, phase_rad, w) = control.bode_plot(GUI.Fourth_Order_VCO_Phase_Noise_TF(),j, dB=True, Hz=True,deg=True, margins=True)
        for i in mag:
            array3.append(control.mag2db(i))
        plt.show()
        plt.grid(which="both")
    def Charge_Pump_PhaseNoise_TF(self):
        global array5
        array5 = []
        j = []
        for k in GUI.frequency_axis():
            j.append(k * 2 * m.pi)
        # (mag, phase_rad, w) = control.bode_plot(GUI.Charge_Pump_Phase_Noise(),GUI.frequency_axis(), dB=True, Hz=True, deg=True, margins=True)
        (mag, phase_rad, w) = control.bode_plot(GUI.Charge_Pump_Phase_Noise(), j, dB=True, Hz=True, deg=True, margins=True)
        for i in mag:
            array5.append(control.mag2db(i))
        plt.show()
        plt.grid(which="both")
    def Plotting_Fourth_Order_Charge_Pump_Phase_Noise_TF(self):
        # (mag, phase_rad, w) = control.bode_plot(GUI.Charge_Pump_Phase_Noise(), GUI.frequency_axis(), dB=True, Hz=True,deg=True, margins=True)
        global array6
        array6 = []
        j = []
        for k in GUI.frequency_axis():
            j.append(k * 2 * m.pi)
        (mag, phase_rad, w) = control.bode_plot(GUI.Fourth_Order_Charge_Pump_Phase_Noise(), j, dB=True, Hz=True,deg=True, margins=True)
        for i in mag:
            array6.append(control.mag2db(i))
        plt.show()
        plt.grid(which="both")
    def LF_PhaseNoise_TF(self):
        global LF_array
        LF_array=[]
        j=[]
        for k in GUI.frequency_axis():
            j.append(k*2*m.pi)
        (mag,phase_rad,w) = control.bode_plot(GUI.Loop_Filter_Phase_Noise(),j, dB=True, Hz=True,deg=True, margins=True)
        for i in mag:
            LF_array.append(control.mag2db(i))
        plt.show()
        plt.grid(which="both")
    def Plotting_Fourth_Order_LF_Phase_Noise_TF(self):
        global LF_array2
        LF_array2 = []
        j = []
        for k in GUI.frequency_axis():
            j.append(k * 2 * m.pi)
        (mag, phase_rad, w) = control.bode_plot(GUI.Fourth_Order_Loop_Filter_Phase_Noise_TF(),j, dB=True, Hz=True,deg=True, margins=True)
        for i in mag:
            LF_array2.append(control.mag2db(i))
        plt.show()
        plt.grid(which="both")
    def Divider_PhaseNoisse_TF(self):
        global array8
        array8=[]
        j=[]
        for k in GUI.frequency_axis():
            j.append(k*2*m.pi)
        (mag, phase_rad, w) = control.bode_plot(GUI.Divider_Phase_Noise(),j, dB=True, Hz=True,deg=True, margins=True)
        for i in mag:
            array8.append(control.mag2db(i))
        plt.show()
        plt.grid(which="both")
    def Plotting_Fourth_Order_Divider_PhaseNoise_TF(self):
        #(mag, phase_rad, w) = control.bode_plot(GUI.Divider_Phase_Noise(),GUI.frequency_axis(), dB=True, Hz=True,deg=True, margins=True)
        global array9
        array9 = []
        j = []
        for k in GUI.frequency_axis():
            j.append(k * 2 * m.pi)
        (mag, phase_rad, w) = control.bode_plot(GUI.Fourth_Order_Divider_Phase_Noise_TF(),j, dB=True, Hz=True,deg=True, margins=True)
        for i in mag:
            array9.append(control.mag2db(i))
        plt.show()
        plt.grid(which="both")
    def VCO_Noise(self):
        global vco
        global vco2
        global total_vco_noise
        vco=[]
        total_vco_noise=[]
        vco2=[]
        global array
        array=[]
        for i in GUI.frequency_axis():
            array.append((-30 * m.log10(i)) + 44)
            vco.append((-20 * m.log10(i)) - 4)
            vco2.append(-155)
        for j in range(0,len(array)):
            total_vco_noise.append(10*m.log10(m.pow(10,array[j]/10)+m.pow(10,vco[j]/10)+m.pow(10,vco2[j]/10)))
        plt.semilogx(GUI.frequency_axis(), total_vco_noise)
        plt.show()
        plt.grid(which="both")
    def Output_Phase_Noise_Due_To_VCO_Phase_Noise(self):
        GUI.VCO_Noise()
        GUI.Plotting_Fourth_Order_VCO_Phase_Noise_TF()
        GUI.VCO_PhaseNoise_TF()
        global Output_Noise
        global Output_Noise2
        Output_Noise=[]
        Output_Noise2=[]
        for i in range(0,len(total_vco_noise)):
            Output_Noise.append(array2[i]+(array[i]))
        for i in range(0,len(total_vco_noise)):
            Output_Noise2.append(total_vco_noise[i]+array3[i])
        plt.figure()
        plt.subplot(2,1,1)
        #plt.semilogx(GUI.frequency_axis(),Output_Noise)
        plt.semilogx(GUI.frequency_axis(),Output_Noise2)
        plt.grid(which="both")
        plt.show()
    def Output_Charge_Pump_Phase_Noise(self):
        global empty_array
        global charge_pump
        global total_charge_pump_noise
        total_charge_pump_noise=[]
        charge_pump=[]
        empty_array=[]
        for i in GUI.frequency_axis():
            #empty_array.append((-10 * m.log10(i)) - 173.7867) #800uA
            #charge_pump.append(-236.797) #800uA
            #empty_array.append((-10 * m.log10(i)) - 167.9897)  # 3 mA
            #charge_pump.append(-231)  # 3 mA
            #empty_array.append((-10 * m.log10(i)) - 170.9897)  # 1.5 mA
            #charge_pump.append(-234)  # 1.5 mA
            #empty_array.append((-10 * m.log10(i)) - 164.9897)  # 6 mA
            #charge_pump.append(-228)  # 6 mA
            #empty_array.append((-10 * m.log10(i)) - 161.9897)  # 12 mA
            #charge_pump.append(-225)  # 12 mA
            #empty_array.append((-10 * m.log10(i)) - 160.9897)  # 15 mA
            #charge_pump.append(-224)  # 15 mA
            #empty_array.append((-10 * m.log10(i)) - 159.5897)  # 21 mA
            empty_array.append((-10 * m.log10(i)) - 172.7897)  # 1 mA
            #charge_pump.append(-222.6)  # 21 mA
            charge_pump.append(-235.8)  # 1 mA
        for j in range(0,len(empty_array)):
            total_charge_pump_noise.append(10*m.log10(m.pow(10,empty_array[j]/10)+m.pow(10,charge_pump[j]/10)))
        #plt.semilogx(GUI.frequency_axis(),empty_array)
        plt.semilogx(GUI.frequency_axis(),total_charge_pump_noise)
        plt.show()
        plt.grid(which="both")
    def Output_Phase_Noise_Due_To_Charge_Pump_Phase_Noise(self):
        GUI.Charge_Pump_PhaseNoise_TF()
        GUI.Plotting_Fourth_Order_Charge_Pump_Phase_Noise_TF()
        GUI.Output_Charge_Pump_Phase_Noise()
        global Output_Phase_Noise
        global Output_Phase_Noise2
        Output_Phase_Noise=[]
        Output_Phase_Noise2=[]
        for i in range(0, len(total_charge_pump_noise)):
            Output_Phase_Noise.append(total_charge_pump_noise[i]+array5[i])
        for i in range(0, len(empty_array)):
            Output_Phase_Noise2.append(total_charge_pump_noise[i]+array6[i])
        plt.figure()
        plt.subplot(2,1,1)
        plt.semilogx(GUI.frequency_axis(),Output_Phase_Noise)
        plt.semilogx(GUI.frequency_axis(),Output_Phase_Noise2)
        plt.grid(which="both")
        plt.show()
    def Output_Divider_Phase_Noise(self):
        GUI.Fout()
        global divider
        global divider2
        divider2=[]
        divider=[]
        empty_array2 = []
        for i in GUI.frequency_axis():
            if fout<200:
                    empty_array2.append((-10 * m.log10(i) - 104.9897))
                    divider.append(-168)
            else:
                    empty_array2.append((-10 * m.log10(i) - 96.98970004))
                    divider.append(-160)
        for j in range(0,len(empty_array2)):
            divider2.append(10*m.log10(m.pow(10,empty_array2[j]/10)+m.pow(10,divider[j]/10)))
        plt.semilogx(GUI.frequency_axis(),divider2)
        plt.show()
        plt.grid(which="both")
    def Output_phase_Noise_Due_To_Feedback_Divider(self):
        GUI.Divider_PhaseNoisse_TF()
        GUI.Plotting_Fourth_Order_Divider_PhaseNoise_TF()
        GUI.Output_Divider_Phase_Noise()
        global Output_Phase_Noise3
        global Output_Phase_Noise4
        Output_Phase_Noise3 = []
        Output_Phase_Noise4 = []
        for i in range(0, len(divider2)):
            Output_Phase_Noise3.append(divider2[i] + array8[i])
        for i in range(0, len(divider2)):
            Output_Phase_Noise4.append(divider2[i] + array9[i])
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.semilogx(GUI.frequency_axis(), Output_Phase_Noise3)
        plt.semilogx(GUI.frequency_axis(), Output_Phase_Noise4)
        plt.grid(which="both")
        plt.show()
    def Reference_Noise(self):
        global empty_array3
        empty_array3 = []
        ref1=[]
        ref2=[]
        for i in GUI.frequency_axis():
            ref1.append((-30*m.log10(i))-42)
            ref2.append(-168)
        for j in range(0,len(ref1)):
            empty_array3.append(10*m.log10((m.pow(10,ref1[j]/10))+(m.pow(10,ref2[j]/10))))
        plt.semilogx(GUI.frequency_axis(), empty_array3)
        plt.show()
        plt.grid(which="both")
    def Output_Phase_Noise_Due_To_reference_Noise(self):
        GUI.Divider_PhaseNoisse_TF()
        GUI.Plotting_Fourth_Order_Divider_PhaseNoise_TF()
        GUI.Reference_Noise()
        global Output_Phase_Noise5
        global Output_Phase_Noise6
        Output_Phase_Noise5 = []
        Output_Phase_Noise6 = []
        for i in range(0, len(empty_array3)):
            Output_Phase_Noise5.append(empty_array3[i] + array8[i])
        for i in range(0, len(empty_array3)):
            Output_Phase_Noise6.append(empty_array3[i] + array9[i])
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.semilogx(GUI.frequency_axis(), Output_Phase_Noise5)
        plt.semilogx(GUI.frequency_axis(), Output_Phase_Noise6)
        plt.grid(which="both")
        plt.show()
    def Output_Phase_Noise_Due_To_MUX_Noise(self):
        GUI.Divider_PhaseNoisse_TF()
        GUI.Output_Divider_Phase_Noise()
        GUI.Plotting_Fourth_Order_Divider_PhaseNoise_TF()
        global Output_Phase_Noise7
        global Output_Phase_Noise8
        Output_Phase_Noise7 = []
        Output_Phase_Noise8 = []
        for i in range(0, len(divider2)):
            Output_Phase_Noise7.append(divider2[i] + array8[i])
        for i in range(0, len(divider2)):
            Output_Phase_Noise8.append(divider2[i] + array9[i])
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.semilogx(GUI.frequency_axis(), Output_Phase_Noise7)
        plt.semilogx(GUI.frequency_axis(), Output_Phase_Noise8)
        plt.grid(which="both")
        plt.show()
    def Loop_Filter_Phase_Noise5(self):
        global arr
        arr = []
        first_term=4*1.38E-23*300*GUI.R3_Value()
        for i in GUI.frequency_axis():
            arr.append(10*m.log10(first_term/(1+(m.pow(i/6678555.811,2)))))
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.semilogx(GUI.frequency_axis(), arr)
        plt.grid(which="both")
        plt.show()
    def Output_Phase_Noise_Due_To_Loop_Filter_Phase_Noise(self):
        global lf_noise
        global lf_noise2
        GUI.Plotting_Fourth_Order_LF_Phase_Noise_TF()
        GUI.LF_PhaseNoise_TF()
        GUI.Loop_Filter_Phase_Noise5()
        lf_noise = []
        lf_noise2=[]
        for i in range(0, len(arr)):
            lf_noise.append(arr[i]+LF_array[i])
        for i in range(0,len(arr)):
            lf_noise2.append(arr[i]+LF_array2[i])
        plt.figure()
        plt.subplot(2, 1, 1)
        #plt.semilogx(GUI.frequency_axis(), lf_noise)
        plt.semilogx(GUI.frequency_axis(), lf_noise2)
        plt.grid(which="both")
        plt.show()
    def Total_Phase_Noise(self):
        global total_phase_noise
        GUI.Output_Phase_Noise_Due_To_VCO_Phase_Noise()
        GUI.Output_Phase_Noise_Due_To_Charge_Pump_Phase_Noise()
        GUI.Output_phase_Noise_Due_To_Feedback_Divider()
        GUI.Output_Phase_Noise_Due_To_reference_Noise()
        GUI.Output_Phase_Noise_Due_To_MUX_Noise()
        GUI.Output_Phase_Noise_Due_To_Loop_Filter_Phase_Noise()
        total_phase_noise=[]
        vco_noise=[]
        charge_pump_noise=[]
        feedback_divider_noise=[]
        ref_noise=[]
        ref_div_noise=[]
        lf_phase_noise=[]
        for i in range(0,len(Output_Noise)):
            vco_noise.append(m.pow(10,Output_Noise[i]/10))
        for i in range(0,len(Output_Phase_Noise)):
            charge_pump_noise.append(m.pow(10,Output_Phase_Noise[i]/10))
        for i in range(0,len(Output_Phase_Noise3)):
            feedback_divider_noise.append(m.pow(10,Output_Phase_Noise3[i]/10))
        for i in range(0,len(Output_Phase_Noise5)):
            ref_noise.append(m.pow(10,Output_Phase_Noise5[i]/10))
        for i in range(0,len(Output_Phase_Noise7)):
            ref_div_noise.append(m.pow(10,Output_Phase_Noise7[i]/10))
        for i in range(0,len(lf_noise)):
            lf_phase_noise.append(m.pow(10,lf_noise[i]/10))
        for i in range(0,len(Output_Noise)):
            total_phase_noise.append(10*m.log10(vco_noise[i]+charge_pump_noise[i])+feedback_divider_noise[i]+ref_noise[i]+ref_div_noise[i]+lf_phase_noise[i])
    def Total_Output_Phase_Noise(self):
        GUI.Out_Divider_Phase_Noise()
        global total_phase_noise2
        GUI.Total_Phase_Noise()
        total_phase_noise2=[]
        total=[]
        out_div_noise=[]
        total2=[]
        noise=20*m.log10(1/GUI.Output_Divider_Value())
        for i in range(0,len(total_phase_noise)):
            total_phase_noise2.append(total_phase_noise[i]+noise) #Total Phase Noise at output ( after output divider )
        for j in range(0,len(total_phase_noise2)):
            total.append(m.pow(10,total_phase_noise2[j]/10))  #to add total phase noise and output divider noise
        for j in range(0,len(divider2)):
            out_div_noise.append(m.pow(10,divider2[j]/10))
        for k in range(0,len(out_div_noise)):
            total2.append(10*m.log10(total[k]+out_div_noise[k]))        #total phase noise (total at vco+output divider noise)
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.semilogx(GUI.frequency_axis(), total2)
        plt.grid(which="both")
        plt.show()
    def Total_Phase_Noise_Fourth_Order(self):
        global total_phase_noise3
        vco_noise2 = []
        charge_pump_noise2 = []
        feedback_divider_noise2 = []
        ref_noise2 = []
        ref_div_noise2 = []
        lf_phase_noise2 = []
        total_phase_noise3=[]
        GUI.Output_Phase_Noise_Due_To_VCO_Phase_Noise()
        GUI.Output_Phase_Noise_Due_To_Charge_Pump_Phase_Noise()
        GUI.Output_phase_Noise_Due_To_Feedback_Divider()
        GUI.Output_Phase_Noise_Due_To_reference_Noise()
        GUI.Output_Phase_Noise_Due_To_MUX_Noise()
        GUI.Output_Phase_Noise_Due_To_Loop_Filter_Phase_Noise()
        for i in range(0,len(Output_Noise2)):
            vco_noise2.append(m.pow(10,Output_Noise2[i]/10))
        for i in range(0,len(Output_Phase_Noise2)):
            charge_pump_noise2.append(m.pow(10,Output_Phase_Noise2[i]/10))
        for i in range(0,len(Output_Phase_Noise4)):
            feedback_divider_noise2.append(m.pow(10,Output_Phase_Noise4[i]/10))
        for i in range(0,len(Output_Phase_Noise6)):
            ref_noise2.append(m.pow(10,Output_Phase_Noise6[i]/10))
        for i in range(0,len(Output_Phase_Noise8)):
            ref_div_noise2.append(m.pow(10,Output_Phase_Noise8[i]/10))
        for i in range(0,len(lf_noise2)):
            lf_phase_noise2.append(m.pow(10,lf_noise2[i]/10))
        for i in range(0,len(Output_Noise2)):
            total_phase_noise3.append(10*m.log10(vco_noise2[i]+charge_pump_noise2[i])+feedback_divider_noise2[i]+ref_noise2[i]+ref_div_noise2[i])
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.semilogx(GUI.frequency_axis(), total_phase_noise3)
        plt.grid(which="both")
        plt.show()
    def Total_Output_Phase_Noise_Fourth_Order(self):
        GUI.Total_Phase_Noise_Fourth_Order()
        GUI.Output_Divider_Phase_Noise()
        total_phase_noise4 = []
        global total4
        total3=[]
        total4=[]
        out_div_noise2=[]
        total5=[]
        noise = 20 * m.log10(1 / GUI.Output_Divider_Value())
        for i in range(0, len(total_phase_noise3)):
            total_phase_noise4.append(total_phase_noise3[i] + noise)
        for j in range(0, len(total_phase_noise4)):
            total3.append(m.pow(10, total_phase_noise4[j] / 10))
        for j in range(0, len(divider2)):
            out_div_noise2.append(m.pow(10, divider2[j] / 10))
        for k in range(0, len(out_div_noise2)):
            total4.append(10 * m.log10(total3[k] + out_div_noise2[k]))
        for u in range(0,len(total4)):
            total5.append(10 * m.log10((m.pow(10,total4[u]/10))+(m.pow(10,divider2[u]/10))))
            #total noise after buffer
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.semilogx(GUI.frequency_axis(), total5)
        plt.grid(which="both")
        plt.show()

QApplication_object=QApplication([])
GUI=GUI()
GUI.show()
QApplication_object.exec_()
print('Output Frequency=',GUI.Fout())
sys.exit()




