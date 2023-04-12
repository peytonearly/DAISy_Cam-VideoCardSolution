##########################################
## Installing required python libraries ##
##########################################

1. Open a powershell/command prompt terminal and navigate into DAISy_Cam-VideoCardSolution/OBC
2. Run "pip install -r requirements.txt" to install the required python libraries.
3*. Run "python Arm_Control_Testing.py" to start the program.

#######################
## Operating Program ##
#######################

* Before running program, connect arduino to computer and open arduino ide. Find the COM port connected to the arduino and update the variable 'COM_PORT'.

>> Press 'q' to quit program.
>> Press '0' to stop arm.
>> Press '1' to open arm.
>> Press '2' to close arm.
>> Press '3' to loop arm between open and closed
