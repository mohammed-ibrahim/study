from random import shuffle

def upload_contest_data(contest_data, content):
    # app_data.contest_content = content
    contest_data.initial_keywords = list()
    contest_data.contest_content = list()

    for i in range(min(20, len(content))):
        contest_data.initial_keywords.append(content[i])

    shuffle(content)
    contest_data.contest_content = content
