import random

class Student:
    def __init__(self, name, marks,
    gender, NationalITy, PlaceofBirth, StageID, GradeID, SectionID, Topic, Semester, Relation, raisedhands, VisITedResources, AnnouncementsView, Discussion, ParentAnsweringSurvey, StudentAbsenceDays, Class,
    IndividualProject, Gender, Age,	City,Influenced,	Perseverance,	DesireToTakeInitiative,	Competitiveness,	SelfReliance,	StrongNeedToAchieve,	SelfConfidence,	GoodPhysicalHealth,	KeyTraits) -> None:
        self.name = name
        self.marks = marks
        self.predicted_marks = int(round((sum(self.marks.values()) / len(self.marks.values())), 3) + random.randint(-5, 10)) % 100
        self.parent_satisfaction = 5
        self.happy_path = 5
        
        # For parent satisfation prediction algorithm
        self.gender = gender
        self.NationalITy = NationalITy
        self.PlaceofBirth = PlaceofBirth
        self.StageID = StageID
        self.GradeID = GradeID
        self.SectionID = SectionID
        self.Topic = Topic
        self.Semester = Semester
        self.Relation = Relation
        self.raisedhands = raisedhands
        self.VisITedResources = VisITedResources
        self.AnnouncementsView = AnnouncementsView
        self.Discussion = Discussion
        self.ParentAnsweringSurvey = ParentAnsweringSurvey
        self.StudentAbsenceDays = StudentAbsenceDays
        self.Class = Class

        # For happy path prediction algorithm
        self.IndividualProject = IndividualProject
        self.Gender = Gender
        self.Age = Age
        self.City = City
        self.Influenced = Influenced
        self.Perseverance = Perseverance
        self.DesireToTakeInitiative = DesireToTakeInitiative
        self.Competitiveness = Competitiveness
        self.SelfReliance = SelfReliance
        self.StrongNeedToAchieve = StrongNeedToAchieve
        self.SelfConfidence = SelfConfidence
        self.GoodPhysicalHealth = GoodPhysicalHealth
        self.KeyTraits = KeyTraits


