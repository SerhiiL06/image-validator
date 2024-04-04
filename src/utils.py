urls_regex = r"(https?|www)://\S+\.(jpg|jpeg|png|webp)"

prompt_message = """
        We want to use you as a validator of the generated images, your task is to analyze the images for certain distortions, 
        inconsistencies in the size of human body parts (if there are people there) and other things that will be strange in your opinion. 
        If you find any of the above, then return the number 1, which will indicate that the image has distortion and we will not send it to the client, 
        but if everything is in order, then return 0. Below I will give several examples of distortions, but this does not say that the list is limited to this. 
        If there is something strange for you in the picture, feel free to return 1. Also, please return only 0 and 1, no more text.
        Refers to distortions:
        - more or less than 2 arms or lags
        - two heads
        - disproportionately long or short fingers
        - disproportionately long or short limbs
        - weird pose or body plastic of people
        - parts of the body are separate from the body
        - limbs of some people stuck in others
        - disproportionate head size
        - crooked limbs
        - crooked fingers
        - blurred face
        - flying objects
        """
