
AA = 4.00
BA = 3.75
BB = 3.50
CB = 3.00
CC = 2.50
CD = 2.00
DD = 1.50
DF = 1.00
FF = 0.00

# fist fall
BIL131 = 7*(FF)     #Programming 1
EEE101 = 5*(BA)     #Introduction to Electrical Engineering
FEF111 = 4*(BB)     #Physics 1
FEF121 = 3*(DD)     #Physics Lab 1
GNL105 = 2*(CC)     #Turk Dili 1
LNG101 = 2*(BA)     #General English 1
MAT121 = 7*(CB)     #Mathematical Analysis 1

s1 = BIL131+EEE101+FEF111+FEF121+GNL105+LNG101+MAT121
# first spring

BIL132 = 4*(BB)     #Programming 2
ENG126 = 5*(CB)     #Engineering Mathematics 1
FEF112 = 4*(CC)     #Physics 2
FEF122 = 3*(CB)     #Physics Lab 2
GNL106 = 2*(CC)     #Turk Dili 2
GNL112 = 3*(BB)     #City Culture and Istanbul
LNG102 = 2*(BA)     #General English 2
MAT122 = 7*(CD)     #Mathematical Analysis 1

s2 = BIL132+ENG126+FEF112+FEF122+GNL106+GNL112+LNG102+MAT122

# second fall

EEE203 = 5*(FF)     # Logic Circuits
EEE205 = 6*(FF)     # Electrical Materials
EEE213 = 7*(FF)     # Circuit Theory
ENG227 = 5*(FF)     # Engineering Mathematics 2
GNL101 = 2*(CB)     # Ataturk ILkeleri 1
s3 = EEE203+EEE205+EEE213+ENG227+GNL101

# second spring

EEE202 = 4*(BB) # Electro-Technic Labrotuary
EEE206 = 5*(FF) # Linear System Theory
EEE225 = 4*(BB) # Logic Labrotuary
EEE431 = 5*(CC) # Embedded System Design and Archiacture
ENG211 = 5*(BA) # Numerical Analysis
GNL102 = 2*(CB) # Ataturk ILkeleri 2
MEE216 = 5*(CB) # Measurment and Insturmentation

s4 = EEE202+EEE206+EEE225+EEE431+ENG211+GNL102+MEE216

gpa = (s1+s2+s3+s4)/115

print(gpa)
