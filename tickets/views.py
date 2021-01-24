from django.views import View
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404

queue = {"change_oil": 0, "inflate_tires": 0, "diagnostic": 0}
tickets = {"change_oil": [], "inflate_tires": [], "diagnostic": []}
i = 0
g = False
next_ = 0
class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        url_name = request.path
        return render(request, 'tickets/main.html', context = {"url_name":url_name})

class Change(View):
    a = 0
    def get(self, request, service, *args, **kwargs ):
        global i
        self.a += 1
        if service == "change_oil":
            time = 2 * queue["change_oil"]
        elif service == "inflate_tires":
            time = 2 * queue["change_oil"] +5 * queue["inflate_tires"]
        else:
            time = 2 * queue["change_oil"] +5 * queue["inflate_tires"] + 30 * queue["diagnostic"]
        queue[service] += 1

        i = sum(queue.values())
        tickets[service].append(i)

        url_name = request.path
        context = {"url": url_name, "queue": queue, "i": i, "time": time}
        return render(request, 'tickets/urlname.html', context=context)

class Processing(View):
    def get(self, request):
        context = {"queue": queue}
        return render(request, 'tickets/process.html', context=context)

    def post(self, request, *args, **kwargs):
        global i
        global g
        global next_
        if i > 1:
            if tickets['change_oil']:
                next_ = tickets['change_oil'].pop(0)
                queue["change_oil"] -= 1
            elif tickets['inflate_tires']:
                next_ = tickets['inflate_tires'].pop(0)
                queue["inflate_tires"] -= 1

            elif tickets['diagnostic']:
                next_ = tickets['diagnostic'].pop(0)
                queue["diagnostic"] -= 1
        return redirect('/next')

class nextv(View):
    def get(self, request, *args, **kwargs):
        global i
        global next_
        context = {'tickets': tickets, 'next': next_,}
        return render(request, 'tickets/next.html', context = context)