from datetime import timezone, timedelta, datetime

KST = timezone(timedelta(hours=9))

def now(stringify=False):
    _now = datetime.now(KST)
    if stringify:
        return _now.strftime('%Y-%m-%d %H:%M:%S')
    return _now
