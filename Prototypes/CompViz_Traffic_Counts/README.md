# This is a POC for Traffic detection. 

- Built in 2018 so use the pip install to avoid compatibility issues. Using a variety of resources online including openCV tutorials and learning about these tools with pyimagesearch and generally looking through tutorials on traffic detection (have others i've tried for ANPR and etc that I will upload soon in another repo).

- This solution is not ideal. Lots of issues like not showing vehicle classification. It does give quite good accuracy though (especially with some small improvements). A small & simple algorithms really - that gives better results than any loop detector ever could. The best way to do this is to use deep convolution networks.

- I was trying to make this work on a raspberry pi which was a bit of a waste of time lol.



## Instructions
Re-adjust inputs with the traffic video of your choice as per below and run t_detection.py when finished.

Your output will be "./tester" dir with frames and etc, and "data.csv" file with format "time, vehicles".

Use compile  script to create video from frames.

How to create report plot -> change in the variables within the file depending on the data csv.

How to adjust.
Edit **t_detection.py** . Should be relatively straightforward.
