# ENV_VAR_ORDER sets the display order of variables on the node

ENV_VAR_ORDER = [
        "JOB",
        "SCENE",
        "SCENE_NAME",
        "LIB",
        "XRES",
        "YRES",
        "PIXEL_ASPECT",
        ]

# JOB directory is the one that this scripts is in
if "/Scene/" in HIP:
    p = HIP.split('/')
    JOB = "/".join(p[:p.index("Scene")])

# Scan scene OTLs under the $JOB/Asset directory
OTL_PATTERN = JOB + "/Asset/*/Houdini/*.otl"

# If a directory called "Scene" is present in the path
# the scene name will be the directory right to the last
# occurance of "Scene", othervise it the scene name is
# the file name without the ".hip" extension, and $SCENE
# is equal to $HIP
if "/Scene/" in HIP:
    p = HIP.split('/')
    i = (len(p) - 1) - p[::-1].index("Scene")
    if i < len(p) - 1:
        SCENE_NAME = p[i+1]
        SCENE = '/'.join(p[:i+2])
else:
    SCENE_NAME = HIPNAME
    if SCENE_NAME.endswith(".hip"):
        SCENE_NAME = SCENE_NAME[:-4]
    SCENE = HIP

# Scene defaults
FPS = 25

# Camera defaults
XRES = 1920
YRES = 1080
PIXEL_ASPECT = 1
HAPERTURE = 23.8
