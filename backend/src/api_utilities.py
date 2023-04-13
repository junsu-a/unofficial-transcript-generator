import requests

UBC_GRADES_URL = "https://ubcgrades.com/api"
UBC_GRADES_VERSION = "v3"
COURSE_PROFILE_DATA = "course-statistics"
UBC_CAMPUS = "UBCV"

# TODO: This function assumes course code will be in a foramt of "CPEN 221" <- Write a doc/comment about it
def get_course_title(course_code: str):
    try:
        subject, code = course_code.split()
    except Exception as e:
        raise Exception(f"Error in `get_course_title` function. Error message: {e}")

    url = f"{UBC_GRADES_URL}/{UBC_GRADES_VERSION}/{COURSE_PROFILE_DATA}/{UBC_CAMPUS}/{subject}/{code}"

    response = requests.get(url=url)

    if response.status_code == 200:
        json_response = response.json()
        return json_response
    else:
        raise Exception(f"API request to UBCGrades failed with status code {response.status_code}")
