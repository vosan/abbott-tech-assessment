import re


def normalize_url(url: str):
    """
    Normalizes url to a single format to avoid inappropriate URL formats as well as avoids false-negative results when
    verifying URLs.
    :param url: a full url that includes base url and subdirectory (optional)
    :return: a formatted url (example: "https://www.baseurl.com/subdir/"
    """
    # remove slash at the end of the base url to avoid possible double-slash
    scheme = url.split(":/")[0]
    # add slashes in the beginning and at the end of the url and replace any multi-slashes with a single slash
    url = re.sub(r"//+", "/", f"/{url.split(':/')[1]}/")
    return f"{scheme}:/{url}"
