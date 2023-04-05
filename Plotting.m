%% Housekeeping
clc
clear all
close all

%% Plotting

figure;
for i = 1:3
    angles = cell2mat(struct2cell(load("Test_"+num2str(i)+"_angles",'-mat',"joint_angles")));
    time = cell2mat(struct2cell(load("Test_"+num2str(i)+"_time",'-mat',"time")));
    subplot(2,2,i)
    plot(time,angles)
    xlabel('Time (s)');
    ylabel('Joint Angle (degrees)');
end
figure;
for i = 1:3
    angles = cell2mat(struct2cell(load("Test_"+num2str(i)+"_angles",'-mat',"joint_angles")));
    time = cell2mat(struct2cell(load("Test_"+num2str(i)+"_time",'-mat',"time")));
    subplot(2,2,i)
    plot(time,angles)
    xlabel('Time (s)');
    ylabel('Joint Angle (degrees)');
end
figure;
for i = 1:3
    angles = cell2mat(struct2cell(load("Test_"+num2str(i)+"_angles",'-mat',"joint_angles")));
    time = cell2mat(struct2cell(load("Test_"+num2str(i)+"_time",'-mat',"time")));
    subplot(2,2,i)
    plot(time,angles)
    xlabel('Time (s)');
    ylabel('Joint Angle (degrees)');
end