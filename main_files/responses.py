
import pickle

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

with open("response_files/total_fees_responses.pickle", "rb") as file7:
    total_fees_responses = pickle.load(file7)

with open("response_files/tuition_fees_responses.pickle", "rb") as file8:
    tuition_fees_responses = pickle.load(file8)

with open("response_files/admission_fees_responses.pickle", "rb") as file9:
    admission_fees_responses = pickle.load(file9)

