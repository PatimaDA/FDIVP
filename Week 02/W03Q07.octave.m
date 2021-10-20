% GNU Octave

lena = im2double(imread('lena.gif'))

k3 = ones(3,3)*(1/9)
k5 = ones(5,5)*(1/25)

lpf3 = imfilter(lena, k3, 'replicate')
lpf5 = imfilter(lena, k5, 'replicate')

mse3 = sum(sum(power(lpf3-lena,2)))/65536
mse5 = sum(sum(power(lpf5-lena,2)))/65536

psnr3 = 10*log10(1/mse3)
psnr5 = 10*log10(1/mse5)

% 29.295
% 25.735
