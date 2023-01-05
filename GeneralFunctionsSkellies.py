''' Import Libraries '''


''' Function Declarations '''
def Open_Camera_Stream():
    '''
    This function will connect to the camera and open the video stream
    '''
    # Connect to and open camera
    # Check that camera stream has been opened without errors
    # Check that image isn't fucked (blue screened or other solid color)
        # May want to make this its own function to be used separately

def Rebuild_Compressed_Video():
    '''
    This function will recompile a video using individual frames
    '''
    # Target framerate of 30 fps
    # Check that frames aren't being added multiple times or at improper framerates

def Transfer_to_OBC():
    '''
    This function will stream the recreated video file to the 
    '''
    # Set transfer limit to within SpaceWire protocol
    # Ensure proper connection to OBC