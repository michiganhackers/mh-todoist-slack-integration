from pytodoist import todoist
import Levenshtein

import conf

MIN_STRING_DISTANCE = 80

class Todoist(object):
    def __init__(self):
        self.user = None


    def __login(self):
        self.user = todoist.login(conf.TODOIST_USER, conf.TODOIST_PASSWORD)

    def __ready(self):
        return self.user and self.user.is_logged_in()

    def find_project(self, search_term):
        """
        Returns the project with the closest name, or None if no project names
        are within MIN_STRING_DISTANCE of the search term
        """
        if not self.__ready():
            self.__login()

        highest_score    = 0
        matching_project = None

        projects = self.user.get_projects()
        for project in projects:
            score = self.__compare_terms(project.name, search_term)
            if score > highest_score:
                highest_score    = score
                matching_project = project

        if highest_score < MIN_STRING_DISTANCE:
            return None

        return matching_project

    def __compare_terms(self, search_string, search_term):
        """
        Returns the levenshtein distance of the normalized strings
        """
        return 100 * Levenshtein.ratio(self.__normalize(search_string),
                                       self.__normalize(search_term))

    def __normalize(self, string):
        """
        Returns the string in lowercase string without special characters
        """
        string = ''.join(e for e in string if e.isalnum())
        return str(string).lower()

