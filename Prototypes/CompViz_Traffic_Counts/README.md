# This is a POC for Traffic detection. 

- Built in 2018 so use the pip install to avoid compatibility issues. Using a variety of resources online including openCV tutorials and learning about these tools with pyimagesearch and generally looking through tutorials on traffic detection (have others i've tried for ANPR and etc that I will upload soon in another repo).

- This solution is not ideal. Lots of issues like not showing vehicle classification. It does give quite good accuracy though (especially with some small improvements). A small & simple algorithms really - that gives better results than any loop detector ever could. The best way to do this is to use deep convolution networks.



## Instructions
Re-adjust inputs with the traffic video of your choice as per below and run t_detection.py when finished.

Your output will be "./tester" dir with frames and etc, and "data.csv" file with format "time, vehicles".

Use compile  script to create video from frames.

How to create report plot -> change in the variables within the file depending on the data csv.

How to adjust.
Edit **t_detection.py**  :
```
IMAGE_DIR = "./tester" # Your output directory for each frame.
VIDEO_SOURCE = "input.mp4" # Your input traffic video.
SHAPE = (720, 1280)  # HxW Your input traffic video's dimensions.
EXIT_PTS = np.array([
    [[732, 720], [732, 590], [1280, 500], [1280, 720]],
    [[0, 400], [645, 400], [645, 0], [0, 0]]
]) Your input traffic video exit points (so where you want the counts to be made for, say end of the road) We use masks because its a simpler way to build a POC.

...

pipeline = ......
        # y_weight == 2.0 for vertical moving traffic.
        # x_weight == 2.0 for horizontal.
        VehicleCounter(exit_masks=[exit_mask], y_weight=2.0),
        ...
```
