import logging
import requests
from typing import Dict

UBC_GRADES_URL = "https://ubcgrades.com/api"
UBC_GRADES_VERSION = "v3"
GRADES = "grades"
COURSE_STAT = "course-statistics"
UBC_CAMPUS = "UBCV"

def fetch_course_title(subject: str, code: str) -> str:
    """
    Fetch the course title from the UBCGrades API for a given subject and course code.

    Args:
        subject (str): The subject code of the course (e.g. 'MATH' for Mathematics).
        code (str): The course code (e.g. '100' for MATH 100).

    Returns:
        str: The course title (e.g. 'Differential Calculus with Applications').

    Raises:
        Logs an error message if the API request fails.
    """
    
    url = f"{UBC_GRADES_URL}/{UBC_GRADES_VERSION}/{COURSE_STAT}/{UBC_CAMPUS}/{subject}/{code}"

    response = requests.get(url=url)

    if response.status_code == 200:
        json_response = response.json()
        title = json_response["course_title"]
        logging.info(f"Fetched new course title. {subject} {code}: {title}")
        return title
    else:
        logging.error(f"Failed fetch course title. Please check api_utilities:get_course_title. Response: {response}")

def fetch_course_title__and_average(session: str, subject:str, code: str, section: str) -> Dict[str, str]:
    """
    Fetch course information from the UBCGrades API and return the course title and average.

    Args:
        session (str): The session in which the course was offered (e.g. '2021W' for 2021 Winter session).
        subject (str): The subject code of the course (e.g. 'MATH' for Mathematics).
        code (str): The course code (e.g. '100' for MATH 100).
        section (str): The section code for the course (e.g. '101' for Section 101).

    Returns:
        dict: A dictionary containing the course title and average.
            {
                "title": str,  # The course title (e.g. 'Differential Calculus with Applications').
                "average": str,  # The average grade for the course (e.g. 69.0).
            }

    Raises:
        Logs an error message if the API request fails.
    """
    url = f"{UBC_GRADES_URL}/{UBC_GRADES_VERSION}/{GRADES}/{UBC_CAMPUS}/{session}/{subject}/{code}/{section}"

    response = requests.get(url=url)

    if response.status_code == 200:
        json_response = response.json()
        return {
            "title": json_response["course_title"],
            "average": json_response["average"],
        }
    else:
        logging.error(f"Failed fetch course title and average. Please check api_utilities:get_course_title_and_average. Response: {response}")
