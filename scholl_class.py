
class Human:
    """"""

    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name

        # gender check
        if gender not in ["M", "F"]:
            raise ValueError(f"Expect gender M of F, but get: {gender}")
        self.gender = gender

    @property
    def full_info(self):
        """"""

        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender
        }


class Parent(Human):
    """"""

    def __init__(self, first_name, last_name, gender,  profession):
        super().__init__(
            first_name=first_name,
            last_name=last_name,
            gender=gender
        )
        self.profession = profession

    @property
    def role(self):
        return {"M": "father", "F": "mother"}[self.gender]


class Pupil(Human):
    """
    Class for create pupil

    """

    def __init__(self, gender, first_name, last_name, class_level):
        super().__init__(
            first_name=first_name,
            last_name=last_name,
            gender=gender
        )

        self.class_level = class_level
        self.rating = []
        self.parents = []
        self.subjects = []

    @property
    def state(self):
        """"""

        if self.class_level < 5:
            return "small"
        return "big"

    def add_parent(self, gender, first_name, last_name, profession):
        """"""

        parent = Parent(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            profession=profession
        )

        if len(self.parents) == 2:
            raise ValueError("Only two parents expected")

        self.parents.append(parent)

    def get_full_middle_by_direction(self, humanities=[], accurate=[]):

        for subject in self.subjects:
            if subject.direction == "Humanities":
                humanities.append(subject)
            else:
                accurate.append(subject)

    def add_raiting(self, new_subject):
        new_subject = School_subject(
        subject_name='new_sublect.title()',
        list_of_marks = [3, 4, 4, 3, 4, 5],
        direction='Accurate',
        middle = []
    
        )

    def add_full_raiting(self, a=0, marks_list=[]):
        for subject in self.subjects:
            for i in subject.list_of_marks:
                i.append(marks_list)

        for x in marks_list:
            a += x
        b = (a / len(marks_list))
        print(b)

    @property
    def full_info(self):
        """"""

        data = {
            **super().full_info,
            "class_level": self.class_level,
            "state": self.state
        }

        for parent in self.parents:
            data[parent.role] = parent.full_info

        return data

class School_subject:

    def __init__(self, subject_name, list_of_marks, direction, middle):
        self.subject_name = subject_name
        self.list_of_marks = list_of_marks
        self.direction = direction
        self.middle = []

    def add_mark(self, a):
        self.list_of_marks.append(a)

    def get_middle_by_marks(self, a=0):
        for i in self.list_of_marks:
            a += i
        
        self.middle.append(a / len(self.list_of_marks))


if __name__ == "__main__":
    danil = Pupil(
        first_name="Danil",
        last_name="Osipov",
        gender="M",
        class_level=8
    )
    danil.add_parent(
        first_name="Alexey",
        last_name="Osipov",
        gender="M",
        profession="Teacher"
    )
    danil.add_parent(
        first_name="Svetlana",
        last_name="Osipova",
        gender="F",
        profession="Ingeneer"
    )

    import pprint
    pprint.pprint(danil.full_info)
    
    russian_language = School_subject(
        subject_name="Russian Language", 
        list_of_marks = [5, 4, 4, 3, 4, 2],
        direction='Humanities',
        middle = [])

    mathematics = School_subject(
        subject_name="Mathematics",
        list_of_marks = [5, 4, 4, 3, 4, 5, 5],
        direction='Accurate',
        middle = []
    )

    print(russian_language.list_of_marks)
    russian_language.get_middle_by_marks()
    print(russian_language.middle)
    
# school subject (школьный предмет) <-> pupil rating:
#   - name (название предмета: физика, история, ...)
#   - marks (список оценок)
#   - direction (точные или гуманитарные)
#   - middle (средняя оценка по предмету)
#   * add mark (добавить оценку в конец)

# pupil (ученик)
#  * get full middle by direction (получить среднее по точным наукам или по гуманитарным)
#  * get full middle (получить общую среднюю оценку)
#  * add rating (добавить предмет с оценками ученику)
