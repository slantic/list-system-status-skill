from mycroft import MycroftSkill, intent_file_handler
import psutil


class ListSystemStatus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('status.system.list.intent')
    def handle_status_system_list(self, message):
        cputemp = round(psutil.sensors_temperatures()['cpu_thermal'][0][1], 1)
        mem = psutil.virtual_memory()[2]
        disk_percentage = psutil.disk_usage('/')[3]
        disk_free = round(((psutil.disk_usage('/')[2] >> 20) / 1000), 1)

        self.speak_dialog('status.system.list', data={
            'mem': mem,
            'cputemp': cputemp,
            'disk_percentage': disk_percentage,
            'disk_free': disk_free
        })


def create_skill():
    return ListSystemStatus()

