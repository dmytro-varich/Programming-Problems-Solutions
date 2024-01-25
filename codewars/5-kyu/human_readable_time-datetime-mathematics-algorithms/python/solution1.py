def make_readable(seconds):
    # hours
    hours = seconds // 3600
    seconds -= hours * 3600
    
    # minutes
    minutes = seconds // 60
    
    # seconds
    seconds -= minutes * 60
    
    # Output
    time = f"{hours}:{minutes}:{seconds}"
    formatted_time = ":".join(part.zfill(2) for part in time.split(":")) 
    
    return formatted_time
