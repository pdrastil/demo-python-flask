from app import app

@app.template_filter('format_date')
def format_date(value, format="%d.%m.%Y"):
    """Format a datetime to date (Default) 31.12.2020"""
    if value is None:
        return ""
    return value.strftime(format)

@app.template_filter('format_time')
def format_time(value, format="%H:%M:%S"):
    """Format a datetime to time (Default) 15:32:20"""
    if value is None:
        return ""
    return value.strftime(format)