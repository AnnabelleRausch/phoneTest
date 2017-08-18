# --------------- Helpers that build all of the responses ----------------------
def empty_response():
    data = {
        'version': '1.0',
        'response': {
            'shouldEndSession': 'true'
        }
    }
    return data


def speechlet_response(speach_output, shouldEndSession="true", sessionAttributes="", reprompt=None):
        data = {
            'version': '1.0',
            'sessionAttributes': sessionAttributes,
            'response': {
                'outputSpeech': {
                    'type': 'SSML',
                    'ssml': "<speak>" + speach_output + "</speak>"
                },
                'shouldEndSession': shouldEndSession
            }
        }
        return data


def speechlet_response_reprompt(speach_output, reprompt_output, shouldEndSession="true", sessionAttributes="", reprompt=None):
        data = {
            'version': '1.0',
            'sessionAttributes': sessionAttributes,
            'response': {
                'outputSpeech': {
                    'type': 'SSML',
                    'ssml': "<speak>" + speach_output + "</speak>"
                },
                'reprompt': {
                    'outputSpeech': {
                        'type': 'SSML',
                        'ssml': "<speak>" + reprompt_output + "</speak>"
                    }
                },
                'shouldEndSession': shouldEndSession
            }
        }
        return data


def speechlet_response_account_card(speach_output, shouldEndSession="true", sessionAttributes="", card=""):
        data = {
            'version': '1.0',
            'sessionAttributes': sessionAttributes,
            'response': {
                'outputSpeech': {
                    'type': 'SSML',
                    'ssml': "<speak>" + speach_output + "</speak>"
                },
                "card": {
                    "type": "Standard",
                    "title": "rnv start.info",
                    "text": card,
                    "image": {
                        "smallImageUrl": "https://via.placeholder.com/720x480",
                        "largeImageUrl": "https://via.placeholder.com/1200x800"
                    }
                },
                'shouldEndSession': shouldEndSession
            }
        }
        return data
