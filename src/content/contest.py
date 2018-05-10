from src.utils import reader_util
from random import shuffle


class Contest:
    contest_content = list()
    initial_keywords = list()
    _iterator = None

    def __init__(self):
        sim_suggestions = reader_util.load_json_from_file("content/metadata/sim_suggestions.json")
        sim_suggestions = [a for a in sim_suggestions if len(a) > 1]
        shuffle(sim_suggestions)
        self._iterator = iter(sim_suggestions)

    def get_next_initial(self):
        if (len(self.initial_keywords) > 0):
            return (self.initial_keywords.pop(), 200)

        return ("Dictionary is over", 405)

    def get_next_contest_word(self):

        if (len(self.contest_content) < 0):
            return ("Dictionary is over", 400)

        return (self.contest_content.pop(), 200)

    def get_next_mcq(self):
        if (len(self.contest_content) < 4):
            return ("Dictionary is over", 400)

        selected = self.contest_content.pop()
        correct_answer = selected['value']
        question = selected['key']

        size = len(self.contest_content)

        op1 = self.contest_content[size-1]
        op2 = self.contest_content[size-2]
        op3 = self.contest_content[size-3]

        options = [selected, op1, op2, op3]
        shuffle(options)
        resp = {
            "question": question,
            "correct_answer": correct_answer,
            "options": options
        }

        shuffle(self.contest_content)
        return (resp, 200)

    def get_next_mtf(self):
        if (len(self.contest_content) < 5):
            return ("Dictionary is over", 400)

        r1 = self.contest_content.pop()
        r2 = self.contest_content.pop()
        r3 = self.contest_content.pop()
        r4 = self.contest_content.pop()
        r5 = self.contest_content.pop()

        correct_order = {}
        correct_order[r1['key']] = r1['value']
        correct_order[r2['key']] = r2['value']
        correct_order[r3['key']] = r3['value']
        correct_order[r4['key']] = r4['value']
        correct_order[r5['key']] = r5['value']

        values = [correct_order[k] for k in correct_order]
        keys = [k for k in correct_order]
        shuffle(values)
        resp = {
            "input": correct_order,
            "value_order": values,
            "key_order": keys
        }
        return (resp, 200)

    def get_next_sim(self):

        try:
            element = next(self._iterator)
            return (element, 200)

        except StopIteration:
            return ([], 400)
