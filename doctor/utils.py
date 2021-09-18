def data(name, email, date, phone_number, content):
    message = f''' Mr/Mrs {name} has booked an Appointment for the Problem {content} on {date}.
    Your Details are ,

    email : {email}
    phone Number : {phone_number} 

    Will get to You as Soon as Possible!
    '''
    return message