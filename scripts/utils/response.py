    """
    status : api call status
    message : api call message
    chat_response : api response
    reference : api reference
    callback_api : callback api to be executed at client side can be one or many
    
    """



def return_response(status,message,chat_response,reference=[],callback_api=False):
    return (
        {
            'status':status,
            'message': message,
            'data': {
                'chatbot_response': chat_response,
                'reference': reference,
                'callback_api' : callback_api
            }            
        }
    )