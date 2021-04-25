
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
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
        if entity in ["Hi","Hello"]:
            dispatcher.utter_message(response="utter_greet")
        else:
            dispatcher.utter_message(text=f"Let me search some restaurants for {entity} cuisine for you")

        return []




