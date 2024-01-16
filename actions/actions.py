import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGetCourses(Action):
    def name(self) -> Text:
        return "action_get_courses"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://127.0.0.1:5000/courses"
        response = requests.post(api_url)

        if response.status_code == 200:
            courses_data = response.json()
            if courses_data:
                course_names = [course['courseName'] for course in courses_data]
                dispatcher.utter_message(f"Here are the available courses: {', '.join(course_names)}")
            else:
                dispatcher.utter_message("No courses available at the moment.")
        else:
            dispatcher.utter_message("Failed to fetch course data from the API.")

        return []

class ActionGetCertificates(Action):
    def name(self) -> Text:
        return "action_get_certificates"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://127.0.0.1:5000/certificates"
        response = requests.post(api_url)

        if response.status_code == 200:
            certificates_data = response.json()
            if certificates_data:
                dispatcher.utter_message("Here are the available certificates: {}".format(certificates_data))
            else:
                dispatcher.utter_message("No certificates available at the moment.")
        else:
            dispatcher.utter_message("Failed to fetch certificate data from the API.")

        return []

class ActionGetLanguageTrips(Action):
    def name(self) -> Text:
        return "action_get_language_trips"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://127.0.0.1:5000/language_trips"
        response = requests.post(api_url)

        if response.status_code == 200:
            language_trips_data = response.json()
            if language_trips_data:
                dispatcher.utter_message("Here are the available language trips: {}".format(language_trips_data))
            else:
                dispatcher.utter_message("No language trips available at the moment.")
        else:
            dispatcher.utter_message("Failed to fetch language trips data from the API.")

        return []

class ActionGetTandemProgramme(Action):
    def name(self) -> Text:
        return "action_get_tandem_programme"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://127.0.0.1:5000/tandem_programme"
        response = requests.post(api_url)

        if response.status_code == 200:
            tandem_programme_data = response.json()
            if tandem_programme_data:
                dispatcher.utter_message("Here is information about the Tandem programme: {}".format(tandem_programme_data))
            else:
                dispatcher.utter_message("No Tandem programme information available at the moment.")
        else:
            dispatcher.utter_message("Failed to fetch tandem programme data from the API.")

        return []

class ActionGetTheatre(Action):
    def name(self) -> Text:
        return "action_get_theatre"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://127.0.0.1:5000/theatre"
        response = requests.post(api_url)

        if response.status_code == 200:
            theatre_data = response.json()
            if theatre_data:
                dispatcher.utter_message("Here is information about the theatre: {}".format(theatre_data))
            else:
                dispatcher.utter_message("No theatre information available at the moment.")
        else:
            dispatcher.utter_message("Failed to fetch theatre data from the API.")

        return []

class ActionGetLanguageCoursesForExternalParticipants(Action):
    def name(self) -> Text:
        return "action_get_language_courses_for_external_participants"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://127.0.0.1:5000/language_courses_external"
        response = requests.post(api_url)

        if response.status_code == 200:
            language_courses_external_data = response.json()
            if language_courses_external_data:
                dispatcher.utter_message("Here are language courses for external participants: {}".format(language_courses_external_data))
            else:
                dispatcher.utter_message("No language courses for external participants available at the moment.")
        else:
            dispatcher.utter_message("Failed to fetch language courses for external participants data from the API.")

        return []

class ActionRegisterForLanguageCourse(Action):
    def name(self) -> Text:
        return "action_register_for_language_course"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        registration_data = {
            "email": tracker.get_slot("email"),
            "course_id": tracker.get_slot("course_id")
        }

        api_url = "http://127.0.0.1:5000/register_for_course"
        response = requests.post(api_url, json=registration_data)

        if response.status_code == 200:
            registration_status = response.json()
            dispatcher.utter_message("Registration status: {}".format(registration_status))
        else:
            dispatcher.utter_message("Failed to register for the language course.")

        return []

class ActionGetFeeInformation(Action):
    def name(self) -> Text:
        return "action_get_fee_information"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://127.0.0.1:5000/fee_information"
        response = requests.post(api_url)

        if response.status_code == 200:
            fee_information_data = response.json()
            if fee_information_data:
                dispatcher.utter_message("Here is the fee information: {}".format(fee_information_data))
            else:
                dispatcher.utter_message("No fee information available at the moment.")
        else:
            dispatcher.utter_message("Failed to fetch fee information data from the API.")

        return []

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Hello! How can I assist you today?")
        return []

class ActionGoodbye(Action):
    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Goodbye! If you have more questions, feel free to ask.")
        return []
