%-*- mode: matlab;-*-
lena = im2double(imread('lena.gif'))

k3 = [1/9,1/9,1/9;1/9,1/9,1/9;1/9,1/9,1/9;]
k5 = ones(5,5)*(1/25)

lpf3 = imfilter(lena, k3, 'replicate')
lpf5 = imfilter(lena, k5, 'replicate')

psnr3 = psnr(lpf3,lena,1)
psnr5 = psnr(lpf5,lena,1)

%29.2951
%25.7335
