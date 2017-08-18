import json
import alexa_response

long_output = True


def on_launch(incoming_data):
    return alexa_response.speechlet_response_reprompt(get_return_string('launch_intent', incoming_data['request']['locale']), "", False)


def say_phone_number(incoming_data):
    phone = ""
    if 'NumberI' in incoming_data['request']['intent']['slots']:
        if 'value' in incoming_data['request']['intent']['slots']['NumberI']:
            phone += str(incoming_data['request']['intent']['slots']['NumberI']['value']) + " "

    if 'NumberII' in incoming_data['request']['intent']['slots']:
        if 'value' in incoming_data['request']['intent']['slots']['NumberII']:
            phone += str(incoming_data['request']['intent']['slots']['NumberII']['value']) + " "

    if 'NumberIII' in incoming_data['request']['intent']['slots']:
        if 'value' in incoming_data['request']['intent']['slots']['NumberIII']:
            phone += str(incoming_data['request']['intent']['slots']['NumberIII']['value']) + " "

    if 'NumberIV' in incoming_data['request']['intent']['slots']:
        if 'value' in incoming_data['request']['intent']['slots']['NumberIV']:
            phone += str(incoming_data['request']['intent']['slots']['NumberIV']['value']) + " "

    if 'NumberV' in incoming_data['request']['intent']['slots']:
        if 'value' in incoming_data['request']['intent']['slots']['NumberV']:
            phone += str(incoming_data['request']['intent']['slots']['NumberV']['value']) + " "

    if 'NumberVI' in incoming_data['request']['intent']['slots']:
        if 'value' in incoming_data['request']['intent']['slots']['NumberVI']:
            phone += str(incoming_data['request']['intent']['slots']['NumberVI']['value']) + " "

    if 'NumberVII' in incoming_data['request']['intent']['slots']:
        if 'value' in incoming_data['request']['intent']['slots']['NumberVII']:
            phone += str(incoming_data['request']['intent']['slots']['NumberVII']['value']) + " "

    if 'NumberVIII' in incoming_data['request']['intent']['slots']:
        if 'value' in incoming_data['request']['intent']['slots']['NumberVIII']:
            phone += str(incoming_data['request']['intent']['slots']['NumberVIII']['value']) + " "

    if 'NumberIX' in incoming_data['request']['intent']['slots']:
        if 'value' in incoming_data['request']['intent']['slots']['NumberIX']:
            phone += str(incoming_data['request']['intent']['slots']['NumberIX']['value']) + " "

    if 'NumberX' in incoming_data['request']['intent']['slots']:
        if 'value' in incoming_data['request']['intent']['slots']['NumberX']:
            phone += str(incoming_data['request']['intent']['slots']['NumberX']['value']) + " "

    if 'NumberXI' in incoming_data['request']['intent']['slots']:
        if 'value' in incoming_data['request']['intent']['slots']['NumberXI']:
            phone += str(incoming_data['request']['intent']['slots']['NumberXI']['value']) + " "

    if 'NumberXII' in incoming_data['request']['intent']['slots']:
        if 'value' in incoming_data['request']['intent']['slots']['NumberXII']:
            phone += str(incoming_data['request']['intent']['slots']['NumberXII']['value'])




    return alexa_response.speechlet_response_reprompt(get_return_string('nummer_intent', incoming_data['request']['locale']).format(phone), "", True)


def get_return_string(response_id, language):
    out = ""
    with open('voice_response.json') as data_file:
        data = json.load(data_file)
        out = data[response_id][language]
    return out


def lambda_handler(incoming_data, context=None):
    if long_output:
        print("\n\n\n##### ##### ##### ##### incoming_data ##### ##### ##### #####  \n\n\n " + json.dumps(incoming_data, sort_keys=True, indent=4, ensure_ascii=False))

    if incoming_data['request']['type'] == 'LaunchRequest':
        return on_launch(incoming_data)
    elif 'intent' in incoming_data['request']:
        if incoming_data['request']['intent']['name'] == 'PhoneNumber':
            return say_phone_number(incoming_data)
        elif incoming_data['request']['intent']['name'] == 'AMAZON.YesIntent':
            return alexa_response.empty_response()
        elif incoming_data['request']['intent']['name'] == 'AMAZON.NoIntent':
            return alexa_response.empty_response()
        elif incoming_data['request']['intent']['name'] == 'AMAZON.HelpIntent':
            return alexa_response.empty_response()
        elif incoming_data['request']['intent']['name'] == 'AMAZON.CancelIntent':
            return alexa_response.empty_response()
        elif incoming_data['request']['intent']['name'] == 'AMAZON.StopIntent':
            return alexa_response.empty_response()
    else:
        response = alexa_response.empty_response()
        if long_output:
            print("\n\n\n##### ##### ##### ##### RESPONSE from ELSE ##### ##### ##### #####  \n\n\n " + json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False))
        return response


if __name__ == "__main__":
    print("\n##### Normal Output #####\n")