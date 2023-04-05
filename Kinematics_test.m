%% Housekeeping
clc
clear all
close all

%% Important Values
img_diag = 40;  % [in]
h_res = 1296;   % [pixels]
v_res = 976;    % [pixels]

PPI = sqrt((h_res^2 + v_res^2)/img_diag);

% Joint 1
R1 = 3.445;
G1 = 3.885;

% Joint 2
R2 = 3.207;
G2 = 2.504;

% Joint 3
R3 = 3.566;
G3 = 2.543;

R = [R1,R1,R1,R1,R2,R2,R2,R3,R3,R3];
G = [G1,G1,G1,G1,G2,G2,G2,G3,G3,G3];

for i = 1:10
    filename = "Test_Log" + num2str(i) + ".txt";
    data = load(filename);
    joint_angles = [];
    time = [];
    r = R(i);
    g = G(i);
    idx = 1;
    for j = 1:length(data)
        rx = data(j,1);
        ry = data(j,2);
        gx = data(j,3);
        gy = data(j,4);
        if rx ~= -1 && gx ~= -1 && ry ~= -1 && gy ~= -1
            pixel_distance =  sqrt((gx-rx)^2+(gy-ry)^2);
            distance = pixel_distance/PPI;
            disp(distance);
            joint_angles(idx) = acosd((r^2+g^2-distance^2)/(2*r*g));
            % disp(acosd((r^2+g^2-distance^2)/(2*r*g)));
            time(idx) = data(j,5);
            idx = idx + 1;
        end
    end
    plot(time,joint_angles);



end

