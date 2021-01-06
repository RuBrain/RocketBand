HUMANITIES = "Humanities"
ACCURATE = "Accurate"
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

    def get_full_middle_by_direction(self, direction, total=0):

        marks = []    
        for subject in self.subjects:
           if subject.direction == direction:
               for mark in subject.list_of_marks:
                   marks.append(mark)

        return self.get_average(marks)

    def add_raiting(self, new_subject, subject_name, list_of_marks, direction):
        new_subject = School_subject(
        subject_name=new_subject,
        list_of_marks=list_of_marks,
        direction=direction)


    def get_average(self, marks):
        result = 0
        for mark in marks:
            result += mark
        return result / len(marks)


    def add_full_raiting(self, total=0, marks_list=[]):
        for subject in self.subjects:
            for i in subject.list_of_marks:
                marks_list.append(i)

        return self.get_average(marks_list)

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

    def __init__(self, subject_name, list_of_marks, direction):
        self.subject_name = subject_name
        self.list_of_marks = list_of_marks
        self.direction = direction
        self.middle = 0

    def add_mark(self, a):
        self.list_of_marks.append(a)

    @property
    def middle_by_marks(self):
        
        return sum(self.list_of_marks) / len(self.list_of_marks)

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
        direction=HUMANITIES)

    mathematics = School_subject(
        subject_name="Mathematics",
        list_of_marks = [5, 4, 4, 3, 4, 5, 5],
        direction=ACCURATE)

    danil.subjects.append(russian_language)
    danil.subjects.append(mathematics)

    print(danil.subjects[0].middle_by_marks)
    print(danil.add_full_raiting())
    print(danil.get_full_middle_by_direction(ACCURATE))
    