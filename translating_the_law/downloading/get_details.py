###not sure if there are imports I need here or not

def details_new(strips):
    details = {}
    caseid = strips.index('Case summary')
    date = strips.index('Judgment date')
    cit = strips.index('Neutral citation')
    justices = strips.index('Justices')
    pdf = strips.index('Judgment (PDF)')
    details['Name'] = strips[0].replace(' - The Supreme Court', '')
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
    print(strips)
    if 'Neutral citation number' in strips:
        cit = strips.index('Neutral citation number')
    else:
        cit = strips.index('Neutral citation number(s)')
    date = strips.index('Judgment date')
    caseid = strips.index('Case ID')
    justices = strips.index('Justices')
    details['Name'] = strips[0].replace(' - The Supreme Court', '')
    details['Case ID'] = ', '.join(strips[caseid+1:justices])
    details['Judgment date'] = ', '.join(strips[date+1:cit])
    details['Neutral citation'] = ', '.join(strips[cit+1:caseid])
    details['Justices'] = strips[justices+1]
    return details
