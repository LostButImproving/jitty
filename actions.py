from typing import Any, Text, Dict, List, Union
from rasa_sdk import Tracker
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction


import requests

class searchwithEnt(Action):
    def name(self) -> Text:
        return "action_search_ent"
    def run(self, dispatcher, tracker, domain):
        
        def search(searchterm):
            url = 'https://readthedocs.org/api/v2/docsearch/?project=jits-docs&version=latest&q='+searchterm
            data = requests.get(url).json()
            data = data['results']
            titlelist = []
            linklist =[]
            answer = ''
            for a in range(min(len(data),3)):
                titlelist.append(data[a]['title'])
                linklist.append(data[a]['link'].replace('docs/','')+'.html')
            dictionary = dict(zip(titlelist, linklist))
            for title, link in dictionary.items(): 
                answer = answer + f"[{title}]({link}) \n"
            return answer

        searchterm = next(tracker.get_latest_entity_values("index"),None)
        if searchterm:
            response = search(searchterm)
        dispatcher.utter_message(response)
        return [SlotSet('searchterm', None)]

class searchwithTerm(FormAction):
    def name(self) -> Text:
        return "søgning_form"
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["searchterm"]

    def slot_mappings(self):
    # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        return {"searchterm": [self.from_text()]}
    
    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
        """Define what the form has to do
        after all required slots are filled"""
        searchterm = tracker.get_slot("searchterm")
        #searchterm = tracker.latest_message.Text
        url = 'https://readthedocs.org/api/v2/docsearch/?project=jits-docs&version=latest&q='+searchterm
        data = requests.get(url).json()
        data = data['results']
        if len(data) > 0:    
            titlelist = []
            linklist =[]
            answer = ''
            for a in range(min(len(data),3)):
                titlelist.append(data[a]['title'])
                linklist.append(data[a]['link'].replace('docs/', '')+'.html')
            dictionary = dict(zip(titlelist, linklist))
            for title, link in dictionary.items(): 
                answer = answer + f"[{title}]({link}) \n"
            dispatcher.utter_message(answer)
        else:
            dispatcher.utter_message("Fandt desværre ingen resultater på din søgning")

        
        return [SlotSet('searchterm', None)]
