# ENV_VAR_ORDER sets the display order of variables on the node
ENV_VAR_ORDER = [
        "JOB",
        "SHOT",
        "SHOT_NAME",
        "XRES",
        "YRES",
        "PIXEL_ASPECT",
        ]

# In this example $JOB points to the directory where "job_env.py" script is.
if "job_env.py" in ENV_SCRIPTS:
    JOB = ENV_SCRIPTS["job_env.py"]

# In this example $SHOT points to the directory where "shot_env.py" script is
# or to the $HIP directory.
if "shot_env.py" in ENV_SCRIPTS:
    SHOT = ENV_SCRIPTS["shot_env.py"]
    SHOT_NAME = basename(SHOT)
else:
    SHOT_NAME = HIPNAME
    if SHOT_NAME.endswith(".hip"):
        SHOT_NAME = SHOT_NAME[:-4]
    SHOT = HIP

# Install job level OTLs under the $JOB/Asset directory
OTL_PATTERN = JOB + "/Asset/*/Otl/*.otl"

# Scene defaults
FPS = 25

# Camera defaults
XRES = 1920
YRES = 1080
PIXEL_ASPECT = 1
HAPERTURE = 23.8
