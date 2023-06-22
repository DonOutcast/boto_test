def add_sub(question_id: int):
    if question_id < 0:
        return 0
    elif question_id > 2:
        return 2
    else:
        return question_id
