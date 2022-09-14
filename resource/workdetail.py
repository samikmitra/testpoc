from .inventory import stringable

## Class to hold incidents (Monthly) for a team priority wise
class incident(stringable):
    priority = 0; monthlyCount = 0; avgEffort = 0; avgComplexity = 'none'
    responseSla = 'none'; resolveSla = 'none'

    ## Constructor
    def __init__(self, priority = 0, monthlyCount = 0, avgEffort = 0, avgComplexity = 'none', \
        responseSla = 'none', resolveSla = 'none') -> None:
        super().__init__()
        self.priority = priority; self.monthlyCount = monthlyCount; self.avgEffort = avgEffort
        self.avgComplexity = avgComplexity; self.responseSla = responseSla
        self.resolveSla = resolveSla

    ## Override base class function
    def toString(self) -> str:
        msg = 'Incident Priority: ' + str(self.priority) + ' Count: ' + str(self.monthlyCount) + \
            ' Avg Effort: ' + str(self.avgEffort) + ' Avg Complexity' + self.avgComplexity + \
                ' Response SLA: ' + self.responseSla + ' Resolve SLA: ' + self.resolveSla
        return msg

## Class to hold Service Requests (Monthly) for a type (prominent ones and misc)
class request(stringable):
    type = 'none'; monthlyCount = 0; avgEffort = 0; avgComplexity = 'none'; daysToComlete = 0

    ## Constructor
    def __init__(self, type = 'none', monthlyCount = 0, avgEffort = 0, avgComplexity = 'none', \
        daysToComlete = 0) -> None:
        super().__init__()
        self.type = type; self.monthlyCount = monthlyCount; self.avgEffort = 0; self.avgComplexity = 'none'
        self.daysToComlete = 0

    ## Override base class function
    def toString(self) -> str:
        msg = 'Request Type: ' + self.type + ' Monthly Count:' + str(self.monthlyCount) + \
            ' Avg Effort: ' + str(self.avgEffort) + ' Avg Complexity: ' + self.avgComplexity + \
                ' Days to Complete: ' + str(self.daysToComlete)
        return msg

## Class to hold periodic activities
class periodicActivity(stringable):
    type = 'none'; recurrence = 'none'; avgEffort = 0; avgComplexity = 'none'; daysToComlete = 0

    ## Constructor
    def __init__(self, type = 'none', recurrence = 'none', avgEffort = 0, avgComplexity = 'none', \
        daysToComlete = 0) -> None:
        super().__init__()
        self.type = type; self.recurrence = recurrence; self.avgEffort = 0; self.avgComplexity = 'none'
        self.daysToComlete = 0

    ## Override base class function
    def toString(self) -> str:
        msg = 'Request Type: ' + self.type + ' Monthly Count:' + self.recurrence + \
            ' Avg Effort: ' + str(self.avgEffort) + ' Avg Complexity: ' + self.avgComplexity + \
                ' Days to Complete: ' + str(self.daysToComlete)
        return msg

## Class to hold total work for a team
class work(stringable):
    incidents = [incident()]; serviceRequests = [request()]; periodicActivities = [periodicActivity()]

    ## Constructor
    def __init__(self, incidents = [incident()], \
        serviceRequests = [request()], periodicActivities = [periodicActivity()]) -> None:
        super().__init__()
        self.incidents= incidents; self.serviceRequests = serviceRequests
        self.periodicActivities = periodicActivities

    ## Override base class function
    def toString(self) -> str:
        msg = '\n List of Incidents: '
        for inc in self.incidents:
            msg += '\n  ' + inc.toString()

        msg += '\n List of Service Requests: '
        for req in self.serviceRequests:
            msg += '\n  ' + req.toString()

        msg += '\n List of Perodic Activities: '
        for act in self.periodicActivities:
            msg += '\n  ' + act.toString()

        return msg