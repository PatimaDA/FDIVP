% GNU Octave

i1 = double(imread('W04Q08IMG01.jpg'))
i2 = double(imread('W04Q08IMG02.jpg'))

bt = i2(65:96,81:112)
size(b)  % 32 x 32

mae0 = 1000
for i = 1:256
  for j = 1:320
    mae1 = sum(sum(abs(bt-i1(i:i+31,j:j+31))))/(32*32)
    if mae0 > mae1
      mae0 = mae1
      ans = [i, j, mae0]
    end
  end
end

ans

%ans = 65 81 22.985

