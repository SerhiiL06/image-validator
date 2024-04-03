urls_regex = r"(https?|www)://\S+\.(jpg|jpeg|png|webp)"

promt_message = """check the image and if you find distortion there, then return 1, otherwise return 0 and nothing else. Without explanations and unnecessary text. refers to distortions:
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
- flying objects"""
