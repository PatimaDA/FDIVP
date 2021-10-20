% GNU Octave

img = im2double(imread('W03Q08IMG00.jpg'))
k = ones(3,3)*(1/9)
lpf = imfilter(img, k, 'replicate')

dsimg = lpf(1:2:359,1:2:479)

upimg = upsample(upsample(dsimg,2)',2)'
upimg = upimg(1:1:359,1:1:479)

ck = [0.25,0.5,0.25;0.5,1,0.5;0.25,0.5,0.25]

cvimg = imfilter(upimg, ck)

mse = sum(sum(power(cvimg-img,2)))/171961

psnr = 10*log10(1/mse)

