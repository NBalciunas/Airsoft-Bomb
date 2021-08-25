EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Airsoft_Bomb-rescue:RaspberryPi4-Airsoft_Bomb_lib-Airsoft_Bomb-rescue-Airsoft_Bomb-rescue U2
U 1 1 6126E5F4
P 5900 4700
F 0 "U2" H 5900 5365 50  0000 C CNN
F 1 "RaspberryPi4" H 5900 5274 50  0000 C CNN
F 2 "" H 5900 4100 50  0001 C CNN
F 3 "" H 5900 4100 50  0001 C CNN
	1    5900 4700
	1    0    0    -1  
$EndComp
$Comp
L Airsoft_Bomb-rescue:4x4_Matrix_Keypad-Airsoft_Bomb_lib-Airsoft_Bomb-rescue-Airsoft_Bomb-rescue U1
U 1 1 6126F9D6
P 4700 3550
F 0 "U1" H 5128 3488 50  0000 L CNN
F 1 "4x4_Matrix_Keypad" H 5128 3397 50  0000 L CNN
F 2 "" H 4700 3900 50  0001 C CNN
F 3 "" H 4700 3900 50  0001 C CNN
	1    4700 3550
	1    0    0    -1  
$EndComp
$Comp
L Airsoft_Bomb-rescue:LCD1602-I2C-Airsoft_Bomb_lib-Airsoft_Bomb-rescue-Airsoft_Bomb-rescue U3
U 1 1 612713C9
P 7100 3700
F 0 "U3" H 7042 4025 50  0000 C CNN
F 1 "LCD1602-I2C" H 7042 3934 50  0000 C CNN
F 2 "" H 7100 3600 50  0001 C CNN
F 3 "" H 7100 3600 50  0001 C CNN
	1    7100 3700
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW1
U 1 1 6127AF34
P 7250 4550
F 0 "SW1" H 7250 4835 50  0000 C CNN
F 1 "SW_Push" H 7250 4744 50  0000 C CNN
F 2 "" H 7250 4750 50  0001 C CNN
F 3 "~" H 7250 4750 50  0001 C CNN
	1    7250 4550
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW2
U 1 1 6127C8D0
P 7250 5100
F 0 "SW2" H 7250 5385 50  0000 C CNN
F 1 "SW_Push" H 7250 5294 50  0000 C CNN
F 2 "" H 7250 5300 50  0001 C CNN
F 3 "~" H 7250 5300 50  0001 C CNN
	1    7250 5100
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 61281220
P 7600 4550
F 0 "R1" V 7393 4550 50  0000 C CNN
F 1 "R" V 7484 4550 50  0000 C CNN
F 2 "" V 7530 4550 50  0001 C CNN
F 3 "~" H 7600 4550 50  0001 C CNN
	1    7600 4550
	0    1    1    0   
$EndComp
$Comp
L Device:R R2
U 1 1 61282430
P 7600 5100
F 0 "R2" V 7393 5100 50  0000 C CNN
F 1 "R" V 7484 5100 50  0000 C CNN
F 2 "" V 7530 5100 50  0001 C CNN
F 3 "~" H 7600 5100 50  0001 C CNN
	1    7600 5100
	0    1    1    0   
$EndComp
Wire Wire Line
	5500 4950 5050 4950
Wire Wire Line
	5050 4950 5050 4150
Wire Wire Line
	5500 5000 4950 5000
Wire Wire Line
	4950 5000 4950 4150
Wire Wire Line
	5500 5050 4850 5050
Wire Wire Line
	4850 5050 4850 4150
Wire Wire Line
	5500 5100 4750 5100
Wire Wire Line
	4750 5100 4750 4150
Wire Wire Line
	5500 5150 4650 5150
Wire Wire Line
	4650 5150 4650 4050
Wire Wire Line
	6300 5200 6350 5200
Wire Wire Line
	6350 5200 6350 5300
Wire Wire Line
	6350 5300 4350 5300
Wire Wire Line
	4350 5300 4350 4050
Wire Wire Line
	6300 5150 6400 5150
Wire Wire Line
	6400 5150 6400 5350
Wire Wire Line
	6400 5350 4450 5350
Wire Wire Line
	4450 5350 4450 4050
Wire Wire Line
	4550 4050 4550 5400
Wire Wire Line
	4550 5400 6450 5400
Wire Wire Line
	6450 5400 6450 5100
Wire Wire Line
	6450 5100 6300 5100
Wire Wire Line
	6500 3600 6350 3600
Wire Wire Line
	6350 3600 6350 4350
Wire Wire Line
	6350 4350 6300 4350
Wire Wire Line
	6300 4250 6400 4250
Wire Wire Line
	6400 4250 6400 3650
Wire Wire Line
	6400 3650 6500 3650
Wire Wire Line
	6500 3700 5850 3700
Wire Wire Line
	5850 3700 5850 3800
Wire Wire Line
	5850 3800 5450 3800
Wire Wire Line
	5450 3800 5450 4300
Wire Wire Line
	5450 4300 5500 4300
Wire Wire Line
	6500 3750 5900 3750
Wire Wire Line
	5900 3750 5900 3850
Wire Wire Line
	5900 3850 5400 3850
Wire Wire Line
	5400 3850 5400 4350
Wire Wire Line
	5400 4350 5500 4350
Wire Wire Line
	5500 4250 5500 3950
Wire Wire Line
	5500 3950 7750 3950
Wire Wire Line
	7750 3950 7750 4550
Wire Wire Line
	7750 5100 7750 4550
Connection ~ 7750 4550
Wire Wire Line
	5500 4550 5450 4550
Wire Wire Line
	5450 4550 5450 5450
Wire Wire Line
	5450 5450 7000 5450
Wire Wire Line
	7000 5450 7000 5100
Wire Wire Line
	7000 5100 7050 5100
Wire Wire Line
	7050 4550 6950 4550
Wire Wire Line
	6950 4550 6950 5500
Wire Wire Line
	6950 5500 5400 5500
Wire Wire Line
	5400 5500 5400 4500
Wire Wire Line
	5400 4500 5500 4500
$EndSCHEMATC
