import os
from .transcript_utilities import Transcript
import pdfplumber

class PdfUtilities:
    """
    A utility class for handling PDF files, including extracting text and creating HTML representation
    of the provided transcript.
    """
    @staticmethod
    async def extract_text_from_pdf(file):
        # Save the uploaded file temporarily
        temp_filename = "temp.pdf"
        with open(temp_filename, "wb") as buffer:
            buffer.write(await file.read())

        # Extract text from the PDF using pdfplumber
        with pdfplumber.open(temp_filename) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        # Remove the temporary file
        os.remove(temp_filename)

        return pages

    @staticmethod
    def create_html_string_for_transcript(transcript: Transcript) -> str:
        """
        Creates an HTML string representing the provided transcript.

        Args:
            transcript (Transcript): The transcript object containing the student and course information.

        Returns:
            str: The HTML string representing the transcript.
        """

        # Formatting student name and student ID
        name = f"{transcript.student_given_name} {transcript.student_surname}"
        student_id = transcript.student_number

        # Formatting courses into HTML table rows
        courses_html = ""
        for session, course_list in transcript.courses.items():
            courses_html += f"<tr><td colspan='11'><b>Session: {session}</b></td></tr>"
            for course in course_list:
                course_code = f"{course.subject} {course.code}"  # Combining subject and code
                courses_html += f"""
                <tr>
                    <td>{course.term}</td>
                    <td>{course_code}</td>
                    <td>{course.credit}</td>
                    <td>{course.title}</td>
                    <td>{course.num_grade}</td>
                    <td>{course.letter_grade}</td>
                    <td>{course.average}</td>
                    <td>{course.year}</td>
                    <td>{course.standing}</td>
                </tr>"""

        # Creating the final HTML string
        html_str = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Transcript</title>
                <style>
                    table {{
                        width: 100%;
                        border-collapse: collapse;
                    }}
                    th, td {{
                        border: 1px solid black;
                        padding: 5px;
                        text-align: left;
                    }}
                    th {{
                        background-color: #f2f2f2;
                    }}
                </style>
            </head>
            <body>
                <h1>Transcript</h1>
                <p>Name: {name}</p>
                <p>ID: {student_id}</p>
                <table>
                    <tr>
                        <th>Term</th>
                        <th>Course Code</th>
                        <th>Credit</th>
                        <th>Title</th>
                        <th>Numeric Grade</th>
                        <th>Letter Grade</th>
                        <th>Average</th>
                        <th>Year</th>
                        <th>Standing</th>
                    </tr>
                    {courses_html}
                </table>
            </body>
            </html>
        """

        return html_str

    @staticmethod
    def delete_file(file_path: str):
        os.remove(file_path)
