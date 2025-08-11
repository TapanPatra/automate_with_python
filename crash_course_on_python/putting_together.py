class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date=event_date
        self.type = event_type
        self.machine= machine_name
        self.user = user

events = [
    Event('2020-01-21 12:45:46', "log in", 'myWorkstation.Local', 'Tap'),
    Event('2020-01-22 12:45:46', "log out", 'myWorkstation.Local', 'Tap'),
    Event('2020-01-23 12:45:46', "log in", 'myWorkstation.Local', 'Pav')
]


def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines ={}
    for event in events:
        if(event.machine not in machines):
            machines[event.machine] = set()
        if(event.type == "log in"):
            machines[event.machine].add(event.user)
        elif(event.type == "log out"):
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if(len(users) > 0):
            users_list = ",".join(users)
            print("{} {}".format(machine, users_list))
        
users = current_users(events)
generate_report(users)
print(users)
