def location (city, country, population=''):

    if population:
        full_location = f"{city}, {country} - {population}"
    else:
        full_location = f"{city}, {country}"
    return full_location.title()