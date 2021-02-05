from django.shortcuts import render
from times.models import Freetime, Service, Reservation
from django.views.generic import (TemplateView)
import datetime
from pytz import timezone
# Create your views here.

class TimeTableView(TemplateView):
    template_name = "timetable.html"

    def get_context_data(self, week, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        d = week #"2013-W26"
        helsinki = timezone("Europe/Helsinki")
        monday = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
        sunday = datetime.datetime.strptime(d + '-0', "%Y-W%W-%w")
        sunday = sunday + datetime.timedelta(hours=24)
        loc_monday = helsinki.localize(monday)
        loc_sunday = helsinki.localize(sunday)
        query_set = Freetime.objects \
                            .filter(start__range=[loc_monday, loc_sunday]) \
                            .order_by('start')
        reserved_times = Reservation.objects.filter( \
                            reserved_date__range=[loc_monday, loc_sunday]) \
                            .order_by('reserved_date')
        times = {str(i):[] for i in range(7)}

        serv_duration = datetime.timedelta(minutes=30)

        resv_num = 0
        for i in query_set:
            start = i.start
            end = i.end
            #context["test"]= {"monday":"12-30"}
            break_time = datetime.timedelta(minutes=15)

            while start <= end:
                serv_end = start + serv_duration
                if reserved_times:
                    if(start==reserved_times[resv_num].reserved_date):
                        start += datetime.timedelta(minutes=reserved_times[resv_num].service.get_extended_duration())
                        #print(reserved_times[resv_num].reserved_date)
                        if resv_num < len(reserved_times)-1:
                            resv_num += 1
                    elif(serv_end > reserved_times[resv_num].reserved_date - break_time and start < reserved_times[resv_num].reserved_date):
                        start += break_time
                    else:
                        end_s = start + serv_duration
                        s_time = start.strftime("%H:%M")+" - "+serv_end.strftime("%H:%M")
                        s_day = start.strftime("%w")
                        time_dict = {s_day:s_time}
                        times[s_day].append(time_dict)
                        start += break_time
                else:
                    end_s = start + serv_duration
                    s_time = start.strftime("%H:%M")+" - "+serv_end.strftime("%H:%M")
                    s_day = start.strftime("%w")
                    time_dict = {s_day:s_time}
                    times[s_day].append(time_dict)
                    start += break_time

        length_list = [len(times[str(i)]) for i in range(7)]
        context["time_list"] = []
        num_con = 0

        while num_con<max(length_list):
            dict={ str(i):"" for i in range(7)}
            for i in range(7):
                try:
                    dict.update({str(i):times[str(i)][num_con][str(i)]})
                except IndexError:
                    dict.update({str(i):""})
            context["time_list"].append(dict)
            num_con+=1

        return context
