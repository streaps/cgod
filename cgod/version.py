# Package:  version
# Date:     19th December 2014
# Author:   James Mills, j dot mills at griffith dot edu dot au


"""Version Module

So we only have to maintain version information in one place!
"""


from time import strftime
from subprocess import check_output


def generate_version():
    try:
        return check_output(
            "git rev-parse --short HEAD",
            shell=True
        ).strip().strip()
    except:
        return "{}-dev".format(strftime("%Y%m%d"))


version_info = (0, 0, 1, "dev")  # (major, minor, patch, dev?)
version = (
    ".".join(map(str, version_info))
    if version_info[-1] != "dev"
    else generate_version()
)
