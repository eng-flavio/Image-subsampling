# Image Subsampling
 Image subsampling (data reduction) in Python
 
  ## Prerequisites
  - [Python 3.9](https://www.python.org/)
  - Install the most recently version of the frameworks and libraries required (`numpy`,`matplotlib` and `pylab`)
  - A  image (I am adding a *.jpg* that worked for me)
  ## Instructions for use
  - Change the input from line 9: `img = pylab.imread("img2.jpg")` to the desired image
  - The image will be converted to 256 levels in **gray scale** and re-sampled  to 50%, 25% and 12.5% of the orignal scale, like the image below: 
  
  <img src="https://github.com/eng-flavio/Image-subsampling/blob/main/results.png" alt="re-sampling" width="1000"/>
