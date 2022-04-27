
import pickle

help_response = """
✅ I can give information about different courses provided by our university, their fees and the exam related information. You can ask me like:-

➡ suggest me a mtech it course
➡ is there any certification course provided by university?
➡ how many departments you have?
➡ give me a list of mtech it courses.
➡ whats about msc it
➡ whats about media science
➡ tuition fee for msc it courses

and many more...
"""

certi_response = """
we provide certification courses in 7 subjects📓. They are...

✅ Advanced Computational Science
✅ Artificial Intelligence
✅ Core Networking
✅ Data Analytics with Python
✅ Web Application Design
✅ Forensic Science and Criminology
✅ Computer Forensic and Cyber Crime

if you want to know about their fees. just click 
https://makautwb.ac.in/page.php?id=220#cer
"""

course_types = """
We provides different types of courses from difference domains \
like Media Science, Information Technology, Computer Science, etc. \
Our provided degrees are **B.Sc**, **B.Tech**, **M.Sc**, **M.Tech**, **MCA**.
"""

departments_text = """
We have 12 departments in total. Those are:-

➡ Department of Information Technology
➡ Department of Computer Science and Engineering
➡ Department of Biotechnology
➡ Department of Industrial Engineering and Management
➡ Department of Microelectronics and VLSI Technology
➡ Department of Media Science
➡ Center for Robotics and 3D Printing
➡ Department of Applied Science
➡ Department of Forensic Science
➡ Department of Materials Science and Technology
➡ Department of Food Science and Technology
➡ Department of Pharmaceutical Science and Technology
"""

with open("response_files/hello_response.pickle", "rb") as file1:
    hello_responses = pickle.load(file1)

with open("response_files/thank_you_response.pickle", "rb") as file2:
    thank_you_responses = pickle.load(file2)

with open("response_files/goodbye_response.pickle", "rb") as file3:
    goodbye_responses = pickle.load(file3)

with open("response_files/ask_response.pickle", "rb") as file4:
    ask_responses = pickle.load(file4)

with open("response_files/whereabouts_response.pickle", "rb") as file5:
    whereabouts_responses = pickle.load(file5)

with open("response_files/data_responses.pickle", "rb") as file6:
    data_responses = pickle.load(file6)

with open("response_files/pg_total_fees_responses.pickle", "rb") as file7:
    pg_total_fees_responses = pickle.load(file7)

with open("response_files/bsc_total_fees_responses.pickle", "rb") as file7:
    bsc_total_fees_responses = pickle.load(file7)

with open("response_files/pg_tuition_fees_responses.pickle", "rb") as file8:
    pg_tuition_fees_responses = pickle.load(file8)

with open("response_files/bsc_tuition_fees_responses.pickle", "rb") as file8:
    bsc_tuition_fees_responses = pickle.load(file8)

with open("response_files/pg_admission_fees_responses.pickle", "rb") as file9:
    pg_admission_fees_responses = pickle.load(file9)

with open("response_files/bsc_admission_fees_responses.pickle", "rb") as file9:
    bsc_admission_fees_responses = pickle.load(file9)

