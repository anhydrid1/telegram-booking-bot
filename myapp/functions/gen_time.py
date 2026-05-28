from datetime import datetime, timedelta, time

def gen_time_slots():

    start_time = datetime.strptime(
        '10:00',
        '%H:%M'
    )

    end_time = datetime.strptime(
        '18:00',
        '%H:%M'
    )

    slot_duration = timedelta(hours=1)

    slots = []

    current_time = start_time

    while current_time < end_time:

        slots.append(
            current_time.strftime('%H:%M')
        )

        current_time += slot_duration

    return slots

slots_main = gen_time_slots()