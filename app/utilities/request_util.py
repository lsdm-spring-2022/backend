def validate_social_media_get_request(region, start_date, end_date, reddit, twitter):
    missing_parameters = []
    if region is None:
        missing_parameters.append('region')
    if start_date is None:
        missing_parameters.append('startDate')
    if end_date is None:
        missing_parameters.append('endDate')
    if reddit is None:
        missing_parameters.append('reddit')
    if twitter is None:
        missing_parameters.append('twitter')
    return missing_parameters
