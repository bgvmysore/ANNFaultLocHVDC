clc;
clear all;

MyTs = 1.0e-4; %original Ts = 5.0e-5

faultFlag = 1;

% generating random fault location m
% nsamples = 20
% mrand = 0.1 + (0.9 - 0.1).*rand(nsamples, 1);
% mrand = round(mrand, 3);

% generating test samples
mrand = [0.309];

for i = 1:length(mrand)
    m = mrand(i);
    sim('power_hvdc12_fault');

    t_data = VdLine_R.Time;
    Vdc_line_rect = VdLine_R.Data;
    Idc_line_rect = IDLine_R.Data;

    data = [t_data, Vdc_line_rect, Idc_line_rect];

    file_name = strcat('./data/test/f_',num2str(m,3),'_.txt');
    fileID = fopen(file_name,'w');
    fprintf(fileID, 'Time, VdcL(Rectifier), IdcL(Rectifier)\n');
    fprintf(fileID,'%f, %f, %f\n',data');

    fclose(fileID);
end