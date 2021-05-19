
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from .cusine_restaurants import Restaurant_List
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Congratulations on building your first custom action")

        return []

class ActionCustomCusine(Action):

    def name(self) -> Text:
        return "action_custom_cuisine"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        #print(tracker.slots)
        print(tracker.get_slot("cuisine"))
        print(tracker.get_intent_of_latest_message())
        #print(tracker.events_after_latest_restart())
        entity = tracker.get_slot("cuisine")
        if entity not in Restaurant_List.keys():
            dispatcher.utter_message(response = "utter_sorry_cuisine")
            return [SlotSet("cuisine",None)]
        else:
            restaurants = Restaurant_List[entity]
            dispatcher.utter_message(text = f"Let me find some restaurants for {entity} cuisine for you")

            return [SlotSet("restaurants",restaurants)]

class ActionFindRestaurants(Action):
    def name(self) -> Text:
        return "action_find_restaurants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        restaurants = tracker.get_slot("restaurants")
        restaurants = ",".join(restaurants)
        dispatcher.utter_message(f"These are the restaurants I found {restaurants}")


        return []






