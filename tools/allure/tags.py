from enum import Enum


class AllureTag(str, Enum):
    USERS = "USERS"
    FILES = "FILES"
    COURSES = "COURSES"
    EXERCISES = "EXERCISES"
    REGRESSION = "REGRESSION"
    AUTHENTICATION = "AUTHENTICATION"