###not sure if there are imports I need here or not

def details_new(strips):
    details = {}
    caseid = strips.index('Case summary')
    date = strips.index('Judgment date')
    cit = strips.index('Neutral citation')
    justices = strips.index('Justices')
    pdf = strips.index('Judgment (PDF)')
    details['Name'] = strips[0].replace('- The Supreme Court', '')
    if 'Case ID:' in strips[caseid-1] and 'UKSC' in strips[caseid-1]:
        details['Case ID'] = strips[caseid-1].replace('Case ID: ', '')
    elif 'Case ID:' in strips[caseid-1]:
        details['Case ID'] = strips[caseid-1].replace('Case ID:', 'UKSC')
    else:
        details['Case ID'] = strips[caseid-1]
    details['Judgment date'] = ', '.join(strips[date+1:cit])
    details['Neutral citation'] = ', '.join(strips[cit+1:pdf])
    details['Justices'] = strips[justices+1]
    return details

def details_old(strips):
    details = {}
    if 'Neutral citation number' in strips:
        cit = strips.index('Neutral citation number')
    else:
        cit = strips.index('Neutral citation number(s)')
    date = strips.index('Judgment date')
    caseid = strips.index('Case ID')
    justices = strips.index('Justices')
    details['Name'] = strips[0].replace('- The Supreme Court', '')
    details['Case ID'] = ', '.join(strips[caseid+1:justices])
    details['Judgment date'] = ', '.join(strips[date+1:cit])
    details['Neutral citation'] = ', '.join(strips[cit+1:caseid])
    details['Justices'] = strips[justices+1]
    return details

def addl_details(strips):
    details = {}
    caseid = strips.index('Case summary')
    if 'Issue' in strips:
        issues = strips.index('Issue')
    else:
        issues = strips.index('Issue(s)')
    facts = strips.index('Facts')
    if 'Judgment appealed' in strips:
        prev = strips.index('Judgment appealed')
    else:
        prev = strips.index('Parties')
    start = strips.index('Hearing start date')
    finish = strips.index('Hearing finish date')
    if 'Case ID:' in strips[caseid-1] and 'UKSC' in strips[caseid-1]:
        details['Case ID'] = strips[caseid-1].replace('Case ID: ', '')
    elif 'Case ID:' in strips[caseid-1]:
        details['Case ID'] = strips[caseid-1].replace('Case ID:', 'UKSC')
    else:
        details['Case ID'] = strips[caseid-1]
    details['Issue'] = ' '.join(strips[issues+1:facts])
    details['Facts'] = ' '.join(strips[facts+1:prev])
    if 'Judgment appealed' in strips:
        details['Judgment appealed'] = strips[prev+1]
    else:
        pass
    details['Hearing start date'] = strips[start+1]
    details['Hearing finish date'] = strips[finish+1]
    return details
