% GNU Octave

img = im2double(imread('W05Q07IMG01.jpg'))
%imshow(img)

imgfil1 = medfilt2(img)
%imgshow(imgfil1)

imgfil2 = medfilt2(imgfil1)
%imgshow(imgfil2)

original = im2double(imread('W05Q07IMG02.jpg'))
%imshow(original)

[h,w] = size(original)
%a
mse = sum(sum(power(img-original,2)))/(h*w)
a = 10*log10(1/mse)

%b
mse = sum(sum(power(imgfil1-original,2)))/(h*w)
b = 10*log10(1/mse)

%c
mse = sum(sum(power(imgfil2-original,2)))/(h*w)
c = 10*log10(1/mse)
